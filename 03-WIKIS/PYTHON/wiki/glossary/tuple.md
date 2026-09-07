---
type: glossary-entry
stage: 05
status: draft
aliases: []
related_terms: ["list", "mutable-immutable"]
timeline: reference
---

# Tuple

## Plain-English Definition

An ordered, immutable collection of items, written in parentheses: `(item1, item2)`.

## What Problem It Helps Solve

Lets you group a small, fixed set of values together that should never change after creation — and signals to anyone reading the code that this group is meant to stay fixed.

## When Chris Will See It

Coordinates, RGB colors, any small fixed record of values that travel together.

## Code Example

```python
point = (3, 4)
x, y = point   # tuple unpacking
```

## Common Confusion

Tuples look like lists but can't be modified — `point[0] = 5` raises a `TypeError`, the same way modifying a string does.

## Physical-World Anchor

A sealed envelope with a fixed set of items inside — you can look, but you can't swap contents without opening a new envelope.

## Related Terms

- [[glossary/list]]
- [[glossary/mutable-immutable]]

## Flashcard Q/A

**Front:** What's the key difference between a tuple and a list?

**Back:** A tuple is immutable (can't be changed after creation); a list is mutable.
