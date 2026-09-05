---
type: report
timeline: log
status: complete
tags: [architecture, digital-garden, compiler, root-v2]
created: 2026-08-07
---

# Review 05 — Jethro Kuan's Braindump

## Source

- Repository: [jethrokuan/braindump](https://github.com/jethrokuan/braindump)
- Build program: [build.py](https://github.com/jethrokuan/braindump/blob/master/build.py)
- Site configuration: [config.toml](https://github.com/jethrokuan/braindump/blob/master/config.toml)
- Accessed: 2026-08-07

## Why it was selected

Braindump is the strongest compilation contrast: canonical Org files are
converted into derived Markdown and a Hugo site through an incremental build.

## What the system does well

- Keeps authored source distinct from generated output.
- Uses dependency-aware incremental work so unchanged notes do not need to be
  rebuilt.
- Makes the web representation disposable; the source remains authoritative.
- Automates repetitive publication rather than asking the human to synchronize
  two representations.

## What `.ROOT V2` should take

1. Build only the context and views affected by a change.
2. Treat dashboards, indexes, briefings, and AI context packs as compiled
   artifacts, not manually maintained truths.
3. Make every compiled artifact reproducible from canonical files and an
   inspectable build rule.
4. Detect source dependencies so a changed policy or plan invalidates the
   correct downstream views.

## What not to copy

The build depends on a substantial chain—Emacs, Org export, ox-hugo, Ninja,
Hugo, and a theme. That maintenance and portability burden is inappropriate
for the core `.ROOT` runtime. V2 should use the smallest viable compiler around
Markdown, metadata, links, and a local index.

## Root-specific inference

The most important transferable idea is incremental compilation, not the
specific tools. `.ROOT` should stop repeatedly loading or rewriting broad
state documents when a deterministic compiler can produce a small current
context from changed sources.
