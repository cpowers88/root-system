---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [reference, programming, parked, sql-strand]
---

# Practical SQL: Creating Your First Database and Table

**Summary**: The mechanics of building a SQL database from scratch in PostgreSQL — defining a database, creating a table with `CREATE TABLE`, loading rows with `INSERT INTO ... VALUES`, viewing the result, and basic error handling and formatting conventions. Uses a six-row `teachers` table as the running example for the rest of the book's early chapters.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 2 ("Creating Your First Database and Table")

**Last updated**: 2026-06-20

---

## Tables and Relational Structure

A table is a grid of rows and columns; each column holds one data type (numbers, characters, dates). A database typically holds **multiple related tables** rather than one giant table — for example, separate `students`, `classes`, and `student_enrollment` tables that relate to each other through shared key columns (like `student_id`). Storing each entity's details once and referencing it by key elsewhere — rather than repeating a student's name on every class row — is the core practice that defines a **relational database**: it reduces redundant data and keeps the database internally consistent.

## Creating a Database and Table

```sql
CREATE DATABASE analysis;
```

Creates a new, empty database. Best practice is to create a new database per project/topic rather than dumping unrelated tables into one shared database — this avoids a pileup of unrelated tables and keeps any application powered by the database scoped to relevant data only.

```sql
CREATE TABLE teachers (
    id bigserial,
    first_name varchar(25),
    last_name varchar(50),
    school varchar(50),
    hire_date date,
    salary numeric
);
```

`CREATE TABLE` followed by a name and a parenthesized, comma-separated list of `column_name data_type` pairs defines a table's structure. `bigserial` is a PostgreSQL-specific auto-incrementing integer type, ideal for a primary identifier column — PostgreSQL fills it automatically with a sequential integer on every insert, even though no value is ever explicitly supplied for it. Every PostgreSQL statement must end with a semicolon (an ANSI SQL standard requirement) — queries sometimes work without one, but treating the semicolon as mandatory is a good habit.

## Inserting Rows

```sql
INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
VALUES ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
       ('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000);
```

`INSERT INTO table_name (columns) VALUES (...), (...);` loads rows. **Text and dates require single quotes; numbers do not.** Dates should use the international `YYYY-MM-DD` format to avoid ambiguity. Each row of values is parenthesized and comma-separated, with the very last row ending the whole statement with a semicolon instead of a comma. The pgAdmin message `INSERT 0 6` reports rows inserted (6) — the leading `0` is an unused legacy value safe to ignore.

## Viewing Data and Handling Errors

`SELECT * FROM teachers;` or the shorthand `TABLE teachers;` displays all rows. In pgAdmin, right-clicking a table and choosing **View/Edit Data > All Rows** does the same without writing SQL. **Syntax errors are unforgiving** — a missing comma produces an error citing the exact line and character position; pasting the verbatim error message (plus the database system name) into a search engine is the standard debugging approach when the message itself isn't self-explanatory.

## SQL Formatting Conventions

- Uppercase SQL keywords (`SELECT`, `CREATE TABLE`).
- Use `lowercase_and_underscores` for table/column names — avoid camelCase.
- Indent clauses/blocks consistently (two or four spaces).

These conventions aren't enforced by SQL itself, but matter because SQL code is almost always read and maintained by more than one person over time.

## Key Takeaways

- A relational database's core advantage is storing each fact once and referencing it by key elsewhere, rather than repeating data across rows.
- `bigserial`/auto-incrementing ID columns give every table row a guaranteed-unique identifier without manual bookkeeping.
- Quoting rules (text/dates need quotes, numbers don't) and the `YYYY-MM-DD` date format are the two most common sources of early INSERT errors.
- Consistent formatting conventions (uppercase keywords, lowercase_underscore names) exist for human readability, not machine requirements.

## Connects to

- [[sql-select-where-and-filtering]] — the `teachers` table created here is the dataset used throughout the next chapter's SELECT/WHERE exercises.
- [[sqlite-and-sql-with-pandas]] — this PostgreSQL-specific table-creation workflow parallels the lighter-weight SQLite approach already covered from the Python for Data Analysis ingest, for situations needing a more robust standalone database.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
