---
type: tool-capability
status: active
stage: 9
python_tools: [csv]
prerequisites: [files, loops, lists, dictionaries]
tags: [programming, capability]
timeline: reference
---

# Capability: Read and Write Spreadsheet Data

## Real-World Problem

A grade sheet, a budget, a client's exported sales log — tabular data that needs totals, averages, filtering, or reformatting, without doing it by hand in Excel.

## Beginner Version

A script that reads a `.csv` file (the universal spreadsheet exchange format), loops over the rows, computes something (a total or average of one column), and prints or writes the result.

## Python Tools Involved

- `csv.reader()` / `csv.writer()` — row-by-row reading and writing.
- `with open(...)` — safe file handling.
- `int()` / `float()` — every CSV value arrives as a string and needs converting.
- Accumulator pattern — running totals.

## Prerequisites

[[stages/stage-06-files-errors-debugging]] (files), [[stages/stage-05-data-shapes]] (lists/dictionaries). Taught properly in [[stages/stage-09-automation-bridge]] via [[concepts/csv-and-json]].

## Tiny Example

```python
import csv

total = 0
with open("sales.csv") as f:
    reader = csv.reader(f)
    next(reader)              # skip header row
    for row in reader:
        total += float(row[2])   # price column
print(f"Total: {total:.2f}")
```

## Mini-Project Idea

A CSV report generator: read a small sales/grades CSV, compute total + average + count, write a one-paragraph summary to a new file. Pattern reference: [[code-patterns/read-csv-and-process]].

## School Relevance

Medium — file I/O is on the syllabus; CSV work is its most realistic practice form.

## Future Business Relevance

Very high — spreadsheets are how client data arrives. This capability is the front door to the entire audit-tool idea.

## Advanced Version — Parked

Real Excel files with formatting (`openpyxl` — ATBS Ch. 14), Google Sheets (ATBS Ch. 15), and pandas DataFrames for large/multi-sheet analysis (parked data-analysis strand — [[reading-writing-csv-with-pandas]]). See [[parking-lot]].
