---
tags: [template, project]
status: template
company: <parent-company-name>
repository: <git URL>
repositories: []
context_schema: 1
sensitivity: <public|internal|restricted>
verified_commit: <full Git SHA>
---

# <Project name>

> This project inherits its company's operating context. Read the parent
> `Company.md` first. The `repository` frontmatter is the canonical git remote
> used by context resolvers; add `repositories` only for additional remotes.

## Parent company

- Company: [[Company|<parent-company-name>]]
- Company context read on:

## Context capsule

<!-- Routine coding context loads this section, not the whole page. Keep it to
roughly 5–8 durable, high-leverage bullets. -->

- Outcome and non-goal that change implementation choices:
- Governing repository instructions and authority order:
- Architecture/data invariant; prohibited alternative:
- Important package or pattern — purpose; location; required helper/entry point;
  prohibited use:
- Security/authorization boundary:
- Verification or approval gate that is not already obvious from `AGENTS.md`:

## Outcome and boundaries

- User or business outcome:
- In scope:
- Explicitly out of scope:
- Owner and collaborators:

## Repository and systems

- Canonical remote: `<git URL>`
- Additional remotes (if any):
- Services, environments, or authorized source-of-truth links:

## Working agreements

- Project-specific implementation, review, test, and release differences:
- Risks, dependencies, and escalation path:

## Decisions and improvement queue

| ID | State | Decision or improvement | Evidence | Planning trigger |
|---|---|---|---|---|
| | | | | |

Use `accepted-constraint`, `accepted-debt`, `open-question`, `deferred`,
`rejected-alternative`, or `superseded`. An observed pattern is not a rule until
accepted; preserve rationale and review triggers for rejected alternatives.
This table is the canonical active state. A detailed Decision note may preserve
rationale/history under the same ID, but must not own a competing state.

## Context index

| Note | Load when | Sensitivity | Max bytes |
|---|---|---|---|
| `Context/Repository Atlas.md` | Locating ownership, routes, entry points, tests, generated boundaries, or verification for a task | <public/internal/restricted> | 16384 |
| `Context/Engineering Contracts.md` | Changing code, package usage, schemas, validation, persistence, APIs, authorization, or tests | <public/internal/restricted> | 16384 |
| `Context/Product and Domain Map.md` | Planning or changing product behavior, actors, entities, invariants, permissions, or cross-domain effects | <public/internal/restricted> | 16384 |
| `Context/Delivery and Operations.md` | Build, CI, migrations, deployment, environments, storage, backup, release, or runtime operations | <public/internal/restricted> | 16384 |

These are the default mature-repository slices, not mandatory empty files.
Link only notes that exist, merge slices for a small repository, and add a
different focused note when its `load when` condition is more precise. Keep
optional detail out of the capsule.

## Repository coverage and freshness

- Verified commit and tree:
- Tracked file and directory totals:
- Inventory hash and category ledger location:
- Generated, vendor, or intentionally excluded boundaries:
- Dirty paths observed during review:
- Freshness trigger:

## Durable plans

- Plans directory: `Plans/`
- Active or accepted plan links:
- Copy the sibling `Plan.md` template only for work that should outlive the
  current agent session.

## Review

- Last verified by / date:
- Next review trigger:
