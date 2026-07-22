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

# SQL: Data Types

**Summary**: PostgreSQL's core data type families — characters, numbers, dates/times, JSON/JSONB, and miscellaneous types (boolean, binary, XML) — plus converting between types with CAST() and its shortcut notation.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 4 ("Understanding Data Types")

**Last updated**: 2026-07-13

---

## Characters

`char(n)` (fixed-length, space-padded), `varchar(n)` (variable-length, capped at n), and `text` (variable-length, uncapped) are the three character types. `text`/uncapped `varchar` are generally preferred in modern PostgreSQL practice — the performance difference between them and length-capped types is negligible, and a hard cap risks truncation-related bugs later.

## Numbers

Integer types (`smallint`, `integer`, `bigint`) differ by storage size and range; auto-incrementing variants (`smallserial`/`serial`/`bigserial`, or `GENERATED ... AS IDENTITY` in modern PostgreSQL) generate sequential values automatically — the standard choice for a surrogate primary key (see [[sql-table-design-constraints-and-indexes]]). Decimal types (`numeric`/`decimal` — exact, arbitrary precision; `real`/`double precision` — inexact floating-point, faster but subject to rounding artifacts) trade off precision against performance. **Rule of thumb: use `numeric` for money or anything requiring exact arithmetic; floating-point types introduce rounding errors that compound in aggregate calculations.**

## Dates and Times

`date`, `time`, `timestamp`, and `timestamp with time zone` cover the core temporal types; `interval` represents a duration and supports direct arithmetic against timestamps (e.g., adding a duration to a date). Time zone handling matters specifically once data crosses zones — `timestamp with time zone` is the safer default for anything that isn't purely local.

## JSON and JSONB

`json` stores an exact text copy of the input (preserves formatting/whitespace, re-parses on every read); `jsonb` stores a decomposed binary format (faster to query, supports indexing, but doesn't preserve exact original formatting or key order). **`jsonb` is the default recommendation** for any JSON column that will actually be queried, not just stored and retrieved whole.

## Miscellaneous Types

`boolean` (true/false), binary types (raw byte storage), and `xml` round out PostgreSQL's type system for less common cases.

## Converting Types with CAST

`CAST(value AS target_type)` explicitly converts a value's type — e.g. `CAST(timestamp_column AS varchar(10))` truncates a timestamp down to just its date portion as text. The shortcut notation `value::type` (e.g. `timestamp_column::varchar(10)`) is PostgreSQL-specific and functionally identical, just terser.

## Key Takeaways

- Prefer `text`/uncapped `varchar` over length-capped character types unless there's a real reason to cap.
- Use `numeric`, never `real`/`double precision`, for money or any value where rounding errors would compound.
- Default to `jsonb` over `json` for anything that will be queried, not just stored.
- `::type` is the terse PostgreSQL shortcut for `CAST(... AS type)` — functionally identical.

## Connects to

- [[sql-table-design-constraints-and-indexes]] — data type choice interacts directly with primary-key design (serial/bigserial types) and constraint behavior.
- [[web-frameworks/flask-databases-with-sqlalchemy]] — Flask-SQLAlchemy's `db.Column(db.Integer)`, `db.String(length)`, etc. map directly onto these same underlying PostgreSQL types.

## North Star Connection

- How this applies to the audit business: correct type choice up front (numeric for money, jsonb for queryable structured data) avoids costly schema-migration rework later on a live client tool.
- Track relevance: Tech — foundational SQL, informs every table design decision.
- Possible future Second Brain use: Yes — the type-selection reference for any new table design.
