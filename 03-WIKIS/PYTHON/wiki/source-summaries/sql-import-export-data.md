---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [reference, programming, parked, sql-strand]
---

# Practical SQL: Importing and Exporting Data

**Summary**: The `COPY` command — PostgreSQL's bulk-loading mechanism for delimited text files (CSV) — covering header rows, quoted delimiters, importing partial columns or rows, using a temporary table to inject a missing value during import, exporting full tables/columns/query results, and the pgAdmin Import/Export wizard as a fallback when COPY can't reach the file system directly (e.g., a remote/cloud-hosted database).

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 5 ("Importing and Exporting Data")

**Last updated**: 2026-06-20

---

## The Three-Step Import Pattern

Most imports follow the same sequence: (1) obtain the source data as a delimited text file, (2) create a table matching its columns and types, (3) run a `COPY` statement to load it. CSV (comma-separated values) is the most portable delimited format; PostgreSQL's `COPY` is its own bulk-import mechanism, distinct from row-by-row `INSERT` statements (impractical past a handful of rows).

```sql
COPY table_name
FROM 'C:\YourDirectory\your_file.csv'
WITH (FORMAT CSV, HEADER);
```

`FROM` takes the *full file path* (Windows: `C:\...`; macOS/Linux: `/Users/...`) — the directory must already exist, since PostgreSQL won't create one. `WITH` options include `FORMAT` (csv/text/binary), `HEADER` (exclude the file's header row on import; include one on export), `DELIMITER '|'` (any single non-carriage-return character, default comma for CSV), and `QUOTE 'character'` (the text qualifier wrapping values that contain the delimiter itself, default double-quote). **Header rows are not used by PostgreSQL to map columns — it relies purely on column order** — so the `HEADER` option exists only to skip importing that row as data, not to align fields by name.

## Choosing Column Types from a Real Dataset

Demonstrated via a 3,142-row US Census county population-estimate import: `state_fips`/`county_fips` are stored as `text`, not integers, because **leading zeros in codes (Alaska's `state_fips` is `02`) would be silently stripped by an integer type** — a key reminder that codes/identifiers are labels, not numbers, even when they look numeric. `area_land`/`area_water` use `bigint` because some Alaska county areas (Yukon-Koyukuk: 377 billion sq meters) exceed `integer`'s ~2.1 billion ceiling. Latitude/longitude use `numeric(10,7)` to hold up to 7 decimal places of precision with a max 3-digit whole-number part (longitude can reach ±180). A `CONSTRAINT ... PRIMARY KEY (state_fips, county_fips)` declares that combination unique per row (constraints covered fully in [[sql-table-design-constraints-and-indexes]] once ingested). **Relying on an official data dictionary when one exists** (the Census Bureau publishes one) is called out explicitly as good practice to avoid misconfiguring a column or losing data on import.

A real surprise surfaced by sorting longitude descending: the Aleutian Islands (Alaska) topped the list ahead of any East Coast county, because they extend past 180° longitude and wrap to positive values on the other side of the antimeridian — a reminder that **unexpected sort results are often a real geographic/domain fact, not a data error**, and worth confirming before assuming something's broken.

## Importing Partial Data

If a source CSV lacks columns your target table has (e.g., a `supervisor_salaries` table with `town`/`county`/`supervisor`/`salary`/`benefits`, but a CSV with only `town`/`supervisor`/`salary`), naming the present columns explicitly in the `COPY` statement tells PostgreSQL which columns to fill and leaves the rest `NULL`:

```sql
COPY supervisor_salaries (town, supervisor, salary)
FROM 'C:\YourDirectory\supervisor_salaries.csv'
WITH (FORMAT CSV, HEADER);
```

Omitting this column list causes PostgreSQL to assume the CSV matches the table's full column order — producing a misleading `invalid input syntax for type integer` error if (for example) the table's auto-incrementing ID column comes first but the CSV doesn't include any matching value for it.

As of PostgreSQL 12, `COPY` also accepts a `WHERE` clause to import only matching rows from the source file directly — e.g., `WHERE town = 'New Brillig'` — without needing a separate filtering step afterward.

## Injecting a Missing Value During Import (Temporary Tables)

When a needed column (e.g., `county`) is entirely absent from the source CSV but you know the correct value to backfill, the pattern is: create a `TEMPORARY TABLE` (`CREATE TEMPORARY TABLE x (LIKE original_table INCLUDING ALL)` — exists only for the current session), `COPY` the raw CSV into it, then `INSERT INTO real_table (...) SELECT town, 'Mills', supervisor, salary FROM temp_table;` — supplying the missing value as a literal string inside the `SELECT` rather than a column reference — then `DROP TABLE` the temp table once done. This is the standard pattern for any import where the source data is incomplete relative to the destination schema but a known, constant value should fill the gap.

## Exporting Data

`COPY` reverses direction for export — `TO` instead of `FROM`:

```sql
COPY us_counties_pop_est_2019
TO 'C:\YourDirectory\us_counties_export.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');
```

Three export patterns: **whole table** (as above); **selected columns only** (`COPY table_name (col1, col2, col3) TO ...` — useful for excluding sensitive fields like SSNs before sharing data externally); **query results** (wrapping a full `SELECT ... WHERE ...` query in parentheses before the `TO` clause, exporting only the filtered/computed result rather than the raw table).

## When COPY Can't Reach the File

`COPY`'s `FROM`/`TO` paths are resolved on the *database server's* filesystem, not the client machine — this breaks down when connected to a remote/cloud-hosted PostgreSQL instance (e.g., AWS) where you lack filesystem access to that machine. **pgAdmin's built-in Import/Export wizard** (right-click a table → Import/Export) works around this by transferring the file through the client connection — it's a GUI wrapper around the `psql` utility's `\copy` meta-command (different from the SQL-level `COPY` keyword) rather than the SQL `COPY` statement directly.

## Key Takeaways

- The three-step import pattern (get delimited file → create matching table → COPY) is the default path for any bulk data load; INSERT is only practical for a handful of rows.
- Store identifier/code columns (ZIP codes, FIPS codes) as text even when they look numeric — integer types silently strip leading zeros.
- Naming columns explicitly in COPY is required whenever the source file's columns don't exactly match the destination table's full column set and order.
- COPY operates on the database server's filesystem, not the client's — pgAdmin's Import/Export wizard (built on psql's `\copy`) is the workaround for remote/cloud-hosted databases.

## Connects to

- [[sql-data-types]] — the Census import is a direct, concrete application of the chapter 4 type-selection rules (text for codes, bigint for outsized integers, numeric for precise decimals).
- [[sql-select-where-and-filtering]] — the ILIKE/wildcard query-export example reuses Chapter 3's pattern-matching syntax directly to filter what gets exported.
- [[reading-writing-csv-with-pandas]] — PostgreSQL's COPY and pandas' read_csv/to_csv solve the same import/export problem at different layers (database vs. DataFrame); audit work will often move data between both.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
