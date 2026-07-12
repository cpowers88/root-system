---
type: tool-capability
status: active
stage: 10
python_tools: [argparse, functions, input]
prerequisites: [functions, loops, conditionals, files]
tags: [reference, programming, capability]
---

# Capability: Build Small Internal Tools

## Real-World Problem

A chore that several people (or future-you) repeat: unit conversion, a lookup, a checklist runner, a tip calculator. It deserves a *tool* — something with a name that anyone can run — not a one-off script you edit each time.

## Beginner Version

A command-line tool: a script that takes its inputs as arguments (`python tipcalc.py 45.50 --percent 20`), does one job well, and prints a clear result. The step up from "script" to "tool" is that inputs come from *outside* the code.

## Python Tools Involved

- `argparse` — named/positional command-line arguments with free `--help`.
- Functions — core logic separated from input/output so it's testable.
- `input()` loops — the even simpler interactive-menu alternative.

## Prerequisites

[[stages/stage-04-functions-parameters-return]] (the logic), [[stages/stage-10-application-thinking]] — home concept: [[concepts/cli-programs-and-argparse]], pattern: [[code-patterns/cli-with-argparse]].

## Tiny Example

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("bill", type=float)
parser.add_argument("--percent", type=float, default=18)
args = parser.parse_args()
print(f"Tip: {args.bill * args.percent / 100:.2f}")
```

## Mini-Project Idea

Already in the vault: the CLI track of [[mini-projects/stage-10-capstone-choice]]. Smaller warm-up: convert any Stage 1-6 drill script into a tool that takes its inputs as arguments.

## School Relevance

Medium — functions and parameter passing are syllabus core; a CLI wrapper is realistic practice.

## Future Business Relevance

Very high — every audit capability on this list becomes deliverable the moment it's wrapped as a tool a non-programmer can run.

## Advanced Version — Parked

GUIs, web apps (Flask/FastAPI), packaging/distributing tools to other machines (ATBS Ch. 12 deployment half, `pip` packaging). See [[parking-lot]].
