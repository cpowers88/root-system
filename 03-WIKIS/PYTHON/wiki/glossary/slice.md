---
type: glossary-entry
stage: 05
status: draft
aliases: ["slicing"]
related_terms: ["index", "list", "string"]
---

# Slice

## Plain-English Definition

A range of items pulled out of a sequence using `[start:stop]` notation — includes `start` up to, but not including, `stop`.

## What Problem It Helps Solve

Lets you grab a sub-portion of a string or list without writing a loop to copy items out one by one.

## When Chris Will See It

`word[1:4]`, `my_list[:3]`, `my_list[2:]` — anywhere a "chunk" of a sequence is needed.

## Code Example

```python
word = "Python"
word[1:4]   # "yth" — indices 1, 2, 3 (stops before 4)
word[:3]    # "Pyt" — from the start up to index 3
word[3:]    # "hon" — from index 3 to the end
```

## Common Confusion

The `stop` index is never included — `word[1:4]` gives 3 characters (indices 1, 2, 3), not 4.

## Physical-World Anchor

Like saying "pages 2 through 4" but the librarian hands you everything up to, but not including, page 4 — slightly different from everyday counting, which is exactly why it trips people up.

## Related Terms

- [[glossary/index]]

## Flashcard Q/A

**Front:** Does a slice `[start:stop]` include the item at the `stop` index?

**Back:** No — it includes everything from `start` up to, but not including, `stop`.
