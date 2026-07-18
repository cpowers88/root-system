---
type: glossary-entry
timeline: reference
stage: 05
status: ready
aliases: []
related_terms: [list, index, numpy]
---

# Array

## Plain-English Definition

A fixed-shape or specialized indexed collection. In beginner course language,
"array" may be used loosely for a sequence; in ordinary Python foundations the
closest built-in structure is usually a `list`.

## What Problem It Helps Solve

It stores many related values in an indexed order. Specialized numeric arrays also
support fast whole-collection calculations.

## When Chris Will See It

In the CSE 1321 course description, other programming languages, and later in
NumPy-based data analysis.

## Code Example

```python
# Built-in Python foundation: use a list.
scores = [88, 91, 76]
print(scores[0])
```

## Common Confusion

A Python `list` and a NumPy array are not interchangeable concepts. Lists are
built in and can mix value types; NumPy arrays require a library and are designed
for efficient numeric operations.

## Physical-World Anchor

A row of numbered storage bins. A Python list is a flexible row; a numeric array is
a more uniform, purpose-built rack.

## Related Terms

- [[glossary/list]]
- [[glossary/index]]

## Flashcard Q/A

**Front:** In this beginner Python path, what should Chris usually use when course material says "array"?

**Back:** A Python list, unless the material explicitly introduces a specialized array library such as NumPy.
