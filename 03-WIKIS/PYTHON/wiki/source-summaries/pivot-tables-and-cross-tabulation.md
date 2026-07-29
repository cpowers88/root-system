---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# Pivot Tables and Cross-Tabulation

**Summary**: `pivot_table` is the convenience interface that combines `groupby` with reshaping — the same tool spreadsheet users know as a "pivot table," producing a rectangle of group statistics with some keys on the rows and others on the columns, with optional row/column subtotals. `crosstab` is the simpler special case for frequency counts between two or more categorical columns. These are the two most direct paths from a raw client dataset to a finished summary table for a report.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 10 ("Data Aggregation and Group Operations"), section 10.5 ("Pivot Tables and Cross-Tabulation")

**Last updated**: 2026-06-20

---

## pivot_table — groupby + Reshape in One Call

```python
tips.pivot_table(index=["day", "smoker"])                       # default aggregation = mean, over all numeric columns
tips.pivot_table(index=["time", "day"], columns="smoker", values=["tip_pct", "size"])   # explicit rows/columns/values
```

This is equivalent to `tips.groupby(["day", "smoker"]).mean()` followed by an `unstack()` to move one key into the columns — `pivot_table` does both steps in one readable call. See [[groupby-split-apply-combine-basics]] and [[reshaping-stack-unstack-pivot-melt]] for the two underlying mechanisms this wraps.

## Adding Subtotals with margins

```python
tips.pivot_table(index=["time", "day"], columns="smoker", values=["tip_pct", "size"], margins=True)
```

`margins=True` adds an `"All"` row and column containing the statistic computed across that whole row/column tier — the partial-total row and column a client expects to see in a summary table (e.g., a grand total row at the bottom).

## Choosing a Different Aggregation Function

```python
tips.pivot_table(index=["time", "smoker"], columns="day", values="tip_pct", aggfunc=len, margins=True)
```

`aggfunc` defaults to `"mean"` but accepts any function valid in a `groupby` context — `"count"`/`len` for a frequency table instead of an average (note: `"count"` excludes nulls from the tally; `len` does not).

## Filling Empty Combinations

```python
tips.pivot_table(index=["time", "size", "smoker"], columns="day", values="tip_pct", fill_value=0)
```

Some row/column key combinations may have no matching data — `fill_value` replaces the resulting `NaN` with a chosen default (commonly `0` for a count-style table) rather than leaving gaps.

## Reference: Key pivot_table Arguments

| Argument | Description |
|---|---|
| `values` | column(s) to aggregate; defaults to all numeric columns |
| `index` | column(s)/keys to group on the rows |
| `columns` | column(s)/keys to group on the columns |
| `aggfunc` | aggregation function or list of functions, `"mean"` by default |
| `fill_value` | replaces missing combinations |
| `margins` | adds row/column subtotals and a grand total (`False` by default) |
| `margins_name` | label to use for the margin row/column, defaults to `"All"` |
| `dropna` | drop columns whose entries are entirely `NA` |

## crosstab — the Frequency-Table Special Case

`pandas.crosstab` is a simpler entry point specifically for counting how often combinations of categorical values occur together — equivalent to `pivot_table` with `aggfunc="count"`, but without needing a numeric `values` column at all:

```python
pd.crosstab(data["Nationality"], data["Handedness"], margins=True)
pd.crosstab([tips["time"], tips["day"]], tips["smoker"], margins=True)   # multiple keys on either side, as a list
```

**Audit-usable rule of thumb**: reach for `crosstab` when the question is purely "how many records fall into each combination of these categories" (e.g., jobs by site and status); reach for `pivot_table` the moment a real numeric metric (cost, hours) needs to be averaged or summed across those same category combinations.

## Connects to

- [[groupby-split-apply-combine-basics]] / [[groupby-aggregation-with-agg]] — `pivot_table` is the higher-level wrapper around exactly this machinery; understanding `groupby` first makes `pivot_table`'s behavior predictable rather than magic.
- [[reshaping-stack-unstack-pivot-melt]] — `pivot_table` aggregates *and* reshapes; plain `pivot` (covered there) reshapes without aggregating, for data that's already one row per combination.
- [[pandas-plotting-shortcuts-and-crosstab]] — a `crosstab` result is usually the direct input to a stacked or grouped bar chart.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
