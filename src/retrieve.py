"""Retrieve the most relevant chunks from the ChromaDB vector store."""

import sys
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHROMA_PATH = PROJECT_ROOT / "data" / "chroma_db"
COLLECTION_NAME = "ucsc_cs_guide"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
DEFAULT_TOP_K = 5
PREVIEW_LENGTH = 700

_model = None
_collection = None


def get_model() -> SentenceTransformer:
    """Load the embedding model once and reuse it."""
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)
    return _model


def get_collection():
    """Load the ChromaDB collection, with a clear error if missing."""
    global _collection
    if _collection is not None:
        return _collection

    if not CHROMA_PATH.exists():
        raise FileNotFoundError(
            "ChromaDB database not found at data/chroma_db/. "
            "Run `python src/build_vector_store.py` first."
        )

    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    try:
        _collection = client.get_collection(COLLECTION_NAME)
    except (ValueError, chromadb.errors.NotFoundError) as exc:
        raise FileNotFoundError(
            f"ChromaDB collection '{COLLECTION_NAME}' not found. "
            "Run `python src/build_vector_store.py` first."
        ) from exc

    return _collection


def retrieve(query: str, top_k: int = DEFAULT_TOP_K) -> list[dict]:
    """Embed a query and return the top-k most similar chunks."""
    if not query.strip():
        raise ValueError("Query must not be empty.")

    model = get_model()
    collection = get_collection()

    query_embedding = model.encode(query, show_progress_bar=False).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    retrieved = []
    ids = results.get("ids", [[]])[0]
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for rank, chunk_id in enumerate(ids, start=1):
        metadata = metadatas[rank - 1] or {}
        item = {
            "rank": rank,
            "chunk_id": chunk_id,
            "source": metadata.get("source", ""),
            "source_path": metadata.get("source_path", ""),
            "chunk_index": metadata.get("chunk_index"),
            "distance": distances[rank - 1],
            "text": documents[rank - 1] or "",
        }
        if metadata.get("url"):
            item["url"] = metadata["url"]
        if metadata.get("description"):
            item["description"] = metadata["description"]
        retrieved.append(item)

    return retrieved


def print_results(query: str, top_k: int, results: list[dict]) -> None:
    """Print retrieval results for CLI usage."""
    print("RETRIEVAL RESULTS")
    print("=" * 60)
    print(f"Query: {query}")
    print(f"Top-k: {top_k}")
    print("=" * 60)

    if not results:
        print("No results found.")
        return

    for result in results:
        preview = result["text"][:PREVIEW_LENGTH]
        if len(result["text"]) > PREVIEW_LENGTH:
            preview += "..."

        print(f"\nRank: {result['rank']}")
        print(f"Distance: {result['distance']:.6f}")
        print(f"Source: {result['source']}")
        print(f"Chunk ID: {result['chunk_id']}")
        print(f"Text preview:\n{preview}")


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python src/retrieve.py "your question here"')
        return 1

    query = sys.argv[1].strip()
    if not query:
        print("Error: query must not be empty.")
        return 1

    try:
        results = retrieve(query, top_k=DEFAULT_TOP_K)
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        return 1

    print_results(query, DEFAULT_TOP_K, results)
    return 0


if __name__ == "__main__":
    sys.exit(main())
