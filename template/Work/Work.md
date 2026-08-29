---
tags: [space, work]
status: stable
---

# Work

Work makes company context available without pouring unrelated knowledge into
every coding task. The hierarchy expresses inheritance:

```text
Work → Companies → <Company> → Projects → <Project>
```

Enter a project directory for implementation work. Its `Project.md` identifies
the canonical repository remote and its parent company supplies how work is
actually done. See [[Companies/Index]], [[Companies/_templates/Company]], and
[[Project Lifecycle]].

## Skills

The package-global `project-learning` skill registers or curates
company/project context from any Git repository. `project-planning` stays under
`Work/.agents/skills/` and creates intentional plans in a project's `Plans/`
directory. Neither may silently change company policy or import learning/video
skills.

An execution checklist used only by the current coding session stays with that
session or repository. Obsidian plans are for stable outcomes, constraints,
decisions, milestones, validation, risks, and ownership. Start from
[[Companies/_templates/Plan]].
