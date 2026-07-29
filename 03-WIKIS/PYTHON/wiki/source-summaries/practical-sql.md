---
type: source-summary
timeline: reference
status: parked
source_role: spine (candidate — parked SQL-fundamentals strand)
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [programming, sql-strand, hub]
---

# Practical SQL — Source Summary and Navigation Hub

**Summary**: Full-source summary for *Practical SQL: A Beginner's Guide to Storytelling with Data* (Anthony DeBarros, 2nd ed., 2022, No Starch Press), mapping the twelve wiki pages created across this ingest. Confirmed scope: **Chapters 1-13 only** — database/table creation through advanced query techniques (subqueries, CTEs, crosstabs, CASE). Chapters 14-19 (text mining/regex, PostGIS spatial analysis, JSON, views/functions/triggers, command-line psql, database maintenance), Chapter 20 ("Telling Your Data's Story"), and the Appendix were excluded as administration/specialty depth beyond current need.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022)

**Last updated**: 2026-06-20

---

## Page Map

- [[sql-creating-databases-and-tables]] — Ch. 2: relational table structure, CREATE DATABASE/TABLE, INSERT INTO, bigserial auto-increment, quoting rules, SQL formatting conventions.
- [[sql-select-where-and-filtering]] — Ch. 3: SELECT as data-interviewing, ORDER BY, DISTINCT as a data-quality check, WHERE operators, the AND/OR parenthesization trap.
- [[sql-data-types]] — Ch. 4: characters/numbers/dates type categories, floating-point inexactness, serial vs. IDENTITY auto-increment, JSON/JSONB, CAST().
- [[sql-import-export-data]] — Ch. 5: the COPY command, the three-step import pattern, partial-column imports, temp-table value backfilling, the pgAdmin wizard fallback.
- [[sql-basic-math-and-stats]] — Ch. 6: operator type-coercion rules, the data-validation self-check pattern, percent-of-whole/percent-change formulas, median/percentile/mode.
- [[sql-joining-tables-and-relationships]] — Ch. 7: JOIN...ON, the five JOIN types, NULL-based anti-joins, the three table-relationship types, multi-table joins, set operators.
- [[sql-table-design-constraints-and-indexes]] — Ch. 8: naming conventions, natural vs. surrogate primary keys, foreign keys and CASCADE, CHECK/UNIQUE/NOT NULL, B-tree indexes.
- [[sql-grouping-and-aggregate-functions]] — Ch. 9: count/max/min as data-quality checks, GROUP BY, joining and percent-change math, HAVING.
- [[sql-inspecting-and-modifying-data]] — Ch. 10: the dirty-data interview checklist, ALTER TABLE/UPDATE/backup tables, transactions, DELETE/TRUNCATE/DROP.
- [[sql-statistical-functions]] — Ch. 11: correlation, linear regression and r-squared, variance/standard deviation, rank()/PARTITION BY, rate calculations, rolling averages.
- [[sql-dates-and-times]] — Ch. 12: the four datetime types, date_part()/make_date(), time zone management, date/interval arithmetic, justify_interval().
- [[sql-advanced-query-techniques]] — Ch. 13: subqueries (derived tables, IN/EXISTS), LATERAL joins, CTEs, crosstab() pivot tables, CASE for reclassifying values.

(Chapter 1, "Setting Up Your Coding Environment," is OS-specific installation instructions with no conceptual content — no page was created for it.)

## Best Use In This Vault

Candidate **spine** for a future "SQL fundamentals" strand extending Stage 10's databases line beyond Automate the Boring Stuff's light SQLite chapter. Until Chris approves that strand, the twelve `sql-*` pages are lookup reference only.

## Connects to

- [[python-for-data-analysis]] — the pandas `read_sql`/SQLAlchemy page (`sqlite-and-sql-with-pandas.md`) is the bridge between this SQL knowledge and a Python analysis workflow; many techniques here (GROUP BY, percentiles, crosstabs) have a direct pandas equivalent already ingested.
- [[sql-grouping-and-aggregate-functions]] and [[sql-advanced-query-techniques]] — CTEs and derived tables are structural upgrades over plain GROUP BY for the same class of question.

## Source Identity

- Title: Practical SQL: A Beginner's Guide to Storytelling with Data, 2nd Ed.
- Author: Anthony DeBarros
- File: `raw/books/PracticalSQL.pdf`
- Type: book (SQL teaching text, PostgreSQL/pgAdmin-based, No Starch Press, 2022)
- Ingest: Ch. 1-13 pre-ingested by FORGE (2026-06-20); Ch. 14-20 and the appendix excluded as specialty/administration depth.

## Difficulty Assessment

Post-Stage-10 intro. Requires [[concepts/databases-and-sqlite]] first. **Caution**: the book teaches PostgreSQL via pgAdmin; the vault's Stage 10 path uses SQLite. Core SQL (SELECT/WHERE/JOIN/GROUP BY) transfers directly; PostgreSQL-specific features (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, COPY, pgAdmin workflow) do not.

## Advanced Material To Park

Ch. 14-19 (text mining/regex, PostGIS spatial, JSON, views/functions/triggers, psql command line, database maintenance) and Ch. 20 — never ingested; keep parked.

## Recommended Placement In Learning Path

After Stage 10, as the spine of a Chris-approved SQL-fundamentals strand — see `wiki/source-map.md` and [[parking-lot]]. Do not fold into the active Stage 0-10 path.

## Notes For Future Claude

Same closed-intake rule as the data-analysis strand: the `sql-*` pages are inventory only until Chris asks to build them into curriculum. If the strand is built, decide first whether to teach on SQLite (matches Stage 10 and needs no server) and translate the book's PostgreSQL-isms, or install PostgreSQL as the book assumes.
