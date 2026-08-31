---
tags: [work, projects, workflow]
status: stable
---

# Project lifecycle

`project-learning` is package-global so registration and knowledge curation can
start directly inside any Git repository. Its description is discoverable, but
its full workflow is loaded only when invoked. `project-planning` remains scoped
to `Work/`, while Learning and Video skills stay out of coding-agent context.

## Register an existing project

1. Confirm that the repository has its intended canonical Git remote.
2. Start Pi directly inside the repository, or from `Work/` when curating a
   repository elsewhere.
3. Invoke `/skill:project-learning register-existing`. Include the repository
   path when Pi is running from `Work/`; the current directory is used when Pi
   is running inside the repository.
4. The skill inventories every tracked file and directory before semantic
   reading. It records the repository HEAD/tree, dirty paths, remotes, category
   counts, and a deterministic inventory hash so no file family disappears
   from coverage merely because it was not sampled.
5. Choose who performs the semantic discovery in Pi's native selector. It
   offers the current agent when it fits, an automatic authenticated choice, a
   short exact list, and `Other`, which searches every fitting model available to the
   current Pi session—including models the shortlist did not anticipate. A
   delegated choice is exact and task-scoped; the child is read-only and the
   parent still validates evidence, asks questions, and owns every vault write.
6. The semantic pass follows authoritative instructions, manifests,
   composition roots, schemas, routes, tests, delivery files, and representative
   domain slices. It separates current code, normative rules, intended plans,
   generated artifacts, and historical material.
7. For a mature repository, require a compact `Project.md` plus focused notes
   for repository ownership, engineering contracts, product/domain behavior,
   and delivery/operations. Every non-empty inventory category must be marked
   covered, generated, vendor, not applicable, or an open question with
   evidence. Small repositories may use fewer notes when the same coverage is
   explicit.
8. If one high-consequence pattern conflict exists, answer or defer the
   selectable question. The answer receives a stable decision/improvement ID;
   later plans must consult it instead of rediscovering the chat.
9. Approve or correct the identity mapping and engineering claims separately.
   Registration rechecks repository HEAD/dirty paths and target-note fingerprints
   before writing.
10. Future coding sessions use the compact `coding` context profile by default;
   planning adds the queue/index and `full` is an explicit whole-note review.
   A matching indexed note is fetched in a second `notesOnly` call with an
   explicit `project:` or `company:` target, so base context is not duplicated.

If the company already exists, the project inherits it. Do not duplicate
company policy in `Project.md`.

## Register a new project

1. Create and initialize the repository through the normal development flow.
2. Decide its company, name, outcome, boundaries, owner, and canonical remote.
3. Start Pi inside the repository and invoke
   `/skill:project-learning register-new`, or include its path from `Work/`.
4. Review the proposed company/project skeleton and approve the exact write.

Registration does not initialize, clone, move, or modify the repository. It
creates the durable Metonia mapping around a repository that already exists.

## Update knowledge after project changes

1. Finish implementation, tests, and review in the coding repository.
2. In a clean curator session inside the repository, invoke
   `/skill:project-learning propose-update` with the verified change evidence.
3. Regenerate the structural inventory and compare its HEAD, tree, hash,
   categories, and dirty paths with the last recorded provenance. Review
   semantically only the changed categories and any contracts they affect.
4. Accept only facts that will remain useful: package usage contracts,
   architecture boundaries, operating rules, accepted decisions,
   quality/release practice, or a changed repository identity. Put detailed
   examples behind a context-index link with a precise `load when` condition.
5. Review the exact proposal, then approve the selected `Company.md`,
   `Project.md`, or focused context-note edits.

Do not copy task status, diffs, chat, logs, tokens, temporary paths, or an
unreviewed inference into company/project knowledge.

## Create a durable plan

Invoke `/skill:project-planning` from the matched Work project. Use
`metonia-interview` when goals or tradeoffs are still consequential. Preview the
full note, then save an approved plan under:

```text
Work/Companies/<Company>/Projects/<Project>/Plans/YYYY-MM-DD-short-title.md
```

Link the result from `Project.md`. Save only stable outcomes, constraints,
decisions, milestones, validation, risks, approvals, and ownership. A checklist
used only by the active coding session stays in the repository or Pi session.
