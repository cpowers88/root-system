---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# Reading and Writing CSV Data with pandas

**Summary**: The practical mechanics of getting a real, messy CSV file into a clean DataFrame, and writing one back out. This is the most directly audit-usable skill in the whole book — almost every piece of client data (timesheets, job costs, material orders) will arrive as a CSV or Excel export, never as a tidy textbook table.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 6 ("Data Loading, Storage, and File Formats"), section 6.1 ("Reading and Writing Data in Text Format") through the JSON Data subsection

**Last updated**: 2026-06-20

---

## The Basic Read

```python
df = pd.read_csv("examples/ex1.csv")
```

`read_csv` has roughly 50 optional arguments, which is overwhelming at first — but in practice only a handful come up repeatedly when dealing with messy real-world exports:

| Need | Argument |
|---|---|
| No header row in the file | `header=None` (pandas assigns `0, 1, 2...` as column names) |
| Want to supply your own column names | `names=["a", "b", "c", "d", "message"]` |
| Use a specific column as the row index | `index_col="message"` (or a column number) |
| Delimiter isn't a comma (e.g., variable whitespace) | `sep="\s+"` (accepts a regex) |
| File has comment lines or a header banner to ignore | `skiprows=[0, 2, 3]` (a list of row numbers, 0-indexed) |
| Custom missing-value markers beyond the defaults | `na_values=["NULL", "-9999"]` |
| Turn off pandas' default NA recognition entirely | `keep_default_na=False` |
| Read only the first N rows (for previewing a huge file) | `nrows=5` |

**Different NA sentinels per column**: pass a dict instead of a list — `na_values={"message": ["foo", "NA"], "something": ["two"]}` — useful when one client's spreadsheet uses different "blank" conventions in different columns (e.g., `"N/A"` in a notes column vs. `0` in a quantity column).

## Reading Huge Files in Pieces

For a file too large to load comfortably at once, `chunksize` returns a `TextFileReader` you can iterate over:

```python
chunker = pd.read_csv("examples/ex6.csv", chunksize=1000)
tot = pd.Series([], dtype="int64")
for piece in chunker:
    tot = tot.add(piece["key"].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
```

This pattern — accumulate a running total/count across chunks using `.add(..., fill_value=0)` — is the standard way to summarize a file too big to hold in memory at once, without needing a database.

## Writing CSV Back Out

```python
data.to_csv("examples/out.csv")
```

Useful variations, all via keyword arguments to `to_csv`:
- `sep="|"` — a different delimiter.
- `na_rep="NULL"` — write a specific string for missing values instead of leaving them blank.
- `index=False, header=False` — suppress the row-label column and/or the column-header row (useful when appending to an existing file, or when the destination system expects bare data).
- `columns=["a", "b", "c"]` — write only a subset of columns, in a chosen order.

## When read_csv Isn't Enough — the csv Module

For a file with malformed lines that trip up `read_csv`'s parser, drop down to Python's built-in `csv` module:

```python
import csv
with open("examples/ex7.csv") as f:
    lines = list(csv.reader(f))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
```

A custom delimiter/quoting convention can be defined either as a `csv.Dialect` subclass or passed directly as keyword arguments to `csv.reader(f, delimiter="|")` — useful for the occasional client export that uses semicolons or pipe characters instead of commas.

## JSON, Briefly

For data arriving as JSON (common from a web API rather than a spreadsheet export): `json.loads(text)` parses a JSON string into native Python dicts/lists; `json.dumps(obj)` converts back. A list of JSON objects (dicts) can be passed straight to `pd.DataFrame(list_of_dicts, columns=[...])` to get a table.

## Connects to

- [[pandas-series-dataframe-fundamentals]] — `read_csv` is the practical entry point that produces the DataFrames described there.
- [[pandas-summary-stats-and-value-counts]] — the chunked-read example above uses `value_counts()` directly, the natural next step after loading.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
