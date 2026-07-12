---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [reference, programming, parked, sql-strand]
---

# Practical SQL: Advanced Query Techniques

**Summary**: Subqueries (scalar/correlated/uncorrelated, derived tables, subquery expressions IN/EXISTS), LATERAL joins, Common Table Expressions, cross-tabulations via the `crosstab()` function, and the `CASE` statement for reclassifying values — the toolkit for restructuring a query to answer a more specific question than a single `SELECT`/`GROUP BY` can.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 13 ("Advanced Query Techniques")

**Last updated**: 2026-06-20

---

## Subqueries: Definition and Three Classifications

A subquery is a query nested inside another query, in parentheses. Three useful ways to classify one: a subquery placed in `FROM` produces a **derived table** — a queryable, joinable result set. A **scalar subquery** returns a single value, usable inside a `WHERE`/`IN`/`HAVING` expression. **Correlated** subqueries depend on values from the outer query/table to execute (they run once per outer row); **uncorrelated** subqueries don't depend on the outer query at all (they run once, independently).

## Filtering with Subqueries in WHERE and DELETE

A scalar subquery in `WHERE` lets one query do what would otherwise need two: `WHERE pop_est_2019 >= (SELECT percentile_cont(.9) WITHIN GROUP (ORDER BY pop_est_2019) FROM us_counties_pop_est_2019)` finds the top 10% of US counties by population in a single statement. **Caveat: `percentile_cont()` only works this way with a single non-array input** — passing an array breaks the `>=` comparison. The identical pattern works in `DELETE`'s `WHERE` clause — e.g., deleting every row below a percentile cutoff from a backup copy of a table, to leave only the top tier.

## Derived Tables

A subquery placed in `FROM` becomes a queryable/joinable table on the fly — useful for computing intermediate aggregates once, then operating on them. Example: a subquery computing both the average and the median population (aliased `calcs`), with the outer query then computing `average - median` to show how far a skewed average sits from the median (avg 104,468 vs. median 25,726 — a gap of 78,742, nearly 3x the median, showing a handful of very large counties pull the average up).

**Joining derived tables**: two separate derived tables — one summing tourism-business establishments by state, one summing population by state — joined `ON est.st = census.state_name` to compute a tourism-business rate per 1,000 population per state. Top: DC, Montana, Vermont, Maine, Wyoming; bottom: Arizona, Alabama, Utah, Mississippi, Kentucky.

**Generating columns with subqueries**: a scalar, uncorrelated subquery placed directly in the `SELECT` column list (must return exactly one row) — e.g., showing the national median population alongside every county's own value, or computing `pop_est_2019 - (subquery) AS diff_from_median` and reusing the same subquery in a `WHERE ... BETWEEN` filter to find counties closest to the median. **Caveat: repeating the same subquery in multiple places adds execution time on large tables** — a problem CTEs solve (see below).

## Subquery Expressions: IN and EXISTS

`WHERE column IN (SELECT ... FROM other_table)` — an uncorrelated subquery expression matching rows against a separately computed list. **Explicit warning: avoid `NOT IN`** — if the subquery's result set contains any `NULL`, `NOT IN` silently returns zero rows for the entire query; the PostgreSQL wiki recommends `NOT EXISTS` instead.

`WHERE EXISTS (SELECT ... FROM other_table WHERE other_table.id = outer_table.id)` — a **correlated** subquery expression that evaluates to true/false once per outer row, referencing the outer query's own values. Particularly useful when a match needs more than one column (`IN` can't do that). `NOT EXISTS` finds rows with no match in the other table — a direct way to find missing values or assess dataset completeness.

## LATERAL Subqueries

**LATERAL with FROM**: a `LATERAL` subquery in `FROM` can reference tables or subqueries listed *before* it in the same `FROM` clause, avoiding redundant recalculation. Example: a first `LATERAL` subquery computes a raw year-over-year population change; a second `LATERAL` subquery reuses that value to compute the percent change, rather than recalculating the raw difference itself. Subqueries used this way in `FROM` must carry an alias.

**LATERAL with JOIN**: combining `LATERAL` with `JOIN` behaves like a for-loop — for each row of the preceding table, the LATERAL-joined subquery runs once, correlated to that row. Demonstrated finding each teacher's two most recent lab-access records: `LEFT JOIN LATERAL (SELECT * FROM access WHERE teacher_id = t.id ORDER BY access_time DESC LIMIT 2) a ON true`. The syntax requires an alias (`a`) and `ON true` (no specific join columns are being matched — `ON true` just enables the correlated per-row execution). Using `LEFT JOIN` (rather than plain `JOIN`) preserves teachers with zero access records, shown as `NULL` rows.

## Common Table Expressions (CTEs)

`WITH name (col1, col2, ...) AS (subquery) SELECT ... FROM name` — informally "WITH queries." The column-rename list is optional; column types are inherited from the subquery automatically. A single `WITH` clause can define **multiple** named temporary tables (comma-separated), each then available to the main query and to each other — a cleaner, more readable rewrite of the derived-table-join pattern above.

