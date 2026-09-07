---
type: glossary-entry
stage: 08
status: draft
aliases: []
related_terms: ["base-case", "function"]
timeline: reference
---

# Recursion

## Plain-English Definition

A function that calls itself to solve a smaller version of the same problem, until it reaches a base case.

## What Problem It Helps Solve

Lets code directly mirror problems that are naturally defined in terms of smaller versions of themselves.

## When Chris Will See It

Countdown-style problems, processing nested structures, certain sorting/searching algorithms.

## Code Example

```python
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
```

## Common Confusion

Each recursive call pauses and waits for the one it called to finish — they don't all run "at once." Tracing this requires tracking a stack of paused calls, not just reading top to bottom once.

## Physical-World Anchor

Russian nesting dolls — each one contains a smaller one, until the smallest doll that doesn't open (the base case).

## Related Terms

- [[glossary/base-case]]

## Flashcard Q/A

**Front:** What are the two essential parts of any correctly-written recursive function?

**Back:** A base case (a simple version answered directly) and a recursive call that moves toward that base case.
