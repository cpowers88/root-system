---
type: concept
stage: 09
status: draft
source_refs: ["Automate the Boring Stuff Ch.18 (CSV, JSON, and XML Files)", "Python Workout Ch.6 (Reading and writing CSV)"]
prerequisites: ["lists", "dictionaries", "file-paths-and-reading-writing"]
tags: [stage-09, csv, json, structured-data]
---

# Concept: CSV and JSON (Structured Data Formats)

## Plain-English Meaning

**CSV** ("comma-separated values") stores tabular data as plain text, one row per line, values separated by commas — basically a spreadsheet saved as text. **JSON** stores nested, labeled data (close to Python's own lists and dictionaries) as plain text — it's the most common format for exchanging structured data between programs.

## What Problem This Solves

Real-world data rarely arrives as a single string or number — it arrives as rows of records or nested structures. CSV and JSON are standard ways to read that data in and write results back out, so other programs (spreadsheets, websites, other scripts) can use it too.

## When To Use It

Use CSV for simple, flat, table-shaped data (rows and columns). Use JSON for data with nesting or varying structure (a list of records where each record has different fields, or data with structure inside structure).

## When Not To Use It

Don't reach for CSV/JSON if the data is genuinely simple and only used within one program — a plain Python list or dictionary, kept in memory, is enough. Reach for these formats specifically when data needs to be saved, shared, or exchanged.

## Code Shape

```python
import csv
import json

# CSV — reading
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # each row is a list of strings

# JSON — reading and writing
with open("data.json", "r") as f:
    data = json.load(f)        # turns JSON text into a Python list/dict

with open("output.json", "w") as f:
    json.dump(data, f)          # turns a Python list/dict into JSON text
```

## Tiny Working Example

```python
import json

student = {"name": "Chris", "age": 16}
with open("student.json", "w") as f:
    json.dump(student, f)

with open("student.json", "r") as f:
    loaded = json.load(f)
print(loaded["name"])   # "Chris"
```

## Beginner Mistakes

- Forgetting that every value read from a CSV file is a string, even if it looks like a number — conversion (`int()`/`float()`) is still needed, same as `input()`.
- Mixing up `json.load()` (reads from a file) with `json.loads()` (parses a string already in memory) — easy to use the wrong one and get a confusing error.
- Malformed JSON (a trailing comma, mismatched quotes) causing a `JSONDecodeError` — JSON has strict syntax rules, unlike Python's more forgiving style in some areas.

## Physical-World Anchor

CSV is like a spreadsheet exported as plain text — rows and columns, nothing fancier. JSON is like a labeled filing system that can nest folders inside folders, matching Python's own lists-and-dictionaries shape closely.

## Required Vocabulary

- [[glossary/csv]]
- [[glossary/json]]

## Related Code Patterns

- [[code-patterns/read-csv-and-process]]

## Drill

- [[drills/stage-09-automation-practice]]

## Explain-Back Questions

1. When would you choose CSV over JSON, and vice versa?
2. Why do values read from a CSV file always need type conversion, even if they look numeric?
3. What's the difference between `json.load()` and `json.loads()`?

## Source Notes

- (source: Automate the Boring Stuff, 3rd Ed., Ch.18, "CSV, JSON, and XML Files")
- (source: Python Workout, 2nd Ed., Ch.6, "Reading and writing CSV," "JSON")
