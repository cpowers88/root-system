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

# SQL: Table Design, Constraints, and Indexes

**Summary**: Creating tables, naming conventions, natural vs. surrogate primary keys, foreign keys and CASCADE deletes, the CHECK/UNIQUE/NOT NULL constraints, and B-tree indexes for query performance.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 2 ("Creating Your First Database and Table") and Chapter 8 ("Table Design That Works for You")

**Last updated**: 2026-07-13

---

## Creating Tables

`CREATE TABLE table_name (column_name data_type constraint, ...);` defines a table's structure; `INSERT INTO table_name (col1, col2) VALUES (val1, val2);` adds rows. A table is fundamentally a grid of typed columns — see [[sql-data-types]] for the type system.

## Naming Conventions

Lowercase, underscore-separated identifiers avoid the need for double-quoting (PostgreSQL folds unquoted identifiers to lowercase by default; quoting an identifier like `"Customers"` preserves case but then requires quoting on *every* reference forever — a maintenance trap). Plural or singular table names both work as conventions as long as applied consistently.

## Primary Keys: Natural vs. Surrogate

A **natural key** is an existing column that's already guaranteed unique (e.g., a government-issued ID) — reusing it avoids adding an extra column, but natural uniqueness is often less certain than it first appears (people share names; codes get reused). A **surrogate key** is a database-generated, meaningless identifier (typically an auto-incrementing `bigserial`/`GENERATED ... AS IDENTITY` integer) added purely to guarantee uniqueness — the safer default in most real schemas, since it never depends on an external system's uniqueness guarantee holding forever. Composite primary keys (multiple columns together forming the unique constraint) use table-level constraint syntax rather than being declared inline on a single column.

## Foreign Keys and CASCADE

A **foreign key** constraint ties a column's values to another table's primary key, enforcing referential integrity (you can't insert a row referencing a nonexistent parent row). `ON DELETE CASCADE` on a foreign key automatically deletes dependent rows when the referenced parent row is deleted — convenient, but a real deletion-blast-radius decision: cascading deletes can silently remove far more data than the immediate row being deleted, so it should be a deliberate design choice, not a default reached for without thinking through what else it will take down.

## Other Constraints

| Constraint | Behavior |
|---|---|
| `CHECK` | Evaluates whether new/updated data meets an arbitrary boolean condition before allowing the write |
| `UNIQUE` | Ensures no duplicate values in a column (or column group), without making it the primary key |
| `NOT NULL` | Rejects any row missing a value for that column |

Constraints can be added or dropped on an existing table with `ALTER TABLE table_name DROP CONSTRAINT constraint_name;` (or `ADD CONSTRAINT`) — schema decisions aren't permanently locked in at creation time.

## Indexes

An index (PostgreSQL's default is a **B-tree**) speeds up lookups and filtering on a column at the cost of extra storage and slightly slower writes (the index itself must be updated on every insert/update). The tradeoff: index columns that are frequently filtered/joined/sorted on (especially in `WHERE`, `ORDER BY`, or `JOIN ON` clauses — see [[sql-select-where-and-filtering]] and [[sql-joining-tables-and-relationships]]); don't index columns that are rarely queried, since the write-cost isn't worth it without a corresponding read-speed payoff.

## Key Takeaways

- Default to lowercase, underscore-separated, unquoted identifiers — quoting an identifier for mixed case creates a permanent quoting requirement everywhere that identifier is used.
- Surrogate (auto-incrementing) primary keys are the safer default over natural keys — external uniqueness guarantees can and do break.
- `ON DELETE CASCADE` is a real blast-radius decision, not a convenience default — know what else it takes down before adding it.
- Index columns that are actually filtered/joined/sorted on; don't index reflexively.

## Connects to

- [[sql-data-types]] — surrogate keys are typically `bigserial`/`IDENTITY` integer types.
- [[sql-joining-tables-and-relationships]] — foreign keys are the mechanism that makes joins meaningful; this page covers how they're declared and constrained.
- [[sql-select-where-and-filtering]] — indexes are what make `WHERE`/`LIKE` filtering fast at scale, directly addressing that page's performance caveat.
- [[web-frameworks/flask-databases-with-sqlalchemy]] — `db.Column(primary_key=True)`, `db.ForeignKey()`, `unique=True`, `nullable=False`, and `index=True` are Flask-SQLAlchemy's direct ORM wrappers around every concept on this page.

## North Star Connection

- How this applies to the audit business: this is the schema-design foundation for any client-facing tool that needs a real database — getting keys/constraints right up front avoids costly migrations once a client tool is live with real data in it.
- Track relevance: Tech — foundational SQL, direct prerequisite for [[web-frameworks/flask-databases-with-sqlalchemy]]'s model definitions.
- Possible future Second Brain use: Yes — the schema-design checklist for any new client database.
