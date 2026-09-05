---
type: glossary-entry
stage: 08
status: draft
aliases: []
related_terms: ["searching", "big-o"]
timeline: reference
---

# Sorting

## Plain-English Definition

Putting items in a meaningful order (smallest to largest, alphabetical, etc.).

## What Problem It Helps Solve

Many tasks (display, comparison, certain search techniques) are easier or only possible once data is in order.

## When Chris Will See It

Anywhere ordered output matters: leaderboards, alphabetized lists, anything described as "in order."

## Code Example

```python
sorted([5, 2, 8, 1])   # [1, 2, 5, 8] — built-in, use this in real code

def selection_sort(items):   # written from scratch, for understanding only
    result = []
    remaining = items.copy()
    while remaining:
        smallest = min(remaining)
        result.append(smallest)
        remaining.remove(smallest)
    return result
```

## Common Confusion

Writing your own sort algorithm is for *understanding how sorting works*, not for replacing Python's built-in `sorted()` in real projects — the built-in is faster and well-tested.

## Physical-World Anchor

Alphabetizing a stack of index cards by hand — there are different strategies (pick the smallest each time, divide and conquer), but the goal is always the same ordered result.

## Related Terms

- [[glossary/searching]]
- [[glossary/big-o]]

## Flashcard Q/A

**Front:** Should you write your own sort algorithm for everyday Python code?

**Back:** No — use the built-in `sorted()`. Writing one yourself is for understanding the algorithm, not for production use.
