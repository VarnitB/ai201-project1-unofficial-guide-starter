"""Gradio interface for The Unofficial Guide RAG system."""

import sys
from pathlib import Path

import gradio as gr

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from query import ask, strip_llm_sources_section

PREVIEW_LENGTH = 300
EXAMPLE_QUESTIONS = [
    "Which UCSC CSE classes are useful for jobs?",
    "Which professors are recommended by students?",
    "What are common pros and cons students mention about UCSC CS?",
    "What official requirements are listed for the UCSC CS B.S.?",
    "Compare UCSC CS to UC Davis CS. Which one is better?",
]


def format_sources(sources: list[str]) -> str:
    """Format source filenames as a bullet list."""
    if not sources:
        return "No sources retrieved."
    return "\n".join(f"- {source}" for source in sources)


def format_retrieved_chunks(chunks: list[dict]) -> str:
    """Format retrieved chunk debug info with short previews."""
    if not chunks:
        return "No chunks retrieved."

    sections = []
    for chunk in chunks:
        preview = chunk.get("text", "")[:PREVIEW_LENGTH]
        if len(chunk.get("text", "")) > PREVIEW_LENGTH:
            preview += "..."

        sections.append(
            "\n".join(
                [
                    f"Rank: {chunk.get('rank')}",
                    f"Distance: {chunk.get('distance', 0):.6f}",
                    f"Source: {chunk.get('source')}",
                    f"Chunk ID: {chunk.get('chunk_id')}",
                    "Preview:",
                    preview,
                ]
            )
        )

    return "\n\n" + ("-" * 40 + "\n\n").join(sections)


def handle_question(question: str, top_k: int) -> tuple[str, str, str]:
    """Run ask() and format outputs for the Gradio UI."""
    question = question.strip()
    if not question:
        return (
            "Please enter a question.",
            "",
            "",
        )

    try:
        result = ask(question, top_k=int(top_k))
    except FileNotFoundError as exc:
        return (f"Error: {exc}", "", "")
    except ValueError as exc:
        return (f"Error: {exc}", "", "")

    answer = strip_llm_sources_section(result["answer"])
    sources = format_sources(result["sources"])
    chunks = format_retrieved_chunks(result["retrieved_chunks"])
    return answer, sources, chunks


def build_app() -> gr.Blocks:
    """Create the Gradio Blocks interface."""
    with gr.Blocks(title="The Unofficial Guide") as demo:
        gr.Markdown(
            "# The Unofficial Guide\n"
            "Ask questions about UCSC Computer Science courses and professors."
        )

        question = gr.Textbox(
            label="Ask a question about UCSC CS courses/professors",
            lines=3,
            placeholder="Example: Which CSE classes do students recommend?",
        )
        top_k = gr.Slider(
            minimum=1,
            maximum=10,
            value=5,
            step=1,
            label="Top-k retrieved chunks",
        )
        ask_button = gr.Button("Ask", variant="primary")

        answer_output = gr.Textbox(label="Answer", lines=10)
        sources_output = gr.Textbox(label="Sources used", lines=6)
        chunks_output = gr.Textbox(label="Retrieved chunks (debug)", lines=16)

        ask_button.click(
            fn=handle_question,
            inputs=[question, top_k],
            outputs=[answer_output, sources_output, chunks_output],
        )
        question.submit(
            fn=handle_question,
            inputs=[question, top_k],
            outputs=[answer_output, sources_output, chunks_output],
        )

        gr.Examples(
            examples=[[example, 5] for example in EXAMPLE_QUESTIONS],
            inputs=[question, top_k],
        )

    return demo


if __name__ == "__main__":
    app = build_app()
    app.launch()
