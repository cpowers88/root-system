---
type: report
timeline: log
status: complete
tags: [architecture, digital-garden, negative-control, root-v2]
created: 2026-08-07
---

# Review 03 — Maxdeviant Knowledge

## Source

- Repository: [maxdeviant/knowledge](https://github.com/maxdeviant/knowledge)
- Book configuration: [book.toml](https://github.com/maxdeviant/knowledge/blob/master/book.toml)
- Explicit hierarchy: [src/SUMMARY.md](https://github.com/maxdeviant/knowledge/blob/master/src/SUMMARY.md)
- Accessed: 2026-08-07

## Why it was selected

This is the deliberate negative control: a small, understandable Markdown book
with a simple build path. It tests whether publishing simplicity alone solves
the `.ROOT` problem.

## What the system does well

- Extremely low conceptual and operational overhead.
- Plain Markdown remains legible without the publishing tool.
- One explicit summary gives a predictable reading hierarchy.
- The build command and configuration are easy to understand.

## What `.ROOT V2` should take

1. Keep canonical knowledge usable when all automation is unavailable.
2. Make generated interfaces disposable and reproducible.
3. Prefer a small core dependency surface.

## What not to copy

Minimal publishing does not supply active-state control, learning diagnosis,
practice, evidence lineage, implementation tracking, opportunity conversion,
or outcome measurement. A clean book can still be passive storage.

## Root-specific inference

This case rejects a tempting false solution: changing `.ROOT` to a simpler
static-site generator would improve presentation but not the system's ability
to teach, execute, or create economic value.
