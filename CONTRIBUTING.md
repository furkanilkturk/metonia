# Contributing

Metonia accepts improvements to the portable vault template, its validation,
and the documented contract between agent spaces and the separate `pi-skills`
repository.

## Principles

- Keep examples fictional and portable: no real company, customer, employee,
  machine path, email, credential, or operational secret.
- Keep each fact in its owning page. Company-wide facts belong in `Company.md`;
  project-only facts belong in `Project.md`; raw evidence stays in Learning.
- Preserve the folder-as-agent boundary. A space may own local skills, but do
  not place learning or studio skills at the vault root.
- Keep the copied vault dependency-free. Repository scripts are maintenance
  tools and never a requirement for using the vault.
- Keep skill bodies canonical in `pi-skills`; vendor an unchanged release copy
  into the scoped destination only when releasing Metonia. Update
  `skill-pack.lock.json` to the reviewed source revision and SHA-256 hashes in
  the same change.

## Workflow

1. Create a concise feature branch and make a focused change.
2. Update the nearest `AGENTS.md`, template, and documentation together when a
   space contract changes.
3. Run `python scripts/validate.py` and `git diff --check`.
4. Review the complete diff for private data and broken links.
5. Explain the user-facing behavior and boundary impact in the pull request.

## Style

- Prefer plain Markdown and short, useful pages over generated dashboards.
- Use `[[wikilinks]]` inside the template; the validator checks internal links.
- Keep `AGENTS.md` files procedural and concise. Put durable facts in the
  corresponding canonical page instead of repeating them in instructions.
- Use `Example Company`, `Atlas Notes`, and `you@example.com` for samples.

By contributing, you license your contribution under the [MIT license](LICENSE).
