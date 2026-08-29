# Security Policy

## Scope

Metonia contains a Markdown vault template, local agent instructions, and a
stdlib validator. The most likely security failure is accidentally publishing
private operational context—not a network-facing runtime vulnerability.

Treat all company pages as potentially sensitive. Keep real-company vaults
private, minimize access, and never copy credentials, access tokens, customer
data, or internal incident details into this public template.

## Report a vulnerability

Do not open a public issue containing sensitive material. Use GitHub's private
vulnerability-report flow for the repository, or contact the maintainer through
the contact method published on GitHub. Include the affected path and a safe
description; redact the secret itself.

## Contributor checklist

- Use fictional company and project names in examples.
- Do not commit credentials, private keys, real emails, usernames, or local
  paths.
- Keep Learning source material lawful to store and share.
- Run `python scripts/validate.py`; it is a guardrail, not secret scanning.

The latest `main` branch is supported. Reported issues are assessed privately,
then fixed and disclosed with a safe summary when appropriate.
