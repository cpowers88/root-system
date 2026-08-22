---
type: glossary-entry
stage: 03
status: draft
aliases: []
related_terms: ["for-loop", "while-loop", "iteration"]
timeline: reference
---

# Loop

## Plain-English Definition

A block of code that repeats — either a fixed number of times (`for`) or until a condition changes (`while`).

## What Problem It Helps Solve

Lets a program repeat an action without writing the same line of code over and over by hand.

## When Chris Will See It

Any time something needs to happen more than once: processing every item in a list, repeating until valid input is given, counting.

## Code Example

```python
for i in range(3):
    print("Hello")
```

## Common Confusion

A loop's *body* (the indented block) is what repeats — the loop statement itself (`for ...:` or `while ...:`) only runs its setup/check once per pass, not the whole thing twice.

## Physical-World Anchor

A washing machine's spin cycle — it repeats the same motion a set number of times, then stops.

## Related Terms

- [[glossary/for-loop]]
- [[glossary/while-loop]]
- [[glossary/iteration]]

## Flashcard Q/A

**Front:** What is a loop?

**Back:** A block of code that repeats, either a fixed number of times or until a condition changes.
