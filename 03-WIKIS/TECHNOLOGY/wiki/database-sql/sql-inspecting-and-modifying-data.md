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

# SQL: Inspecting and Modifying Data

**Summary**: A repeatable data-quality inspection workflow (missing/inconsistent/malformed values), then safely modifying data — ALTER TABLE, UPDATE, backup tables, and transactions as the safety net for destructive changes.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 10 ("Inspecting and Modifying Data")

**Last updated**: 2026-07-13

---

## A Data-Quality Inspection Workflow

A repeatable sequence for vetting any newly-imported dataset before trusting it:

1. **Missing values** — `WHERE column IS NULL` combined with a `GROUP BY`/`count()` pass (see [[sql-grouping-and-aggregate-functions]]) to quantify the gap, not just spot it.
2. **Inconsistent values** — `GROUP BY` on a text column that should have a small, fixed set of valid values, sorted by `count()`, surfaces spelling variants or unexpected categories immediately.
3. **Malformed values** — `length(column)` combined with `GROUP BY`/`count()` catches structurally wrong data (e.g., ZIP codes that should be exactly 5 characters but aren't) even when the value looks superficially plausible.

This is the same "interview the data" discipline from [[sql-select-where-and-filtering]], systematized into a specific checklist rather than ad hoc spot-checks.

## Modifying Table Structure

```sql
ALTER TABLE table ADD COLUMN column data_type;
ALTER TABLE table DROP COLUMN column;
ALTER TABLE table ALTER COLUMN column SET DATA TYPE new_type;
ALTER TABLE table ALTER COLUMN column DROP NOT NULL;
```

Standard ANSI SQL syntax for adding/removing columns and changing a column's type or nullability after the table already exists — schema evolution without dropping and recreating the table.

## Modifying Data with UPDATE

`UPDATE table SET column = value WHERE criteria;` — **the `WHERE` clause is what scopes an update to specific rows; omitting it updates every row in the table.** `RETURNING` appended to an `UPDATE` (or `DELETE`/`INSERT`) statement shows the affected rows immediately, without a separate follow-up `SELECT` — useful for confirming exactly what changed in the same statement.

## Backup Tables Before Destructive Changes

`CREATE TABLE backup_name AS SELECT * FROM original_table;` snapshots a table before a risky bulk update or delete — cheap insurance restorable with a follow-up `UPDATE ... FROM backup_name` or full table swap if something goes wrong. A lighter-weight version backs up just one column (`ALTER TABLE ... ADD COLUMN col_copy` + copy the existing values) when only that column is at risk.

## Deleting Data

`DELETE FROM table WHERE criteria;` removes rows (again, **omitting `WHERE` deletes every row**); `ALTER TABLE table DROP COLUMN column;` removes a column; `DROP TABLE table;` removes an entire table.

## Transactions

Wrapping a sequence of changes in `BEGIN;` ... `COMMIT;` (or `ROLLBACK;` to abort) makes the whole sequence atomic — either every change in the block takes effect, or none do, preventing a partial, inconsistent update if something fails midway through a multi-step change. The book also notes batching large `UPDATE` operations (rather than one massive single-statement update) improves performance on very large tables.

## Key Takeaways

- **Always write and verify the `WHERE` clause before running `UPDATE`/`DELETE`** — the single most common way to accidentally destroy an entire table's data in one statement.
- Backup tables (`CREATE TABLE ... AS SELECT * FROM ...`) are cheap insurance before any bulk destructive change — create one as a habit, not just when something feels risky.
- Wrap multi-step changes in a transaction (`BEGIN`/`COMMIT`/`ROLLBACK`) so a failure partway through doesn't leave the data in a half-changed, inconsistent state.

## Connects to

- [[sql-grouping-and-aggregate-functions]] — the `count(*)`/`GROUP BY` techniques from that page are the mechanism behind this page's data-quality inspection workflow.
- [[sql-select-where-and-filtering]] — the same `WHERE`-clause discipline that scopes a `SELECT` is what makes `UPDATE`/`DELETE` safe or dangerous.
- [[web-frameworks/flask-databases-with-sqlalchemy]] — Flask-SQLAlchemy's `db.session.commit()`/`rollback()` is the ORM-level wrapper around this page's transaction concept; that page's own migration-safety caution ("never skip reviewing an auto-generated migration script") is the same destructive-change discipline this page teaches at the raw-SQL level.

## North Star Connection

- How this applies to the audit business: this is the safe-change discipline for any live client database — backup-before-bulk-change and transaction-wrapped multi-step updates are exactly the practices that prevent an audit engagement from becoming a data-loss incident.
- Track relevance: Tech — foundational SQL, direct extension of [[sql-grouping-and-aggregate-functions]] into data modification.
- Possible future Second Brain use: Yes — the standing pre-flight checklist before any destructive change to a live client database.
