---
tags: [system, pi, skills]
status: stable
---

# Skill Packs

Metonia combines three cross-cutting package-global skills with scoped Pi skills
whose instructions belong to one agent space. `pi-skills` is the canonical
source; a Metonia release vendors exact scoped copies into the destinations
below.

| Space | Destination | Pack names |
|---|---|---|
| Learning | `Learning/.agents/skills/` | `doc-learning`, `video-learning` |
| Work | `Work/.agents/skills/` | `project-planning` |
| Studio/Video | `Studio/Video/.agents/skills/` | `video-research`, `video-concept`, `video-review` |

The Pi package installs `metonia-context`, `metonia-interview`, and
`project-learning` globally. Only their discovery metadata is visible until a
skill is invoked; their full instructions are not copied into every prompt.
When invoked, `project-learning` accounts for every tracked repository path
structurally, then performs targeted semantic passes. Detailed repository,
engineering, domain, and operations notes remain behind the project's context
index, so routine coding receives the compact capsule instead of the whole
knowledge base.

Install or copy only the pack needed by the space. A skill is invoked on demand;
its description may be visible at startup, but its full instructions should not
be loaded into unrelated tasks. If a pack is absent, the Markdown space still
works manually. `project-learning` is the intentional global exception because
it must register and curate Metonia context from external repositories.

Use the corresponding pack's README or the `pi-skills` release instructions to
vendor it. Keep the copied body unchanged so upgrades and security review remain
traceable. The Metonia repository pins release copies in
`skill-pack.lock.json`; that maintenance file is not needed inside a copied
vault.
