---
type: glossary-entry
stage: 09
status: draft
aliases: ["JavaScript Object Notation"]
related_terms: ["csv", "dictionary"]
timeline: reference
---

# JSON

## Plain-English Definition

A plain-text format for nested, labeled data — its shape closely matches Python's own lists and dictionaries. The most common format for exchanging structured data between programs.

## What Problem It Helps Solve

Lets data with structure (not just flat rows/columns) be saved and exchanged in a standard, widely-supported text format.

## When Chris Will See It

Saving program settings, exchanging data with web services (in later, parked stages), any data that has nesting (a list of records, each with multiple labeled fields).

## Code Example

```python
import json

data = {"name": "Chris", "scores": [85, 92, 78]}
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded["scores"])
```

## Common Confusion

`json.load()` reads from an already-open file; `json.loads()` (with an "s") parses a JSON string that's already in memory. Mixing these up causes confusing errors.

## Physical-World Anchor

A nested filing system — folders inside folders, each labeled — saved as plain text in a format any program can read back.

## Related Terms

- [[glossary/csv]]
- [[glossary/dictionary]]

## Flashcard Q/A

**Front:** What's the difference between `json.load()` and `json.loads()`?

**Back:** `json.load()` reads from an open file. `json.loads()` parses a JSON string already in memory.
