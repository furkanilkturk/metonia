# Metonia repository guide

Metonia is a plain-Markdown knowledge operating system for Obsidian and Pi.
Its unit of context is an **agent space**: a folder with an `AGENTS.md`, a
clear ownership boundary, and optional skills local to that folder.

## Route by working directory

- Start learning work in `template/Learning/`; its agent guide and local skills
  govern source ingestion and synthesis.
- Start company and project work in `template/Work/`; descend through
  `Companies/<Company>/Projects/<Project>/` for the smallest useful context.
- Start video work in `template/Studio/Video/`.
- Keep the repository root a router. Do not place domain knowledge or global
  skills here.

Pi loads `AGENTS.md` from the working directory and its ancestors. A coding
agent launched in a company project therefore receives only the root, Work,
company, and project context—not Learning or Video skills.

## Repository boundaries

- `template/` is copied into a user's vault; it must remain portable Markdown.
- `skills/` is a legacy compatibility source while `pi-skills` is the canonical
  skill-pack repository. Releases vendor packs into `template/Learning/.agents/skills/`,
  `template/Work/.agents/skills/`, and `template/Studio/Video/.agents/skills/`.
- Do not add real companies, credentials, machine paths, customer data, or
  private operational details. The Example Company is fictional.
- Do not turn the vault into a scheduler, database, or required plugin setup.

## Before committing

```bash
python scripts/validate.py
git diff --check
```
