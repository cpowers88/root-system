---
type: glossary-entry
stage: 05
status: draft
aliases: []
related_terms: ["index", "mutable-immutable", "aliasing"]
timeline: reference
---

# List

## Plain-English Definition

An ordered, mutable collection of items, written in square brackets: `[item1, item2, item3]`.

## What Problem It Helps Solve

Lets a program store and work with a group of related values as one thing, with the ability to add, remove, or change items.

## When Chris Will See It

Anywhere an ordered, changeable group of items is needed: scores, names, to-do items.

## Code Example

```python
scores = [85, 92, 78]
scores.append(100)
scores[0] = 90
```

## Common Confusion

Assigning one list to a new variable name doesn't copy it — both names point to the same list (see [[glossary/aliasing]]).

## Physical-World Anchor

A numbered shelf of bins — you can look in any bin, swap its contents, or add a new bin at the end.

## Related Terms

- [[glossary/index]]
- [[glossary/mutable-immutable]]

## Flashcard Q/A

**Front:** What is a list?

**Back:** An ordered, mutable collection of items, written in square brackets.
