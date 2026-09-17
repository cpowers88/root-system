---
type: glossary-entry
stage: 08
status: draft
aliases: ["linear search"]
related_terms: ["sorting", "hash-table"]
timeline: reference
---

# Searching

## Plain-English Definition

Finding whether (and sometimes where) a specific item exists in a collection. The simplest form, linear search, checks items one at a time.

## What Problem It Helps Solve

Almost every program needs to find something — a name in a list, whether a value already exists, the position of a target item.

## When Chris Will See It

Any "does X exist?" or "where is X?" question on a collection of data.

## Code Example

```python
def linear_search(items, target):
    for item in items:
        if item == target:
            return True
    return False

# Python's built-in equivalent:
target in items
```

## Common Confusion

Linear search checks every item until it finds a match (or runs out) — it works on any list, but is slower (O(n)) than a dictionary/set lookup (close to O(1)) for the same "does this exist?" question.

## Physical-World Anchor

Flipping through a stack of unsorted papers one by one to find a specific document — versus looking it up directly in an indexed filing system.

## Related Terms

- [[glossary/sorting]]
- [[glossary/hash-table]]

## Flashcard Q/A

**Front:** Why is searching a dictionary or set usually faster than searching a list?

**Back:** A dictionary/set uses a hash table, which can jump near-directly to where an item would be, instead of checking every item one by one like a list does.
