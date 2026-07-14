---
domain: technology
type: concept
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, subject/sql, stack/sql]
---

# SQL: SELECT, WHERE, and Filtering

**Summary**: The core query vocabulary — SELECT with column subsets, sorting with ORDER BY, finding unique values with DISTINCT, filtering rows with WHERE and its comparison/pattern operators, and combining conditions with AND/OR/parentheses.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 3 ("Beginning Data Exploration with SELECT")

**Last updated**: 2026-07-13

---

## Basic SELECT and Column Subsets

`SELECT * FROM table_name;` retrieves every row and column (`*` is a wildcard for "all columns"). Naming specific columns, comma-separated, after `SELECT` limits the result to just those columns, in any order — column order in the query doesn't need to match the table's actual column order. `TABLE table_name;` is a lesser-known standard-SQL shortcut equivalent to `SELECT * FROM table_name;`.

## Sorting with ORDER BY

`ORDER BY column_name` sorts a query's *result*, not the underlying table (ascending by default; `DESC` for descending, `ASC` explicit-ascending). `ORDER BY` accepts a column's ordinal position instead of its name (`ORDER BY 3 DESC`). Multiple columns sort hierarchically — `ORDER BY school ASC, hire_date DESC` groups by school, then orders newest-hire-first within each school. More than two or three sort columns becomes hard to read; better to run several narrowly-scoped queries than one query with many sort columns.

## DISTINCT for Unique Values

`SELECT DISTINCT column FROM table;` eliminates duplicate rows, showing only unique values — a fast first data-quality check (e.g., spotting inconsistent spelling variants of the same category value). `DISTINCT` on multiple columns returns each unique *combination*, not each column's unique values independently.

## Filtering with WHERE

| Operator | Function | Example |
|---|---|---|
| `=` | Equal to | `WHERE school = 'Baker Middle'` |
| `<>` / `!=` | Not equal to | `WHERE school <> 'Baker Middle'` |
| `>` / `<` | Greater/less than | `WHERE salary > 20000` |
| `>=` / `<=` | Greater/less or equal | `WHERE salary >= 20000` |
| `BETWEEN` | Within a range (inclusive) | `WHERE salary BETWEEN 20000 AND 40000` |
| `IN` | Match one of a set | `WHERE last_name IN ('Bush', 'Roush')` |
| `LIKE` | Pattern match, case-sensitive | `WHERE first_name LIKE 'Sam%'` |
| `ILIKE` | Pattern match, case-insensitive (PostgreSQL-only) | `WHERE first_name ILIKE 'sam%'` |
| `NOT` | Negates a condition | `WHERE first_name NOT ILIKE 'sam%'` |

**`BETWEEN` is inclusive** — chaining `BETWEEN 10 AND 20` with a second `BETWEEN 20 AND 30` double-counts the value 20. Explicit `>=`/`<=` avoids the ambiguity when boundary handling matters.

**`LIKE` vs. `ILIKE`**: `%` matches one-or-more characters, `_` matches exactly one. `LIKE` is case-sensitive (ANSI standard); `ILIKE` is case-insensitive (PostgreSQL extension) — default toward `ILIKE` when vetting data, since inconsistent capitalization in source data is common and a case-sensitive search silently misses matches. Both can be slow on large tables without an index (see [[sql-table-design-constraints-and-indexes]]).

## Combining Conditions

`AND` requires both conditions true; `OR` requires at least one. Parenthesized groups evaluate first, before combining with the rest of the clause — `WHERE school = 'X' AND (salary < 38000 OR salary > 40000)` is a materially different result from the same clause without parentheses, since AND binds before OR when precedence isn't made explicit. Always parenthesize when mixing AND and OR to make the evaluation order unambiguous rather than relying on default precedence.

## Query Structure Order

```sql
SELECT column_names
FROM table_name
WHERE criteria
ORDER BY column_names;
```

This fixed keyword order is not stylistic — SQL requires it.

## Key Takeaways

- `DISTINCT` is a fast, cheap first data-quality check on any new table or column.
- Default to `ILIKE` over `LIKE` when searching human-entered text — case-sensitivity silently drops matches on inconsistently-capitalized data.
- Always parenthesize mixed `AND`/`OR` conditions — don't rely on default precedence being obviously correct to the next reader.

## Connects to

- [[sql-table-design-constraints-and-indexes]] — indexes are what make `WHERE`/`LIKE` filtering fast on large tables.
- [[sql-grouping-and-aggregate-functions]] — `DISTINCT` is the simple case of what `GROUP BY` generalizes into (aggregating instead of just deduplicating).
- [[web-frameworks/flask-databases-with-sqlalchemy]] — Flask-SQLAlchemy's `.filter_by()`/`.filter()` chain methods are a Python wrapper around this exact WHERE-clause vocabulary.

## North Star Connection

- How this applies to the audit business: this is the first-pass "interview the data" toolkit for any new client dataset — checking completeness, spotting inconsistent values, and pulling the specific slice a report needs.
- Track relevance: Tech — foundational SQL, prerequisite for every later page in this ingest.
- Possible future Second Brain use: Yes — the default starting query pattern for any new client database.
