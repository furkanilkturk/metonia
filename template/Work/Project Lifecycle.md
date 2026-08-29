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
4. The skill inspects the repository and proposes the company, project name,
   canonical remote, outcome, boundaries, and exact target files.
5. Approve or correct the proposal. Registration writes only after the company,
   project, remote, and paths are explicit.
6. Future coding sessions may use `metonia_context` from that repository to
   load only the matched `Company.md` and `Project.md` on demand.

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
3. Accept only facts that will remain useful: architecture boundaries,
   operating rules, accepted decisions, quality/release practice, or a changed
   repository identity.
4. Review the exact proposal, then approve the selected `Company.md` or
   `Project.md` edits.

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
