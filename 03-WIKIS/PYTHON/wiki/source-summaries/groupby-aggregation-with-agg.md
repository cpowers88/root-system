---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# pandas groupby: Aggregation with agg()

**Summary**: Once data is grouped (see [[groupby-split-apply-combine-basics]]), `agg`/`aggregate` is how you apply one or more summary functions to each group — including different functions per column, all in a single call. This is the tool for producing a multi-statistic summary table (count, mean, max, etc., all at once) rather than calling `.mean()` and `.max()` separately and gluing the results together by hand.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 10 ("Data Aggregation and Group Operations"), section 10.2 ("Data Aggregation")

**Last updated**: 2026-06-20

---

## Optimized Built-in Aggregations

`count`, `sum`, `mean`, `median`, `std`/`var`, `min`/`max`, `first`/`last`, `cumsum`/`cumprod`, `cummin`/`cummax`, `prod`, `quantile`, `rank`, `size`, `any`/`all` all have fast, optimized GroupBy implementations — reach for these by name before writing a custom function.

## Custom Aggregations with agg()

```python
def peak_to_peak(arr):
    return arr.max() - arr.min()

grouped.agg(peak_to_peak)     # works even though it's not a built-in — pandas slices each group and calls it
```

Custom aggregation functions are noticeably slower than the Table 10-1 built-ins (extra overhead from constructing each group's intermediate data) — prefer the named built-ins when one fits.

## Multiple Functions at Once

```python
grouped_pct.agg(["mean", "std", peak_to_peak])      # by name (string) or by function — mix freely
grouped_pct.agg([("average", "mean"), ("stdev", np.std)])   # (name, function) tuples control the output column names
```

Without explicit names, a lambda shows up labeled `"<lambda>"` in the result — hard to read. Use the `(name, function)` tuple form to avoid that.

## Different Functions per Column

```python
grouped[["tip_pct", "total_bill"]].agg(["count", "mean", "max"])   # same functions, multiple columns -> hierarchical columns

grouped.agg({"tip": np.max, "size": "sum"})                          # a dict maps each column to its own single function
grouped.agg({"tip_pct": ["min", "max", "mean", "std"], "size": "sum"})   # a dict can map a column to a LIST of functions too
```

A DataFrame result only gets hierarchical columns when **multiple** functions are applied to **at least one** column — a single function per column keeps flat column names.

**Audit-usable pattern**: `grouped.agg({"cost": ["sum", "mean"], "hours": "sum", "job_id": "count"})` is the direct way to build a one-shot multi-metric summary table (total and average cost, total hours, job count) per category — exactly the shape of table that goes straight into an audit report.

## Returning a Flat Result Instead of a Hierarchical Index

```python
tips.groupby(["day", "smoker"], as_index=False).mean()   # group keys come back as regular columns, not the index
```

This avoids needing `reset_index()` afterward and is the more report-friendly default when the grouped result is headed straight to a CSV export or a chart.

## Connects to

- [[groupby-split-apply-combine-basics]] — this page covers *how* to specify the grouping key; this page covers *what* to compute once grouped.
- [[pandas-summary-stats-and-value-counts]] — the same reduction methods (`mean`, `sum`, `describe`) apply both to a whole DataFrame and, via `agg`, to each group independently.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
