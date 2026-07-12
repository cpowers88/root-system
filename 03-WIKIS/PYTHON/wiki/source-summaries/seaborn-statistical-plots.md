---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, data-analysis-strand]
---

# seaborn: Statistical Plots Built on matplotlib

**Summary**: seaborn is a higher-level charting library built on matplotlib, specialized for the case where the data needs aggregation or grouping before plotting (averages by category, distributions, relationships between variables) — exactly the situation a client dataset is usually in. Where raw matplotlib expects you to compute the summary yourself, seaborn functions take a `data=` DataFrame and column names directly, computing the aggregation and styling internally.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 9 ("Plotting and Visualization"), section 9.2 ("Plotting with pandas and seaborn") — "Bar Plots" (seaborn portion), "Histograms and Density Plots" (seaborn portion), "Scatter or Point Plots", "Facet Grids and Categorical Data"

**Last updated**: 2026-06-20

---

## Setup

```python
import seaborn as sns
sns.set_style("whitegrid")        # switch the overall plot theme
sns.set_palette("Greys_r")        # greyscale palette, useful for black-and-white print reports
```

## Bar Plots with Automatic Aggregation

```python
sns.barplot(x="tip_pct", y="day", data=tips, orient="h")
sns.barplot(x="tip_pct", y="day", hue="time", data=tips, orient="h")   # split each bar by a second category
```

Unlike pandas' `.plot.bar()` (which needs a pre-aggregated table — see [[pandas-plotting-shortcuts-and-crosstab]]), `sns.barplot` averages `tip_pct` for you across every row sharing the same `day`, and draws the 95% confidence interval as an error bar automatically. **This is the key practical difference**: reach for seaborn the moment a chart needs an aggregation (mean by category) rather than a chart of already-summarized numbers.

## Histograms and Density Plots

```python
sns.histplot(values, bins=100, color="black")   # histogram + can overlay a density estimate in one call
```

A density plot (KDE — kernel density estimate) is a smoothed version of a histogram, useful for seeing the shape of a distribution without bin-width artifacts. `Series.plot.density()` (plain pandas) does this too but requires SciPy installed.

## Scatter Plots with a Fitted Trend Line

```python
ax = sns.regplot(x="m1", y="unemp", data=trans_data)
ax.title("Changes in log(m1) versus log(unemp)")
```

`regplot` draws a scatter plot **and** fits/overlays a linear regression line with a confidence band in one call — the standard quick check for "is there a relationship between these two numeric columns" (e.g., job duration vs. cost overrun).

## Pair Plots — All Relationships at Once

```python
sns.pairplot(trans_data, diag_kind="kde", plot_kws={"alpha": 0.2})
```

A pair plot (scatter plot matrix) draws every pairwise scatter plot among a group of numeric columns, with each variable's own distribution on the diagonal. This is the fast first-look exploratory step for a multi-column numeric dataset — scan it for any column pair that looks correlated before digging deeper.

## Facet Grids — Splitting a Chart Across Categorical Dimensions

```python
sns.catplot(x="day", y="tip_pct", hue="time", col="smoker", kind="bar", data=tips)
sns.catplot(x="day", y="tip_pct", row="time", col="smoker", kind="bar", data=tips)   # row AND column splits
sns.catplot(x="tip_pct", y="day", kind="box", data=tips)                              # box plot instead of bar
```

`catplot` is the general entry point for categorical plots split across one or two extra grouping dimensions — `hue` adds color-coded groups within each subplot, `col`/`row` create a separate subplot per category (a "facet grid"). `kind="box"` swaps the chart type to a box plot (median, quartiles, outliers) instead of a bar.

**Audit-usable pattern**: this is the direct tool for a question like "does [some metric] vary by site, broken down by crew and shift" — three categorical dimensions split into a clean grid of small charts rather than one unreadable combined chart.

## Connects to

- [[pandas-plotting-shortcuts-and-crosstab]] — pandas' `.plot` family expects pre-aggregated data; seaborn aggregates for you. Use pandas' shortcuts for already-summarized tables, seaborn when the raw rows still need averaging or grouping.
- [[matplotlib-figures-axes-and-styling]] — seaborn functions return matplotlib Axes/Figure objects under the hood, so titles, labels, and `savefig` all still apply.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
