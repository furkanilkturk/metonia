---
name: project-planning
description: Create, review, or deliberately persist a durable company/project plan in a Metonia Work space; do not use for transient coding checklists, agent status, or session logs.
---

# Project Planning

Create plans only for work worth retaining beyond the current agent session.
The runtime execution plan stays in the repository or Pi session; Obsidian
receives the stable goal, constraints, decisions, milestones, validation, and
ownership that people should revisit.

## Resolve ownership

1. Read the nearest `AGENTS.md`, then the `## Context capsule` in `Project.md`
   and parent `Company.md`.
2. From an external repository, use `metonia_context` with `profile: planning`
   and require exactly one repository match. Do not guess a company or project.
3. Inspect the returned `Context index`; load only notes whose `load when`
   condition matches this plan by making a second `metonia_context` call with
   `profile: planning` and the exact `project:` or `company:` `contextNotes`
   target plus `notesOnly: true`. Do not repeat base context or scan every
   linked plan/context note.
4. Save project plans under
   `Work/Companies/<Company>/Projects/<Project>/Plans/`. Put a genuinely
   cross-project plan at company level only with explicit approval.

## Plan and persist

1. Treat open/deferred decision and improvement IDs as explicit planning
   inputs. Carry relevant IDs into the plan; never silently resolve them.
2. Use `metonia-interview` on material uncertainty before drafting: desired
   outcome, boundaries, decision owner, dependencies, validation, risks, and
   approval points.
3. Draft a compact plan with this structure: frontmatter (`type: plan`,
   `status`, `company`, `project`, `created`, `updated`), then Outcome,
   Constraints, Decisions, Milestones, Validation, Risks and approvals, Open
   questions, and Evidence/links.
4. Use checkboxes only for durable milestones. Never store child-agent status,
   worktree paths, event IDs, token usage, command logs, or a chat transcript.
5. Preview the exact target path and full proposed note. Write only after user
   approval unless the request explicitly names and approves that plan write.
6. Use `YYYY-MM-DD-short-title.md`; preserve existing notes and create a new
   revision or supersession link rather than silently replacing an accepted
   plan.
7. After writing, link the plan from `Project.md` and report both changed paths.

If the work is still exploratory or likely to expire with the current session,
keep it out of Obsidian and explain why.
