# The Unofficial Guide — Project 1

---

## Domain

The Unofficial Guide covers UCSC Computer Science courses and professors. It helps students answer questions about which CSE classes are useful, which professors students recommend, workload and difficulty, official B.S. requirements, and broader student experiences in the major.

This knowledge is valuable because official UCSC pages describe requirements and course listings, but they do not capture the informal advice students share about professor teaching style, class difficulty, project load, and which electives matter for jobs or research. Reddit threads, student guides, and peer-written course reviews fill that gap, but they are scattered and hard to search. This RAG system combines official and unofficial sources so answers stay grounded in collected documents rather than generic outside knowledge.

---

## Document Sources

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Official UCSC Page — UCSC CS Major Introduction | Web | https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/computer-science-and-engineering/computer-science-bs |
| 2 | Official UCSC Page — UCSC CSE Course Catalogue | Web | https://catalog.ucsc.edu/en/current/general-catalog/courses/cse-computer-science-and-engineering |
| 3 | Reddit — Important CS Classes | Web (manual `.txt`) | https://www.reddit.com/r/UCSC/comments/13imo75/what_are_the_most_important_cs_classes_yall_took/ |
| 4 | Github — UCSC CS Student Guide | Web | https://github.com/williamsantosa/ucsc-cs#professors |
| 5 | Reddit — UCSC CS Major FAQ | Web (manual `.txt`) | https://www.reddit.com/r/UCSC/comments/1j3k9qx/questions_about_computer_science_ucsc/ |
| 6 | Reddit — How is UCSC CS Program | Web (manual `.txt`) | https://www.reddit.com/r/UCSC/comments/120x5m1/cs_major_how_is_ucsc_program/ |
| 7 | Reddit — Example CS Path | Web (manual `.txt`) | https://www.reddit.com/r/UCSC/comments/ui7qpy/the_classes_i_took_for_my_computer_science_bs/ |
| 8 | PDF — CS Degree Curriculum Chart | PDF / `.txt` extract | `data/raw/CS_BS_24-25.pdf`, `data/raw/pdf_cs_degree_curriculum_chart.txt` |
| 9 | Reddit — "Best" Professors | Web (manual `.txt`) | https://www.reddit.com/r/UCSC/comments/1271hpo/who_are_the_best_teachers_for_cs_at_ucsc/ |
| 10 | Official UCSC Page — Official UCSC CS Faculty | Web | https://engineering.ucsc.edu/departments/computer-science-and-engineering/people/ |

**Total sources collected:** 10

Reddit pages were not reliably scrapeable with `requests`, so those threads were manually copied into cleaned `.txt` files in `data/raw/`.

---

## Chunking Strategy

**Chunk size:** ~1000 characters (target range from planning: 900–1200 characters)

**Overlap:** ~200 characters (planning range: 150–200 characters), applied at sentence or paragraph boundaries when possible

**Why these choices fit your documents:**

Many sources are Reddit comments, student guide sections, or catalog paragraphs where useful information appears in short opinion-based blocks. A ~1000-character target is large enough to keep course numbers, professor names, and student opinions together, but small enough for retrieval to match specific questions. Overlap helps when context such as a CSE number or professor name appears near a chunk boundary.

**Preprocessing before chunking (`src/ingest.py`):**

- Loaded all `.txt` files from `data/raw/`
- Parsed `Source`, `Description`, and `URL` headers from each file
- Normalized whitespace and removed empty lines
- Removed Reddit UI words such as Upvote, Downvote, Award, Share, and avatar
- Removed obvious webpage boilerplate lines from GitHub and UCSC catalog pages (for example: Skip to content, Fork, Star, Catalog Links)
- Saved cleaned full documents to `data/processed/cleaned_docs.jsonl`
- Chunked with paragraph-aware logic: combine paragraphs until near target size; split long paragraphs by sentences; merge tiny chunks under 150 characters when possible

**Final chunk count:** 262 chunks across 10 source documents

Sample chunks are saved in `data/processed/sample_chunks.txt`.

---

## Embedding Model

**Model used:** `sentence-transformers/all-MiniLM-L6-v2`

This model runs locally, is free, and is fast enough for a class project with 262 chunks. Embeddings are created in `src/build_vector_store.py` and stored in a persistent ChromaDB collection named `ucsc_cs_guide` at `data/chroma_db/`.

**Production tradeoff reflection:**

If cost were not a constraint and this were deployed for real UCSC students, I would compare embedding models on retrieval accuracy for informal student language, exact course/professor name matching, latency, and context length. Reddit-style text, abbreviations, and CSE numbers are harder for small general-purpose models than for larger or domain-tuned embeddings. I would also weigh local inference versus an API-hosted embedding service based on update frequency, privacy, and operating cost.

