---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# pandas: Summary Statistics, value_counts, and isin

**Summary**: The closing tools from Chapter 5 — the ones used to actually *describe* a dataset once it's loaded and cleaned. Covers `describe()`, the reduction methods (`sum`, `mean`, etc.) and their missing-data behavior, `value_counts()` for building quick frequency tables, and `isin()` for filtering rows down to a known set of values. These are the tools that turn a raw DataFrame into the numbers that go in an audit report.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 5, section 5.3 ("Summarizing and Computing Descriptive Statistics") through the chapter conclusion

**Last updated**: 2026-06-20

---

## describe() — The One-Line Dataset Summary

```python
df.describe()
```
On numeric columns, this returns count, mean, std, min, 25/50/75th percentiles, and max in one call — the fastest way to sanity-check a freshly loaded dataset (e.g., "are these job-cost numbers in a plausible range?"). On non-numeric (text/categorical) columns, `describe()` instead returns `count`, `unique`, `top` (most frequent value), and `freq` (its count).

## Reduction Methods and Missing Data

`sum()`, `mean()`, `min()`, `max()`, `median()`, `std()`, `var()` all **skip missing values (`NaN`) by default** (`skipna=True`). This matters because it differs from a naive loop — a row that's all `NaN` sums to `0` (not `NaN`) under the default behavior, while a row with *some* valid and some missing values still gets summed over only the valid ones.

- `axis="columns"` (or `axis=1`) computes the reduction **across each row** instead of down each column — easy to get backwards, so it's worth re-checking which axis you actually want each time.
- `idxmin()` / `idxmax()` return the **label** (not the value) where the min/max occurs — useful for answering "which crew/job had the worst variance" rather than just "what was the worst variance."
- `cumsum()` and `pct_change()` are running/relative versions — `pct_change()` specifically computes period-over-period percent change and is the standard building block for tracking trends over time (covered further in time series work).

## Correlation and Covariance

`series_a.corr(series_b)` computes the correlation between two aligned Series; `frame.corr()` returns the full pairwise correlation matrix for every column against every other column. `frame.corrwith(other)` computes correlation of each column against a single reference Series or against matching column names in another DataFrame — useful for a quick "what's actually related to what" pass over a multi-column audit dataset before building any chart.

## value_counts() — The Fast Frequency Table

```python
obj.value_counts()
```
Returns a Series indexed by each distinct value, sorted by frequency descending — this is the single fastest way to answer "how often does each category show up" (e.g., how many site visits per crew, how many job types per month). Also available as the top-level `pd.value_counts(array)` for working with a plain NumPy array or list instead of a full Series.

To get this for every column of a DataFrame at once: `data.apply(pd.value_counts).fillna(0)`.

## isin() — Filtering to a Known Set of Values

```python
mask = obj.isin(["b", "c"])
obj[mask]
```
`isin` performs a vectorized membership check against a list of values, and is the standard way to filter a dataset down to a known subset (e.g., keep only rows where `crew` is in `["Crew A", "Crew C"]`) — much cleaner than chaining multiple `==` comparisons with `|`.

## Connects to

- [[pandas-series-dataframe-fundamentals]] / [[pandas-arithmetic-and-function-application]] — this page assumes the construction, indexing, and `apply` patterns covered there.
- (forthcoming) data-loading-and-csv.md — Chapter 6 (next) covers getting real data into this shape in the first place via CSV/Excel loading.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
