---
type: tool-capability
status: active
stage: 9
python_tools: [f-strings, csv, file writing]
prerequisites: [files, loops, accumulators, string formatting]
tags: [reference, programming, capability]
---

# Capability: Generate Reports from Data

## Real-World Problem

The same summary needed every week: "total sales, best day, item count" from a data file — currently done by opening the file and eyeballing it. Any repeated read-data → summarize → present chore.

## Beginner Version

A script that reads a data file, computes 3-4 summary numbers with accumulators, and writes a clean, readable text report using f-strings.

## Python Tools Involved

- `csv.reader()` / `open()` — read the data in.
- Counters and accumulators — totals, counts, max/min.
- f-strings (`f"Total: {total:.2f}"`) — formatted output.
- `open("report.txt", "w")` — write the result to a file.

## Prerequisites

[[stages/stage-03-loops-and-repetition]] ([[concepts/counters-and-accumulators]]), [[stages/stage-06-files-errors-debugging]] (write files), [[stages/stage-09-automation-bridge]] (CSV input).

## Tiny Example

```python
scores = [88, 94, 71, 100, 65]
report = (
    f"Scores graded: {len(scores)}\n"
    f"Average: {sum(scores) / len(scores):.1f}\n"
    f"Highest: {max(scores)}\n"
)
with open("report.txt", "w") as f:
    f.write(report)
```

## Mini-Project Idea

Weekly summary bot: read a CSV of transactions, write a `report.txt` with total, average, biggest single entry, and a warning line if any value looks invalid (ties in the validate-data capability).

## School Relevance

Medium — combines file I/O, loops, and formatting; a realistic end-of-unit exercise shape.

## Future Business Relevance

Very high — a recurring client-facing summary is the most obvious first audit deliverable a script can produce.

## Advanced Version — Parked

PDF/Word output (ATBS Ch. 17), charts (matplotlib — [[matplotlib-figures-axes-and-styling]], parked strand), pivot-table summaries ([[pivot-tables-and-cross-tabulation]], parked strand), and live dashboards (well past Stage 10). See [[parking-lot]].
