---
type: glossary-entry
stage: 05
status: draft
aliases: ["nested data", "nested list", "nested dictionary"]
related_terms: ["list", "dictionary"]
timeline: reference
---

# Nested Structure

## Plain-English Definition

A data structure that contains another data structure inside it — a list of lists, a dictionary whose values are lists, etc.

## What Problem It Helps Solve

Real-world data often has structure within structure (a list of students, where each student is a dictionary of their attributes). Nesting lets that be represented directly.

## When Chris Will See It

A list of dictionaries (multiple records), a dictionary of lists (categories mapping to groups of items), a grid represented as a list of lists.

## Code Example

```python
students = [
    {"name": "Chris", "age": 16},
    {"name": "Alex", "age": 17},
]
print(students[0]["name"])   # "Chris" — index into the list, then key into the dict
```

## Common Confusion

Reading nested structures requires chaining access steps in the right order — `students[0]["name"]` means "get item 0 from the list, then get the value at key 'name' from that dictionary." Getting the order backward causes errors.

## Physical-World Anchor

A filing cabinet (dictionary) where each drawer contains folders (a list), and each folder contains labeled documents (another dictionary) — you open things in order, one layer at a time.

## Related Terms

- [[glossary/list]]
- [[glossary/dictionary]]

## Flashcard Q/A

**Front:** What does `students[0]["name"]` mean, step by step?

**Back:** First get item 0 from the list `students` (a dictionary), then look up the key `"name"` in that dictionary.
