---
type: glossary-entry
stage: 02
status: draft
aliases: ["conditional statement", "if statement"]
related_terms: ["condition", "branch"]
---

# `if` / `elif` / `else`

## Plain-English Definition

The keywords that make a program branch: `if` checks a condition; `elif` ("else if") checks another condition only if the previous ones were False; `else` catches everything not already handled.

## What Problem It Helps Solve

Lets a program take different actions depending on the situation, instead of always running the same fixed steps.

## When Chris Will See It

Any time the program needs to make a decision.

## Code Example

```python
if score == 100:
    print("Perfect!")
elif score >= 50:
    print("Pass")
else:
    print("Try again")
```

## Common Confusion

Only **one** branch in an `if`/`elif`/.../`else` chain ever runs — as soon as one condition is True, the rest are skipped. Using separate `if` statements instead of `elif` can accidentally let more than one branch run.

## Physical-World Anchor

A flowchart's diamond decision box — you follow exactly one path out, never more than one.

## Related Terms

- [[glossary/condition]]
- [[glossary/branch]]

## Flashcard Q/A

**Front:** How many branches of an `if`/`elif`/`else` chain run for a single pass through it?

**Back:** Exactly one — as soon as one condition is True, the rest are skipped.
