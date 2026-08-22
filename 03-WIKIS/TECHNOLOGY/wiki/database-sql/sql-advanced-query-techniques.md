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

# SQL: Advanced Query Techniques — Subqueries, CTEs, and CASE

**Summary**: Subqueries in WHERE/FROM/column-list positions, EXISTS/NOT EXISTS for correlated existence checks, LATERAL for row-by-row subquery evaluation, Common Table Expressions for readable multi-step queries, and CASE for reclassifying values inline.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 13 ("Advanced Query Techniques")

**Last updated**: 2026-07-13

---

## Subqueries

A subquery is a complete `SELECT` statement nested inside another query, and it can appear in several positions:

- **In `WHERE`**: generates a value or set of values to filter against (`WHERE population >= (SELECT percentile_cont(0.9) ...)`) — lets a filter threshold be computed from the data itself rather than hardcoded.
- **As a derived table in `FROM`**: `FROM (SELECT ...) AS alias` — treats a subquery's result as if it were a table, joinable with other tables/derived tables just like a real one.
- **In the column list**: a subquery that returns exactly one value per outer row can appear directly in `SELECT`, computing a per-row value (e.g., a per-county share of a state total).

Subqueries also work inside `DELETE`/`UPDATE` statements the same way they work in a `SELECT`'s `WHERE` clause — generating the set of rows to act on.

## EXISTS and NOT EXISTS

A **correlated subquery** references a column from the outer query inside the subquery itself, re-evaluating per outer row rather than running once. `WHERE EXISTS (correlated subquery)` checks whether any matching row exists at all — often faster and clearer than an equivalent `IN` subquery when only existence (not the actual matched values) matters. `NOT EXISTS` inverts the check — "find rows in table A with no corresponding row in table B," a join-free alternative to the `LEFT JOIN ... WHERE ... IS NULL` pattern from [[sql-joining-tables-and-relationships]].

## LATERAL

`LATERAL` before a subquery in a `FROM` clause allows that subquery to reference columns from a table earlier in the same `FROM` clause — normal subqueries can't do this. Combined with `JOIN`, `LATERAL` behaves similarly to a for-loop: for each row on the left, re-run the subquery using that row's own values (e.g., "for each teacher, find their two most recent access-log entries").

## Common Table Expressions (CTEs)

`WITH name AS (SELECT ...) SELECT ... FROM name` names a subquery upfront and can reference it multiple times in the main query — the same underlying capability as a derived table in `FROM`, but readable top-to-bottom and avoiding writing the same subquery logic twice when it's needed in more than one place. CTEs are the preferred technique over nested derived tables once a query has more than one or two levels of subquery, purely for readability and to eliminate duplicated logic.

## CASE for Reclassifying Values

```sql
SELECT max_temp,
  CASE WHEN max_temp >= 90 THEN 'hot'
       WHEN max_temp >= 70 THEN 'warm'
       ELSE 'cool'
  END AS temp_category
FROM table;
```

`CASE WHEN ... THEN ... ELSE ... END` evaluates conditions in order and returns the first match — a general-purpose inline reclassification/bucketing tool, usable directly in a `SELECT` list or inside a CTE for a multi-step reclassify-then-aggregate query.

## Key Takeaways

- `WHERE EXISTS`/`NOT EXISTS` with a correlated subquery is often the clearer (and sometimes faster) alternative to `IN` or an outer-join-plus-`IS NULL` pattern when only existence matters.
- Prefer CTEs over nested derived tables once a query needs more than one level of subquery — readability and avoiding duplicated subquery logic both matter more than the marginal terseness of nesting.
- `CASE` is the standard tool for turning a continuous or many-valued column into a small number of meaningful categories directly in a query, without a separate data-transformation step.

## Connects to

- [[sql-joining-tables-and-relationships]] — `NOT EXISTS` is a join-free alternative to that page's `LEFT JOIN ... WHERE ... IS NULL` orphan-row pattern.
- [[sql-grouping-and-aggregate-functions]] — CTEs are frequently used to reclassify with `CASE` first, then `GROUP BY` the reclassified category in a second step.
- [[web-frameworks/flask-rest-apis]] — `Model.query.paginate()`'s `LIMIT`/`OFFSET` pagination pattern is the ORM-level equivalent of scoping a derived-table subquery to a page of results.

## North Star Connection

- How this applies to the audit business: CTEs make a multi-step audit query (filter → reclassify → aggregate) readable and maintainable months later, when the exact reasoning needs to be re-explained to a client or revisited for a follow-up engagement.
- Track relevance: Tech — SQL technique, builds on [[sql-select-where-and-filtering]] and [[sql-grouping-and-aggregate-functions]].
- Possible future Second Brain use: Yes — CTEs are the default structure for any non-trivial multi-step client reporting query going forward.
