---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [programming, sql-strand]
---

# Practical SQL: Beginning Data Exploration with SELECT

**Summary**: The core query toolkit for "interviewing" a dataset — `SELECT`, `ORDER BY`, `DISTINCT`, and `WHERE` with comparison/matching operators (`=`, `<>`, `BETWEEN`, `LIKE`/`ILIKE`, `AND`/`OR`) — framed explicitly as a data-quality inspection process, not just a retrieval mechanism.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 3 ("Beginning Data Exploration with SELECT")

**Last updated**: 2026-06-20

---

## SELECT as Data Interviewing

The chapter frames `SELECT` queries as a process of **interviewing the data** — checking whether it's clean or dirty, complete or missing values, and what story it tells — analogous to interviewing a job candidate to see if reality matches the résumé. `SELECT * FROM teachers;` retrieves every row and column (`*` is a wildcard meaning "all columns"); `SELECT last_name, first_name, salary FROM teachers;` retrieves only named columns, in whatever order they're listed, regardless of the table's actual column order. **Limiting columns in early exploratory queries is itself a data-quality check** — confirming dates are properly formatted, every row has values where expected, and no unexpected gaps exist in the value range.

## Sorting with ORDER BY

```sql
SELECT first_name, last_name, salary
FROM teachers
ORDER BY salary DESC;
```

`ORDER BY` sorts query *output* only — it never changes the underlying table. Default order is ascending (`ASC`, the default); `DESC` reverses it. `ORDER BY` can reference a column by its position number in the `SELECT` clause (e.g., `ORDER BY 3 DESC`) instead of its name, and can sort on multiple columns (`ORDER BY school ASC, hire_date DESC`) for layered sorts — though stacking more than two or three sort columns quickly produces output too complex to read or communicate clearly; better to run several focused queries than one over-sorted one.

## Finding Unique Values with DISTINCT

```sql
SELECT DISTINCT school FROM teachers ORDER BY school;
```

`DISTINCT` (placed immediately after `SELECT`) eliminates duplicate rows from the result, useful for understanding the actual range of values in a column — and for spotting **data-quality problems directly**: inconsistent spelling variants of the same value, or malformed dates stored as free-text rather than a proper `date` type, both show up immediately as spurious extra "unique" values. `DISTINCT` across multiple columns (`SELECT DISTINCT school, salary FROM teachers`) returns each unique *combination* of those columns' values, not just unique values per column independently — letting you ask "for each X, what are all the Y values?"

## Filtering Rows with WHERE

`WHERE` restricts which rows a query returns, using comparison operators:

| Operator | Function | Example |
|---|---|---|
| `=` | Equal to | `WHERE school = 'Baker Middle'` |
| `<>` or `!=` | Not equal to | `WHERE school <> 'Baker Middle'` |
| `>` `<` `>=` `<=` | Greater/less than (or equal) | `WHERE salary > 20000` |
| `BETWEEN` | Within a range (inclusive) | `WHERE salary BETWEEN 20000 AND 40000` |
| `IN` | Match one of a set | `WHERE last_name IN ('Bush', 'Roush')` |
| `LIKE` / `ILIKE` | Pattern match, case-sensitive / insensitive | `WHERE first_name ILIKE 'sam%'` |
| `NOT` | Negates a condition | `WHERE first_name NOT ILIKE 'sam%'` |

**`BETWEEN` is inclusive on both ends** — a caution worth noting, since chaining two adjacent `BETWEEN` ranges (e.g., 10–20 and 20–30) will double-count any row with the boundary value 20; using explicit `>=`/`<=` instead avoids the ambiguity.

`LIKE` (ANSI standard, case-sensitive) and `ILIKE` (PostgreSQL-specific, case-insensitive) match text patterns using `%` (one or more characters) and `_` (exactly one character) wildcards. The author's stated practice is to default to `ILIKE` for data-quality vetting specifically because it won't silently miss results due to inconsistent capitalization in how names or proper nouns were originally entered. Pattern matching (`LIKE`/`ILIKE`) is slower on large tables than exact-match comparisons; indexes (covered in [[sql-table-design-constraints-and-indexes]] once ingested) mitigate this.

## Combining Operators with AND/OR

`AND` requires every connected condition to be true; `OR` requires only one. **Without explicit parentheses, `AND` is evaluated before `OR`** — so `WHERE school = 'X' AND salary < 38000 OR salary > 40000` does NOT mean "school X with salary outside that range"; it means "(school X AND salary<38000) OR (any school with salary>40000)." Wrapping the `OR` portion in parentheses — `WHERE school = 'X' AND (salary < 38000 OR salary > 40000)` — forces the intended grouping. This is one of the most common sources of silently wrong query results, since the query still runs without error.

## Standard Query Order

```sql
SELECT column_names
FROM table_name
WHERE criteria
ORDER BY column_names;
```

SQL enforces this clause order strictly (`SELECT` → `FROM` → `WHERE` → `ORDER BY`) even though it doesn't enforce formatting style.

## Key Takeaways

- Treat early SELECT queries as a data-quality interview, not just a way to fetch known-good data — DISTINCT and ORDER BY both double as diagnostic tools.
- BETWEEN's inclusivity is a common silent double-counting trap; prefer explicit >=/<= when chaining ranges.
- AND binds tighter than OR with no parentheses — always parenthesize mixed AND/OR conditions explicitly, since the query will run "successfully" with the wrong logic otherwise.
- ILIKE is the safer default for any data-vetting query involving names or free-text fields, since it won't miss inconsistent capitalization.

## Connects to

- [[sql-creating-databases-and-tables]] — uses the same `teachers` table created in Chapter 2 as its running example throughout.
- [[python-for-data-analysis]] — pandas' `.loc`/boolean-mask filtering and `.sort_values()` are the DataFrame-side equivalents of SQL's WHERE and ORDER BY, for audit work that moves between SQL storage and Python analysis.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
