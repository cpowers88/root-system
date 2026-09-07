---
type: glossary-entry
stage: 03
status: draft
aliases: ["range()"]
related_terms: ["for-loop"]
timeline: reference
---

# `range()`

## Plain-English Definition

A built-in function that generates a sequence of numbers to loop over, without writing them all out by hand.

## What Problem It Helps Solve

Lets a `for` loop repeat a specific number of times, or step through a numeric sequence, instead of needing an existing list of numbers.

## When Chris Will See It

Almost every `for` loop that isn't looping over an existing string or list.

## Code Example

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 5)     # 2, 3, 4
range(0, 10, 2) # 0, 2, 4, 6, 8 (step of 2)
```

## Common Confusion

`range(5)` stops **before** 5 — it produces 5 numbers (0 through 4), not 0 through 5. This is the single most common off-by-one mistake in Stage 3.

## Physical-World Anchor

Like counting off a head count starting from zero: "zero, one, two, three, four" — five people counted, but the last number said is 4, not 5.

## Related Terms

- [[glossary/for-loop]]

## Flashcard Q/A

**Front:** What numbers does `range(5)` actually produce?

**Back:** 0, 1, 2, 3, 4 — five numbers total, stopping before 5.
