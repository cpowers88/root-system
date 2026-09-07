---
type: glossary-entry
stage: 09
status: draft
aliases: ["comma-separated values"]
related_terms: ["json"]
timeline: reference
---

# CSV

## Plain-English Definition

"Comma-separated values" — a plain-text format for tabular data, one row per line, values separated by commas. Essentially a spreadsheet saved as text.

## What Problem It Helps Solve

Lets table-shaped data move between programs (spreadsheets, databases, scripts) in a simple, universally-readable text format.

## When Chris Will See It

Exported spreadsheet data, simple data logs, anything row-and-column shaped that needs to be read or written by a script.

## Code Example

```python
import csv

with open("scores.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # each row is a list of strings
```

## Common Confusion

Every value read from a CSV file is a string, even numbers — they need `int()`/`float()` conversion just like `input()` does.

## Physical-World Anchor

A spreadsheet's grid, but flattened into plain text — rows separated by line breaks, columns separated by commas.

## Related Terms

- [[glossary/json]]

## Flashcard Q/A

**Front:** What type are values read from a CSV file, before any conversion?

**Back:** Strings — even values that look like numbers.
