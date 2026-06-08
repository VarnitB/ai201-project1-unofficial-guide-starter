"""Embed processed chunks and store them in a persistent ChromaDB collection."""

import json
import sys
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "chunks.jsonl"
CHROMA_PATH = PROJECT_ROOT / "data" / "chroma_db"
COLLECTION_NAME = "ucsc_cs_guide"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
BATCH_SIZE = 64

REQUIRED_FIELDS = ("chunk_id", "source", "source_path", "chunk_index", "text")
OPTIONAL_METADATA_FIELDS = ("title", "description", "url")


def load_chunks(path: Path) -> list[dict]:
    """Load chunk records from chunks.jsonl."""
    if not path.exists():
        raise FileNotFoundError(f"Chunks file not found: {path}")

    chunks = []
    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            chunk = json.loads(line)
            validate_chunk(chunk, line_number)
            chunks.append(chunk)
    return chunks


def validate_chunk(chunk: dict, line_number: int) -> None:
    """Ensure a chunk has the required fields."""
    missing = [field for field in REQUIRED_FIELDS if field not in chunk]
    if missing:
        raise ValueError(
            f"Line {line_number} is missing required fields: {', '.join(missing)}"
        )

    if not str(chunk["text"]).strip():
        raise ValueError(f"Line {line_number} has empty text for {chunk['chunk_id']}")


def build_metadata(chunk: dict) -> dict:
    """Build ChromaDB metadata for a chunk."""
    metadata = {
        "source": chunk["source"],
        "source_path": chunk["source_path"],
        "chunk_index": int(chunk["chunk_index"]),
    }
    for field in OPTIONAL_METADATA_FIELDS:
        value = chunk.get(field)
        if value is not None and str(value).strip():
            metadata[field] = str(value)
    return metadata


def reset_collection(client: chromadb.PersistentClient):
    """Delete and recreate the target collection."""
    try:
        client.delete_collection(COLLECTION_NAME)
    except (ValueError, chromadb.errors.NotFoundError):
        pass

    return client.create_collection(name=COLLECTION_NAME)


def embed_and_store(chunks: list[dict], model: SentenceTransformer, collection) -> int:
    """Embed chunks in batches and add them to ChromaDB."""
    stored = 0

    for start in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[start : start + BATCH_SIZE]
        ids = [chunk["chunk_id"] for chunk in batch]
        documents = [chunk["text"] for chunk in batch]
        metadatas = [build_metadata(chunk) for chunk in batch]
        embeddings = model.encode(documents, show_progress_bar=False).tolist()

        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings,
        )
        stored += len(batch)

    return stored


def main() -> int:
    print("Loading chunks...")
    chunks = load_chunks(CHUNKS_PATH)
    print(f"Loaded {len(chunks)} chunks from {CHUNKS_PATH}")

    print(f"Loading embedding model: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)

    CHROMA_PATH.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    collection = reset_collection(client)

    print("Embedding and storing chunks in ChromaDB...")
    stored = embed_and_store(chunks, model, collection)

    print("\nVECTOR STORE SUMMARY")
    print("=" * 60)
    print(f"Chunks loaded:               {len(chunks)}")
    print(f"Chunks embedded/stored:      {stored}")
    print(f"ChromaDB path:               {CHROMA_PATH}")
    print(f"Collection name:             {COLLECTION_NAME}")
    print(f"Collection count:            {collection.count()}")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
