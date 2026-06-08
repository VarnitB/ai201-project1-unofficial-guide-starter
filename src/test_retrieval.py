"""Run retrieval tests on evaluation questions from planning.md."""

import sys
from io import StringIO
from pathlib import Path

from retrieve import retrieve

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "retrieval_test_results.txt"
TOP_K = 5
PREVIEW_LENGTH = 1000
DIVIDER = "=" * 80

EVALUATION_QUESTIONS = [
    "Which UCSC CSE classes do students mention as especially important for CS majors?",
    "What are common pros and cons students mention about UCSC CS?",
    "Which professors or teachers are recommended by students in the collected sources?",
    "What official requirements or course categories are listed for the UCSC CS B.S.?",
    "Does the system have enough information to compare UCSC CS to UC Davis CS?",
]


def format_query_results(query_number: int, query: str, results: list[dict]) -> str:
    """Format retrieval results for one evaluation question."""
    lines = [
        DIVIDER,
        f"Question {query_number}",
        DIVIDER,
        f"Query: {query}",
        f"Top-k: {TOP_K}",
        "",
    ]

    if not results:
        lines.append("No results found.")
        return "\n".join(lines) + "\n"

    for result in results:
        preview = result["text"][:PREVIEW_LENGTH]
        if len(result["text"]) > PREVIEW_LENGTH:
            preview += "..."

        lines.extend(
            [
                f"Rank: {result['rank']}",
                f"Distance: {result['distance']:.6f}",
                f"Source: {result['source']}",
                f"Chunk ID: {result['chunk_id']}",
                "Text preview:",
                preview,
                "",
            ]
        )

    return "\n".join(lines) + "\n"


def run_tests() -> str:
    """Run all evaluation queries and return the full report text."""
    report = StringIO()
    report.write("RETRIEVAL TEST RESULTS\n")
    report.write(f"{DIVIDER}\n\n")

    for index, query in enumerate(EVALUATION_QUESTIONS, start=1):
        results = retrieve(query, top_k=TOP_K)
        section = format_query_results(index, query, results)
        report.write(section)
        print(section, end="")

    return report.getvalue()


def main() -> int:
    try:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        report_text = run_tests()
        OUTPUT_PATH.write_text(report_text, encoding="utf-8")
        print(DIVIDER)
        print(f"Full results written to: {OUTPUT_PATH.resolve()}")
        return 0
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
