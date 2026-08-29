---
tags: [project, example]
status: fictional-example
company: Example Company
repository: https://github.com/example-company/atlas-notes.git
repositories: []
context_schema: 1
sensitivity: public
---

# Atlas Notes

## Parent company

- Company: [[Company|Example Company]]
- This project inherits the operating model, privacy expectations, and release
  practices in its parent `Company.md`.

## Context capsule

- Outcome: expose a note's lineage without revealing private source content.
- Identity, billing, and cross-workspace migrations are outside this project.
- The nearest `AGENTS.md` and this Project page govern project-local work;
  company privacy and approval rules remain inherited.
- Retrieval must preserve workspace boundaries and fail closed when lineage
  authorization is ambiguous.
- Customer-visible data-handling changes follow the company privacy review path.
- Keep transient implementation checklists and test snapshots in the repository,
  not in this page.

## Outcome and boundaries

- Outcome: make note lineage visible without exposing private source content.
- In scope: a fictional note-history experience and its retrieval behavior.
- Out of scope: identity, billing, and cross-workspace migrations.
- Owner: fictional Atlas Notes team.

## Repository and systems

- Canonical remote: `https://github.com/example-company/atlas-notes.git`
- The repository frontmatter above is the context resolver's canonical identity.
- Authoritative product requests and incident records remain outside this vault.

## Working agreements

- Review changes that affect lineage visibility, tests for key retrieval paths,
  and provide a rollback note for customer-visible releases.
- Escalate ambiguous data handling to the company privacy review path.

## Decisions and improvement queue

| ID | State | Decision or improvement | Evidence | Planning trigger |
|---|---|---|---|---|
| ATLAS-001 | accepted-constraint | Lineage visibility must not reveal private source content. | Project outcome and company privacy policy | Any retrieval or sharing change |

## Context index

- No optional engineering note is needed for this compact fictional example.

## Durable plans

- Planning index: [[Plans/README]]
- No active durable plan; ordinary implementation checklists stay in the
  repository or Pi session.

## Review

- Last verified: fictional example, 2026-08-29.
- Review when the repository remote, outcome, or company policy changes.
