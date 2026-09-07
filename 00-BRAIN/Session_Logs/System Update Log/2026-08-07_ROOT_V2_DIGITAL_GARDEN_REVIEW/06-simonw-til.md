---
type: report
timeline: log
status: complete
tags: [architecture, digital-garden, implementation, evidence, root-v2]
created: 2026-08-07
---

# Review 06 — Simon Willison's TIL

## Source

- Repository: [simonw/til](https://github.com/simonw/til)
- Database builder: [build_database.py](https://github.com/simonw/til/blob/main/build_database.py)
- Generated index updater: [update_readme.py](https://github.com/simonw/til/blob/main/update_readme.py)
- Build/deployment workflow: [build.yml](https://github.com/simonw/til/blob/main/.github/workflows/build.yml)
- Accessed: 2026-08-07

## Why it was selected

This is the economic and implementation contrast. The notes are small lessons
derived from real technical work, while the searchable database, dates, and
README index are generated from those notes and Git history.

## What the system does well

- Captures atomic knowledge close to the implementation event.
- Organizes simple Markdown by topic without requiring each note to maintain a
  global navigation structure.
- Derives created and updated dates from Git history.
- Builds a SQLite full-text-search database and a generated README index.
- Reuses the prior database when possible and renders only changed bodies,
  reducing unnecessary work.
- Runs an automated soundness check before deployment.

## What `.ROOT V2` should take

1. Capture “what changed, what worked, and how it was verified” immediately
   after a real task.
2. Derive indexes, dates, and retrieval structures from source and history.
3. Use a local searchable database as an index, never as the only copy of the
   knowledge.
4. Require a soundness check for generated context and client deliverables.
5. Promote repeated implementation lessons into reusable checklists, skills,
   audit criteria, or service assets.

## What not to copy

The deployment workflow includes cloud services and a growing plugin chain.
Those are useful for a public site but unnecessary for a private operating
core. Atomic TILs also need an added synthesis step before they become a method
or sellable capability.

## Root-specific inference

This is the best model for the missing bridge between learning and economic
value: knowledge should originate in a performed task, carry verification, and
then be compiled upward into reusable operational IP. The note itself is not
the value; the tested method and measurable outcome are.
