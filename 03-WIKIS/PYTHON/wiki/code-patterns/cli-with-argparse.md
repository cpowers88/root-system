---
type: code-pattern
stage: 10
status: draft
concepts: ["cli", "argument-parsing"]
tags: [stage-10, cli, argparse]
---

# Code Pattern: CLI Program With `argparse`

## Purpose

Accept input as command-line arguments instead of interactive prompts, with built-in validation and help text.

## Use This When

A script should be runnable directly from a terminal with options specified up front — especially if it'll be run repeatedly, scripted, or used by someone other than you.

## Do Not Use This When

A quick personal script you'll always run interactively yourself doesn't need this overhead — plain `input()` is simpler.

## Skeleton

```python
import argparse

parser = argparse.ArgumentParser(description="What this program does")
parser.add_argument("required_arg")
parser.add_argument("--optional_flag", action="store_true")
args = parser.parse_args()

# use args.required_arg and args.optional_flag
```

## Filled Example

```python
import argparse

parser = argparse.ArgumentParser(description="Count lines in a file")
parser.add_argument("filename")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

with open(args.filename) as f:
    lines = f.readlines()

if args.verbose:
    print(f"Reading {args.filename}...")
print(f"{len(lines)} lines found.")
```

## Step-by-Step Trace

1. `parser.add_argument("filename")` declares a required positional argument.
2. `parser.add_argument("--verbose", action="store_true")` declares an optional flag, defaulting to `False` unless provided.
3. `args = parser.parse_args()` reads whatever was typed after the script name and validates it against the declared arguments.
4. `args.filename` and `args.verbose` are now usable like any normal variables.

## Beginner Mistakes

- Running the script without the required argument, then being confused by `argparse`'s automatic error message — this is expected behavior, not a bug to fix in the code.
- Using `action="store_true"` incorrectly for something that should hold a value, not just be a flag (use a plain `add_argument("--name")` for that instead).
- Forgetting that testing this pattern requires actually running the script from a terminal with real arguments — it can't be fully exercised just by importing it.

## Related Terms

- [[glossary/cli]]
- [[glossary/argument-parsing]]

## Drill Link

- [[drills/stage-10-application-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-10-application-thinking]].
