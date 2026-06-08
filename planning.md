# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Unofficial Guide to UCSC Computer Science Courses and Professors: This system helps UCSC CS students answer questions about which CSE classes/professors are difficult, helpful, project-heavy, exam-heavy, or good for specific goals like interviews, research, or electives.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source             | Description                | URL or location |
|---|--------------------|----------------------------|-----------------|
| 1 | Official UCSC Page | UCSC CS Major Introduction | https://catalog.ucsc.edu/en/current/general-catalog/academic-units/baskin-engineering/computer-science-and-engineering/computer-science-bs |
| 2 | Official UCSC Page | UCSC CSE Course Catalogue  | https://catalog.ucsc.edu/en/current/general-catalog/courses/cse-computer-science-and-engineering |
| 3 | Reddit             | Important CS Classes       | https://www.reddit.com/r/UCSC/comments/13imo75/what_are_the_most_important_cs_classes_yall_took/ |
| 4 | Github             | UCSC CS Student Guide      | https://github.com/williamsantosa/ucsc-cs#professors
| 5 | Reddit             | UCSC CS Major FAQ          | https://www.reddit.com/r/UCSC/comments/1j3k9qx/questions_about_computer_science_ucsc/ |
| 6 | Reddit             | How is UCSC CS Program     | https://www.reddit.com/r/UCSC/comments/120x5m1/cs_major_how_is_ucsc_program/ |
| 7 | Reddit             | Example CS Path            | https://www.reddit.com/r/UCSC/comments/ui7qpy/the_classes_i_took_for_my_computer_science_bs/ |
| 8 | PDF                | CS Degree Curriculum Chart | data/raw/CS_BS_24-25.pdf |
| 9 | Reddit             | "Best" Professors          |  https://www.reddit.com/r/UCSC/comments/1271hpo/who_are_the_best_teachers_for_cs_at_ucsc/ |
| 10 | Official UCSC Page| Official UCSC CS Faculty   | https://engineering.ucsc.edu/departments/computer-science-and-engineering/people/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** around 900–1200 characters, or about 150–250 words.

**Overlap:** around 150–200 characters, or one sentence/short paragraph of overlap.

**Reasoning:** Paragraph-aware chunking instead of splitting every fixed number of characters. Many sources are Reddit comments or guide sections where useful information appears in short opinion-based paragraphs. A 900–1200 character target is large enough to preserve context, such as course name + professor + student opinion, but small enough that retrieval can still match specific questions. The overlap helps when important context, like a course number or professor name, appears near a chunk boundary.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** sentence-transformers/all-MiniLM-L6-v2

**Top-k:** 5

**Production tradeoff reflection:** I am using all-MiniLM-L6-v2 because it runs locally, is free, and is fast enough for this project. I will retrieve the top 5 chunks for each query because that should give the LLM enough context without flooding it with loosely related text. In a production system, I would compare embedding models based on retrieval accuracy, context length, latency, cost, and whether the model handles informal student language well. Since this domain includes Reddit-style writing, slang, abbreviations, and course numbers, I would care about how well the embedding model handles short informal text and exact course/professor names.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Which UCSC CSE classes do students mention as especially important for CS majors? | Students mention CSE 130 with Harrison as useful for systems, CSE 113 with Sorensen for multithreading, CSE 186/CSE 187 with Harrison for full-stack web development, and CSE 138 with Kuper for distributed systems, microservices, and REST APIs. The strongest recommendations are CSE 138 and full-stack web development because students say those apply to a broader set of jobs. Other recommended classes depend on interest area, such as CSE 150/156 for networking, CSE 140/144 for AI/ML, CSE 160/164/168 for graphics/computer vision, CSE 104/105 for math, and CSE 180/181 for databases. (citation) |
| 2 | What are common pros and cons students mention about UCSC CS? | Students describe UCSC CS positively overall, saying the program has good younger professors, interesting classes, high class-enrollment priority for declared CS majors, and many required CS classes offered frequently. Students also say it is possible to build strong skills if you choose challenging classes and professors carefully. Common negatives are that students do not get to specialize until later in the major, the core classes may not clearly show what area of CS to pursue, housing in Santa Cruz is limited and expensive, and students need to plan early for both classes and housing. (citation) |
| 3 | Which professors or teachers are recommended by students in the collected sources? | Students recommend Sesh, Fremont, Harrison, Sorensen, Kuper, Tantalo, De Alfaro, Miller, Qian, and Alvaro. Harrison receives the strongest mixed recommendation: students say his classes are hard and demanding, but that students “level up” as software engineers after taking his classes, especially full-stack or systems courses. Sorensen and Kuper are recommended for interesting upper-division electives, and Alvaro is mentioned positively for CSE 138. (citation) |
| 4 | What official requirements or course categories are listed for the UCSC CS B.S.? | The UCSC CS B.S. curriculum includes lower-division programming courses such as CSE 20, CSE 30, CSE 12, and CSE 13S; math courses such as calculus, discrete math, linear algebra, and probability/statistics; upper-division core courses such as CSE 101, CSE 102, CSE 103, CSE 114A, CSE 120, and CSE 130; a Disciplinary Communication requirement; a comprehensive/capstone requirement; and four upper-division electives. The curriculum chart also says upper-division electives are generally 5-credit upper-division CSE/CE courses numbered 100–189, CSE 195, or approved computational media/math electives, with some restrictions. (citation) |
| 5 | Does the system have enough information to compare UCSC CS to UC Davis CS? | No. The collected documents focus on UCSC CS courses, professors, requirements, and student experiences. Unless one of the collected sources specifically discusses UC Davis, the system should say it does not have enough information to make a grounded comparison between UCSC CS and UC Davis CS. It should not guess using outside knowledge. (citation) |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Some sources are noisy or informal, especially Reddit threads. They may include jokes, outdated advice, deleted comments, or opinions that conflict with each other. This could make retrieval return chunks that sound relevant but are not reliable enough to answer the question clearly.

