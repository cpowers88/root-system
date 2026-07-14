---
domain: technology
type: reference
tags: [priority/now, status/wiki-only, domain/technology, source-role/reference, use-case/tech-stack, subject/sql, subject/postgresql, stack/sql]
---

# Practical SQL — Source Summary and Navigation Hub

**Summary**: Full-source summary for *Practical SQL, 2nd Edition: A Beginner's Guide to Storytelling with Data* (Anthony DeBarros, No Starch Press, 2022), mapping the ten wiki pages created across this ingest. Confirmed scope: **Chapters 2-4 (table creation, querying, data types), Chapters 6-11 (math/stats, joins, table design, aggregation, data quality/modification, window functions/ranking), and Chapters 13 + 17 (subqueries, CTEs, CASE, views, and user-defined functions)**. Chapter 1 (environment setup — pgAdmin/PostgreSQL installation, OS-specific) and Chapters 12 (dates/times), 14 (text mining/regex), 15 (PostGIS spatial analysis), 16 (JSON data), 18 (psql command line), 19 (database maintenance/VACUUM/backups), and 20 (data storytelling narrative) were excluded as either setup-mechanical, specialized beyond current audit/build need, or DBA-depth — same scoping discipline the Flask ingest used.

**Naming note**: page names below match forward-references already present in `web-frameworks/flask-databases-with-sqlalchemy.md`, `web-frameworks/flask-rest-apis.md`, and two `data-science-ml/` pages, written before this ingest existed. Matched exactly so those pre-existing dead links resolve, rather than introducing new near-duplicate names.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., No Starch Press, 2022)

**Last updated**: 2026-07-13

---

## Page Map

- [[sql-select-where-and-filtering]] — Ch. 3: SELECT syntax, querying column subsets, ORDER BY, DISTINCT, WHERE with comparison operators, LIKE/ILIKE pattern matching, combining AND/OR.
- [[sql-data-types]] — Ch. 4: character, numeric, date/time, JSON/JSONB, and miscellaneous (boolean, binary, XML) data types; CAST() and the `::` shortcut notation.
- [[sql-importing-and-basic-math]] — Ch. 5 (COPY-based CSV import/export basics) + Ch. 6: math operators, division/modulo, column-to-column math, percentages and percent change, aggregate functions (sum/avg), median/percentile/mode functions.
- [[sql-joining-tables-and-relationships]] — Ch. 7: JOIN/LEFT JOIN/RIGHT JOIN/FULL OUTER JOIN/CROSS JOIN, primary/foreign key relationships, the three relationship types (1:1, 1:many, many:many), table aliases, UNION/INTERSECT/EXCEPT set operators.
- [[sql-table-design-constraints-and-indexes]] — Ch. 8 (+ Ch. 2 CREATE TABLE basics): naming conventions, natural vs. surrogate primary keys, foreign keys and CASCADE, CHECK/UNIQUE/NOT NULL constraints, B-tree indexes.
- [[sql-grouping-and-aggregate-functions]] — Ch. 9: count()/max()/min(), GROUP BY (single and multi-column), HAVING.
- [[sql-inspecting-and-modifying-data]] — Ch. 10: data-quality checks (missing/inconsistent/malformed values), ALTER TABLE, UPDATE, backup tables, transactions.
- [[sql-window-functions-and-ranking]] — Ch. 11: rank()/dense_rank() window functions, PARTITION BY for grouped rankings, rate calculations for fair comparisons, rolling averages for smoothing time series.
- [[sql-advanced-query-techniques]] — Ch. 13: subqueries in WHERE/FROM/column lists, EXISTS/NOT EXISTS, LATERAL, Common Table Expressions, CASE reclassification.
- [[sql-views-functions-and-triggers]] — Ch. 17: views and materialized views, user-defined functions, brief note on triggers.

## Why This Source Belongs Here

`TECHNOLOGY_LIBRARY_STRATEGY.md` Category 5 (Data Storage & Retrieval) names the exact failure mode this book solves: "the spreadsheet became the database and now it's breaking." This is the complete relational-querying foundation for the next rung up that ladder (SQLite/PostgreSQL), and it directly underlies the ORM layer in [[web-frameworks/flask-databases-with-sqlalchemy]] — Flask-SQLAlchemy's `db.session` queries and relationship declarations are a Python-object wrapper around exactly the JOIN, constraint, and aggregation concepts this ingest covers. This page fulfills a `[[practical-sql]]` link that page has carried since its own ingest without a target, plus five more forward-references discovered across `flask-databases-with-sqlalchemy.md`, `flask-rest-apis.md`, and two `data-science-ml/` pages.

## Connects to

- [[web-frameworks/flask-web-development]] — the reverse direction of the link this page fulfills.
- [[web-frameworks/flask-databases-with-sqlalchemy]] — the specific Flask chapter whose CRUD operations and relationship declarations this ingest gives the underlying SQL vocabulary for.
- [[web-frameworks/flask-rest-apis]] — `Model.query.paginate()`'s LIMIT/OFFSET pattern connects to [[sql-advanced-query-techniques]].
- [[data-science-ml/information-gain-entropy-and-attribute-selection]], [[data-science-ml/related-analytics-techniques-and-business-questions]] — both already reference this ingest's grouping/filtering pages as the applied-SQL companion to their conceptual data-mining coverage.
- [[data-science-ml/crisp-dm-process-and-data-leakage]] — SQL is the data-preparation tooling layer beneath that page's conceptual CRISP-DM coverage.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Direct prerequisite for Flask-SQLAlchemy work and any client audit involving "the spreadsheet became the database" |
| Current usefulness | 4 | Immediately usable — PostgreSQL is free, and this is core querying skill with no dependency on other unbuilt tools |
| KSU support | 1 | Not coursework-related |
| Tech-stack relevance | 4 | SQL underlies the Data Storage & Retrieval category and the ORM layer of any Flask client tool |
| Business audit value | 4 | "One giant Excel file everyone edits" is a named Category 5 need-signal this book's skills directly answer |
| Data/workflow value | 4 | Pairs directly with pandas/Flask for any client-facing data tool |
| Reading urgency | 2 | Scoped ingest is closed; nothing further to read in this source unless a specific need (dates/times, JSON, spatial) arises |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**: Tech-stack decision / future reference — building or auditing a client-facing tool with a relational-database backend.

**Use when**: A client's data has outgrown a spreadsheet, or a Flask tool needs a real schema with relationships and constraints rather than ad hoc CSV files.

**Do not use when**: The need is a one-off script against a small, single CSV — that's pandas territory, not a full database.

**Fast retrieval query**: `stack/sql` + `use-case/tech-stack` — or see the individual chapter pages linked in the Page Map above.

## North Star Connection

- How this applies to the audit business: this is the query/design/modify toolkit for any client engagement where "the spreadsheet became the database" is the diagnosed problem (`TECHNOLOGY_LIBRARY_STRATEGY.md` Category 5) — from first SELECT through constraint-backed table design to the window-function ranking a client-facing report often needs.
- Track relevance: Tech — core relational-database skillset, direct prerequisite for the Flask client-tool toolkit.
- Possible future Second Brain use: Yes — [[sql-table-design-constraints-and-indexes]] (schema) + [[sql-joining-tables-and-relationships]] (relationships) + [[sql-grouping-and-aggregate-functions]] (reporting queries) is the ready-to-use foundation the moment a Flask client tool needs a real database instead of a Sheet.
