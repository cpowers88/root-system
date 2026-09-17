---
type: code-pattern
stage: 09
status: draft
concepts: ["csv", "list", "for-loop"]
tags: [csv, automation]
timeline: reference
---

# Code Pattern: Read a CSV File and Process Its Rows

## Purpose

Load tabular data from a CSV file, process each row, and produce a result — a sum, a filtered list, a report.

## Use This When

Data arrives as a CSV file (an exported spreadsheet, a data log) and needs to be summarized, filtered, or transformed.

## Do Not Use This When

The data is nested or varies in structure between records — that's a better fit for JSON (see [[concepts/csv-and-json]]).

## Skeleton

```python
import csv

with open("filename.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)              # skip the header row, if there is one
    for row in reader:
        # row is a list of strings — convert as needed
        process(row)
```

## Filled Example

```python
import csv

total = 0
with open("sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)   # skip header: "item,price"
    for row in reader:
        price = float(row[1])
        total += price

print(f"Total sales: ${total:.2f}")
```

## Step-by-Step Trace

1. `csv.reader(f)` wraps the open file so each iteration gives one row, as a list of strings.
2. `next(reader)` consumes the first row (the header) before the loop starts, so it isn't treated as data.
3. Each `row` is something like `["Widget", "9.99"]` — `row[1]` is the price, still a string.
4. `float(row[1])` converts it before adding to `total`.

## Beginner Mistakes

- Forgetting to skip the header row, causing a `ValueError` when trying to convert a column title (like `"price"`) to a number.
- Forgetting that every value in a CSV row is a string and needs conversion before doing math.
- Assuming column order without checking — if the CSV's column order changes, hardcoded index positions (`row[1]`) silently break.

## Related Terms

- [[glossary/csv]]
- [[glossary/list]]

## Drill Link

- [[drills/stage-09-automation-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-09-automation-bridge]].
