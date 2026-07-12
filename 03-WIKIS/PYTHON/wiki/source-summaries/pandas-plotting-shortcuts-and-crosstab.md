---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# Plotting Directly from pandas: .plot, Bar Charts, and crosstab

**Summary**: Raw matplotlib is verbose for the common case of "chart this column/these columns." pandas' `.plot` accessor on Series and DataFrame wraps matplotlib for the standard chart types (line, bar, hist, etc.) and automatically handles labels, legends, and index ticks. `pandas.crosstab` is the companion tool for turning two categorical columns into the frequency table that's usually the actual input to a bar chart.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 9 ("Plotting and Visualization"), section 9.2 ("Plotting with pandas and seaborn") — "Line Plots" and "Bar Plots"

**Last updated**: 2026-06-20

---

## Line Plots — the .plot Default

```python
s.plot()              # Series: line plot, index becomes the x-axis automatically
df.plot()              # DataFrame: one line per column, on the same subplot, legend created automatically
```

`df.plot()` is shorthand for `df.plot.line()` — `.plot` is a family of methods (`.line`, `.bar`, `.barh`, `.hist`, `.box`, `.kde`, `.area`, `.scatter`, `.pie`, ...), accessed either via the `kind=` argument or as a method directly.

Most `.plot` options pass straight through to matplotlib, so anything from [[matplotlib-figures-axes-and-styling]] (color, linestyle, title, ticks) still applies. A few pandas-specific options worth knowing:

| Argument | What it does |
|---|---|
| `ax` | the matplotlib Axes to draw on — pass this to place a pandas plot into a specific subplot of a larger grid |
| `kind` | `"line"` (default), `"bar"`, `"barh"`, `"hist"`, `"kde"`, `"area"`, `"pie"` |
| `subplots` | (DataFrame only) plot each column on its own subplot instead of one shared plot |
| `figsize` | size of the figure to create |
| `title` | plot title |
| `grid` | toggle a background grid (off by default) |

## Bar Plots

```python
data.plot.bar(color="black", alpha=0.7)     # vertical bars; Series/index becomes the x ticks
data.plot.barh(color="black", alpha=0.7)    # horizontal bars; index becomes the y ticks

df.plot.bar()                    # DataFrame: grouped bars, one cluster per row, one bar per column
df.plot.barh(stacked=True, alpha=0.5)   # stacked instead of grouped — each row's columns sum into one bar
```

A DataFrame's column-index `name` (e.g., `columns=pd.Index([...], name="Genus")`) automatically becomes the legend title — naming your columns' index pays off directly in chart readability.

**Audit-usable pattern**: `series.value_counts().plot.bar()` is the fastest way to chart a frequency breakdown (e.g., how many jobs fall into each status category) straight from the [[pandas-summary-stats-and-value-counts]] tool.

## crosstab — Building a Frequency Table to Chart

`pandas.crosstab` computes a simple frequency table from two categorical columns — exactly the shape a grouped or stacked bar chart needs as input:

```python
party_counts = pd.crosstab(tips["day"], tips["size"])
party_counts = party_counts.reindex(index=["Thur", "Fri", "Sat", "Sun"])   # control row order explicitly

# normalize each row to sum to 1 (percentage breakdown instead of raw counts)
party_pcts = party_counts.div(party_counts.sum(axis="columns"), axis="index")
party_pcts.plot.bar(stacked=True)
```

**Audit-usable pattern**: `crosstab` plus the normalize-by-row trick (`.div(.sum(axis="columns"), axis="index")`) is the direct path from two raw categorical client columns (e.g., job site × job status) to the "percentage breakdown by category" stacked bar chart that's a standard audit-report visual.

## Connects to

- [[matplotlib-figures-axes-and-styling]] — pandas' `.plot` is a thin wrapper; anything learned there (labels, legends, saving to file) still applies to a pandas-generated chart.
- [[pandas-summary-stats-and-value-counts]] — `value_counts()` and `crosstab` are the two most common ways to turn raw rows into the small summary table that actually gets charted.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
