---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# pandas: The Categorical Data Type

**Summary**: A specialized pandas dtype for columns with a small set of repeated values (e.g., crew names, job status, trade type). Stores the data as integer codes pointing to a small lookup table of distinct categories instead of repeating the full string every row — meaningfully faster and more memory-efficient for `groupby` and `value_counts` once a dataset gets large. Lower priority than the core cleaning tools, since SMB-scale audit datasets are unlikely to be large enough for this to matter — but worth recognizing.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 7 ("Data Cleaning and Preparation"), the "Categorical Data" section (7.5)

**Last updated**: 2026-06-20

---

## Converting a Column to Categorical

```python
fruit_cat = df["fruit"].astype("category")
fruit_cat.cat.categories     # the distinct values
fruit_cat.cat.codes          # the integer code for each row
```

The benchmark in the book: on 10 million rows with only 4 distinct string values, the categorical version used roughly **60x less memory** and ran `value_counts()` roughly **28x faster** than the plain string version. The conversion itself has an upfront one-time cost.

## Useful Categorical Methods (via the `.cat` accessor)

```python
cat_s.cat.set_categories(["a", "b", "c", "d", "e"])   # add categories not yet observed in the data
cat_s.cat.remove_unused_categories()                   # drop categories that no longer appear (e.g., after filtering)
```

`pd.cut`/`pd.qcut` (covered in [[pandas-transformation-binning-and-dummies]]) actually return a `Categorical` under the hood — the bin labels are an ordered categorical, which is why they sort and group correctly without extra work.

## Connects to

- [[pandas-transformation-binning-and-dummies]] — `pd.cut`/`pd.qcut` output is a Categorical; this page explains what that type actually is and why it behaves the way it does.
- [[pandas-summary-stats-and-value-counts]] — `value_counts()` is one of the operations that gets noticeably faster on categorical data.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
