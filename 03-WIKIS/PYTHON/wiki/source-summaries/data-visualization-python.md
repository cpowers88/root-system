---
type: source-summary
timeline: reference
status: parked
source_role: project-source
difficulty: stage-10
source_file: raw/books/PythonCrashCourse.pdf
tags: [programming, stage-10-support]
---

# Data Visualization in Python (Matplotlib & Plotly)

**Summary**: Python's two main data visualization libraries — Matplotlib for static/customizable charts and Plotly for interactive, browser-rendered charts and maps — covered through the lens of generating and downloading datasets, then visualizing them.

**Sources**: python-crash-course.pdf (Chapters 15–16)

**Last updated**: 2026-06-17

---

## Matplotlib basics

Matplotlib is the standard plotting library for static charts. Core pattern:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)
ax.set_title("Title", fontsize=24)
ax.set_xlabel("X label", fontsize=14)
ax.set_ylabel("Y label", fontsize=14)
ax.tick_params(labelsize=14)
plt.show()
```
(source: python-crash-course.pdf)

- `fig` = the whole figure; `ax` = a single plot within it — almost all styling happens on `ax`.
- `ax.scatter()` for point plots, supports `s=` (size), `color=`, or a colormap via `c=values, cmap=plt.cm.Blues` to encode a third dimension as color.
- Built-in styles via `plt.style.use('seaborn')` (or similar) applied before `subplots()`.
- `plt.savefig('file.png', bbox_inches='tight')` to save instead of (or alongside) displaying.
- `ax.fill_between(x, series_a, series_b, alpha=0.1)` shades the region between two series — useful for showing a range/band (e.g., high/low temperature, min/max of any business metric) (source: python-crash-course.pdf).

## Reading real-world data into a plot

- **CSV**: `csv.reader()` over lines read via `pathlib.Path.read_text().splitlines()`. First row is usually headers — inspect with `enumerate(header_row)` to find the column indexes you need before looping over data rows (source: python-crash-course.pdf).
- **Dates**: `datetime.strptime(value, '%Y-%m-%d')` converts string dates to objects you can plot directly on an x-axis; `fig.autofmt_xdate()` angles the labels so they don't overlap.
- **Error handling on messy data**: wrap row-extraction in `try/except ValueError ... else:` so one malformed/missing field doesn't crash the whole import — only append to your result lists in the `else` block. This is the realistic shape of working with real (not toy) datasets exported from another system (source: python-crash-course.pdf).
- **JSON / GeoJSON**: `json.loads()` to parse, `json.dumps(data, indent=4)` to pretty-print and explore an unfamiliar nested structure before writing extraction code. Real-world JSON data is usually a dict with a list of records nested inside (e.g., GeoJSON's `"features"` list, each a dict with `"properties"` and `"geometry"`) — the general pattern is: load → find the list of records → loop and pull out the specific keys you need.

## Plotly Express

Plotly renders interactive charts as HTML (opens in browser), and is the better choice when output needs to be explored by someone else, not just viewed once.

```python
import plotly.express as px

fig = px.bar(x=names, y=values, title=title, labels={'x': '...', 'y': '...'})
fig.show()            # opens in browser
fig.write_html('out.html')   # save instead
```
(source: python-crash-course.pdf)

- Philosophy: write the simplest possible call first, confirm the data is right, *then* layer on styling — avoids wasted customization on wrong data.
- `fig.update_layout(...)` changes chart-level settings (titles, font sizes, tick spacing via `xaxis_dtick=1`).
- `fig.update_traces(marker_color=..., marker_opacity=...)` changes the data markers themselves.
- `px.scatter_geo(lat=, lon=, size=, color=, color_continuous_scale=, hover_name=, projection='natural earth')` plots geographic data on a world map — `size`/`color` can both encode a magnitude (e.g., earthquake severity), and `hover_name` adds a label shown on hover (source: python-crash-course.pdf).
- Interactivity (resize-to-fit, hover tooltips) comes for free — no extra code required beyond the normal call.

## Connects to

- [[working-with-apis-python]] — APIs are the other major source of the data fed into these visualizations; the combination (pull via API → visualize via Plotly) is the same pipeline shape end to end.
- [[source-map]] — Python Crash Course's full entry (chapter→stage mapping) lives there; the FORGE-era whole-book hub page was archived 2026-07-07.

## Pathway Placement

- **Role**: support/project-source detail for **Stage 10** — this material is already on the Source Roster as "PCC Part II" in [[learning-path]]; this page is the pre-ingested detail for those chapters.
- **Prerequisites**: [[stages/stage-10-application-thinking]]; the APIs material pairs with [[concepts/apis-and-web-requests]], the visualization material with the Stage 10 capstone options.
- **Status**: parked until Chris reaches Stage 10 (see [[parking-lot]], APIs / web-scraping / image-graphs rows). No change to the mapped path needed — the Source Roster already accounts for these chapters.
