---
domain: technology
type: concept
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, subject/sql, stack/sql]
---

# SQL: Importing Data and Basic Math/Stats

**Summary**: Getting delimited text (CSV) data into and out of PostgreSQL with COPY, then the core math operators, aggregate functions (sum/avg), and percentile/median/mode functions for summarizing a column.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 5 ("Importing and Exporting Data") and Chapter 6 ("Basic Math and Stats with SQL")

**Last updated**: 2026-07-13

---

## Importing and Exporting with COPY

`COPY table_name FROM 'path/to/file.csv' WITH (FORMAT CSV, HEADER);` loads a delimited file into an existing table (the table must be created first with matching columns — see [[sql-table-design-constraints-and-indexes]]). `HEADER` tells PostgreSQL to skip the file's first row rather than importing it as data. `COPY` can target a subset of columns or rows, and can add a fixed value to a column during import (useful for tagging which source file a row came from). `COPY table_name TO 'path/to/file.csv' WITH (FORMAT CSV, HEADER);` reverses the direction for export — including exporting the results of an arbitrary query, not just a whole table. pgAdmin's Import/Export UI wraps the same mechanism for users who prefer a GUI over raw SQL.

## Math Operators and Data Types

Standard operators (`+ - * /`) plus modulo (`%`), exponents (`^`), roots, and factorials. **Integer division truncates**, discarding any remainder — dividing two `integer` columns and expecting a decimal result is a common bug; cast at least one operand to `numeric` first. Standard order-of-operations rules apply, and parentheses control evaluation order explicitly (`3 ^ 3 - 1` differs from `3 ^ (3 - 1)`).

## Column Math and Derived Values

Arithmetic works directly across columns in a SELECT list (`SELECT col_a - col_b AS difference FROM table`), including calculating a percentage-of-whole (`(part / total) * 100`) or percent change between two time periods (`(new - old) / old * 100`). Aliasing (`AS`) names the computed column in the result set.

## Aggregate Functions

`sum()` and `avg()` are the basic aggregate functions, computed across all rows matching the query (or per-group when combined with `GROUP BY` — see [[sql-grouping-and-aggregate-functions]]). **Average is sensitive to outliers; median is not** — PostgreSQL computes median via `percentile_cont(0.5) WITHIN GROUP (ORDER BY column)`, and the same `percentile_cont()` function generalizes to any quantile, including passing an array to get several at once (`percentile_cont(ARRAY[.25,.5,.75])`). `mode() WITHIN GROUP (ORDER BY column)` finds the most frequent value. `unnest()` turns an array result (like the multi-percentile output) back into individual rows.

## Key Takeaways

- Integer division truncates — cast to `numeric` before dividing if a decimal result is expected.
- Median (`percentile_cont(0.5)`), not average, is the right summary statistic when outliers could skew the picture — a common real-world case with salary or income data.
- `COPY` is the standard, fast path for bulk CSV import/export; it requires the target table to already exist with matching structure.

## Connects to

- [[sql-table-design-constraints-and-indexes]] — `COPY` requires a table already created with the right columns and types.
- [[sql-grouping-and-aggregate-functions]] — `sum()`/`avg()`/`count()` generalize from whole-table to per-group aggregation via `GROUP BY`.
- [[sql-window-functions-and-ranking]] — rolling averages (a smoothing technique covered there) build directly on the aggregate-function foundation here.

## North Star Connection

- How this applies to the audit business: `COPY` is the standard path for getting a client's exported CSV data into a real database instead of leaving it as a spreadsheet; median-over-average is a direct, citable audit-report improvement whenever summarizing skewed data like income or job cost.
- Track relevance: Tech — foundational SQL for any data-import or reporting task.
- Possible future Second Brain use: Yes — the default bulk-import mechanism for any new client dataset.
