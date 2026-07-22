---
type: glossary-entry
stage: 03
status: draft
aliases: []
related_terms: ["counter", "loop"]
timeline: reference
---

# Accumulator

## Plain-English Definition

A variable that builds up a combined result (a sum, a joined string, a running maximum) across the passes of a loop.

## What Problem It Helps Solve

Lets a program combine many individual values into one result without storing every value first.

## When Chris Will See It

Running totals, averages, building a string piece by piece, finding the largest/smallest value seen so far.

## Code Example

```python
total = 0
for n in [4, 8, 15]:
    total = total + n
print(total)   # 27
```

## Common Confusion

Like a counter, an accumulator must start **before** the loop with an appropriate starting value (`0` for sums, `""` for strings) — and the update line must include the old value (`total = total + n`, not `total = n`).

## Physical-World Anchor

A jar where you keep dropping in coins — the jar's total only grows because each coin is added to what's already there, not replacing it.

## Related Terms

- [[glossary/counter]]

## Flashcard Q/A

**Front:** What's the difference between a counter and an accumulator?

**Back:** A counter tracks how many times something happened. An accumulator builds up a combined value (like a sum) across iterations.
