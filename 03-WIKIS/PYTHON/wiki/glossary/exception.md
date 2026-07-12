---
type: glossary-entry
stage: 06
status: draft
aliases: []
related_terms: ["traceback", "try-except"]
---

# Exception

## Plain-English Definition

Python's way of signaling that something went wrong while the program was running — e.g., `ValueError`, `TypeError`, `KeyError`, `FileNotFoundError`.

## What Problem It Helps Solve

Gives every kind of runtime failure a specific, nameable category, so code can detect and respond to particular problems with `try`/`except`.

## When Chris Will See It

Any time a program crashes during execution (not before it even starts, which would be a syntax error instead).

## Code Example

```python
try:
    age = int("not a number")
except ValueError:
    print("That wasn't a valid number.")
```

## Common Confusion

An exception's *name* (like `ValueError`) tells you the category of problem — reading it is the fastest way to know what went wrong, faster than re-reading the whole traceback.

## Physical-World Anchor

A specific alarm type (smoke alarm vs. carbon monoxide alarm) — knowing which one is going off tells you immediately what kind of problem to look for.

## Related Terms

- [[glossary/traceback]]
- [[glossary/try-except]]

## Flashcard Q/A

**Front:** What is an exception in Python?

**Back:** A signal that something went wrong while the program was running, named by category (ValueError, TypeError, etc.).
