---
type: glossary-entry
stage: 10
status: draft
aliases: ["command-line interface", "command-line program"]
related_terms: ["argument-parsing"]
timeline: reference
---

# CLI

## Plain-English Definition

A "command-line interface" program — one that takes its input as arguments typed after the command, instead of through interactive `input()` prompts.

## What Problem It Helps Solve

Lets a program be run unattended, scripted by other programs, or take several options at once, instead of requiring someone to sit and answer prompts.

## When Chris Will See It

Running any script from a terminal with extra options: `python script.py file.txt --verbose`.

## Code Example

```bash
python organize.py downloads --by-extension
```

## Common Confusion

A CLI program isn't a different *kind* of Python file — it's the same `.py` file, just designed to receive its input via arguments (often with `argparse`) instead of `input()`.

## Physical-World Anchor

A structured order form filled out all at once, versus a back-and-forth conversation at a counter.

## Related Terms

- [[glossary/argument-parsing]]

## Flashcard Q/A

**Front:** What does CLI stand for, and what does it mean for a program?

**Back:** Command-line interface — a program that takes its input as arguments typed after the command, rather than through interactive prompts.
