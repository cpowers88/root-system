---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# pandas groupby: apply(), Quantile/Bucket Analysis, and Group-Specific Fill Values

**Summary**: `apply` is the most general groupby tool — it splits the data into groups, runs *any* function (not just an aggregation) on each piece, and glues the results back together. This covers cases `agg` can't: returning a different number of rows per group (e.g., "top N per category"), or applying a whole DataFrame transformation rather than reducing to a single number. This page also covers two common `apply`-based recipes: bucket/quantile analysis (combining `cut`/`qcut` with `groupby`) and filling missing values with a group-specific value.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 10 ("Data Aggregation and Group Operations"), section 10.3 ("Apply: General split-apply-combine") through "Example: Filling Missing Values with Group-Specific Values"

**Last updated**: 2026-06-20

---

## apply() — When agg() Isn't Enough

```python
def top(df, n=5, column="tip_pct"):
    return df.sort_values(column, ascending=False)[:n]

tips.groupby("smoker").apply(top)                          # top 5 rows per group, by tip_pct
tips.groupby(["smoker", "day"]).apply(top, n=1, column="total_bill")   # extra args/kwargs pass straight through
```

The passed function must return either a scalar or a pandas object (Series/DataFrame) — `apply` then concatenates the per-group results, labeling the pieces with the group keys, producing a hierarchical index by default.

**Audit-usable pattern**: this is the direct tool for "show me the 3 most expensive jobs per site" or "the latest invoice per client" — a per-group *subset*, which a plain aggregation (one number per group) can't produce.

`describe()` called on a GroupBy object is really shorthand for this same pattern: `grouped.apply(lambda g: g.describe())`.

## Suppressing the Hierarchical Group-Key Index

```python
tips.groupby("smoker", group_keys=False).apply(top)   # result keeps the original row index, no extra group-key level
```

## Quantile and Bucket Analysis

Combining [[pandas-transformation-binning-and-dummies]]'s `cut`/`qcut` with `groupby` is the standard recipe for "compute summary stats within each bucket of a continuous variable":

```python
quartiles = pd.cut(frame["data1"], 4)        # equal-width buckets, returned as a Categorical
grouped = frame.groupby(quartiles)
grouped.agg(["min", "max", "count", "mean"])   # one row per bucket

# equal-SIZE buckets (by sample quantile) instead of equal-width:
quartiles_samp = pd.qcut(frame["data1"], 4, labels=False)   # labels=False returns bucket index (0,1,2,3) instead of interval labels
```

The `Categorical` object returned by `cut`/`qcut` can be passed directly as a `groupby` key — no need to first convert it into a plain array.

**Audit-usable pattern**: bucket a continuous client metric (job cost, days-to-complete) with `pd.cut`, then `groupby` the buckets and `agg(["count", "mean"])` — this is the direct way to answer "how does [outcome] vary across job-size tiers."

## Filling Missing Values with a Group-Specific Value

A flat `series.fillna(series.mean())` uses one fill value for the whole Series. When the right fill value should vary by category (e.g., fill a missing value with *that region's* mean, not the overall mean), combine `groupby` with `apply`:

```python
def fill_mean(group):
    return group.fillna(group.mean())

data.groupby(group_key).apply(fill_mean)   # each NaN filled with its OWN group's mean
```

If the fill values are already known per group rather than computed, the group's `.name` attribute (available inside the function) gives access to the current group's key:

```python
fill_values = {"East": 0.5, "West": -1}
def fill_func(group):
    return group.fillna(fill_values[group.name])

data.groupby(group_key).apply(fill_func)
```

**Audit-usable pattern**: this is the right tool when a client dataset has missing values that shouldn't be filled with one global number — e.g., filling a missing labor-hour estimate with that specific crew's or site's historical average, not the company-wide average.

## Connects to

- [[groupby-split-apply-combine-basics]] / [[groupby-aggregation-with-agg]] — `apply` is the general-purpose fallback when the per-group operation isn't a simple named aggregation; reach for `agg` first, `apply` when you need a different shape of result per group.
- [[pandas-missing-data-and-duplicates]] — the group-specific `fillna` pattern here is a direct extension of that page's flat fillna strategies, made category-aware.
- [[pandas-transformation-binning-and-dummies]] — `cut`/`qcut` are defined there; this page is their main downstream use case (bucket-then-groupby).

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
