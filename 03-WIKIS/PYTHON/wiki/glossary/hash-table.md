---
type: glossary-entry
stage: 08
status: draft
aliases: []
related_terms: ["dictionary", "searching"]
timeline: reference
---

# Hash Table

## Plain-English Definition

A data structure that stores items at computed positions based on their key, making lookup very fast (close to O(1)) instead of checking items one by one. Python's `dict` and `set` are both built on hash tables.

## What Problem It Helps Solve

Lets "does this exist?" and "look this up" questions stay fast even as the amount of data grows large, where a list's linear search would slow down.

## When Chris Will See It

Every time a dictionary or set is used — the speed benefit is happening automatically under the hood, even without thinking about it directly.

## Code Example

```python
prices = {"apple": 1.50, "banana": 0.75}
"apple" in prices    # fast — hash table lookup, not a one-by-one scan
```

## Common Confusion

You don't need to implement a hash table yourself to benefit from one — using a dictionary or set in Python already gives you this performance automatically.

## Physical-World Anchor

A library's barcode scanning system — instead of searching every shelf, the scanner computes exactly where a book belongs and jumps straight there.

## Related Terms

- [[glossary/dictionary]]
- [[glossary/searching]]

## Flashcard Q/A

**Front:** What Python built-in data structures are based on hash tables?

**Back:** Dictionaries (`dict`) and sets (`set`).
