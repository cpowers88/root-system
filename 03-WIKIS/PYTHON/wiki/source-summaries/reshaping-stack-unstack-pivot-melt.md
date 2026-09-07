---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# Reshaping and Pivoting: stack, unstack, pivot, melt

**Summary**: Four operations for rearranging tabular data between "long" (one observation per row, tidy/database-friendly) and "wide" (one row per entity, one column per variable, report-friendly) formats. `stack`/`unstack` work through hierarchical indexing; `pivot`/`melt` are the higher-level DataFrame-to-DataFrame equivalents most people reach for first.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 8 ("Data Wrangling: Join, Combine, and Reshape"), section 8.3 ("Reshaping and Pivoting")

**Last updated**: 2026-06-20

---

## stack and unstack — the Low-Level Mechanism

- `stack()` pivots **columns into rows**, producing a Series with a new innermost index level.
- `unstack()` pivots the **innermost row-index level into columns**, the inverse operation.

```python
data.stack()          # columns -> rows
result.unstack()      # rows -> columns (innermost level by default)
result.unstack(level=0)          # unstack a specific level by position
result.unstack(level="state")    # or by name
```

**Missing data note**: unstacking can introduce `NaN` if a level's values aren't present in every subgroup. `stack()` filters missing values out by default (making round trips lossy unless overridden) — pass `dropna=False` to `stack` to preserve them: `data2.unstack().stack(dropna=False)`.

> Data selection and reshaping performance on a hierarchical index is much better when the index is lexicographically sorted from the outermost level — see [[pandas-hierarchical-indexing]].

## pivot — Long to Wide (the Common Reporting Shape)

`DataFrame.pivot(index=..., columns=..., values=...)` is the direct, higher-level equivalent of `set_index([...]).unstack()`:

```python
pivoted = long_data.pivot(index="date", columns="item", values="value")
```

This takes a "long" table (one row per observation, e.g. `date, item, value`) and reshapes it so each distinct `item` value becomes its own column, indexed by `date`. Omit `values` to pivot **all** remaining columns at once, producing a result with hierarchical columns (one top level per original value column).

**Audit-usable pattern**: this is the standard move for turning a long client export (`date, metric, value` — common from databases and time-tracking systems) into the wide report table a client actually wants to see (`date` as rows, each metric as its own column).

## melt — Wide to Long (the Inverse)

`pandas.melt` merges multiple columns into one `variable`/`value` pair, producing a longer DataFrame — the inverse of `pivot`:

```python
melted = pd.melt(df, id_vars="key")                       # "key" stays a column; everything else melts
pd.melt(df, id_vars="key", value_vars=["A", "B"])          # only melt a chosen subset of columns
pd.melt(df, value_vars=["A", "B", "C"])                    # no id_vars at all — melts everything
```

`id_vars` marks the columns that should stay as-is (group identifiers); every other column gets stacked into two new columns, `variable` (the original column name) and `value` (the original cell value). To reverse a melt back to the original wide shape, use `pivot` followed by `reset_index()` (since `pivot` puts the row labels into the index).

**Audit-usable pattern**: a client's wide spreadsheet (one column per month, e.g. `Jan, Feb, Mar, ...`) is the wrong shape for `groupby`-based analysis or charting — `melt` it into a single `month`/`value` pair of columns first, then analyze or chart from the long form.

## Connects to

- [[pandas-hierarchical-indexing]] — `stack`/`unstack` are literally hierarchical-indexing operations; `pivot` is the convenience wrapper most people use instead of calling `set_index` + `unstack` manually.
- [[merging-datasets-with-merge-and-join]] / [[pandas-concat-and-combine-first]] — combining and reshaping are separate problems that often happen in sequence: combine multiple sources first, then reshape the result into a report-ready layout.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
