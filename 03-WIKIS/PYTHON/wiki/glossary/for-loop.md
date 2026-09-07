---
type: glossary-entry
stage: 03
status: draft
aliases: ["for statement"]
related_terms: ["loop", "range", "iteration"]
timeline: reference
---

# `for` Loop

## Plain-English Definition

A loop that runs its body once for each item in an iterable (a `range()`, a string, later a list), automatically handling the "next item" step.

## What Problem It Helps Solve

Lets you repeat an action across a known sequence without manually tracking position or writing a stop condition yourself.

## When Chris Will See It

Whenever the number of repetitions is known or comes from a sequence: "do this 10 times," "do this for every letter."

## Code Example

```python
for i in range(5):
    print(i)
```

## Common Confusion

A `for` loop in Python is not like counting loops in some other languages — there's no manual "increment the counter" step to forget; Python handles that automatically as it steps through the iterable.

## Physical-World Anchor

Going down a numbered checklist, one line at a time, until you reach the last line.

## Related Terms

- [[glossary/range]]
- [[glossary/iteration]]

## Flashcard Q/A

**Front:** When should you choose a `for` loop over a `while` loop?

**Back:** When you know in advance what you're looping over — a fixed count or a known sequence — rather than waiting for a condition to change.
