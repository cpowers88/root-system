---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [reference, programming, parked, sql-strand]
---

# Practical SQL: Extracting Information by Grouping and Summarizing

**Summary**: Aggregate functions (`count()`, `max()`/`min()`, `sum()`) for summarizing a column into a single value, the `GROUP BY` clause for aggregating per-category, combining `GROUP BY` with joins and percent-change math to track multi-year trends, and the `HAVING` clause for filtering aggregated results — all demonstrated on three years of IMLS Public Libraries Survey data.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 9 ("Extracting Information by Grouping and Summarizing")

**Last updated**: 2026-06-20

---

## Validating an Import with count()

After any import, `count(*)` confirms the row total matches what the data source's documentation states — a fast first check for missing rows or a wrong-file import (here: 9,261/9,245/9,252 rows for the 2018/2017/2016 library survey tables, matching the IMLS documentation exactly). Supplying a column name instead of `*` (`count(phone)`) counts only **non-`NULL`** values in that column — useful for verifying a `NOT NULL` constraint actually holds or for spotting unexpectedly sparse data. Adding `DISTINCT` (`count(DISTINCT libname)`) counts unique values only — comparing this against the plain `count()` surfaced that 526 library agencies share a name with at least one other (ten are all named "Oxford Public Library," in ten different towns called Oxford).

## max() and min() as a Data-Quality Check

Beyond showing the range of real values, `max()`/`min()` can expose **sentinel values** — placeholder numbers a dataset uses to encode a special condition rather than an actual measurement. The library survey's `visits` column returned a minimum of `-3`, not a data error: the survey convention uses `-1` for "nonresponse" and `-3` for "not applicable" (agency closed). **Negative sentinel values must be filtered out with `WHERE column >= 0` before summing or averaging**, or they silently corrupt the total. The author notes a cleaner schema design would use actual `NULL` plus a separate `_flag` column to explain the absence — but that's not always within an analyst's control when working with someone else's data.

## GROUP BY

`GROUP BY column_name` (standard ANSI SQL) collapses duplicate values in the grouped column(s), similar to `DISTINCT`, and can group on multiple columns at once (`GROUP BY city, stabr` surfaces every unique city/state combination). **Any column selected alongside an aggregate function must appear in the `GROUP BY` clause**, or the database raises an error — you can't mix an aggregated value and an ungrouped raw column in the same result. Combining `GROUP BY` with `count(*)` (`SELECT stabr, count(*) ... GROUP BY stabr ORDER BY count(*) DESC`) produces a per-category frequency count — used to find which states have the most library agencies (New York, Illinois, Texas led in 2018). **A high agency count doesn't necessarily mean a high outlet/branch count** — those are different columns (`centlib`, `branlib`) requiring `sum()`, a reminder to verify what a column actually measures before drawing a conclusion from it.

Grouping on two columns together (`GROUP BY stabr, stataddr`) reveals the frequency of every combination — used here to confirm that the "no address change" code (`00`) was the most common value in every state, which is itself a sanity check: if a "moved" code had been most common everywhere, that would flag a likely query or data error rather than a real trend.

## Combining GROUP BY, JOIN, and Percent-Change Math

Summing `visits` separately across the 2018/2017/2016 tables suggested a ~5% national decline, but each table has a slightly different row count (agencies opening/closing/merging), so a more rigorous comparison joins all three tables on the shared `fscskey` primary key and sums only the agencies present (and non-negative) in all three — narrowing to agencies that exist consistently across the period. This refined join-based total confirmed the same downward trend (1.36B → 1.32B → 1.29B visits), while the same query swapped to a `wifisess` column revealed Wi-Fi usage rose sharply over the same period — a useful illustration that **a single declining metric doesn't tell the whole story; check adjacent metrics before concluding "libraries are in decline."**

Grouping the joined, percent-change query by `stabr` (state) breaks the national trend down geographically, surfacing wide variation: some states grew (up to +3.4%) while others (American Samoa, -28%) collapsed. **A national aggregate can mask regional reality — always check whether a trend holds uniformly before generalizing it.**

## HAVING — Filtering an Aggregated Result

`WHERE` filters rows *before* aggregation and can't reference an aggregate function's result (aggregate functions operate across rows, not within one). **`HAVING` filters *after* aggregation, evaluated against the grouped/summed values** — e.g., `HAVING sum(pls18.visits) > 50000000` narrows a per-state percent-change report down to only the handful of states with the largest visit volume, so trend comparisons happen between comparably sized groups rather than across wildly different scales (a small state's volatility shouldn't be compared directly to a large state's). This is the standard technique whenever you want to filter on a computed total/count/average rather than a raw column value.

## Key Takeaways

- Run `count(*)` (and `count(column)`/`count(DISTINCT column)`) immediately after any import — it's the fastest way to confirm row totals match documentation and spot unexpectedly sparse or duplicate-heavy columns.
- `max()`/`min()` aren't just descriptive — they're a data-quality probe. An implausible extreme value (a negative count, a date far in the future) usually means the dataset uses a sentinel/placeholder convention that must be filtered out before further math.
- `WHERE` filters rows pre-aggregation; `HAVING` filters groups post-aggregation — reach for `HAVING` whenever the filter condition involves a `sum()`/`count()`/`avg()` result.
- A national/aggregate-level trend can hide opposite trends within subgroups — always check whether a headline number holds when broken out by category (state, region, segment) before treating it as the whole story.

## Connects to

- [[sql-joining-tables-and-relationships]] — the three-year library-trend query directly reuses the multi-table JOIN and table-alias patterns from Chapter 7, joining on a shared natural key (`fscskey`).
- [[sql-basic-math-and-stats]] — the percent-change formula applied per-state here is the identical calculation from Chapter 6's Census population work, just nested inside a `GROUP BY`.
- [[sql-table-design-constraints-and-indexes]] — the library tables' `fscskey` natural-key and `libname` index were both set up using Chapter 8's constraint/indexing techniques.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