2. Course numbers and professor names may be hard for semantic search. A query like “Is CSE 101 useful for interviews?” might not retrieve the right chunk if the document says “algorithms” but does not repeat “interviews,” or if the course number appears far away from the opinion. I will need to inspect retrieved chunks and adjust chunk size/overlap if important context gets split.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->


Document Ingestion
(raw .txt, PDF, Reddit pages, UCSC pages)
        |
        |  Load files / extract text
        |  Tools: Python, requests/BeautifulSoup if needed, pdfplumber for PDFs
        v
Cleaning + Preprocessing
(remove HTML, nav text, repeated headers, empty lines)
        |
        v
Chunking
(paragraph-aware chunks, ~900-1200 characters, ~150-200 character overlap)
        |
        v
Embedding + Vector Store
(embed chunks with sentence-transformers/all-MiniLM-L6-v2)
(store vectors + metadata in ChromaDB)
        |
        v
Retrieval
(user question -> retrieve top-k=5 relevant chunks with source metadata)
        |
        v
Grounded Generation
(Groq llama-3.3-70b-versatile answers using only retrieved chunks)
        |
        v
Query Interface
(Gradio app showing answer + cited sources)


---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

I plan to use ChatGPT and Cursor to help implement the ingestion and chunking script. I will give the AI my Documents section, Chunking Strategy section, and Architecture diagram. I will ask it to write Python code that loads .txt and .pdf files from data/raw/, cleans the text, attaches source metadata, and creates paragraph-aware chunks using my chosen chunk size and overlap. I will verify the output by printing at least 5 random chunks and checking that they are readable, substantive, and not filled with HTML, navigation text, or fragments.

**Milestone 4 — Embedding and retrieval:**

I plan to use ChatGPT and Cursor to help implement the embedding and retrieval code. I will give the AI my Retrieval Approach section and Architecture diagram. I will ask it to use sentence-transformers/all-MiniLM-L6-v2 to embed the chunks and store them in ChromaDB with metadata for source name and chunk index. I will verify the code by running at least 3 evaluation questions and checking whether the top returned chunks are actually relevant before adding generation.

**Milestone 5 — Generation and interface:**

I plan to use ChatGPT and Cursor to help connect retrieval to grounded response generation and a simple interface. I will give the AI my grounding requirement, evaluation questions, and Architecture diagram. I will ask it to create a function that retrieves the top chunks, sends only those chunks to Groq’s llama-3.3-70b-versatile, and returns an answer with visible source attribution. I will also ask for a simple Gradio interface with a question input, answer output, and source list. I will verify the system by asking both answerable questions and out-of-scope questions to make sure it does not hallucinate.