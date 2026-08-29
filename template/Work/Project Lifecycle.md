---
tags: [work, projects, workflow]
status: stable
---

# Project lifecycle

Project registration and knowledge curation run from the Work agent space, not
inside every coding session. Start Pi from `Work/` (or a descendant) so
`project-learning` and `project-planning` are discovered. Point the workflow at
the repository when it lives elsewhere. This keeps Learning and Video skills
out of coding-agent context.

## Register an existing project

1. Confirm that the repository has its intended canonical Git remote.
2. Either start Pi from `Work/`, or load only the curator skill while starting
   Pi directly inside the external repository:

   ```powershell
   pi --skill "$env:METONIA_VAULT\Work\.agents\skills\project-learning"
   ```

   The explicit load applies only to this registration session, so normal
   coding sessions remain lean.
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
3. Start Pi from `Work/`, or start it inside the repository with the same
   one-session `--skill` command above, and invoke
   `/skill:project-learning register-new`.
4. Review the proposed company/project skeleton and approve the exact write.

Registration does not initialize, clone, move, or modify the repository. It
creates the durable Metonia mapping around a repository that already exists.

## Update knowledge after project changes

1. Finish implementation, tests, and review in the coding repository.
2. In a separate Work curator session, or from the repository with the same
   one-session `--skill` command above, invoke
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
