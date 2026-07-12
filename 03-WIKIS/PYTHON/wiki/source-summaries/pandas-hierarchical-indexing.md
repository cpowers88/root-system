---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# pandas: Hierarchical Indexing (MultiIndex)

**Summary**: A `MultiIndex` lets a Series or DataFrame have more than one label per row (or column) — e.g., a row identified by both `state` and `year`, or a column identified by both `state` and `color`. This is how pandas represents data that's naturally grouped on more than one key without resorting to a wide, repetitive flat table. Lower priority than the core cleaning tools, but the foundation `stack`/`unstack`/`pivot` (reshaping) and multi-key `groupby` build on.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 8 ("Data Wrangling: Join, Combine, and Reshape"), section 8.1 ("Hierarchical Indexing")

**Last updated**: 2026-06-20

---

## Building a MultiIndex

```python
data = pd.Series(np.random.uniform(size=9),
                  index=[["a", "a", "a", "b", "b", "c", "c", "d", "d"],
                         [1, 2, 3, 1, 2, 3, 1, 2, 3]])
data.index   # a MultiIndex with two levels
```

A DataFrame can have a MultiIndex on either or both axes, and each level can be named:

```python
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                      index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
                      columns=[["Ohio", "Ohio", "Colorado"], ["Green", "Red", "Green"]])
frame.index.names = ["key1", "key2"]
frame.columns.names = ["state", "color"]
frame.index.nlevels   # number of index levels (2 here)
```

`pd.MultiIndex.from_arrays(...)` builds a MultiIndex directly from a list of label arrays, useful when constructing one independently of a DataFrame (e.g., to use as an `index=` argument for a second object you want aligned to the first).

## Partial Indexing — Selecting by an Outer Level

```python
data["b"]                    # all rows where the outer level is "b"
data.loc[["b", "d"]]         # multiple outer-level selections at once
data.loc[:, 2]               # select by INNER level — needs the full slice on the outer level
frame["Ohio"]                # partial selection on a MultiIndex *column* axis works the same way
```

**Audit-usable pattern**: if a client dataset naturally has two grouping keys (e.g., job site + month, or crew + week), a MultiIndex lets you slice "all rows for site X" or "all rows for month Y" without writing a Boolean filter every time.

## Reshaping: stack and unstack

```python
frame.unstack()   # pivot an inner row-index level into columns
frame.stack()      # inverse: pivot a column level back into the row index
```

These are inverse operations. `unstack()` is the more commonly useful direction for reporting — it turns a long, "tidy" table into a wide table where one key becomes columns (e.g., turning a `key1, key2, value` table into a table with `key1` as rows and `key2` as columns).

## Sorting and Reordering Levels

```python
frame.swaplevel("key1", "key2")        # swap which level is outer vs. inner (data unchanged)
frame.sort_index(level=1)               # sort rows by a specific level
frame.swaplevel(0, 1).sort_index(level=0)   # common combo: swap, then sort the new outer level
```

> Data selection performance is much better on a MultiIndex if the index is lexicographically sorted starting from the outermost level — i.e., the result of `sort_index(level=0)` or `sort_index()`.

## Summary Statistics by Level

```python
frame.groupby(level="key2").sum()                    # aggregate by row level
frame.groupby(level="color", axis="columns").sum()    # aggregate by column level
```

This previews [[pandas-summary-stats-and-value-counts]]'s reduction methods extended across one level of a MultiIndex instead of the whole axis — full `groupby` mechanics are covered later in Chapter 10.

## Moving Between Columns and the Index

```python
frame.set_index(["c", "d"])             # promote one or more columns into a (Multi)Index
frame.set_index(["c", "d"], drop=False) # keep the original columns too
frame2.reset_index()                    # inverse: move index levels back into columns
```

**Audit-usable pattern**: `set_index` is the standard way to turn two flat columns (e.g., `site`, `week`) into a structured index once a dataset has been cleaned, making downstream slicing and reshaping cleaner than repeated `df[df["site"] == x]` filtering.

## Connects to

- [[pandas-series-dataframe-fundamentals]] — MultiIndex is a more structured version of the same Index concept covered there; `.loc`/`.iloc` work the same way on top of it.
- [[pandas-summary-stats-and-value-counts]] — the `level=` argument on summary methods extends those reductions across a MultiIndex level.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
