---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# pandas: Handling Missing Data and Duplicate Rows

**Summary**: The two most common "is this data actually clean" checks in any audit dataset — missing values and duplicate rows — and the standard tools for fixing each: `dropna`/`fillna` for missing data, `duplicated`/`drop_duplicates` for repeated rows. McKinney notes that 80%+ of real analyst time goes into exactly this kind of cleanup, not analysis itself.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 7 ("Data Cleaning and Preparation"), section 7.1 ("Handling Missing Data") and the "Removing Duplicates" subsection of 7.2

**Last updated**: 2026-06-20

---

## Detecting Missing Data

pandas represents missing numeric data as `NaN` and treats Python's built-in `None` the same way. `isna()` / `notna()` return a Boolean mask — `True` wherever a value is missing:

```python
data.isna()        # element-wise Boolean DataFrame/Series
```

## Filtering Out Missing Rows/Columns — dropna

```python
data.dropna()                       # drop any row with at least one NA (default)
data.dropna(how="all")              # only drop rows that are entirely NA
data.dropna(axis="columns", how="all")   # same idea, for columns
data.dropna(thresh=2)               # keep rows with at least 2 non-NA values
```

**Important**: `dropna` (like most pandas cleaning methods) returns a *new* object by default — it does not modify the original DataFrame in place.

## Filling In Missing Data — fillna

```python
df.fillna(0)                        # replace every NA with 0
df.fillna({1: 0.5, 2: 0})           # different fill value per column (by column position/name)
df.fillna(method="ffill")           # forward-fill: carry the last valid value down
df.fillna(method="ffill", limit=2)  # cap how many consecutive gaps get filled
data.fillna(data.mean())            # simple imputation — fill with the column mean
```

**Audit-usable judgment call**: forward-fill (`ffill`) makes sense for ordered data where a missing reading likely equals the last known reading (e.g., a daily inventory count with an occasional skipped day). Mean-imputation makes sense for noisy numeric data where you want to avoid biasing toward zero. Dropping rows entirely makes sense when missingness itself might signal a data-quality problem worth flagging rather than papering over — this judgment call should be made explicitly and documented, not applied automatically.

## Removing Duplicate Rows

```python
data.duplicated()                          # Boolean Series: True if row is a repeat of an earlier one
data.drop_duplicates()                     # keep only the first occurrence of each unique row
data.drop_duplicates(subset=["k1"])        # treat rows as duplicates based on only one column
data.drop_duplicates(["k1", "k2"], keep="last")  # keep the last occurrence instead of the first
```

**Audit-usable diagnostic**: running `data.duplicated().sum()` on any freshly loaded client dataset is a fast first check — a nonzero count often signals either a genuine data-entry error (the same job logged twice) or an export artifact (the same row pulled from two overlapping date ranges).

## Connects to

- [[reading-writing-csv-with-pandas]] — missing-value handling is the natural next step after loading a file (`na_values` controls what gets *read* as missing; `dropna`/`fillna` controls what happens to it *after*).
- [[pandas-summary-stats-and-value-counts]] — `describe()` and `isna().sum()` together are the fast first-look combo for any new dataset.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
