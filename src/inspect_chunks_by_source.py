import json
from collections import defaultdict
from pathlib import Path

CHUNKS_PATH = Path("data/processed/chunks.jsonl")
SAMPLE_CHUNKS_PATH = Path("data/processed/sample_chunks.txt")

PREFERRED_SAMPLE_SOURCES = [
    "pdf_cs_degree_curriculum_chart.txt",
    "reddit_important_cs_classes.txt",
    "reddit_how_is_ucsc_cs_program.txt",
    "reddit_example_cs_path.txt",
    "github_ucsc_cs_student_guide.txt",
]


def load_chunks(path: Path) -> list[dict]:
    chunks = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))
    return chunks


def pick_representative_chunk(source_chunks: list[dict]) -> dict:
    """Pick a substantive chunk, preferring the earliest readable one."""
    sorted_chunks = sorted(source_chunks, key=lambda chunk: chunk.get("chunk_index", 0))
    for chunk in sorted_chunks:
        if len(chunk.get("text", "").strip()) >= 150:
            return chunk
    return sorted_chunks[0]


def format_sample_chunks_file(samples: list[dict]) -> str:
    """Format sample chunks for easy copy/paste into README.md."""
    sections = []
    for index, chunk in enumerate(samples, start=1):
        sections.append(
            "\n".join(
                [
                    f"### Sample Chunk {index}",
                    "",
                    f"**Source:** `{chunk.get('source', 'UNKNOWN')}`  ",
                    f"**Chunk ID:** `{chunk.get('chunk_id', 'UNKNOWN')}`",
                    "",
                    "```text",
                    chunk.get("text", "").rstrip(),
                    "```",
                ]
            )
        )
    return "\n\n".join(sections) + "\n"


def select_sample_chunks(by_source: dict[str, list[dict]]) -> list[dict]:
    """Select one representative chunk from each preferred source."""
    samples = []
    for source in PREFERRED_SAMPLE_SOURCES:
        source_chunks = by_source.get(source)
        if not source_chunks:
            print(f"Warning: no chunks found for preferred source {source}")
            continue
        samples.append(pick_representative_chunk(source_chunks))
    return samples


def main() -> None:
    if not CHUNKS_PATH.exists():
        raise FileNotFoundError(f"Could not find {CHUNKS_PATH}")

    chunks = load_chunks(CHUNKS_PATH)

    by_source = defaultdict(list)
    for chunk in chunks:
        by_source[chunk.get("source", "UNKNOWN")].append(chunk)

    print(f"Total chunks: {len(chunks)}")
    print(f"Total sources: {len(by_source)}")
    print("\nChunks per source:")
    for source, source_chunks in sorted(by_source.items()):
        print(f"- {source}: {len(source_chunks)} chunks")

    samples = select_sample_chunks(by_source)
    SAMPLE_CHUNKS_PATH.parent.mkdir(parents=True, exist_ok=True)
    SAMPLE_CHUNKS_PATH.write_text(format_sample_chunks_file(samples), encoding="utf-8")

    print(f"\nSample chunks written to: {SAMPLE_CHUNKS_PATH.resolve()}")


if __name__ == "__main__":
    main()
