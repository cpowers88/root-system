---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# Reading Excel Files, HTML Tables, and Web APIs with pandas

**Summary**: Three more real-world data sources beyond CSV that come up constantly in audit work: Excel spreadsheets (the most common client-data format after CSV), HTML tables scraped from a web page, and JSON data pulled from a web API. Binary formats (pickle, HDF5, Parquet) are also covered briefly — useful to recognize, but lower priority for SMB audit work since they're built for large/recurring datasets rather than one-off client exports.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 6, sections 6.1 ("XML and HTML: Web Scraping") through 6.3 ("Interacting with Web APIs")

**Last updated**: 2026-06-20

---

## Reading Excel Files

```python
xlsx = pd.ExcelFile("examples/ex1.xlsx")
xlsx.sheet_names                          # list available sheets first
df = xlsx.parse(sheet_name="Sheet1", index_col=0)
```

Or, for a single sheet, skip the intermediate object: `pd.read_excel("examples/ex1.xlsx", sheet_name="Sheet1")`. Requires the `openpyxl` (for `.xlsx`) or `xlrd` (for legacy `.xls`) packages.

**Writing** back to Excel: `frame.to_excel("examples/ex2.xlsx", sheet_name="Sheet1")` for the simple case, or build an `ExcelWriter` object first if writing multiple sheets to one file.

**Audit relevance**: Excel is the single most likely format a contractor or small business will hand over data in (job costing spreadsheets, material lists, timesheets) — this is arguably more directly useful day-to-day than CSV.

## Scraping Tables from HTML

```python
tables = pd.read_html("examples/fdic_failed_bank_list.xhtml")
failures = tables[0]   # read_html returns a list of DataFrames, one per <table> tag
```

`read_html` parses every `<table>` element on a page automatically (needs `lxml`, `beautifulsoup4`, and `html5lib` installed). Once extracted, dates often need explicit conversion: `pd.to_datetime(failures["Closing Date"])` followed by `.dt.year.value_counts()` is the standard pattern for turning a scraped date column into a usable year/count breakdown.

**Audit relevance**: useful if a client's only record of something (permit history, inspection results, supplier pricing) lives on a public-facing webpage rather than in an exportable file.

## Binary Formats — Recognize, Don't Prioritize

- **pickle** (`to_pickle()` / `pd.read_pickle()`): the simplest way to save a DataFrame to disk in Python's native binary format. **Caution**: only a reliable *short-term* format — not guaranteed to be readable across different pandas/Python versions, so never use it as a long-term archive for client data.
- **HDF5** (`pd.HDFStore`): built for large, write-once/read-many scientific datasets that don't fit in memory; explicitly **not a database** — concurrent writers can corrupt the file. Overkill for SMB-scale audit data.
- **Parquet** (`pd.read_parquet`): a compressed, typed binary format suited to large or distributed data. Same story — likely irrelevant until working with a dataset too large for CSV/Excel to handle comfortably.

## Web APIs — requests + JSON

```python
import requests
resp = requests.get(url)
resp.raise_for_status()          # always check for HTTP errors before using the response
data = resp.json()               # parses to a dict/list
issues = pd.DataFrame(data, columns=["number", "title", "labels", "state"])
```

The `requests` library is the standard way to hit a JSON web API from Python; `resp.json()` does the parsing, and the result (usually a list of dicts) can be passed straight into `pd.DataFrame(..., columns=[...])` to select just the fields of interest.

**Audit relevance**: lower priority for now — most SMB clients won't have an API to pull from — but this is the mechanism that would eventually power any tool that pulls live data out of a client's existing software (e.g., a job-management platform with an API).

## Connects to

- [[reading-writing-csv-with-pandas]] — same `pd.DataFrame`-construction endpoint, just a different upstream source format.
- [[pandas-series-dataframe-fundamentals]] — every format here ultimately lands in the same Series/DataFrame structures described there.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
