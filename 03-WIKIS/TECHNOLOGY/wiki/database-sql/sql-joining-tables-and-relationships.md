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

# SQL: Joining Tables and Relationships

**Summary**: The JOIN family (JOIN/LEFT/RIGHT/FULL OUTER/CROSS), how key columns relate tables, the three table-relationship shapes, and the set operators (UNION/INTERSECT/EXCEPT) for combining query results.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 7 ("Joining Tables in a Relational Database")

**Last updated**: 2026-07-13

---

## Why Joins Exist

Relational database design (Codd's model) splits data into separate tables to avoid duplication, then reassembles related data at query time via JOIN. A **key column** (or set of columns) with a unique value per row is what makes two tables relatable — one table's key referenced as a **foreign key** in another.

## The JOIN Types

| Type | Behavior |
|---|---|
| `JOIN` (inner join) | Returns rows only where matching values exist in **both** tables |
| `LEFT JOIN` | All rows from the left table, matched rows from the right (unmatched right-side columns are `NULL`) |
| `RIGHT JOIN` | Mirror of `LEFT JOIN` — all rows from the right table |
| `FULL OUTER JOIN` | Every row from both tables, matched where possible, `NULL` where not |
| `CROSS JOIN` | Every possible combination of rows from both tables (Cartesian product) — no matching condition |

`ON` specifies the join condition explicitly (`ON table_a.id = table_b.a_id`); `USING (column_name)` is shorthand when both tables use the identical column name for the join key. `WHERE column IS NULL` after a `LEFT`/`RIGHT`/`FULL OUTER JOIN` is the standard technique for finding rows with no match on the other side — e.g., "which departments have no employees."

## The Three Relationship Types

- **One-to-one**: each row in table A relates to exactly one row in table B (rare — usually a candidate for a single merged table).
- **One-to-many**: one row in table A (the "one" side) relates to multiple rows in table B — the most common shape (e.g., one department, many employees).
- **Many-to-many**: requires an intermediate junction table with foreign keys to both sides — cannot be expressed with a single foreign key column.

## Simplifying Join Syntax

Table aliases (`FROM employees AS e JOIN departments AS d ON e.dept_id = d.id`) shorten repeated full table-name references, especially valuable once joining three or more tables in one query.

## Combining Query Results with Set Operators

| Operator | Behavior |
|---|---|
| `UNION` | Combines rows from two queries, removing duplicates |
| `UNION ALL` | Same, but keeps duplicates (faster — no dedup pass) |
| `INTERSECT` | Only rows present in **both** query results |
| `EXCEPT` | Rows in the first query's results but **not** the second |

Both queries being combined must return the same number of columns with compatible types.

## Key Takeaways

- `LEFT`/`RIGHT`/`FULL OUTER JOIN` + `WHERE ... IS NULL` is the standard pattern for finding orphaned or unmatched rows across two related tables.
- Many-to-many relationships always require a junction table — there is no way to express them with a single foreign key.
- `UNION ALL` is preferable to `UNION` whenever duplicates genuinely can't occur or don't matter — it skips the deduplication cost.

## Connects to

- [[sql-table-design-constraints-and-indexes]] — foreign keys (the mechanism that makes joins meaningful) are declared and constrained there.
- [[web-frameworks/flask-databases-with-sqlalchemy]] — Flask-SQLAlchemy's `db.relationship()` + `backref` is the ORM-level abstraction directly over one-to-many joins; many-to-many relationships there also require an association table, the same junction-table pattern.

## North Star Connection

- How this applies to the audit business: JOIN literacy is required the moment a client's data lives in more than one table (customers + orders, employees + departments) — the single most common relational-database skill an audit or build engagement needs.
- Track relevance: Tech — core relational-database skill, direct prerequisite for [[web-frameworks/flask-databases-with-sqlalchemy]].
- Possible future Second Brain use: Yes — the standard toolkit for any multi-table client reporting query.
