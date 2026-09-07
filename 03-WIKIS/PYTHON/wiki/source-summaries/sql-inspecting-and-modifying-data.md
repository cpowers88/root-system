---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [programming, sql-strand]
---

# Practical SQL: Inspecting and Modifying Data

**Summary**: A repeatable "interview the dataset" workflow for finding dirty data (duplicate addresses, missing values, inconsistent spellings, malformed ZIP codes) using `GROUP BY`/`HAVING`/`length()`, then fixing it safely with `ALTER TABLE`, `UPDATE`, backup tables, transactions (`START TRANSACTION`/`COMMIT`/`ROLLBACK`), and `DELETE`/`TRUNCATE`/`DROP` for removing what's no longer needed.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 10 ("Inspecting and Modifying Data")

**Last updated**: 2026-06-20

---

## Interviewing a Dataset for Dirty Data

"Dirty data" — errors, missing values, or poor organization that breaks standard queries — has multiple typical origins: file-format conversion losses, wrong data types, and human data-entry inconsistency. A repeatable interview sequence, demonstrated on a 6,287-row FSIS meat/poultry/egg establishment directory:

- **Duplicate-row detection**: `GROUP BY company, street, city, st HAVING count(*) > 1` surfaces every combination appearing more than once — not automatically an error (a company can legitimately have two plants at one address), but worth investigating before trusting downstream counts.
- **Missing-value detection**: `GROUP BY` on a column reveals a `NULL` row in the grouped totals (PostgreSQL sorts `NULL` last by default; `ORDER BY column NULLS FIRST` overrides this). Following up with `WHERE column IS NULL` returns the exact rows missing that value.
- **Inconsistent-spelling detection**: `GROUP BY company, count(*)` scanned visually can reveal that one real-world entity (e.g., "Armour-Eckrich Meats") is spelled four different ways across rows — a problem for any later aggregation by that column.
- **Malformed-value detection via `length()`**: `GROUP BY length(column)` exposes values that don't match an expected fixed format — used here to discover that ZIP codes had lost their leading zeros during an Excel-to-CSV conversion (PostgreSQL doesn't allow leading zeros on an integer, so `07502` became `7502`).

**The general principle: always check whether an "odd" result is a real-world fact or a data artifact** — and when it's a genuine quality problem, log it to a running list of fixes before doing anything else, rather than patching ad hoc as issues are noticed.

## Modifying Tables and Values: ALTER TABLE and UPDATE

`ALTER TABLE table ADD COLUMN col type` / `DROP COLUMN col` / `ALTER COLUMN col SET DATA TYPE type` / `SET NOT NULL` / `DROP NOT NULL` covers the standard schema-modification operations. **Adding a constraint to an existing table forces a full-table validation check** (can be slow on a huge table); **dropping a column gives no warning and is not reversible without a backup** — PostgreSQL doesn't immediately reclaim the space, it just marks the column deleted internally.

`UPDATE table SET column = value [WHERE criteria]` modifies existing row values — omitting `WHERE` updates every row. Multiple columns can be set in one statement (comma-separated). Values being set can come from another table via a **subquery** (`SET column = (SELECT ... FROM table_b WHERE ...) WHERE EXISTS (SELECT ... WHERE ...)` — the standard ANSI pattern) or, in PostgreSQL specifically, a simpler `UPDATE table SET column = table_b.column FROM table_b WHERE table.column = table_b.column` syntax. **The `WHERE EXISTS` subquery guard matters**: without it, rows in the target table with no match in the source table would get silently set to `NULL`.

A `RETURNING column_list` clause appended to `UPDATE` (also works with `INSERT`/`DELETE`, PostgreSQL-specific) shows the affected rows' resulting values immediately, without a separate follow-up `SELECT`.

## Backups Before Modifying

**Always back up before any destructive change.** `CREATE TABLE backup_name AS SELECT * FROM original_table;` makes a full table copy — note that **indexes are not copied** by this pattern, so a backup meant for active querying needs its own `CREATE INDEX`. A lighter-weight safeguard for a single risky column edit: `ALTER TABLE ADD COLUMN col_copy text; UPDATE ... SET col_copy = col;` duplicates just that column in-place, letting you verify success with `WHERE col IS DISTINCT FROM col_copy` (returns zero rows if the values still match everywhere) — **`IS DISTINCT FROM` is the `NULL`-safe alternative to `<>`**, since `<>` against a `NULL` returns `NULL` (neither true nor false) rather than a usable comparison.

