---
type: code-pattern
stage: 03
status: draft
concepts: ["for-loop", "range", "counter", "accumulator"]
tags: [for-loop, range]
timeline: reference
---

# Code Pattern: `for` Loop Over `range()`

## Purpose

Repeat an action a known number of times, optionally tracking a count or building up a total as you go.

## Use This When

You know exactly how many repetitions you need, or you're stepping through numbers in a known range.

## Do Not Use This When

The number of repetitions depends on a condition that might change unpredictably (use [[code-patterns/while-loop-until-condition]] instead).

## Skeleton

```python
total = 0   # or whatever starting value the accumulator needs
for i in range(n):
    total = total + something
```

## Filled Example

```python
total = 0
for i in range(1, 6):       # 1, 2, 3, 4, 5
    total = total + i
print(f"Sum 1 to 5: {total}")   # 15
```

## Step-by-Step Trace

1. `range(1, 6)` produces 1, 2, 3, 4, 5 (stopping before 6).
2. Each pass, `i` takes the next value in that sequence.
3. `total = total + i` adds the current value of `i` to whatever `total` already held.
4. After the last pass (`i = 5`), the loop ends and `total` holds the final sum.

## Beginner Mistakes

- Forgetting `range()` stops one before its argument — `range(5)` gives 0-4, not 0-5.
- Initializing `total` (or any accumulator) inside the loop instead of before it.
- Forgetting the colon and indentation.

## Related Terms

- [[glossary/for-loop]]
- [[glossary/range]]
- [[glossary/accumulator]]
- [[glossary/counter]]

## Drill Link

- [[drills/stage-03-loop-tracing]]

## Flashcards To Create

- Already covered in [[flashcards/stage-03-repetition]].
