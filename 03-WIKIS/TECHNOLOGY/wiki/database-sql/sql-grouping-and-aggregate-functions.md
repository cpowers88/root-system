---
domain: technology
type: concept
tags: [subject/sql]
timeline: now
status: wiki-only
source_role: primary
use_cases: [data-workflow]
stack: [sql]
---

# SQL: Grouping and Aggregate Functions

**Summary**: count()/max()/min() as aggregate functions, GROUP BY for per-category summaries (single and multi-column), and HAVING for filtering on aggregated results.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 9 ("Extracting Information by Grouping and Summarizing")

**Last updated**: 2026-07-13

---

## count(), max(), min()

`count(*)` counts all rows; `count(column)` counts only rows where that column is non-`NULL` (a fast way to spot missing-value gaps — compare `count(*)` against `count(some_column)` on the same table). `count(DISTINCT column)` counts unique values rather than all non-null occurrences. `max()`/`min()` find the largest/smallest value in a column across the matched rows.

## GROUP BY

`GROUP BY column` collapses all rows sharing the same value in that column into one summary row — any aggregate function in the `SELECT` list (typically paired with `count()`, `sum()`, `avg()`) then computes per-group instead of across the whole table. Grouping by multiple columns (`GROUP BY city, state`) produces one row per unique combination, similar in spirit to multi-column `DISTINCT` (see [[sql-select-where-and-filtering]]) but with aggregation attached rather than just deduplication.

A concrete pattern: `SELECT state, count(*) FROM table GROUP BY state ORDER BY count(*) DESC;` — ranks categories by frequency, a near-universal first exploratory query on any new categorical column.

## HAVING

`WHERE` filters rows *before* grouping; `HAVING` filters groups *after* aggregation — the only clause that can reference an aggregate function's result directly (`HAVING count(*) > 10` — "only show groups with more than 10 rows"). This distinction (row-level filter vs. group-level filter) is a common point of confusion: attempting to use `WHERE` with an aggregate function fails, because at the point `WHERE` executes, no aggregation has happened yet.

## Key Takeaways

- Comparing `count(*)` against `count(specific_column)` on the same table is a fast, standard way to quantify how many rows are missing a value in that column.
- `GROUP BY` + `count(*)` + `ORDER BY count(*) DESC` is close to a universal first query for understanding the distribution of any categorical column.
- `HAVING` filters on aggregated (post-`GROUP BY`) results; `WHERE` filters on raw rows before grouping — they operate at different stages and aren't interchangeable.

## Connects to

- [[sql-select-where-and-filtering]] — `HAVING` is the group-level counterpart to `WHERE`'s row-level filtering; `GROUP BY` generalizes `DISTINCT`.
- [[sql-inspecting-and-modifying-data]] — the `count(*)` vs. `count(column)` missing-value check is the entry point into the fuller data-quality inspection workflow covered there.
- [[sql-window-functions-and-ranking]] — window functions (rank/PARTITION BY) extend this same grouped-aggregation idea without collapsing rows into one summary row per group.
- [[data-science-ml/information-gain-entropy-and-attribute-selection]] — entropy/information gain is a more formal, predictive-purpose-built cousin of the same "how is this population distributed" question `GROUP BY`/`count()` answers descriptively.

## North Star Connection

- How this applies to the audit business: `GROUP BY`-based summaries are the standard shape of a client-facing report — totals and counts by category, region, or time period.
- Track relevance: Tech — foundational SQL, direct extension of [[sql-select-where-and-filtering]].
- Possible future Second Brain use: Yes — the default reporting-query pattern for categorical summaries.
