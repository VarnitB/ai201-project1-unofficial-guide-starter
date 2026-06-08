"""Load raw .txt sources, clean text, chunk, and save processed JSONL files."""

import json
import random
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
CLEANED_DOCS_PATH = PROCESSED_DIR / "cleaned_docs.jsonl"
CHUNKS_PATH = PROCESSED_DIR / "chunks.jsonl"

TARGET_CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
MIN_CHUNK_SIZE = 150

REDDIT_UI_WORDS = re.compile(
    r"\b(?:Upvote|Downvote|Award|Share|avatar)\b",
    re.IGNORECASE,
)
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
PARAGRAPH_SPLIT = re.compile(r"\n\s*\n+")
SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+")

BOILERPLATE_PHRASES = [
    "Skip to content",
    "You signed in with another tab or window",
    "You signed out in another tab or window",
    "You switched accounts on another tab or window",
    "Reload to refresh your session",
    "to refresh your session",
    "Dismiss alert",
    "Notifications",
    "Fork",
    "Star",
    "Branches",
    "Tags",
    "Open more actions menu",
    "Folders and files",
    "Last commit message",
    "Last commit date",
    "Repository files navigation",
    "Uh oh!",
    "There was an error while loading",
    "Please reload this page",
    "You can't perform that action at this time",
    "Catalog Links",
    "Catalog Home",
    "All Catalogs",
    "this page on Facebook",
    "this page on Twitter",
    "Email this page",
    "Print this page",
    "json/catalogs.json",
]


def parse_header(raw_text: str) -> tuple[dict, str]:
    """Extract Source/Description/URL header fields and return body text."""
    lines = raw_text.splitlines()
    metadata = {"title": "", "description": "", "url": ""}
    body_start = 0

    for i, line in enumerate(lines):
        if line.startswith("Source:"):
            metadata["title"] = line[len("Source:") :].strip()
        elif line.startswith("Description:"):
            metadata["description"] = line[len("Description:") :].strip()
        elif line.startswith("URL:"):
            metadata["url"] = line[len("URL:") :].strip()
        elif line.strip() == "" and metadata["title"]:
            body_start = i + 1
            break

    body = "\n".join(lines[body_start:]).strip()
    return metadata, body


def phrase_in_text(phrase: str, text: str) -> bool:
    """Match boilerplate phrases without false positives on short UI words."""
    text_lower = text.lower()
    phrase_lower = phrase.lower().replace("’", "'")
    text_lower = text_lower.replace("’", "'")

    if re.search(r"[\s/!?]", phrase_lower):
        return phrase_lower in text_lower

    return re.search(rf"\b{re.escape(phrase_lower)}\b", text_lower) is not None


def line_is_boilerplate(line: str) -> bool:
    """Return True if a line is obvious webpage or repository UI noise."""
    if line.lower() in {"reload", "to refresh your session.", "to refresh your session"}:
        return True
    return any(phrase_in_text(phrase, line) for phrase in BOILERPLATE_PHRASES)


def find_boilerplate_phrases(text: str) -> list[str]:
    """Return boilerplate phrases still present in text."""
    return [phrase for phrase in BOILERPLATE_PHRASES if phrase_in_text(phrase, text)]


