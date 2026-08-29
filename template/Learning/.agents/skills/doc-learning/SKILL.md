---
name: doc-learning
description: Turn documents, articles, PDFs, slides, or lesson text into source-backed notes inside a Learning agent space. Use for ingesting reading material; do not use for coding-repository context or video production.
---

# Document Learning

Work inside the current Learning agent space. Read its `AGENTS.md` and existing
index/template notes before proposing changes. Do not search for or modify other
agent spaces unless the user explicitly expands the scope.

## Workflow

1. Identify the source, author/date when known, access rights, and reliability.
2. Inspect nearby courses and concepts before proposing new pages.
3. Present a compact write proposal: source location, pages to create or merge,
   links to add, uncertain claims, and expected learning value.
4. Write only after the user approves that proposal, unless the current request
   already explicitly authorizes ingest-and-write.
5. Preserve the source under `Raw/`; keep `Courses/` and `Concepts/` distilled.
   Add a concept only when it is reusable beyond this source.
6. Link the source, lesson, concepts, recall prompts, and open questions with
   reciprocal `[[wikilinks]]` where they help navigation.
7. Report changed files, evidence, confidence, and factual spot checks.

Use adaptive depth. A short source may need five bullets; a foundational source
may need a full lesson. Distinguish source claims from explanations and examples.
Label uncertain extraction rather than silently repairing it.

Never store secrets, private customer data, or unauthorized/paywalled source
material. A link and personal notes are safer than copying restricted content.
