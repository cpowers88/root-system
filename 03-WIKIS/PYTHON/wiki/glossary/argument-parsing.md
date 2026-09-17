---
type: glossary-entry
stage: 10
status: draft
aliases: ["argparse"]
related_terms: ["cli"]
timeline: reference
---

# Argument Parsing

## Plain-English Definition

Reading and validating the arguments a user typed after a command, usually with the standard library's `argparse` module.

## What Problem It Helps Solve

Manually splitting and validating command-line text is fiddly and error-prone — `argparse` handles required vs. optional arguments, type conversion, and even auto-generates help text.

## When Chris Will See It

At the top of any CLI program, setting up what arguments it accepts before doing anything else.

## Code Example

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
print(args.filename)
```

## Common Confusion

A required (positional) argument and an optional flag (`--something`) are set up differently in `argparse` and behave differently if missing — positional arguments are required by default; flags usually aren't.

## Physical-World Anchor

A form with both required fields (must fill in) and optional checkboxes (can leave blank) — argument parsing is what enforces that distinction.

## Related Terms

- [[glossary/cli]]

## Flashcard Q/A

**Front:** What's the difference between a positional argument and an optional flag in argparse?

**Back:** A positional argument is required by position and usually mandatory. An optional flag (starting with `--`) is named and usually optional.
