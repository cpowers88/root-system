---
domain: technology
type: concept
timeline: reference
status: wiki-only
tags: [subject/sql, subject/python]
use_cases: [data-workflow]
stack: [sqlite]
---

# SQL: Python's `sqlite3` Module — Connecting Code to a Database

**Summary**: How Python's built-in `sqlite3` standard-library module actually talks to a database — connecting, the cursor object, creating tables safely on repeat runs, inserting one row versus many, parameterized queries, and reading data back. This is the "how do I run SQL from Python" layer underneath the SQL syntax the rest of this folder covers.

**Sources**: Applied practice — MCP Bootcamp Day 3 (Data Engineering lens), 2026-07-21, building `02-LIBRARY\.PROJECTS\MCP_Bootcamp\Code\build_fixture.py` against `05-BUSINESS\02-Field Notes\observation_one.md`.

**Last updated**: 2026-07-21

---

## Connecting to a Database

`sqlite3.connect("filename.db")` opens a database file, creating it on disk automatically if it doesn't already exist. Unlike PostgreSQL (the rest of this folder's default dialect), SQLite has no separate server process to install or start — the "database" *is* the file. This makes it the natural choice for small local fixtures, prototypes, and single-user tools rather than a shared production system.

## The Cursor Object

`cursor = conn.cursor()` creates the object that actually sends SQL to the database and gets results back. The connection (`conn`) represents the open file; the cursor is what you call `.execute()` on to do anything with it.

## Creating Tables Safely — `CREATE TABLE IF NOT EXISTS`

A script that builds a fixture is normally run more than once while you're still developing it. Plain `CREATE TABLE` fails with `sqlite3.OperationalError: table X already exists` the second time it runs against a `.db` file that already has that table. Adding `IF NOT EXISTS` right after `CREATE TABLE` makes the statement a no-op if the table is already there, instead of an error — the standard idiom for any script meant to be re-run during development. See [[sql-table-design-constraints-and-indexes]] for what actually goes inside the parentheses (columns, `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`).

## Inserting One Row — Parameterized `?` Placeholders

```python
cursor.execute(
    "INSERT INTO friction_categories (category_name) VALUES (?)",
    ("bad estimates",),
)
```

The `?` is a placeholder; the actual value comes from the tuple passed as the second argument, matched in order. Two reasons to always do it this way instead of pasting values directly into the SQL string with an f-string or `.format()`:

1. **It's the safe way to run SQL with real-world data.** Building the query string by directly inserting text (especially text a user typed) opens the door to SQL injection — a malicious or malformed value can alter the query itself. Parameter placeholders keep data and SQL structure separate, so a value can never be interpreted as SQL syntax.
2. **It handles quoting and escaping for you.** Text with an apostrophe (`"it's broken"`) would break a hand-built SQL string; the parameterized version handles it correctly without any extra work.

A single-item tuple needs a trailing comma — `("bad estimates",)` not `("bad estimates")` — otherwise Python treats the parentheses as just grouping, not tuple construction, and `execute()` receives a plain string instead of a sequence of parameters.

## Inserting Many Rows — `executemany()`

```python
cursor.executemany(
    "INSERT INTO friction_categories (category_name) VALUES (?)",
    [
        ("crew/sub-contractor oversight",),
        ("bad estimates",),
        ("bad or no records",),
    ],
)
```

`executemany()` takes the same parameterized SQL as `execute()`, but a **list of tuples** instead of one tuple — it runs the insert once per tuple in the list. This replaces writing the same `execute()` call repeatedly by hand for every row, and is the natural way to load a batch of real records (e.g., every row of a field-observation log) in one call.

**Caveat carried from practice**: `executemany()` doesn't skip rows that would violate a `UNIQUE` constraint any more than `execute()` does — re-running a script that already inserted a row will still fail with an `IntegrityError` on a duplicate. For a fixture-build script, the practical fix during development is to delete the `.db` file and rebuild it fresh each time, rather than engineering full insert-idempotency (`INSERT OR IGNORE`) for what's meant to be a from-scratch build step.

## Saving and Closing — `commit()` and `close()`

`conn.commit()` writes all pending changes permanently to the `.db` file. Skip it, and everything done in the script — tables, inserts, all of it — vanishes when the script ends, because SQLite (like most databases) buffers changes until they're explicitly committed. `conn.close()` releases the connection cleanly once you're done.

## Reading Data Back — `SELECT` + `fetchall()`

```python
cursor.execute("SELECT * FROM friction_categories")
print(cursor.fetchall())
```

`execute()` runs the query; `fetchall()` retrieves every matching row as a list of tuples — `[(1, 'change-order info flow'), (2, 'bad estimates'), ...]`. The first value in each tuple is whatever the table's primary key column produced (an auto-incrementing integer, in the fixture built this session); the rest are the columns in the order they were declared. This is the fastest way to verify data actually landed the way you think it did, with no separate viewer tool required.

## Key Takeaways

- `sqlite3` is Python's standard-library interface to SQLite — no install, no separate server process; the `.db` file *is* the database.
- `CREATE TABLE IF NOT EXISTS` is the standard idiom for any script that will be re-run during development.
- Parameterized `?` placeholders (not string-building) are the correct, safe way to pass real values into SQL from Python — this matters for injection safety, not just convenience.
- `executemany()` batches repeated inserts from a list of tuples but does not make them idempotent against `UNIQUE` constraints — plan for that separately (or rebuild the fixture from scratch each run).
- `conn.commit()` is what actually persists changes; forgetting it silently discards everything.
- A `.db` file is binary — it will never open as readable text in a code editor. Query it (via `sqlite3`, or a dedicated extension/GUI) rather than opening it directly.

## Connects to

- [[sql-table-design-constraints-and-indexes]] — the SQL-syntax side of everything created here: `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`.
- [[practical-sql]] — the source-summary hub for this folder's PostgreSQL-flavored SQL reference; this page is the SQLite/Python-specific complement to it.
- [[web-frameworks/flask-databases-with-sqlalchemy]] — Flask-SQLAlchemy's ORM wraps this same connect/cursor/execute pattern behind Python objects; useful comparison once a project needs a real web app instead of a local script.

## North Star Connection

- How this applies to the audit business: this is the exact mechanism behind any lightweight client-facing tool that needs local, dependency-free data storage before a real database server is justified — matches the Recommendation Ladder's "build light" rung.
- Track relevance: Tech — direct output of MCP Bootcamp Day 3 (Data Engineering), immediately reusable for the Academic Tracker and any future fixture/prototype work.
- Possible future Second Brain use: Yes — this pattern (connect → cursor → `CREATE TABLE IF NOT EXISTS` → parameterized insert → commit) is the reusable skeleton for any small Python+SQLite build.
