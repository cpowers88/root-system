---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# pandas: Series and DataFrame Fundamentals

**Summary**: The two core pandas data structures and the operations needed to build and reshape a basic audit dataset. A **Series** is a one-dimensional labeled array (think: one labeled column). A **DataFrame** is a two-dimensional table of labeled columns (think: a spreadsheet) and is the structure almost every audit data tool will be built around. This page covers construction, the two indexing operators (`loc`/`iloc`), reindexing, and dropping — the minimum vocabulary needed before doing any real data cleaning.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 5 ("Getting Started with pandas"), sections 5.1–5.2 (through "Selection on DataFrame with loc and iloc")

**Last updated**: 2026-06-20

---

## Series — One Labeled Column

```python
import pandas as pd
obj = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])
```

Every Series has two parts: the **values** (a NumPy-style array) and the **index** (the labels). Without an explicit index, pandas assigns integers `0` to `N-1` automatically. A Series behaves like an ordered dictionary — you can check `"b" in obj`, build one directly from a Python dict, and convert back with `.to_dict()`.

**Key behavior to remember**: math operations and Boolean filtering on a Series preserve the index-to-value link automatically (`obj[obj > 0]`, `obj * 2`, `np.exp(obj)` all keep the original labels attached to the right values).

## DataFrame — A Table of Columns

```python
data = {"state": ["Ohio", "Ohio", "Nevada"], "year": [2000, 2001, 2002], "pop": [1.5, 1.7, 3.6]}
frame = pd.DataFrame(data)
```

A DataFrame is best thought of as a **dictionary of Series that all share the same index** — every column is itself a Series. Constructing one from a dict of equal-length lists is the most common pattern for hand-built audit data (e.g., one row per job site visit, columns for date/crew/finding).

- `frame["state"]` or `frame.state` retrieves a column as a Series (dot notation only works if the column name is a valid Python identifier with no spaces).
- `frame["debt"] = 16.5` adds a new column; `del frame["debt"]` removes it.
- **Caution**: a column retrieved by indexing is a *view*, not a copy — modifying it in place changes the original DataFrame. Use `.copy()` if you need an independent copy.

## Index Objects

The Index (row labels, and column labels too) is **immutable** — `index[1] = "d"` raises a `TypeError`. This is deliberate: immutability lets the same Index object be safely shared across multiple Series/DataFrames without one of them silently corrupting another's labels. Unlike a Python set, an Index *can* contain duplicate labels — selecting a duplicated label returns all matching rows.

## Reindexing

`reindex` creates a *new* object with data rearranged to match a new set of labels, introducing `NaN` for any label that didn't already exist:

```python
obj2 = obj.reindex(["a", "b", "c", "d", "e"])  # "e" becomes NaN if not in obj
```

For ordered data (e.g., a date-indexed series of weekly site-visit counts), `method="ffill"` forward-fills gaps instead of leaving `NaN`. On a DataFrame, `reindex` can target rows (`index=`), columns (`columns=`), or both.

## Dropping Entries

`obj.drop("c")` or `obj.drop(["d", "c"])` returns a new object with those labels removed. On a DataFrame, specify `index=[...]` to drop rows or `columns=[...]` (equivalently `axis=1` or `axis="columns"`) to drop columns.

## loc vs. iloc — The Two Indexing Operators to Standardize On

This is the single most important habit for avoiding indexing bugs:

- **`.loc[...]`** selects by **label** (the actual row/column names).
- **`.iloc[...]`** selects by **integer position** (0-based, like a plain list), regardless of what the labels are.

```python
data.loc["Colorado"]            # the row labeled "Colorado"
data.loc["Colorado", ["two", "three"]]   # row + column subset, by label
data.iloc[2]                    # the third row, by position
data.iloc[2, [3, 0, 1]]          # third row, specific columns by position
```

**Why this matters in practice**: plain bracket indexing (`obj[...]`) treats integers as labels *if the index itself contains integers* — which silently changes behavior depending on what kind of index a dataset happens to have. `.loc`/`.iloc` remove that ambiguity entirely, so defaulting to them (instead of bare `[]`) avoids a whole class of "worked yesterday, broke today" bugs once real, messier client data is involved.

**Slicing caution**: label-based slicing with `.loc` is *inclusive* of the endpoint (`obj.loc["b":"c"]` includes `"c"`) — this differs from ordinary Python list slicing, which excludes the endpoint.

## Connects to

- The customer-questionnaire and sales-funnel tracking tools proposed in the E-Myth ingest (business-strategy material that stayed with the FORGE split — route via `03-WIKIS\BUSINESS`, not this vault) are exactly the kind of small tabular dataset a DataFrame is built to hold and analyze.
- (forthcoming) data-loading-and-csv.md — Chapter 6 covers reading this kind of tabular data in from CSV files, the actual entry point for real audit data.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
