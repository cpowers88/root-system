---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# pandas: Arithmetic Alignment, apply/map, and Sorting

**Summary**: Three everyday pandas behaviors that matter for cleaning real audit data: how arithmetic between differently-indexed objects auto-aligns (and fills gaps with `NaN`), how to run a custom function across rows/columns/elements (`apply`, `applymap`, `map`), and how to sort by index or by value. Builds directly on [[pandas-series-dataframe-fundamentals]].

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 5, section 5.2 ("Arithmetic and Data Alignment" through "Sorting and Ranking")

**Last updated**: 2026-06-20

---

## Data Alignment — Mismatched Indexes Don't Error, They Produce NaN

When two Series or DataFrames with different indexes are combined arithmetically, pandas takes the **union** of the labels and fills any non-overlapping spot with `NaN` rather than raising an error:

```python
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=["a", "c", "e", "f", "g"])
s1 + s2   # "d", "f", "g" all become NaN — no overlap, no error
```

**Why this matters for audit data**: if you're combining two datasets collected at different times (e.g., week-1 site visit log + week-3 site visit log) and they don't have identical labels, the join will silently fill gaps with `NaN` instead of failing loudly. Always check `.isna().sum()` after combining datasets from different sources.

**Controlling the fill value**: use `.add(other, fill_value=0)` (or `.sub`, `.mul`, `.div`, etc.) instead of the bare operator when you want missing values treated as 0 rather than propagated as `NaN`.

## Function Application — apply, applymap, map

Three related tools for running custom logic across pandas data, each at a different "shape":

| Method | Runs on | Use case |
|---|---|---|
| `frame.apply(f)` | each *column* (or each row with `axis="columns"`) | summary stats per column, e.g. `f1 = lambda x: x.max() - x.min()` |
| `frame.applymap(f)` | every individual *element* of a DataFrame | reformat every value, e.g. format every float as a 2-decimal string |
| `series.map(f)` | every individual *element* of a Series | same idea, one column at a time |

```python
def f1(x):
    return x.max() - x.min()
frame.apply(f1)                  # one result per column
frame.apply(f1, axis="columns")  # one result per row
```

The function passed to `apply` can return either a single scalar (collapsing to a Series) or a Series with multiple values (expanding to a DataFrame).

## Sorting

- **By label**: `obj.sort_index()` (Series) or `frame.sort_index()` (DataFrame, with `axis="columns"` for column-label sorting). `ascending=False` reverses.
- **By value**: `obj.sort_values()` for a Series; for a DataFrame, `frame.sort_values(by="column_name")` (or a list of column names for tie-breaking).
- **Missing values sort to the end by default** — use `na_position="first"` to push them to the start instead.

## Connects to

- [[pandas-series-dataframe-fundamentals]] — this page assumes familiarity with Series/DataFrame construction and `.loc`/`.iloc` covered there.
- (forthcoming) data-cleaning-missing-values.md — Chapter 7 covers `NaN` handling in much more depth; the alignment behavior here is the reason missing-data handling matters so much in pandas specifically.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
