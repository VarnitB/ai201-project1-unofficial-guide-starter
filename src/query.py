"""Grounded question answering using retrieval and Groq."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from retrieve import retrieve

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GROQ_MODEL = "llama-3.3-70b-versatile"
DEFAULT_TOP_K = 5

SYSTEM_PROMPT = """You are a helpful assistant for UCSC Computer Science courses and professors.

Answer using only the retrieved context provided below.
Do not use outside knowledge.
If the context does not contain enough information to answer, say exactly:
"I don't have enough information in the provided sources to answer that."
Cite source filenames in the answer when making claims, for example (reddit_best_professors.txt).
Do not invent course names, professor names, requirements, or comparisons."""


def get_groq_client() -> Groq:
    """Create a Groq client using the API key from .env."""
    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key.strip() == "your_key_here":
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to .env before running query.py."
        )
    return Groq(api_key=api_key)


def build_context(chunks: list[dict]) -> str:
    """Format retrieved chunks into a context block for the LLM."""
    sections = []
    for chunk in chunks:
        header = (
            f"[Source: {chunk.get('source', 'unknown')} | "
            f"Chunk ID: {chunk.get('chunk_id', 'unknown')}]"
        )
        sections.append(f"{header}\n{chunk.get('text', '').strip()}")
    return "\n\n---\n\n".join(sections)


def unique_sources(chunks: list[dict]) -> list[str]:
    """Return unique source filenames from retrieved chunks, in rank order."""
    seen = set()
    sources = []
    for chunk in chunks:
        source = chunk.get("source", "")
        if source and source not in seen:
            seen.add(source)
            sources.append(source)
    return sources


def strip_llm_sources_section(answer: str) -> str:
    """Remove any LLM-generated sources section before appending our own."""
    if "Sources used:" in answer:
        return answer.split("Sources used:")[0].rstrip()
    return answer.rstrip()


def append_sources_section(answer: str, sources: list[str]) -> str:
    """Guarantee a programmatic Sources used section after the answer."""
    answer = strip_llm_sources_section(answer)
    source_lines = "\n".join(f"- {source}" for source in sources)
    return f"{answer}\n\nSources used:\n{source_lines}"


def generate_answer(client: Groq, question: str, context: str) -> str:
    """Send the question and retrieved context to Groq."""
    user_prompt = f"""Retrieved context:
{context}

Question:
{question}

Answer the question using only the retrieved context above."""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()


def ask(question: str, top_k: int = DEFAULT_TOP_K) -> dict:
    """Retrieve relevant chunks and generate a grounded answer."""
    if not question.strip():
        raise ValueError("Question must not be empty.")

    retrieved_chunks = retrieve(question, top_k=top_k)
    sources = unique_sources(retrieved_chunks)

    if not retrieved_chunks:
        answer = (
            "I don't have enough information in the provided sources to answer that."
        )
        return {
            "answer": answer,
            "sources": [],
            "retrieved_chunks": [],
        }

    context = build_context(retrieved_chunks)
    client = get_groq_client()
    raw_answer = generate_answer(client, question, context)
    answer = append_sources_section(raw_answer, sources)

    return {
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": retrieved_chunks,
    }


def print_response(question: str, result: dict) -> None:
    """Print the ask() result for CLI usage."""
    print("GROUNDED QUERY RESULT")
    print("=" * 60)
    print(f"Question: {question}")
    print("=" * 60)
    display_answer = strip_llm_sources_section(result["answer"])
    print("\nAnswer:")
    print(display_answer)

    print("\nSources used:")
    if result["sources"]:
        for source in result["sources"]:
            print(f"- {source}")
    else:
        print("- none")

    print("\nRetrieved chunks:")
    for chunk in result["retrieved_chunks"]:
        print(
            f"- rank={chunk['rank']} | distance={chunk['distance']:.6f} | "
            f"source={chunk['source']} | chunk_id={chunk['chunk_id']}"
        )


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python src/query.py "your question here"')
        return 1

    question = sys.argv[1].strip()
    if not question:
        print("Error: question must not be empty.")
        return 1

    try:
        result = ask(question, top_k=DEFAULT_TOP_K)
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        return 1
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    print_response(question, result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
