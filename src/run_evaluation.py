"""Run final evaluation questions through the RAG system and save results."""

import sys
from pathlib import Path

from query import ask

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "evaluation_results.md"
PREVIEW_LENGTH = 1000

EVALUATION_CASES = [
    {
        "number": 1,
        "question": (
            "Which UCSC CSE classes do students mention as especially important for CS majors?"
        ),
        "expected_answer": (
            "Students mention CSE 130 with Harrison as useful for systems, CSE 113 with "
            "Sorensen for multithreading, CSE 186/CSE 187 with Harrison for full-stack web "
            "development, and CSE 138 with Kuper for distributed systems, microservices, and "
            "REST APIs. The strongest recommendations are CSE 138 and full-stack web "
            "development because students say those apply to a broader set of jobs. Other "
            "recommended classes depend on interest area, such as CSE 150/156 for networking, "
            "CSE 140/144 for AI/ML, CSE 160/164/168 for graphics/computer vision, CSE 104/105 "
            "for math, and CSE 180/181 for databases."
        ),
        "top_k": 5,
    },
    {
        "number": 2,
        "question": "What are common pros and cons students mention about UCSC CS?",
        "expected_answer": (
            "Students describe UCSC CS positively overall, saying the program has good younger "
            "professors, interesting classes, high class-enrollment priority for declared CS "
            "majors, and many required CS classes offered frequently. Students also say it is "
            "possible to build strong skills if you choose challenging classes and professors "
            "carefully. Common negatives are that students do not get to specialize until later "
            "in the major, the core classes may not clearly show what area of CS to pursue, "
            "housing in Santa Cruz is limited and expensive, and students need to plan early for "
            "both classes and housing."
        ),
        "top_k": 5,
    },
    {
        "number": 3,
        "question": (
            "Which professors or teachers are recommended by students in the collected sources?"
        ),
        "expected_answer": (
            'Students recommend Sesh, Fremont, Harrison, Sorensen, Kuper, Tantalo, De Alfaro, '
            "Miller, Qian, and Alvaro. Harrison receives the strongest mixed recommendation: "
            'students say his classes are hard and demanding, but that students "level up" as '
            "software engineers after taking his classes, especially full-stack or systems "
            "courses. Sorensen and Kuper are recommended for interesting upper-division "
            "electives, and Alvaro is mentioned positively for CSE 138."
        ),
        "top_k": 5,
    },
    {
        "number": 4,
        "question": (
            "What official requirements or course categories are listed for the UCSC CS B.S.?"
        ),
        "expected_answer": (
            "The UCSC CS B.S. curriculum includes lower-division programming courses such as "
            "CSE 20, CSE 30, CSE 12, and CSE 13S; math courses such as calculus, discrete math, "
            "linear algebra, and probability/statistics; upper-division core courses such as "
            "CSE 101, CSE 102, CSE 103, CSE 114A, CSE 120, and CSE 130; a Disciplinary "
            "Communication requirement; a comprehensive/capstone requirement; and four "
            "upper-division electives. The curriculum chart also says upper-division electives "
            "are generally 5-credit upper-division CSE/CE courses numbered 100–189, CSE 195, or "
            "approved computational media/math electives, with some restrictions."
        ),
        "top_k": 10,
    },
    {
        "number": 5,
        "question": (
            "Does the system have enough information to compare UCSC CS to UC Davis CS?"
        ),
        "expected_answer": (
            "No. The collected documents focus on UCSC CS courses, professors, requirements, "
            "and student experiences. Unless one of the collected sources specifically discusses "
            "UC Davis, the system should say it does not have enough information to make a "
            "grounded comparison between UCSC CS and UC Davis CS. It should not guess using "
            "outside knowledge."
        ),
        "top_k": 5,
    },
]


def format_sources(sources: list[str]) -> str:
    """Format source filenames as a markdown bullet list."""
    if not sources:
        return "- none"
    return "\n".join(f"- {source}" for source in sources)


def format_retrieved_chunks(chunks: list[dict]) -> str:
    """Format retrieved chunk details for the evaluation report."""
    if not chunks:
        return "_No chunks retrieved._"

    sections = []
    for chunk in chunks:
        preview = chunk.get("text", "")[:PREVIEW_LENGTH]
        if len(chunk.get("text", "")) > PREVIEW_LENGTH:
            preview += "..."

        sections.append(
            "\n".join(
                [
                    f"**Rank:** {chunk.get('rank')}",
                    f"**Distance:** {chunk.get('distance', 0):.6f}",
                    f"**Source:** {chunk.get('source')}",
                    f"**Chunk ID:** {chunk.get('chunk_id')}",
                    "",
                    "**Text preview:**",
                    "```text",
                    preview,
                    "```",
                ]
            )
        )

    return "\n\n".join(sections)


def format_question_section(case: dict, result: dict) -> str:
    """Format one evaluation question and its results."""
    return "\n".join(
        [
            f"## Question {case['number']}",
            "",
            f"**Question:** {case['question']}",
            "",
            f"**Top-k:** {case['top_k']}",
            "",
            "**Expected answer:**",
            case["expected_answer"],
            "",
            "**System answer:**",
            result["answer"],
            "",
            "**Sources used:**",
            format_sources(result["sources"]),
            "",
            "**Retrieved chunks:**",
            format_retrieved_chunks(result["retrieved_chunks"]),
            "",
            "**Accuracy judgment:**",
            "",
            "**Notes:**",
            "",
            "---",
            "",
        ]
    )


def run_evaluation() -> str:
    """Run all evaluation questions and return the full markdown report."""
    sections = [
        "# Evaluation Results — The Unofficial Guide",
        "",
        "Fill in **Accuracy judgment** and **Notes** for each question after reviewing.",
        "",
    ]

    for case in EVALUATION_CASES:
        print(f"Running question {case['number']} (top_k={case['top_k']})...")
        result = ask(case["question"], top_k=case["top_k"])
        sections.append(format_question_section(case, result))

    return "\n".join(sections)


def main() -> int:
    try:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        report = run_evaluation()
        OUTPUT_PATH.write_text(report, encoding="utf-8")

        print("\nEVALUATION SUMMARY")
        print("=" * 60)
        print(f"Questions evaluated: {len(EVALUATION_CASES)}")
        print(f"Report saved to:     {OUTPUT_PATH.resolve()}")
        print("=" * 60)
        return 0
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        return 1
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