---

## Grounded Generation

**System prompt grounding instruction:**

`src/query.py` uses Groq model `llama-3.3-70b-versatile` with a system prompt that instructs the model to:

- Answer using only the retrieved context
- Not use outside knowledge
- Say exactly *"I don't have enough information in the provided sources to answer that."* when context is insufficient
- Cite source filenames when making claims
- Not invent course names, professor names, requirements, or comparisons

**Mechanism:**

1. `ask()` in `src/query.py` calls `retrieve(question, top_k=top_k)` from `src/retrieve.py`
2. Retrieved chunks are formatted into a context block with source filename and chunk ID headers
3. The question and context are sent to Groq in a single user message
4. The model is constrained to answer only from that context

**How source attribution is surfaced in the response:**

Source attribution is programmatically guaranteed. Unique source filenames are taken from retrieved chunk metadata, not from free-form LLM output. After generation, `src/query.py` appends a **Sources used:** section listing those filenames. The Gradio app in `app.py` also displays sources separately from the answer.

Because generation only sees retrieved chunks, broad or imperfect retrieval sometimes limits answer completeness rather than causing hallucinated facts.

---

## Evaluation Report

Evaluation was run with `src/run_evaluation.py` and saved to `data/processed/evaluation_results.md`. Default `top_k=5` was used for questions 1, 2, 3, and 5. Question 4 used `top_k=10` because manual testing showed official requirement questions needed more retrieved context.

| # | Question | Expected answer (summarized) | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|------------------------------|------------------------------|-------------------|-------------------|
| 1 | Which UCSC CSE classes do students mention as especially important for CS majors? | CSE 130/Harrison, CSE 113/Sorensen, CSE 186–187/Harrison, CSE 138/Kuper, plus interest-area electives | Mentioned CSE 101 as a required course and listed general CSE classes from the GitHub guide; missed key Reddit recommendations such as CSE 113, CSE 138, and job-focused full-stack advice | Partially relevant — missed `reddit_important_cs_classes.txt` | Partially accurate |
| 2 | What are common pros and cons students mention about UCSC CS? | Pros: strong professors, class priority, frequent offerings; cons: late specialization, unclear core focus, housing cost/availability | Correctly named class priority, frequent offerings, and strong professors; mentioned rigor/preparation cons but missed housing and late-specialization negatives | Partially relevant — mostly one Reddit thread | Partially accurate |
| 3 | Which professors or teachers are recommended by students? | Sesh, Fremont, Harrison, Sorensen, Kuper, Tantalo, De Alfaro, Miller, Qian, Alvaro; Harrison mixed but valuable | Named Sesh, Fremont, Harrison, Sorensen, Kuper, and Tantalo; missed several professors and did not fully explain Harrison’s mixed reputation | Partially relevant — best chunk ranked #2, weaker GitHub chunk ranked #1 | Partially accurate |
| 4 | What official requirements or course categories are listed for the UCSC CS B.S.? | Lower-division programming, math, upper-division core, DC, capstone, four electives, plus elective restrictions | Mentioned GE, major requirements, transfer GPA rules, physics, and grade rules; did not list full curriculum categories | Partially relevant — retrieved weaker PDF chunk instead of main curriculum-chart chunk | Partially accurate |
| 5 | Does the system have enough information to compare UCSC CS to UC Davis CS? | No — sources are UCSC-only; should refuse comparison | Correctly refused: *"I don't have enough information in the provided sources to answer that."* | Relevant for refusal — retrieved UCSC-only chunks and no UC Davis comparison evidence | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

**Overall:** The system grounded answers well and refused the out-of-scope comparison question. Its main weakness was retrieval on broad queries: GitHub boilerplate, general catalog chunks, or the wrong PDF chunk sometimes ranked above the most directly relevant Reddit or curriculum-chart evidence. When retrieval missed key chunks, answers were incomplete but usually still grounded.

---

## Example Responses

**Successful query 1:** “Which UCSC CSE classes are useful for jobs?”  
The system recommended CSE 186/187 for full-stack development, CSE 180 for databases, CSE 144/142 for AI/ML, CSE 121 for embedded, CSE 183 for mobile apps, and the CSE 115 series for project experience.  
**Sources shown:** `reddit_important_cs_classes.txt`, `reddit_example_cs_path.txt`, `reddit_how_is_ucsc_cs_program.txt`, `github_ucsc_cs_student_guide.txt`

