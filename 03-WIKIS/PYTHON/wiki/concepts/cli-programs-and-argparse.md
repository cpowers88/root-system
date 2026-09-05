---
type: concept
stage: 10
status: draft
source_refs: ["Automate the Boring Stuff Ch.12 (Designing and Deploying Command Line Programs)", "raw/docs/howto/argparse.txt"]
prerequisites: ["modules-and-packages", "defining-and-calling-functions"]
tags: [cli, argparse]
timeline: reference
---

# Concept: Command-Line Programs and `argparse`

## Plain-English Meaning

A **CLI** (command-line interface) program takes its input as arguments typed right after the command, instead of through `input()` prompts — `python script.py --name Chris` rather than asking interactively. The standard library's `argparse` module handles parsing those arguments, including validation and built-in help text.

## What Problem This Solves

Interactive `input()` prompts are fine for small, hands-on scripts — but a real tool often needs to run unattended, be scripted by other programs, or take several options at once. CLI arguments make that possible.

## When To Use It

When a script should be runnable directly from a terminal with options specified up front (a file to process, a mode to run in), rather than needing someone to sit and answer prompts.

## When Not To Use It

For a quick personal script you'll always run interactively yourself, plain `input()` is simpler and `argparse`'s setup overhead isn't worth it.

## Code Shape

```python
import argparse

parser = argparse.ArgumentParser(description="What this program does")
parser.add_argument("name")                       # required positional argument
parser.add_argument("--shout", action="store_true")  # optional flag
args = parser.parse_args()

print(f"Hello, {args.name}!")
if args.shout:
    print("HELLO!!!")
```

## Tiny Working Example

```bash
python greet.py Chris --shout
```
```text
Hello, Chris!
HELLO!!!
```

## Beginner Mistakes

- Forgetting a required positional argument when running the script, causing `argparse` to print a usage error and exit — this is expected behavior, not a bug.
- Confusing positional arguments (no `--`, required by position) with optional flags (`--shout`, named, often boolean).
- Not testing the script from an actual terminal — some `argparse` behavior (like the auto-generated `--help` text) only shows up when run that way, not when imported.

## Physical-World Anchor

Ordering at a counter with a structured form ("size: medium, topping: extra cheese") versus a free-form conversation — CLI arguments are the structured form, filled out all at once before the order starts.

## Required Vocabulary

- [[glossary/cli]]
- [[glossary/argument-parsing]]

## Related Code Patterns

- [[code-patterns/cli-with-argparse]]

## Drill

- [[drills/stage-10-application-practice]]

## Explain-Back Questions

1. What's the difference between a positional argument and an optional flag in `argparse`?
2. Why might a CLI tool be more useful than an interactive `input()`-based script for some tasks?
3. What happens if you run a script that requires an argument, without providing one?

## Source Notes

- (source: Automate the Boring Stuff, 3rd Ed., Ch.12, "Designing and Deploying Command Line Programs")
- (source: `raw/docs/howto/argparse.txt` — official Python argparse tutorial, used as reference)
