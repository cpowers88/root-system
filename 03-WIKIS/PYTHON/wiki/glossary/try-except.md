---
type: glossary-entry
stage: 06
status: draft
aliases: ["try-except block", "exception handling"]
related_terms: ["exception"]
---

# `try` / `except`

## Plain-English Definition

A block that attempts some code (`try`), and if a specific exception happens, runs alternative code instead of crashing (`except`).

## What Problem It Helps Solve

Lets a program handle expected, recoverable failures gracefully instead of stopping entirely.

## When Chris Will See It

Validating input, opening files that might not exist, anywhere a specific failure is anticipated and has a sensible response.

## Code Example

```python
try:
    age = int(input("Age? "))
except ValueError:
    print("Please enter a number.")
    age = 0
```

## Common Confusion

A bare `except:` (no error type listed) catches *every* exception, including ones you didn't anticipate — this can hide real bugs. Always name the specific exception type when possible.

## Physical-World Anchor

A backup plan for a specific, anticipated problem — like having an umbrella ready *if* it rains, not a vague "something might go wrong" plan for literally anything.

## Related Terms

- [[glossary/exception]]

## Flashcard Q/A

**Front:** Why is a bare `except:` (with no error type) considered risky?

**Back:** It catches every exception, including unexpected bugs, which can hide real problems instead of surfacing them.
