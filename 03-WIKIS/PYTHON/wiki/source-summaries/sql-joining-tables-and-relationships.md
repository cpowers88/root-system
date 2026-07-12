---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [reference, programming, parked, sql-strand]
---

# Practical SQL: Joining Tables in a Relational Database

**Summary**: The `JOIN ... ON` construct for combining rows across tables, the five JOIN types (JOIN/INNER, LEFT, RIGHT, FULL OUTER, CROSS), using `NULL` to find unmatched rows (anti-joins), the three table-relationship types (one-to-one, one-to-many, many-to-many), table aliases, multi-table joins, the set operators (UNION/UNION ALL/INTERSECT/EXCEPT), and performing math across joined tables.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 7 ("Joining Tables in a Relational Database")

**Last updated**: 2026-06-20

---

## Why Relate Tables at All

Following Edgar F. Codd's 1970 relational model, data is split into separate tables by entity (e.g., `departments` and `employees`) rather than crammed into one flat table. **Normalizing data this way avoids three problems**: repeating long strings across many rows (wasted space at scale), error-prone updates (changing one fact — like a department name — should mean editing one row, not thousands), and it doesn't sacrifice the ability to view data as a whole, since `JOIN` reassembles it on demand.

A **primary key** uniquely identifies each row in a table (must be unique, can't be missing). A **foreign key** is a column whose values must already exist in another table's referenced column (often that table's primary key) — unlike a primary key, a foreign key can be empty or contain duplicates. Primary key values only need to be unique *within* their own table — two different tables can reuse the same key values.

## JOIN ... ON Syntax

```sql
SELECT *
FROM employees JOIN departments
ON employees.dept_id = departments.dept_id;
```

The database connects rows where the `ON` clause expression evaluates `true` — any Boolean expression works, not just equality. Columns from both tables appear in the result if requested (even duplicated key columns, if using `SELECT *`).

## The Five JOIN Types

- **JOIN** (alternate syntax: **INNER JOIN**) — returns only rows where matching values exist in both tables. Best for well-maintained datasets where you only want rows present in all joined tables.
- **LEFT JOIN** — returns every row from the left table; unmatched right-table columns come back `NULL`.
- **RIGHT JOIN** — the mirror of LEFT JOIN: every row from the right table, unmatched left-table columns come back `NULL`.
- **FULL OUTER JOIN** — every row from both tables, matched where possible, `NULL` filled where not. Less commonly used; good for visualizing how much two partially-overlapping sources actually overlap.
- **CROSS JOIN** — every possible combination of rows from both tables (a *Cartesian product*; no `ON` clause needed, since there's no key match to evaluate). **Avoid on large tables** — two 250,000-row tables would produce 62.5 billion result rows.

A **`USING (column)`** clause can replace `ON table_a.col = table_b.col` whenever the joined column has an identical name in both tables — it also displays the shared column only once in the results, rather than duplicated.

## Using NULL to Find Missing Matches (Anti-Joins)

When a `LEFT JOIN` (or `RIGHT JOIN`) returns no match for a row, the unmatched side's columns come back as `NULL` rather than being omitted. Filtering `WHERE right_table.id IS NULL` after a `LEFT JOIN` isolates exactly the left-table rows with no match on the right — a pattern called an **anti-join**. (Reverse the direction with `RIGHT JOIN` + `WHERE left_table.id IS NULL` to find right-table-only rows.) `NULL` is distinct from `0` or an empty string — it specifically represents an unknown/absent value, and unlike those values it's consistent across all data types.

## Three Types of Table Relationships

- **One-to-one** — a key value in one table matches at most one row in the other (e.g., two tables both keyed by US state).
- **One-to-many** — one key value in a table matches multiple rows in another (e.g., one car manufacturer row relates to many model rows).
- **Many-to-many** — multiple rows in each table relate to multiple rows in the other; this typically requires a third intermediate ("junction") table holding the key pairs (e.g., a `players_positions` table linking `players` and `positions`).

Understanding which relationship type applies is essential for judging whether a join's result count makes sense given the database's actual structure.

## Selecting Specific Columns and Table Aliases

`SELECT *` is fine for quick checks, but selecting named columns avoids surprises if a table gains new columns later. **When the same column name exists in more than one joined table, prefix it with the table name** (`table_a.id`) — an unqualified `id` throws `column reference "id" is ambiguous`. **Table aliases** (declared in the `FROM` clause: `FROM table_name AS alias` or simply `table_name alias`) shorten repeated table-name references throughout the query — especially valuable once many columns or many tables are involved. The `AS` keyword is optional for aliases.

## Joining Multiple Tables

A query can chain additional `JOIN ... ON` clauses to bring in more tables, as long as each new join has a column to match on:

```sql
SELECT d20.id, d20.school_2020, en.enrollment, gr.grades
FROM district_2020 AS d20 JOIN district_2020_enrollment AS en
    ON d20.id = en.id
JOIN district_2020_grades AS gr
    ON d20.id = gr.id
ORDER BY d20.id;
```

There's no SQL-standard hard limit on the number of tables joinable in one query, though a given database system might impose one.

## Combining Query Results with Set Operators

Set operators combine the *results* of separate `SELECT` queries into one result, rather than placing columns side-by-side as a join does — useful when a downstream tool (e.g., a charting library) expects one long combined table instead of wide joined columns. **Both queries must return the same number of columns with compatible data types.**

- **UNION** — appends the second query's rows to the first's, removing duplicates.
- **UNION ALL** — same, but keeps duplicates.
- **INTERSECT** — returns only rows present in both queries' results, deduplicated.
- **EXCEPT** — returns rows in the first query's results that are absent from the second's, deduplicated.

`ORDER BY` applies once, after the set operation, and can't be attached to either individual `SELECT`. A useful customization pattern: add a literal string column (e.g., `SELECT '2020' AS year, ...`) to each half of a `UNION ALL` so the merged result can be traced back to its source query — directly useful when merging the same kind of data captured at two different points in time.

## Performing Math on Joined Table Columns

Chapter 6's arithmetic and `round()` patterns work identically across joined tables — just qualify each operand with its table name. Demonstrated by joining 2019 and 2010 Census county-population tables on a compound key (`state_fips` AND `county_fips`, combined with `AND` since the pairing — not either column alone — uniquely identifies a county) to compute `raw_change` and `pct_change` in population, sorted descending to surface the fastest-growing counties. This is the standard pattern for comparing any two periodic snapshots of the same entity (e.g., a "this year vs. last year" comparison).

## Key Takeaways

- Default to `JOIN`/`INNER JOIN` only when you specifically want to discard unmatched rows; use `LEFT`/`RIGHT JOIN` whenever you need to preserve all rows from one side, including ones with no match.
- A `LEFT JOIN` + `WHERE right.id IS NULL` is the standard anti-join pattern for finding what's missing between two datasets — directly useful any time you need to know which records in one source don't appear in another.
- Qualify column names with their table (or alias) whenever the same column name exists in more than one joined table.
- Set operators (UNION/INTERSECT/EXCEPT) solve a different problem than JOIN: stacking comparable result sets into one column set, rather than combining different columns side-by-side.

## Connects to

- [[sql-creating-databases-and-tables]] — primary/foreign key concepts introduced briefly here get a fuller treatment (constraints, indexes) in Chapter 8.
- [[sql-basic-math-and-stats]] — the percent-change formula and `round()` usage applied to joined 2010/2019 Census tables reuses Chapter 6's math patterns directly.
- [[sql-import-export-data]] — the 2010 Census comparison table is loaded using the same `COPY` import pattern covered in Chapter 5.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
