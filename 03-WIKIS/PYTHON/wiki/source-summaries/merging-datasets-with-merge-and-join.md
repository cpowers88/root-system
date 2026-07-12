---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# Combining Datasets: merge and join

**Summary**: `pandas.merge` is the database-style join — connecting rows across two DataFrames based on one or more shared key columns, exactly like a SQL `JOIN`. This is the tool for combining two separate client data sources that share a common identifier (e.g., a job list and a separate invoice list, both keyed by job ID). `DataFrame.join` is a convenience wrapper for the common case of joining on the index.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 8 ("Data Wrangling: Join, Combine, and Reshape"), section 8.2 ("Combining and Merging Datasets") — `pandas.merge` and "Merging on Index"

**Last updated**: 2026-06-20

---

## Basic Merge

```python
pd.merge(df1, df2)              # uses overlapping column names as the join key automatically
pd.merge(df1, df2, on="key")    # explicit — always prefer this over relying on auto-detection
```

If the key column has a different name in each DataFrame, specify both sides separately:

```python
pd.merge(df3, df4, left_on="lkey", right_on="rkey")
```

## Join Types (`how=`)

| Option | Behavior |
|---|---|
| `how="inner"` (default) | only key combinations present in **both** tables |
| `how="left"` | all keys from the left table |
| `how="right"` | all keys from the right table |
| `how="outer"` | union of keys from both tables |

Non-matching rows get `NaN`/`<NA>` filled in for the columns coming from the side that had no match. **Default behavior to watch for**: a plain `pd.merge(df1, df2)` silently drops any row whose key doesn't exist in the other table (inner join) — if you expect every original row to survive, use `how="left"` explicitly.

**Audit-usable pattern**: merging a job list (left) with an invoice list (right) using `how="left"` is the direct way to find jobs with no matching invoice — they show up as `NaN` in the invoice columns after the merge.

## Many-to-Many Merges

If a key value repeats on both sides, the result is the **Cartesian product** of the matching rows on each side — three `"b"` rows on the left and two `"b"` rows on the right produce six `"b"` rows in the merged result. This is easy to get wrong silently (row count balloons) if a key that should be unique on one side actually has duplicates — worth checking row counts before and after a merge on real client data.

## Merging on Multiple Keys

```python
pd.merge(left, right, on=["key1", "key2"], how="outer")
```

Pass a list of column names to treat the combination of those columns as a single composite join key (e.g., joining on both `site` and `week` together, not each independently).

## Overlapping Column Names

If both DataFrames have a same-named column that isn't part of the join key, pandas appends `_x`/`_y` suffixes automatically. Control this explicitly:

```python
pd.merge(left, right, on="key1", suffixes=("_left", "_right"))
```

## Merging on the Index

When the join key lives in the index rather than a column, use `left_index=True`/`right_index=True`:

```python
pd.merge(left1, right1, left_on="key", right_index=True)
```

`DataFrame.join` is a simpler instance-method wrapper for this case — it defaults to a **left** join (unlike `merge`'s default inner join) and is more convenient when combining several DataFrames sharing an index at once:

```python
left2.join(right2, how="outer")
left2.join([right2, another])          # join more than one DataFrame at once, all on index
```

## Reference: Key `pandas.merge` Arguments

| Argument | Description |
|---|---|
| `how` | `"inner"` (default), `"left"`, `"right"`, `"outer"` |
| `on` | column(s) to join on (must exist in both) |
| `left_on` / `right_on` | join columns when names differ between the two DataFrames |
| `left_index` / `right_index` | use the row index as the join key |
| `suffixes` | tuple to disambiguate overlapping non-key column names |
| `validate` | verifies the merge is actually one-to-one / one-to-many / many-to-many as expected — useful as a sanity check on unfamiliar client data |
| `indicator` | adds a `_merge` column showing whether each row came from `"left_only"`, `"right_only"`, or `"both"` |

**Audit-usable pattern**: `indicator=True` on an outer merge is the fastest way to produce a literal list of "records only in System A" vs. "records only in System B" — exactly the kind of reconciliation finding an audit report needs.

## Connects to

- [[pandas-hierarchical-indexing]] — merging two MultiIndex-based DataFrames on their shared index levels is the multi-key extension of the same `left_index`/`right_index` mechanism.
- [[pandas-missing-data-and-duplicates]] — non-matching rows from `how="left"`/`"right"`/`"outer"` merges are exactly the kind of `NaN` the missing-data tools there are built to catch and handle.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
