---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-09
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, data-analysis-strand]
---

# matplotlib: Figures, Axes, Styling, Ticks, and Legends

**Summary**: matplotlib is the core Python plotting library — the tool that turns a cleaned DataFrame into a chart for an audit report. Every plot lives inside a `Figure`, which contains one or more `Axes` (subplots) that you actually draw onto. This page covers the building blocks: creating figures/subplots, the basic plot-styling options (color, line style, markers), and labeling a plot properly (ticks, axis labels, title, legend) — the minimum needed to produce a presentable chart, not a publication-grade one.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 9 ("Plotting and Visualization"), section 9.1 ("A Brief matplotlib API Primer") through "Annotations and Drawing on a Subplot"

**Last updated**: 2026-06-20

---

## The Core Object Model: Figure and Axes

```python
import matplotlib.pyplot as plt

fig = plt.figure()                  # the overall canvas/window
ax1 = fig.add_subplot(2, 2, 1)      # a 2x2 grid of subplots, this is the 1st (top-left)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
```

**Better default**: `plt.subplots()` creates the figure and all its subplots in one call, returning the figure plus a NumPy array of Axes objects you can index like a grid:

```python
fig, axes = plt.subplots(2, 3)      # 2x3 grid
axes[0, 1]                          # top row, middle column
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)   # same axis scale across all subplots — use this whenever comparing values across panels
```

**Prefer Axes methods over the top-level `plt.plot`**: once you have an Axes object, draw directly on it (`ax.plot(...)`, `ax.hist(...)`, `ax.scatter(...)`) rather than the global `plt.plot`-style functions — this avoids ambiguity about which subplot you're drawing on.

```python
ax1.plot(np.random.standard_normal(50).cumsum(), color="black", linestyle="dashed")
ax1.hist(np.random.standard_normal(100), bins=20, color="black", alpha=0.3)   # alpha = transparency
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.standard_normal(30))
```

If subplots end up with overlapping tick labels (common with `sharex`/`sharey` and tight spacing), fix the spacing with `fig.subplots_adjust(wspace=0, hspace=0)` (percent of figure width/height used as padding between subplots).

## Colors, Line Styles, and Markers

```python
ax.plot(x, y, linestyle="--", color="green")             # dashed green line
ax.plot(data, linestyle="dashed", marker="o")              # add markers at each actual data point
ax.plot(data, linestyle="dashed", drawstyle="steps-post")   # step interpolation instead of straight lines between points
```

Markers (`marker="o"`) matter because `plot` linearly interpolates between points by default — without markers it can be unclear exactly where the real data points are.

## Labeling a Plot Properly

```python
ax.set_xlabel("Stages")
ax.set_title("My first matplotlib plot")
ax.set(title="My first matplotlib plot", xlabel="Stages")   # batch-set multiple properties at once

ticks = ax.set_xticks([0, 250, 500, 750, 1000])              # where the ticks go
labels = ax.set_xticklabels(["one", "two", "three", "four", "five"], rotation=30, fontsize=8)
```

**Audit-usable rule**: an unlabeled chart with default numeric ticks is not a report-ready chart — `set_title`/`set_xlabel`/`set_ylabel` plus, if needed, `set_xticklabels` for human-readable category names, are the minimum bar for anything that goes in front of a client.

## Legends

```python
ax.plot(data1, color="black", label="one")
ax.plot(data2, color="black", linestyle="dashed", label="two")
ax.legend()    # must be called explicitly — passing label= alone does not create a legend
```

To exclude a series from the legend, either don't pass a `label`, or pass `label="_nolegend_"`. The `loc` argument controls placement (default `"best"` auto-picks an out-of-the-way spot).

## Annotations

```python
ax.text(x, y, "Hello world!", family="monospace", fontsize=10)   # plain text at a data coordinate
```

`annotate` (with arrows) is the tool for calling out specific points on a chart — e.g., marking the date of a cost spike or a missed deadline directly on a time-series chart, rather than relying only on a caption.

## Saving Plots to File

```python
fig.savefig("figpath.png", dpi=400)   # file type inferred from extension (.png, .pdf, .svg, ...)
```

`dpi` controls resolution — worth bumping above the ~100 default when a chart needs to look sharp in a printed or PDF audit report. `facecolor`/`edgecolor` control the background color outside the plot area (defaults to white).

## Connects to

- [[pandas-summary-stats-and-value-counts]] — summary statistics are the typical input data a chart visualizes; clean the numbers first, then plot.
- [[reshaping-stack-unstack-pivot-melt]] — `pivot` is frequently the step right before plotting, since matplotlib (and pandas' plotting shortcuts) expect one series per column in a wide layout.

## Pathway Placement

- **Role**: reference for the parked **data-analysis strand** (candidate Stage 9-10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-05-data-shapes]] (lists, dictionaries, indexing), [[stages/stage-06-files-errors-debugging]] (files), and Stage 9's CSV/JSON work ([[concepts/csv-and-json]]).
- **Status**: parked per [[parking-lot]] (pandas/NumPy rows). Not part of the active Stage 0-10 path — do not introduce before Stage 9 mastery and Chris's go-ahead to build the strand.
