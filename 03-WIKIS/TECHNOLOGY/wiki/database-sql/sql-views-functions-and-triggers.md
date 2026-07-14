---
domain: technology
type: concept
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, subject/sql, stack/sql]
---

# SQL: Views, Functions, and Triggers

**Summary**: Views as stored, reusable queries (including materialized views for cached results), user-defined functions for encapsulating repeated calculations, and a brief note on triggers as automated database actions.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 17 ("Saving Time with Views, Functions, and Triggers") — Views and Functions sections; Triggers not read in this ingest (chapter section past the extracted range) and noted only as a topic that exists, not summarized

**Last updated**: 2026-07-13

---

## Views

`CREATE VIEW view_name AS SELECT ...;` stores a query under a name that can then be queried itself (`SELECT * FROM view_name;`) — a view is not a copy of the data, just a saved query definition that re-runs against current data every time it's referenced. This is the direct fix for the duplicated-subquery-logic problem CTEs solve within a single query (see [[sql-advanced-query-techniques]]) — a view makes the same reusable logic available *across* many separate queries, not just within one.

Views can also restrict which columns or rows of an underlying table are exposed — e.g., a view exposing only certain columns of an `employees` table to a department that shouldn't see salary data. Inserting, updating, or deleting through a view is possible for simple views (one underlying table, no aggregation), but PostgreSQL rejects writes through a view that would violate the view's own column/row restrictions — attempting to insert a value into a column the view doesn't expose, or that would produce a row outside the view's filter, fails.

## Materialized Views

`CREATE MATERIALIZED VIEW ... AS SELECT ...;` differs from a regular view by actually storing the query's result at creation time, like a cached snapshot — subsequent queries against it are fast (no need to re-run the underlying query) but the data goes stale until explicitly refreshed with `REFRESH MATERIALIZED VIEW view_name;`. The tradeoff: query speed vs. data freshness — appropriate for expensive queries against slowly-changing data, not for anything needing up-to-the-second accuracy.

## User-Defined Functions

PostgreSQL supports writing custom functions (`CREATE FUNCTION function_name(parameters) RETURNS type AS $$ ... $$ LANGUAGE ...;`) that encapsulate a calculation for reuse across many queries — e.g., a `percent_change(new, old, decimal_places)` function wrapping the percent-change formula from [[sql-importing-and-basic-math]] into a single callable unit, rather than repeating the raw arithmetic expression in every query that needs it. Functions can be written in PostgreSQL's native procedural language or, per the book's own coverage, in Python — extending SQL with a general-purpose language when the logic is awkward to express in pure SQL.

## Triggers (noted, not summarized here)

The book's Chapter 17 also covers **triggers** — database actions that fire automatically in response to a table event (insert/update/delete), such as logging every change to an audit table or auto-classifying a value on insert. This ingest did not read that section in depth; noted here as a real chapter topic worth returning to if a future need (audit logging, automated data classification on write) specifically calls for it — not fabricated from title alone.

## Key Takeaways

- A view is a saved, reusable query — not a data copy — so it always reflects current underlying data; a materialized view trades that freshness for query speed by caching the result until explicitly refreshed.
- User-defined functions are the SQL-level equivalent of extracting a repeated calculation into a named, reusable unit — the same DRY discipline that applies at the application-code level.
- Triggers exist for automated on-write actions (audit logging, auto-classification) but weren't covered in this ingest's scope — flagged for a future targeted read if a real need arises, not guessed at.

## Connects to

- [[sql-advanced-query-techniques]] — views solve the same duplicated-logic problem CTEs solve, but across separate queries rather than within one.
- [[sql-importing-and-basic-math]] — the percent-change calculation from that page is the worked example for a user-defined function here.
- [[web-frameworks/flask-databases-with-sqlalchemy]] — Flask-SQLAlchemy models can be pointed at a database view the same way as a table, when a client tool needs a restricted or precomputed data slice without duplicating query logic in application code.

## North Star Connection

- How this applies to the audit business: a view is the standard way to give a client-facing tool a restricted or precomputed slice of data (e.g., a department-scoped view hiding salary columns) without duplicating filter logic across every query that needs it.
- Track relevance: Tech — SQL technique, closes out the PracticalSQL ingest.
- Possible future Second Brain use: Yes — views are directly applicable the moment a client tool needs row/column-restricted data access without building that restriction into every individual query.
