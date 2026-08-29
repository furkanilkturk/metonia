---
tags: [system, agents, context]
status: stable
---

# Agent Spaces

An agent space is a folder that has one purpose, a concise `AGENTS.md`, and
canonical pages that hold its durable facts. A space can have Pi skills under
`.agents/skills/`; those skills are discovered only when Pi starts in that
folder or a descendant.

## Context paths

```text
Learning/                  root → Learning
Work/Companies/<Company>/  root → Work → company
.../Projects/<Project>/    root → Work → company → project
Studio/Video/              root → Studio → Video
```

This makes context a property of where work begins. A project agent does not
inherit Learning or Video instructions because those folders are siblings, not
ancestors.

Pi does not follow the currently selected Obsidian note. Start Pi from the
smallest owning directory, or run `/metonia` when the companion package is
installed to inspect the resolved space and active skill commands.

## Operating rules

- Enter the smallest owning directory before launching an agent.
- Read canonical pages before acting; instructions route, pages remember.
- Keep source evidence, company operations, project execution, and video work
  separate unless a user explicitly asks to connect them.
- For an uncertain write, prepare a compact preview: target page, proposed
  change, evidence, and confidence. Wait for approval when it changes company
  policy or crosses a boundary.
- Create a new space only when it has a durable purpose, clear owner, and a
  likely local workflow—not for every short-lived task.
- Keep runtime task plans in the repository or Pi session. Persist a Work plan
  only when people should revisit its outcome, decisions, milestones,
  validation, and ownership after the session ends.

## New space checklist

1. Create the folder and a short `AGENTS.md`.
2. Name its canonical page and links to parent/adjacent spaces.
3. Specify allowed writes and sensitive material handling.
4. Add a local skill only if it is reusable and should not reach other spaces.
5. Add it to [[Home]] only when people need to navigate to it.
