# Metonia

Metonia is a portable Obsidian + Pi knowledge operating system. It organizes
context as small **agent spaces** instead of one enormous AI instruction file:
Learning preserves evidence, Work carries company and project operating
knowledge, and Studio/Video develops video work. Each space works as ordinary
Markdown when no agent is present.

## Why agent spaces

Pi reads `AGENTS.md` from the current directory upward. Start a task inside the
smallest relevant folder and it receives the appropriate rules and context:

```text
template/
  Learning/                         evidence-backed learning
    .agents/skills/                 doc-learning, video-learning
  Work/                             company and project context
    .agents/skills/                 project-planning
    Companies/<Company>/Projects/<Project>/
  Studio/Video/                     video research and concepts
    .agents/skills/                 video-research, video-concept, video-review
```

Learning and Studio skills never sit above a coding/project directory, so they
do not inflate a coding agent's context. The root guide is intentionally only a
router. See [Agent Spaces](template/System/Agent%20Spaces.md) for the loading
model and [Skill Packs](template/System/Skill%20Packs.md) for installation.

## Company context is first-class

Every company gets one canonical `Company.md` that records how it works: its
customers and business model, vocabulary, decision and approval paths,
engineering and release process, quality expectations, security and privacy
constraints, shared platforms, and cross-project decisions. A project inherits
that context and adds only its local goal, boundaries, repositories, and active
decisions. The [company template](template/Work/Companies/_templates/Company.md)
and fictional [Example Company](template/Work/Companies/Example%20Company/Company.md)
show the shape.

## Start a vault

1. Copy `template/` into a new directory and open it as an Obsidian vault.
2. Read `Home.md`, then enter the space that matches the work.
3. If using Pi, launch it from that space (or a nested company/project folder).
4. Install only the packs that belong in that space; no Pi integration is
   required for the vault itself.

Pi chooses an agent space from its working directory, not from the note selected
in Obsidian. The companion Pi package provides `/metonia` to show the current
space and active skill commands. Its three global skills route context, run
decision interviews, and let `project-learning` register or curate a repository
from wherever Pi is running. Learning, project planning, and video workflows
remain folder-scoped.

Its `task_agents` tool is adaptive rather than a mandatory pipeline. The parent
agent remains responsible for work it can handle directly. It delegates only
when parallelism, isolation, specialization, cost, or independent verification
outweighs handoff overhead; a clear low-risk task can go straight to one
efficient child without planner and reviewer stages. Routing is provider
agnostic: it works from Pi's authenticated model catalog, ordered exact
`provider/model` candidates, and explicit provider/model trust allowlists. No
vendor is required or silently treated as trusted for private company context.
During existing-project registration, the native selector includes `Other` so
any fitting authenticated session model can be found even when it is absent
from the short recommendation list. Delegation is read-only; the parent agent
validates the research and remains the sole owner of questions and vault edits.

The template contains no required plugin, runtime, telemetry, or cloud service.
It uses fictional samples only. Keep private company context in a private vault
or repository.

## Contribute and validate

```bash
python scripts/validate.py
git diff --check
```

Read [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and the
[license](LICENSE) before contributing.

The vendored skill snapshot is pinned in `skill-pack.lock.json`; validation
checks every scoped copy against that manifest so releases cannot drift from
their reviewed `pi-skills` revision.
