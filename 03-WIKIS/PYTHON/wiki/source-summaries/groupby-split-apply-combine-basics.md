---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# pandas groupby: Split-Apply-Combine Fundamentals

**Summary**: `groupby` is the core tool for "calculate this metric, broken out by category" — the single most common operation in an audit deliverable (cost by job site, hours by crew, defect rate by inspector). The mental model is **split** the data into groups by a key, **apply** a function to each group independently, then **combine** the results back into one object. This page covers how to specify grouping keys (columns, arrays, dicts, functions, index levels) and the mechanics of the resulting GroupBy object.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 10 ("Data Aggregation and Group Operations"), section 10.1 ("How to Think About Group Operations") through "Grouping by Index Levels"

**Last updated**: 2026-06-20

---

## The Split-Apply-Combine Model

1. **Split**: the data is divided into groups based on one or more keys you provide.
2. **Apply**: a function (mean, sum, a custom function) is applied independently to each group.
3. **Combine**: the per-group results are stitched back into one result object, indexed by the group keys.

```python
grouped = df["data1"].groupby(df["key1"])   # nothing computed yet — just sets up the grouping
grouped.mean()                                # NOW the split-apply-combine actually runs
```

`groupby(...)` alone is lazy — it returns a `GroupBy` object holding the information needed to apply a function later, not a result.

## Ways to Specify the Grouping Key

A grouping key can be:

- **A column name** (the most common case, when the key lives in the same DataFrame): `df.groupby("key1").mean()`
- **A list of column names** (multiple keys at once, producing a hierarchical result index): `df.groupby(["key1", "key2"]).mean()`
- **An array/list of the same length as the axis**, not necessarily a column in the DataFrame: `df["data1"].groupby([states, years]).mean()`
- **A dict or Series** mapping individual labels to a group name: useful when grouping columns by category (e.g., mapping `"a", "b" -> "red"` and `"c", "d" -> "blue"`)
- **A function**, called once per index label (or per column label with `axis="columns"`), with the return value used as the group name — e.g., `people.groupby(len)` groups rows by the *length* of their index label

```python
mapping = {"a": "red", "b": "red", "c": "blue", "d": "blue", "e": "red"}
people.groupby(mapping, axis="columns").sum()        # dict groups columns into "red"/"blue"
people.groupby(len).sum()                              # function groups rows by name length
people.groupby([len, key_list]).min()                  # functions and arrays can mix freely
```

**Important default**: rows with a missing value (`NaN`/`None`) in the grouping key are **excluded** from the result by default. Pass `dropna=False` to `groupby` to keep them as their own group instead of silently dropping them — easy to miss on real client data where a category column has gaps.

```python
df.groupby("key1", dropna=False).size()   # missing key1 values become their own group instead of vanishing
```

## Nuisance Columns

By default, `groupby(...).mean()` (or any other numeric aggregation) automatically drops any non-numeric column from the result — these are called "nuisance columns." This is convenient but can be surprising: a column you expected in the output may quietly disappear because it wasn't numeric.

## Useful General-Purpose Methods

```python
df.groupby(["key1", "key2"]).size()    # group sizes (a Series), including missing-key groups if dropna=False
df.groupby("key1").count()              # count of non-null values per column, per group
```

## Selecting a Column or Subset for Aggregation

```python
df.groupby("key1")["data1"]              # equivalent to df["data1"].groupby(df["key1"]) — a SeriesGroupBy
df.groupby("key1")[["data2"]]            # a DataFrameGroupBy with just one column
df.groupby(["key1", "key2"])[["data2"]].mean()   # narrow to a subset before aggregating, especially valuable on large datasets
```

**Audit-usable pattern**: narrowing to just the column(s) you need (`df.groupby("site")[["cost"]].sum()`) before aggregating avoids wasted computation on irrelevant columns in a large client dataset.

## Iterating Over Groups

The GroupBy object supports iteration, yielding `(group_name, group_data)` pairs — useful for inspecting each group manually or building a dict of pieces:

```python
for name, group in df.groupby("key1"):
    print(name)
    print(group)

pieces = {name: group for name, group in df.groupby("key1")}   # one-liner to materialize each group as its own DataFrame
```

With multiple keys, the first element of each tuple is itself a tuple of key values: `for (k1, k2), group in df.groupby(["key1", "key2"]):`.

## Grouping by an Index Level (MultiIndex Columns or Rows)

```python
hier_df.groupby(level="cty", axis="columns").count()    # group by a named level of a MultiIndex
```

This connects directly to [[pandas-hierarchical-indexing]] — when a MultiIndex level itself represents a meaningful category (e.g., `cty` for country), `level=` lets `groupby` use it directly without first flattening it into a column.

## Connects to

- [[pandas-hierarchical-indexing]] — multi-key `groupby` results are returned with a hierarchical index; `level=` grouping is the reverse direction, grouping *by* an existing MultiIndex level.
- [[reshaping-stack-unstack-pivot-melt]] — a multi-key groupby result is frequently `unstack()`ed right after, to turn the hierarchical result into a wide reporting table.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
