---
domain: technology
type: concept
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, subject/sql, stack/sql]
---

# SQL: Window Functions and Ranking

**Summary**: rank()/dense_rank() window functions, PARTITION BY for ranking within subgroups, rate calculations for fair cross-group comparisons, and rolling averages for smoothing noisy time-series data.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 11 ("Statistical Functions in SQL") — ranking/window-function and rate/smoothing sections

**Last updated**: 2026-07-13

---

## rank() and dense_rank()

Window functions compute a value across a "window" of related rows **without** collapsing them into one summary row per group, unlike `GROUP BY` (see [[sql-grouping-and-aggregate-functions]]) — every original row stays in the result, with the window function's output added as an extra column. `rank() OVER (ORDER BY column DESC)` assigns each row a rank; tied values get the same rank, and the *next* rank skips ahead by the number of ties (1, 2, 2, 4). `dense_rank()` behaves identically except it doesn't skip — ties still share a rank, but the next distinct value gets the very next integer (1, 2, 2, 3). Choice between them depends on whether skipped ranks after a tie are meaningful for the use case (e.g., "3rd place" after two people tied for 1st vs. "2nd place").

## PARTITION BY: Ranking Within Subgroups

`rank() OVER (PARTITION BY category_column ORDER BY value_column DESC)` resets the ranking separately within each value of `category_column` — e.g., ranking stores by sales *within each region* rather than one global ranking across every store regardless of region. This is the single most useful window-function pattern for client reporting: "top performer per category" rather than just "top performer overall."

## Rate Calculations for Fair Comparisons

Raw counts mislead when comparing populations of different sizes (a county with more businesses isn't necessarily "more business-friendly" — it might just have more people). Rates (count per 1,000 or per 100,000 population) normalize for population size before comparing, the standard technique whenever comparing a count-based metric across unevenly-sized groups.

## Smoothing with Rolling Averages

A rolling (moving) average — computed via a window function ranging over a fixed number of preceding rows — smooths short-term noise out of a time series to reveal the underlying trend, at the cost of lagging behind sudden real changes. Rolling averages need date-ordered, gap-free data to be meaningful; missing periods in the underlying series distort the window's actual time span without the calculation itself flagging that anything is wrong.

## Key Takeaways

- Window functions add a computed column per row without collapsing the result — the key structural difference from `GROUP BY`.
- `PARTITION BY` is the pattern for "rank within category" — the most commonly useful window-function shape for reporting.
- Always convert to a rate (per capita, per 1,000) before comparing counts across differently-sized groups — raw counts alone are a common, easy-to-miss audit-report error.
- Rolling averages assume gap-free, date-ordered input; verify that before trusting a smoothed trend line.

## Connects to

- [[sql-grouping-and-aggregate-functions]] — the structural contrast (collapses rows) that window functions (keeps every row) deliberately avoid.
- [[sql-importing-and-basic-math]] — `sum()`/`avg()` from that page are the aggregate functions window functions extend into a per-row, non-collapsing form.

## North Star Connection

- How this applies to the audit business: "top N per category" and rate-normalized comparisons are two of the most common client-facing report shapes — both are direct applications of this page's techniques.
- Track relevance: Tech — SQL reporting technique, builds on [[sql-grouping-and-aggregate-functions]].
- Possible future Second Brain use: Yes — the standard technique for any "rank within category" or population-normalized comparison report.
