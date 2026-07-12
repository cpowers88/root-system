---
type: concept
stage: 06
status: draft
source_refs: ["Think Python Ch.14 (Catching Exceptions)", "Python Crash Course Ch.10 (Exceptions)", "Automate the Boring Stuff Ch.5"]
prerequisites: ["file-paths-and-reading-writing"]
tags: [stage-06, exceptions, try-except, tracebacks]
---

# Concept: Exceptions, Tracebacks, and `try`/`except`

## Plain-English Meaning

An **exception** is Python's way of signaling that something went wrong while the program was running. A **traceback** is the report Python prints describing exactly where and why. `try`/`except` lets a program catch an exception and handle it gracefully instead of crashing.

## What Problem This Solves

Some failures are expected and recoverable — a file might not exist, user input might be invalid. `try`/`except` lets the program respond sensibly instead of stopping dead.

## When To Use It

Wrap code in `try`/`except` when failure is a realistic possibility you want to handle gracefully — opening a file that might not exist, converting input that might not be a valid number.

## When Not To Use It

Don't wrap *everything* in `try`/`except` "just in case" — that hides real bugs instead of fixing them. Only catch exceptions you actually expect and have a sensible response for.

## Code Shape

```python
try:
    # code that might fail
    risky_operation()
except SomeErrorType:
    # what to do if that specific error happens
    handle_it()
```

## Tiny Working Example

```python
try:
    age = int(input("Age? "))
except ValueError:
    print("That wasn't a valid number.")
    age = 0
```

## Beginner Mistakes

- Using a bare `except:` with no error type — this catches *everything*, including bugs you didn't anticipate, making them hard to find.
- Reading a traceback from the top down instead of the bottom up — the most useful information (the actual error type and message) is at the very bottom.
- Wrapping code in `try`/`except` to "fix" an error without understanding why it happened first — this often just hides the real bug.

## Physical-World Anchor

A traceback is like a flight recorder readout after something goes wrong — it shows the sequence of steps that led to the failure, read in order, with the final outcome (the crash) at the end.

## Required Vocabulary

- [[glossary/exception]]
- [[glossary/traceback]]
- [[glossary/try-except]]

## Related Code Patterns

- [[code-patterns/try-except-block]]

## Drill

- [[drills/stage-06-debugging-practice]]

## Explain-Back Questions

1. Why is `except:` with no error type considered risky?
2. Which part of a traceback should you read first, and why?
3. Give an example of a situation where `try`/`except` is the *right* tool, and one where it would just hide a bug.

## Source Notes

- (source: Think Python, 2nd Ed., Ch.14, "Catching Exceptions")
- (source: Python Crash Course, 3rd Ed., Ch.10, "Exceptions," "Handling the ZeroDivisionError Exception," "Using try-except Blocks")
- (source: Automate the Boring Stuff, 3rd Ed., Ch.5, "Debugging")
