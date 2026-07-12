---
type: glossary-entry
stage: 09
status: draft
aliases: []
related_terms: ["module", "pip"]
---

# Package

## Plain-English Definition

A published bundle of one or more modules, written by someone else, installed with `pip` before it can be imported.

## What Problem It Helps Solve

Lets you use solutions other people have already built and shared, instead of writing everything from scratch.

## When Chris Will See It

Anywhere third-party functionality is used that isn't part of the standard library — Pygame, Matplotlib, requests (these appear in later, parked stages).

## Code Example

```bash
pip install pygame
```
```python
import pygame   # only works after installing it
```

## Common Confusion

Standard library modules (`os`, `csv`, `json`) never need `pip install` — they come built into Python. Only third-party packages need installation first.

## Physical-World Anchor

Ordering a specialized tool from a catalog before you can use it, versus a tool that already came in your starter toolbox (the standard library).

## Related Terms

- [[glossary/module]]
- [[glossary/pip]]

## Flashcard Q/A

**Front:** Do standard library modules like `os` or `csv` need to be installed with pip?

**Back:** No — they come built into Python already. Only third-party packages need pip install.