If an update goes wrong, restoring is just another `UPDATE`: `SET column = backup_column` (in-table) or joining back to the full backup table by primary key.

## Transactions: Testing Changes Before Committing

`START TRANSACTION` (or PostgreSQL's `BEGIN`) opens a transaction block; subsequent statements aren't visible to other database users and aren't permanent until `COMMIT`. `ROLLBACK` discards everything done since the transaction started. **This lets you run an `UPDATE`, inspect the result with a `SELECT`, and decide whether to keep it — entirely risk-free** — a far safer default than running an `UPDATE` directly and hoping it's correct. Demonstrated by intentionally introducing a typo mid-transaction, catching it via a verification `SELECT`, and discarding the whole block with `ROLLBACK` rather than needing a second corrective `UPDATE`.

## Repairing Values: String Concatenation and Cross-Table Updates

The `||` double-pipe **string concatenation operator** (ANSI standard, supported by PostgreSQL) combines two strings (or a string and number) into one — used to restore the ZIP codes' lost leading zeros: `SET zip = '0' || zip WHERE st IN (...) AND length(zip) = 4` (one leading zero for most affected states) and `SET zip = '00' || zip WHERE st IN ('PR','VI') AND length(zip) = 3` (Puerto Rico/Virgin Islands need two).

Cross-table updates use the subquery/`WHERE EXISTS` or PostgreSQL `FROM`-clause pattern shown above — demonstrated by joining a separate `state_regions` lookup table to populate an `inspection_deadline` column on every row whose state falls in a given US Census region, without that region designation existing anywhere in the original table.

## Improving Performance on Large-Table Updates

**Adding a column and filling it with `UPDATE` roughly doubles a table's on-disk size in PostgreSQL** — each updated row creates a new internal row version without immediately deleting the old one (cleaned up later via `VACUUM`, out of scope here). For large tables, a faster alternative is to **create a new table with the added column already populated** (`CREATE TABLE new AS SELECT *, value::type AS new_column FROM original;`), then use `ALTER TABLE ... RENAME TO ...` three times in sequence to atomically swap the new table into the original table's name while preserving the original as a backup — avoiding the per-row update/bloat cost entirely.

## Deleting Data

`DELETE FROM table [WHERE expression]` removes rows (omitting `WHERE` empties the whole table, scanning every row in the process). `TRUNCATE table [RESTART IDENTITY]` empties a table faster by skipping the row-by-row scan, and can optionally reset an `IDENTITY` auto-increment sequence back to its start in the same statement. `ALTER TABLE table DROP COLUMN column` removes a column (and its data, irreversibly without a backup). `DROP TABLE table_name` removes an entire table — useful for retiring an outlived backup/working table, or for replacing a table's structure wholesale rather than issuing many `ALTER TABLE` calls. **Any deletion that would violate a foreign key constraint must be resolved first** (drop the constraint, delete the dependent rows, or delete the dependent table) — there's no universal shortcut.

## Key Takeaways

- Build a standing checklist for interviewing any new dataset: duplicate-key detection (`GROUP BY ... HAVING count(*) > 1`), missing-value detection (`WHERE col IS NULL`), spelling-consistency checks (`GROUP BY` + visual scan), and format checks (`length()`).
- Never modify a table without a backup first — a full `CREATE TABLE ... AS SELECT *` copy, a single-column `_copy` backup, or both, depending on the risk.
- Wrap any `UPDATE`/`DELETE` you're not 100% sure about in a transaction (`START TRANSACTION` ... verify with `SELECT` ... `COMMIT` or `ROLLBACK`) — it costs nothing and eliminates the need for a restore-from-backup recovery.
- For large tables, prefer the create-new-table-and-rename-swap pattern over an in-place `UPDATE` when adding a populated column, to avoid roughly doubling the table's storage footprint.

## Connects to

- [[sql-grouping-and-aggregate-functions]] — the duplicate-address and inconsistent-spelling detection techniques here directly reuse Chapter 9's GROUP BY/HAVING/count() pattern as a data-quality diagnostic rather than a reporting tool.
- [[sql-table-design-constraints-and-indexes]] — ALTER TABLE's ADD/DROP COLUMN and constraint-management syntax extends directly from Chapter 8's constraint-modification commands; deleting rows that violate foreign keys is the inverse of the CASCADE behavior covered there.
- [[sql-joining-tables-and-relationships]] — the cross-table UPDATE (state_regions lookup table joined to populate inspection_deadline) reuses the JOIN/subquery concepts from Chapter 7 in a write rather than read context.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
