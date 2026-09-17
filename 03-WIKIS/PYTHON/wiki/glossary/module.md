---
type: glossary-entry
stage: 04
status: ready
aliases: []
related_terms: ["import-statement", "standard-library", "package", "pip"]
timeline: reference
---

# Module

## Plain-English Definition

A single `.py` file full of reusable code — functions, classes, or values — that can be brought into another program with `import`.

## What Problem It Helps Solve

Lets code be organized into separate, reusable files instead of one giant file, and lets you use code other people have already written (the standard library).

## When Chris Will See It

`import os`, `import csv`, `import json` — anywhere a built-in capability is being used.

## Code Example

```python
import csv

with open("data.csv") as f:
    reader = csv.reader(f)
```

## Common Confusion

A module you write yourself works exactly the same way as a standard library module — `import my_helpers` works fine if `my_helpers.py` exists in the right location.

## Physical-World Anchor

A single toolbox someone already built and labeled, ready to open and use.

## Related Terms

- [[glossary/package]]
- [[glossary/import-statement]]
- [[glossary/standard-library]]

## Flashcard Q/A

**Front:** What is a module?

**Back:** A single .py file of reusable code that can be brought into another program with import.