**Successful query 2:** “What do students say about Harrison's classes?”  
The system said students have mixed opinions about Harrison: some recommend him and say his classes help students “level up,” while others describe his classes as demanding or strict.  
**Sources shown:** `reddit_example_cs_path.txt`, `reddit_best_professors.txt`, `reddit_how_is_ucsc_cs_program.txt`

**Out-of-scope query:** “Compare UCSC CS to UC Davis CS. Which one is better?”  
**System response:** “I don't have enough information in the provided sources to answer that.”

---

## Failure Case Analysis

**Question that failed:**

What official requirements or course categories are listed for the UCSC CS B.S.?

**What the system returned:**

A partially accurate answer mentioning general education, major requirements, transfer qualification/GPA information, physics requirements, and grade rules. It did not list the full expected curriculum categories: lower-division programming courses, math courses, upper-division core courses, four upper-division electives, Disciplinary Communication requirement, and comprehensive/capstone requirement.

**Root cause (tied to a specific pipeline stage):**

Retrieval stage. The relevant information existed in `pdf_cs_degree_curriculum_chart.txt`, including a stronger chunk (`pdf_cs_degree_curriculum_chart_0001`) listing lower-division programming, math, and upper-division core courses. Instead, retrieval surfaced weaker chunks such as `pdf_cs_degree_curriculum_chart_0006` (physics and grade rules), plus general GitHub and official catalog chunks. Because `src/query.py` forces the LLM to answer only from retrieved context, generation stayed grounded but incomplete.

**What you would change to fix it:**

- Add source-type filtering or query rewriting for official requirement questions so PDF/catalog chunks rank higher
- Improve chunk labels/metadata during ingestion (for example: `section=lower_division_programming`, `section=upper_division_core`)
- Split or relabel the PDF curriculum chart by section so requirement categories are easier to retrieve as standalone chunks

---

## Spec Reflection

**One way the spec helped you during implementation:**

`planning.md` forced me to define the domain, source list, chunk size, overlap, embedding model, top-k, evaluation questions, and expected answers before writing pipeline code. That made it easier to prompt AI tools with concrete requirements and verify each milestone against the spec instead of improvising the architecture while coding.

**One way your implementation diverged from the spec, and why:**

Two main divergences. First, Reddit pages were not reliably scrapeable with `requests` and BeautifulSoup, so I manually cleaned Reddit threads into `.txt` files instead of fully automated scraping. Second, during evaluation I used `top_k=10` for the official requirements question because `top_k=5` did not retrieve enough official context; the spec assumed top-k=5 for all queries, but one question needed more chunks.

---

## AI Usage

**Instance 1**

- *What I gave the AI:* My chunking strategy, document list, and architecture notes from `planning.md`; asked for ingestion and chunking code.
- *What it produced:* Scripts for loading raw documents, cleaning text, chunking, and writing `cleaned_docs.jsonl` and `chunks.jsonl` (`src/ingest.py`, plus scraping helpers).
- *What I changed or overrode:* I manually cleaned Reddit files, inspected chunks with `src/inspect_chunks.py` and `src/inspect_chunks_by_source.py`, improved boilerplate removal in `src/ingest.py`, and generated `data/processed/sample_chunks.txt` for README inspection.

**Instance 2**

- *What I gave the AI:* My retrieval approach from `planning.md`; asked for ChromaDB + `all-MiniLM-L6-v2` embedding and retrieval code.
- *What it produced:* `src/build_vector_store.py`, `src/retrieve.py`, and `src/test_retrieval.py`.
- *What I changed or overrode:* I tested retrieval on all 5 evaluation questions, noticed imperfect results for professor and official requirement queries, documented limitations in `data/processed/retrieval_notes.txt`, and used those results to guide final evaluation.

**Instance 3**

- *What I gave the AI:* Grounding requirements, evaluation questions, and architecture diagram; asked for Groq generation and a Gradio UI.
- *What it produced:* `src/query.py`, `app.py`, and `src/run_evaluation.py`.
- *What I changed or overrode:* I verified out-of-scope refusal on the UC Davis comparison question, confirmed programmatic source attribution, and manually judged accuracy in `data/processed/evaluation_results.md`.

---

## How to Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env` in the project root:

```bash
GROQ_API_KEY=your_key_here
```

Build and test the pipeline:

```bash
python src/ingest.py
python src/build_vector_store.py
python src/test_retrieval.py
python src/run_evaluation.py
python app.py
```

- `src/ingest.py` — clean and chunk raw documents
- `src/build_vector_store.py` — embed chunks into ChromaDB
- `src/test_retrieval.py` — retrieval-only evaluation
- `src/run_evaluation.py` — full RAG evaluation with Groq
- `app.py` — Gradio demo interface

---

## Demo Video

Demo video: https://youtu.be/yfXBheGHIzM 
