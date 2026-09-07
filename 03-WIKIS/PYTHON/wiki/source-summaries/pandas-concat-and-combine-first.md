---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# Combining Datasets: concat and combine_first

**Summary**: `pandas.concat` glues multiple Series or DataFrames together end-to-end (stacking rows, or lining up columns) — the tool for the common case of combining several files or exports that share the same structure (e.g., twelve monthly CSV exports with identical columns). `combine_first` is a narrower tool for patching missing values in one dataset using values from another, aligned by index/column labels.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 8 ("Data Wrangling: Join, Combine, and Reshape"), "Concatenating Along an Axis" and "Combining Data with Overlap"

**Last updated**: 2026-06-20

---

## Basic Concatenation

```python
pd.concat([s1, s2, s3])                    # default axis="index" — stacks rows, union of labels
pd.concat([s1, s2, s3], axis="columns")     # lines objects up side by side as columns instead
```

**Audit-usable pattern**: this is the direct tool for stacking twelve monthly export files (same columns, different rows) into one full-year DataFrame — `pd.concat([jan, feb, mar, ...])`.

## Inner vs. Outer Join Along the Other Axis

When concatenating, the labels on the *other* axis (not the one being stacked) may not fully overlap. By default `pandas.concat` takes the union (`join="outer"`) and fills gaps with `NaN`; pass `join="inner"` to keep only the labels common to all objects:

```python
pd.concat([s1, s4], axis="columns", join="inner")   # drops any label not shared by every object
```

## Tagging Where Each Piece Came From

Plain concatenation loses track of which rows came from which original object. The `keys` argument creates a hierarchical label (see [[pandas-hierarchical-indexing]]) identifying each source:

```python
result = pd.concat([s1, s1, s3], keys=["one", "two", "three"])
pd.concat([df1, df2], axis="columns", keys=["level1", "level2"])
pd.concat({"level1": df1, "level2": df2}, axis="columns")   # a dict's keys serve the same role
```

**Audit-usable pattern**: when stacking exports from multiple job sites or crews into one combined dataset, `keys=["site_a", "site_b", ...]` preserves which rows came from which source — essential for tracing a finding back to its origin.

## Discarding the Original Index

If the row index of each piece carries no meaningful information (e.g., it's just a default `RangeIndex`), pass `ignore_index=True` to produce a fresh, continuous index instead of preserving (and likely duplicating) the originals:

```python
pd.concat([df1, df2], ignore_index=True)
```

## Reference: Key `pandas.concat` Arguments

| Argument | Description |
|---|---|
| `objs` | list or dict of objects to combine (required) |
| `axis` | `"index"` (default, stack rows) or `"columns"` |
| `join` | `"outer"` (default, union) or `"inner"` (intersection) on the other axis |
| `keys` | values to tag each source object with, forming a hierarchical label |
| `verify_integrity` | raise an error if the result has duplicate labels on the concatenation axis (off by default) |
| `ignore_index` | discard original indexes, assign a fresh range index |

## combine_first — Patching Missing Values from a Second Source

Where `concat`/`merge` don't apply — two datasets that overlap, where you want one to fill in the other's gaps — `combine_first` aligns by label and prefers the calling object's non-null values, falling back to the other object's value when the caller has `NaN`:

```python
a.combine_first(b)        # Series version
df1.combine_first(df2)    # DataFrame version, applied column by column
```

This differs from `numpy.where(pd.isna(a), b, a)` in that `combine_first` actually aligns by label first — `numpy.where` does not check alignment and can silently produce wrong results if the two objects aren't already in the same order.

**Audit-usable pattern**: if two overlapping exports of the same data exist (e.g., a partial re-export after a system migration) and one has more complete records than the other, `combine_first` merges them into one record per row, preferring whichever source has real data for each field.

## Connects to

- [[merging-datasets-with-merge-and-join]] — `merge` connects rows on a shared key; `concat` instead stacks whole objects together; `combine_first` patches gaps. Three distinct combination problems, easy to reach for the wrong one.
- [[pandas-hierarchical-indexing]] — `concat`'s `keys` argument is the most common way a MultiIndex gets created incidentally, rather than built directly.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
