import json
import random
from pathlib import Path

CHUNKS_PATH = Path("data/processed/chunks.jsonl")

def load_chunks(path):
    chunks = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))
    return chunks

def main():
    if not CHUNKS_PATH.exists():
        raise FileNotFoundError(f"Could not find {CHUNKS_PATH}")

    chunks = load_chunks(CHUNKS_PATH)

    print(f"Total chunks: {len(chunks)}")

    empty_chunks = [c for c in chunks if not c.get("text", "").strip()]
    html_chunks = [
        c for c in chunks
        if "<div" in c.get("text", "").lower()
        or "</" in c.get("text", "").lower()
        or "&nbsp;" in c.get("text", "").lower()
        or "&amp;" in c.get("text", "").lower()
    ]

    lengths = [len(c.get("text", "")) for c in chunks]
    print(f"Shortest chunk length: {min(lengths)}")
    print(f"Longest chunk length: {max(lengths)}")
    print(f"Average chunk length: {sum(lengths) // len(lengths)}")
    print(f"Empty chunks: {len(empty_chunks)}")
    print(f"Chunks with possible HTML artifacts: {len(html_chunks)}")

    print("\n==============================")
    print("5 RANDOM SAMPLE CHUNKS")
    print("==============================\n")

    sample_size = min(5, len(chunks))
    for i, chunk in enumerate(random.sample(chunks, sample_size), start=1):
        print(f"--- SAMPLE CHUNK {i} ---")
        print(f"Chunk ID: {chunk.get('chunk_id')}")
        print(f"Source: {chunk.get('source')}")
        print(f"Chunk index: {chunk.get('chunk_index')}")
        print()
        print(chunk.get("text", ""))
        print("\n")

if __name__ == "__main__":
    main()