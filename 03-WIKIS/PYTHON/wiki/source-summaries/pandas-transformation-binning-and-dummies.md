---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# pandas: Value Mapping, Binning, Outliers, and Dummy Variables

**Summary**: A set of data-transformation tools for turning raw values into cleaner or more analyzable categories — mapping/replacing values, renaming axis labels, binning continuous data into buckets (`cut`/`qcut`), detecting outliers, drawing random samples, and converting categorical columns into 0/1 dummy variables. These are the tools that convert a cleaned dataset into something ready for summarizing or charting.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 7 ("Data Cleaning and Preparation"), section 7.2 ("Data Transformation"), from "Transforming Data Using a Function or Mapping" through "Computing Indicator/Dummy Variables"

**Last updated**: 2026-06-20

---

## Mapping and Replacing Values

```python
data["animal"] = data["food"].map(meat_to_animal)   # dict or function, applied element-wise
data.replace(-999, np.nan)                            # swap a known sentinel for real NA
data.replace([-999, -1000], np.nan)                   # multiple sentinels at once
data.replace({-999: np.nan, -1000: 0})                # different replacement per sentinel
```

**Audit-usable pattern**: client data frequently encodes "no data" as a magic number (`-999`, `0`, `9999`) instead of a true blank. `replace` converts these known placeholders into real `NaN` so the missing-data tools from [[pandas-missing-data-and-duplicates]] actually catch them — without this step, a sentinel value like `-999` would silently get averaged into summary statistics as if it were real data.

## Renaming Axis Labels

```python
data.index = data.index.map(transform)              # modify in place via a function
data.rename(index=str.title, columns=str.upper)      # returns a new object
data.rename(index={"OHIO": "INDIANA"}, columns={"three": "peekaboo"})   # partial relabeling via dict
```

## Binning Continuous Data — cut and qcut

```python
bins = [18, 25, 35, 60, 100]
age_categories = pd.cut(ages, bins, labels=["Youth", "YoungAdult", "MiddleAged", "Senior"])
```

`pd.cut` divides continuous data into **fixed-width or custom-edge bins** you specify — useful for turning a numeric field (age, job duration, dollar amount) into meaningful categories for grouping or reporting. `right=False` makes bin edges left-inclusive instead of the default right-inclusive.

`pd.qcut` divides data into **bins with roughly equal numbers of observations** (quantile-based) rather than equal-width ranges — better when the data is skewed and equal-width bins would leave some buckets nearly empty.

**Audit-usable distinction**: use `cut` when you want bins that match meaningful real-world categories (e.g., "small jobs under $5k," "mid-size $5k-$20k," "large $20k+"); use `qcut` when you want to split jobs into, say, quartiles by cost regardless of where the natural breakpoints fall.

## Detecting and Capping Outliers

```python
col = data[2]
col[col.abs() > 3]                                   # find outliers in one column
data[(data.abs() > 3).any(axis="columns")]            # find any row with an outlier in any column
data[data.abs() > 3] = np.sign(data) * 3              # cap (clip) outliers at +/-3, preserving sign
```

`np.sign(data)` returns `1` or `-1` per value, which is the trick used above to cap extreme values to a boundary while preserving their original direction.

## Random Sampling

```python
sampler = np.random.permutation(len(df))
df.take(sampler)            # or df.iloc[sampler] — shuffles rows
df.sample(n=3)              # random subset, no repeats
series.sample(n=10, replace=True)   # sample with replacement (repeats allowed)
```

**Audit-usable pattern**: `df.sample(n=...)` is the standard way to pull a representative spot-check sample from a large client dataset (e.g., randomly sample 20 job records to manually verify against paper invoices) rather than reviewing everything by hand.

## Dummy/Indicator Variables

```python
pd.get_dummies(df["key"])                    # one 0/1 column per distinct category value
pd.get_dummies(df["key"], prefix="key")       # prefix the new column names to avoid collisions
df[["data1"]].join(dummies)                   # combine back with the rest of the data
```

For a column where each row can belong to **multiple** categories at once (e.g., a delimited string like `"Action|Adventure"`), use `series.str.get_dummies("|")` instead of plain `get_dummies`.

A common combined recipe: `pd.get_dummies(pd.cut(values, bins))` — bin a continuous variable first, then convert the resulting categories into dummy columns in one step, useful for preparing a numeric field for grouped reporting.

## Connects to

- [[pandas-missing-data-and-duplicates]] — `replace` is frequently the step that converts hidden sentinel values into real `NaN` before the missing-data tools there can do their job.
- [[pandas-summary-stats-and-value-counts]] — `pd.cut`/`pd.qcut` output pairs naturally with `value_counts()` to produce a quick frequency table of binned categories (e.g., how many jobs fall into each cost tier).

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
