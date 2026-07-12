---
type: glossary-entry
stage: 05
status: draft
aliases: ["key", "dictionary value"]
related_terms: ["dictionary"]
---

# Key / Value (Dictionary)

## Plain-English Definition

In a dictionary, the **key** is the label you look up by; the **value** is the data stored under that label. Together they form a key-value pair.

## What Problem It Helps Solve

Gives precise names to the two halves of every entry in a dictionary, so "look up by key, get back a value" can be described exactly.

## When Chris Will See It

Every dictionary entry: `{"name": "Chris"}` — `"name"` is the key, `"Chris"` is the value.

## Code Example

```python
student = {"name": "Chris", "age": 16}
for key, value in student.items():
    print(f"{key} -> {value}")
```

## Common Confusion

Each key in a dictionary must be unique — assigning to an existing key overwrites its value rather than creating a second entry.

## Physical-World Anchor

A labeled file folder (key) containing a document (value) — the label is how you find the folder; the document is what you actually wanted.

## Related Terms

- [[glossary/dictionary]]

## Flashcard Q/A

**Front:** What happens if you assign a value to a key that already exists in a dictionary?

**Back:** It overwrites the old value under that key — dictionary keys are unique.
