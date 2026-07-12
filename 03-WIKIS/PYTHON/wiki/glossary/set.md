---
type: glossary-entry
stage: 05
status: draft
aliases: []
related_terms: ["list", "dictionary"]
---

# Set

## Plain-English Definition

An unordered collection of unique items, written in curly braces without keys: `{item1, item2}`. Duplicates are automatically removed.

## What Problem It Helps Solve

Lets a program quickly check whether something is present, or get rid of duplicates, when order and position don't matter.

## When Chris Will See It

Removing duplicates from a list, checking membership quickly, tracking "have I seen this already?"

## Code Example

```python
names = {"Chris", "Alex", "Chris"}
print(names)   # {"Chris", "Alex"} — duplicate removed automatically
```

## Common Confusion

`{}` by itself creates an empty *dictionary*, not an empty set — use `set()` for an empty set.

## Physical-World Anchor

A guest list where you only care who's on it, not the order they arrived or how many times their name was written down.

## Related Terms

- [[glossary/list]]
- [[glossary/dictionary]]

## Flashcard Q/A

**Front:** What does `{}` create — an empty set or an empty dictionary?

**Back:** An empty dictionary. Use `set()` to create an empty set.