def clean_text(text: str) -> str:
    """Lightly clean document text while preserving useful content."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = REDDIT_UI_WORDS.sub("", text)

    cleaned_lines = []
    for line in text.splitlines():
        line = re.sub(r"[ \t]+", " ", line).strip()
        if line and not line_is_boilerplate(line):
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def split_sentences(paragraph: str) -> list[str]:
    """Split a long paragraph into sentence-sized pieces."""
    parts = SENTENCE_SPLIT.split(paragraph.strip())
    return [part.strip() for part in parts if part.strip()]


def split_paragraphs(text: str) -> list[str]:
    """Split text into paragraphs, falling back to line-based blocks."""
    paragraphs = [p.strip() for p in PARAGRAPH_SPLIT.split(text) if p.strip()]
    if len(paragraphs) > 1:
        return paragraphs

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines if lines else [text.strip()] if text.strip() else []


def merge_small_chunks(chunks: list[str]) -> list[str]:
    """Merge trailing tiny chunks into the previous chunk when possible."""
    if not chunks:
        return chunks

    merged = [chunks[0]]
    for chunk in chunks[1:]:
        if len(chunk) < MIN_CHUNK_SIZE and merged:
            merged[-1] = f"{merged[-1]}\n{chunk}"
        else:
            merged.append(chunk)
    return merged


def get_overlap_prefix(prev: str, target_overlap: int) -> str:
    """Return overlap text starting at a sentence or paragraph boundary."""
    if not prev:
        return ""
    if len(prev) <= target_overlap:
        return prev

    cut = len(prev) - target_overlap
    search_start = max(0, cut - 200)
    region = prev[search_start:]

    boundary_positions = []
    for index, char in enumerate(region):
        if char == "\n" and index + 1 < len(region):
            boundary_positions.append((0, search_start + index + 1))

    for match in SENTENCE_BOUNDARY.finditer(region):
        boundary_positions.append((1, search_start + match.end()))

    if boundary_positions:
        valid = [pos for _, pos in boundary_positions if pos <= len(prev)]
        if valid:
            preferred = [pos for pos in valid if pos >= cut - 80]
            chosen = min(preferred or valid, key=lambda pos: abs(pos - cut))
            return prev[chosen:].strip()

    # Fallback: start at the nearest word boundary instead of mid-word.
    prefix = prev[cut:]
    if prefix and not prev[cut - 1 : cut].isspace() and cut > 0:
        space_index = prefix.find(" ")
        if 0 <= space_index < 30:
            prefix = prefix[space_index + 1 :]
    return prefix.strip()


def add_overlap(chunks: list[str], overlap: int) -> list[str]:
    """Prepend boundary-aligned overlap text from the previous chunk."""
    if overlap <= 0 or len(chunks) <= 1:
        return chunks

    with_overlap = [chunks[0]]
    for chunk in chunks[1:]:
        prev = with_overlap[-1]
        prefix = get_overlap_prefix(prev, overlap)
        with_overlap.append(f"{prefix}\n{chunk}" if prefix else chunk)
    return with_overlap


def chunk_paragraph(paragraph: str, target_size: int) -> list[str]:
    """Chunk one paragraph, splitting by sentences if it exceeds target size."""
    if len(paragraph) <= target_size:
        return [paragraph]

    sentences = split_sentences(paragraph)
    if len(sentences) <= 1:
        # Hard split if there are no sentence boundaries.
        pieces = []
        start = 0
        while start < len(paragraph):
            pieces.append(paragraph[start : start + target_size].strip())
            start += target_size
        return [piece for piece in pieces if piece]

    chunks = []
    current = ""
    for sentence in sentences:
        candidate = f"{current} {sentence}".strip() if current else sentence
        if len(candidate) <= target_size:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = sentence
    if current:
        chunks.append(current)
    return chunks


def chunk_text(text: str, target_size: int = TARGET_CHUNK_SIZE) -> list[str]:
    """Create paragraph-aware chunks close to the target size."""
    paragraphs = split_paragraphs(text)
    chunks = []
    current = ""

    for paragraph in paragraphs:
        if len(paragraph) > target_size:
            if current:
                chunks.append(current)
                current = ""
            chunks.extend(chunk_paragraph(paragraph, target_size))
            continue

        candidate = f"{current}\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= target_size:
            current = candidate
        else:
            chunks.append(current)
            current = paragraph

    if current:
        chunks.append(current)

    chunks = merge_small_chunks(chunks)
    return add_overlap(chunks, CHUNK_OVERLAP)


def load_raw_documents(raw_dir: Path) -> list[dict]:
    """Load and clean all .txt files from data/raw/."""
    documents = []
    for path in sorted(raw_dir.glob("*.txt")):
        raw_text = path.read_text(encoding="utf-8")
        header, body = parse_header(raw_text)
        cleaned_body = clean_text(body)

        documents.append(
            {
                "source": path.name,
                "source_path": str(path.relative_to(PROJECT_ROOT)),
                "title": header["title"],
                "description": header["description"],
                "url": header["url"],
                "text": cleaned_body,
            }
        )
    return documents


def write_jsonl(path: Path, records: list[dict]) -> None:
    """Write records to a JSONL file."""
    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_chunks(documents: list[dict]) -> list[dict]:
    """Build chunk records from cleaned documents."""
    all_chunks = []
    stem_counts: dict[str, int] = {}

    for doc in documents:
        doc_chunks = chunk_text(doc["text"])
        file_stem = Path(doc["source"]).stem

        for index, chunk_text_value in enumerate(doc_chunks):
            stem_counts[file_stem] = stem_counts.get(file_stem, 0) + 1
            chunk_number = stem_counts[file_stem]
            chunk_id = f"{file_stem}_{chunk_number:04d}"

            all_chunks.append(
                {
                    "chunk_id": chunk_id,
                    "source": doc["source"],
                    "source_path": doc["source_path"],
                    "title": doc["title"],
                    "description": doc["description"],
                    "url": doc["url"],
                    "chunk_index": index,
                    "text": chunk_text_value,
                }
            )

    return all_chunks


def warn_boilerplate_in_chunks(chunks: list[dict]) -> None:
    """Print warnings for chunks that still contain boilerplate phrases."""
    warnings = []
    for chunk in chunks:
        matches = find_boilerplate_phrases(chunk["text"])
        if matches:
            warnings.append((chunk["chunk_id"], matches))

    if not warnings:
        print("\nBoilerplate check: no remaining boilerplate phrases found in chunks.")
        return

    print(f"\nWARNING: {len(warnings)} chunk(s) still contain boilerplate phrases:")
    for chunk_id, matches in warnings:
        print(f"  - {chunk_id}: {', '.join(matches)}")


def print_sample_chunks(chunks: list[dict], count: int = 5) -> None:
    """Print a few random chunk previews for manual inspection."""
    samples = random.sample(chunks, min(count, len(chunks)))
    print(f"\nSample chunks ({len(samples)}):")
    for sample in samples:
        preview = sample["text"][:200].replace("\n", " ")
        if len(sample["text"]) > 200:
            preview += "..."
        print(f"  - {sample['source']} [{sample['chunk_id']}]")
        print(f"    {preview}")


def main() -> int:
    if not RAW_DIR.exists():
        print(f"Error: raw directory not found at {RAW_DIR}")
        return 1

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    raw_documents = sorted(RAW_DIR.glob("*.txt"))
    documents = load_raw_documents(RAW_DIR)
    chunks = build_chunks(documents)

    write_jsonl(CLEANED_DOCS_PATH, documents)
    write_jsonl(CHUNKS_PATH, chunks)

    avg_chunk_length = (
        sum(len(chunk["text"]) for chunk in chunks) / len(chunks) if chunks else 0
    )

    print("INGEST SUMMARY")
    print("=" * 60)
    print(f"Raw documents loaded:      {len(raw_documents)}")
    print(f"Cleaned documents saved:     {len(documents)}")
    print(f"Total chunks created:        {len(chunks)}")
    print(f"Average chunk length:        {avg_chunk_length:.1f} characters")
    print(f"Cleaned docs output:         {CLEANED_DOCS_PATH}")
    print(f"Chunks output:               {CHUNKS_PATH}")
    print("=" * 60)

    warn_boilerplate_in_chunks(chunks)
    print_sample_chunks(chunks)
    return 0


if __name__ == "__main__":
    sys.exit(main())