CTEs also eliminate **redundant subquery code**: rather than repeating an identical `percentile_cont(.5)` subquery in both a calculated column and a `WHERE` filter, define it once as `WITH us_median AS (...)` and reference it via `CROSS JOIN us_median` — the cross join makes that single computed value available to every row, written once and used as many times as needed. Briefly noted but out of scope here: the `RECURSIVE` CTE keyword, for looping through hierarchical data such as an org chart's reporting structure.

## Cross Tabulations (Pivot Tables)

A crosstab summarizes two variables in a row/column matrix, with a value (count, percentage) at each row-column intersection. Standard ANSI SQL has no crosstab function; PostgreSQL provides `crosstab()` through the `tablefunc` module, enabled with `CREATE EXTENSION tablefunc;` (SQL Server's equivalent is `PIVOT`).

`crosstab()` takes two query parameters (passed as quoted strings) plus an `AS` column-definition list:
1. The **data query** — three required columns: row name, category/column name, and the intersection value (e.g., `office`, `flavor`, `count(*)`, grouped by office and flavor).
2. The **category query** — must return exactly one column, listing the unique category values that will become columns (e.g., `SELECT DISTINCT flavor ... ORDER BY flavor`).
3. The `AS (row_col type, cat1 type, cat2 type, ...)` clause names and types the output columns — **the column order must match the order the category query produces them in** (e.g., alphabetical, if that's how the category query sorts).

Demonstrated on a 200-row ice-cream-flavor survey (`office`, `flavor` columns) — the flat `GROUP BY office, flavor` list made chocolate look like the clear favorite, but the crosstab revealed nuance the flat list hid: Midtown favors chocolate with **zero** strawberry votes (shown as `NULL`), Downtown actually prefers strawberry, and Uptown is roughly even across all three flavors. A second example cross-tabulated a year of daily temperature readings from three weather stations into a station-by-month median-high-temperature table, using `date_part('month', ...)` to generate column categories and PostgreSQL's `generate_series(1,12)` to supply the twelve month labels for the category query. **Caveat: `crosstab()` is resource-intensive — use it cautiously on tables with millions/billions of rows.**

## Reclassifying Values with CASE

The ANSI-standard `CASE` statement is a conditional expression — "if this, then..." logic inside a query:

```sql
CASE WHEN condition THEN result
     WHEN another_condition THEN result
     ELSE result
END
```

Each `WHEN` is evaluated in order; the first one that's true returns its `result` and stops evaluating further conditions. The optional `ELSE` clause supplies a fallback when no condition matches — **without it, an unmatched row returns `NULL`** rather than an error. Demonstrated reclassifying daily max temperatures into six descriptive bands (Hot/Warm/Pleasant/Cold/Frigid/Inhumane) using `>=`/`<` range conditions covering every possible value with no gaps.

**Using CASE inside a CTE**: wrapping the same `CASE` reclassification in a `WITH temps_collapsed (...) AS (...)` CTE, then running `GROUP BY station_name, max_temperature_group` with `count(*)` on top of it, turns a year of daily readings into a compact climate profile per city — e.g., revealing Waikiki as "Warm" 361 days a year (confirming its reputation), while Chicago spends 30 days "Frigid" and 8 "Inhumane." This is the general pattern for any "collapse a continuous measure into business-meaningful categories, then count by category" question.

## Key Takeaways

- Subqueries let a single query do filtering (`WHERE`/`DELETE`), pre-aggregation (derived tables, `FROM`), or row-by-row matching (`IN`/`EXISTS`) without splitting the work across multiple manual queries.
- `EXISTS`/`NOT EXISTS` (correlated) is the safer, more flexible alternative to `IN`/`NOT IN` (uncorrelated) — especially avoid `NOT IN` whenever the subquery's result might contain a `NULL`.
- `LATERAL` is the tool whenever a `FROM`/`JOIN` subquery needs to reference a value from an earlier item in the same `FROM` clause, or needs to run once per outer row (e.g., "top N per group").
- CTEs (`WITH ... AS`) are the readability and redundancy-elimination upgrade over derived tables and repeated subqueries — write a calculation once, reference it by name as many times as needed.
- `crosstab()` (via the `tablefunc` extension) turns a flat `GROUP BY` list into a row/column matrix that often reveals patterns a flat list hides — at the cost of being resource-intensive on very large tables.
- `CASE` is the standard way to collapse a continuous measure into named categories before counting, grouping, or reporting on it.

## Connects to

- [[sql-grouping-and-aggregate-functions]] — derived tables and CTEs are structural alternatives to plain `GROUP BY` for the same kind of "aggregate then compare" question; `crosstab()` is a direct visual upgrade over a flat `GROUP BY` result.
- [[sql-joining-tables-and-relationships]] — joining two derived tables (tourism establishments + population by state) is the JOIN pattern from Chapter 7 applied to subquery results instead of base tables.
- [[sql-basic-math-and-stats]] — the percentile-based top-10%-of-counties filter and the median-max-temp crosstab both reuse `percentile_cont()` directly from Chapter 6.
- [[sql-dates-and-times]] — the temperature crosstab reuses `date_part('month', ...)` from Chapter 12 to generate the crosstab's category columns.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
