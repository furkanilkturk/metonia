---
tags: [system, pi, skills]
status: stable
---

# Skill Packs

Metonia uses scoped Pi skills so task-specific instructions never become global
coding-agent context. `pi-skills` is the canonical source; a Metonia release
vendors exact copies into the destinations below.

| Space | Destination | Pack names |
|---|---|---|
| Learning | `Learning/.agents/skills/` | `doc-learning`, `video-learning` |
| Work | `Work/.agents/skills/` | `project-learning`, `project-planning` |
| Studio/Video | `Studio/Video/.agents/skills/` | `video-research`, `video-concept`, `video-review` |

Install or copy only the pack needed by the space. A skill is invoked on demand;
its description may be visible at startup, but its full instructions should not
be loaded into unrelated tasks. If a pack is absent, the Markdown space still
works manually—do not invent a substitute global skill.

Use the corresponding pack's README or the `pi-skills` release instructions to
vendor it. Keep the copied body unchanged so upgrades and security review remain
traceable. The Metonia repository pins release copies in
`skill-pack.lock.json`; that maintenance file is not needed inside a copied
vault.
