---
domain: technology
type: tool
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, use-case/automation, subject/flask, subject/python, subject/sql, stack/flask, stack/sql-sqlite]
---

# Flask: Databases with Flask-SQLAlchemy

**Summary**: SQL vs. NoSQL tradeoffs for a Flask app, why Flask-SQLAlchemy was chosen as the database framework, defining models and one-to-many relationships, the core CRUD operations through the database session, shell integration, and managing schema changes safely with Flask-Migrate.

**Sources**: FlaskWebDevelopment.pdf (Miguel Grinberg, 2nd ed., 2018), Chapter 5 ("Databases")

**Last updated**: 2026-06-20

---

## SQL vs. NoSQL

Relational (SQL) databases store data in normalized tables connected by **relationships** (foreign keys) — efficient, low-duplication, but require **joins** to reassemble related data, and rely on **ACID** guarantees (Atomicity, Consistency, Isolation, Durability) for reliability. NoSQL databases (document/key-value stores) typically **denormalize** instead — duplicating data (e.g., storing a role name directly on every user row) to avoid needing joins, trading some update cost (renaming a duplicated value means updating every copy) for faster reads. For small-to-medium applications, the book treats both as practically equivalent choices; this chapter, and the rest of the book, uses **Flask-SQLAlchemy**, the Flask wrapper around the **SQLAlchemy** ORM, chosen specifically for its database portability (one interface works across MySQL/Postgres/SQLite) and its native Flask integration.

## Models and Database Configuration

A **model** is a Python class (inheriting `db.Model`) whose attributes map to a database table's columns — the ORM's core abstraction. `db.Column(type, **options)` defines each attribute; common types include `Integer`, `String(length)`, `Text`, `Boolean`, `Date`/`DateTime`, and common options include `primary_key=True`, `unique=True`, `index=True`, `nullable`, and `default`. The `__tablename__` class variable names the underlying table explicitly (recommended, since Flask-SQLAlchemy's auto-generated default names don't follow the plural-table-name convention).

The database itself is configured as a URL string (`app.config['SQLALCHEMY_DATABASE_URI']`) — e.g. `sqlite:///` + a file path for SQLite, or `mysql://user:pass@host/dbname` for MySQL/Postgres — then `db = SQLAlchemy(app)` instantiates the extension.

## Relationships

A **one-to-many** relationship (e.g., one role has many users) is expressed with a foreign key column on the "many" side (`role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))`) plus a `db.relationship()` declaration on the "one" side that exposes the related rows as a Python attribute (`users = db.relationship('User', backref='role')`). The `backref` argument adds the reverse-direction attribute automatically (`some_user.role` returns the `Role` object). One-to-one and many-to-one relationships reuse the same mechanism with minor option changes; **many-to-many** relationships require an additional association/junction table (covered in the book's followers chapter — out of this ingest's confirmed scope).

By default, accessing a relationship attribute (e.g., `role.users`) triggers an immediate query and returns a list. Setting `lazy='dynamic'` on the relationship instead returns an **unexecuted query object**, letting the caller chain additional filters/ordering before the query actually runs — important whenever a relationship might return a large, filterable collection.

## Database Operations (CRUD)

`db.create_all()` creates tables for every defined model (does nothing if a table already exists — it does **not** auto-update an existing schema; see Flask-Migrate below). Changes are managed through a **database session** (`db.session`, conceptually a transaction): new objects must be `db.session.add(obj)`'d (or `add_all([...])`'d) and then `db.session.commit()`'d to actually be written — **commits are atomic**, so an error partway through discards the whole batch, preventing partial updates. `db.session.delete(obj)` followed by `commit()` removes a row; modifying an existing object's attribute and re-adding/committing it performs an update. `db.session.rollback()` discards uncommitted changes.

Queries run through each model's `.query` attribute: `.all()` returns every row as a list, `.filter_by(column=value).all()` applies an equality filter, `.first()`/`.first_or_404()` return a single result (or `None`/a 404 response), `.get(primary_key)`/`.get_or_404()` look up by primary key. Filters (`filter()`, `filter_by()`, `order_by()`, `limit()`, `group_by()`) can be chained before the query executes via `all()`/`first()`/`count()`/etc.

## Shell Integration and Migrations

A **shell context processor** (`@app.shell_context_processor`) registers a function returning a dict of objects (the `db` instance, model classes) to auto-import every time `flask shell` starts — removing the need to manually re-import them in every session.

`db.create_all()` cannot update an already-existing table when a model changes — the brute-force fix (`db.drop_all()` then `create_all()`) destroys all existing data. **Flask-Migrate** (a lightweight Flask wrapper around **Alembic**, SQLAlchemy's own migration framework) solves this properly: a **migration script** has `upgrade()`/`downgrade()` functions that apply or reverse a specific schema change, letting the database move to or from any point in its schema history. The workflow: change the models → `flask db migrate -m "description"` (auto-generates a migration script by diffing models against the current schema) → **always manually review the generated script** (automatic migrations can misinterpret an ambiguous change, e.g. reading a column rename as a drop-and-add, which silently loses that column's data) → `flask db upgrade` to apply it. Migration scripts belong in version control alongside the application code.

## Key Takeaways

- Flask-SQLAlchemy models are the standard way to define both the database schema and the Python-side object interface in one place — no separate schema file to keep in sync.
- Every write goes through `db.session`: add/delete the affected objects, then `commit()` — commits are atomic, which is the main consistency guarantee this layer provides.
- Use `lazy='dynamic'` on any relationship that might return a large collection, so filters can be applied before the query executes rather than after loading everything into memory.
- **Never skip reviewing an auto-generated migration script** — Flask-Migrate/Alembic can misread a column rename as a destructive drop-and-recreate.

## Connects to

- [[sql-table-design-constraints-and-indexes]] and [[sql-joining-tables-and-relationships]] — the PracticalSQL chapters on primary/foreign keys and JOINs are the raw-SQL foundation that Flask-SQLAlchemy's models and relationships abstract over.
- [[sqlite-and-sql-with-pandas]] — the same SQLAlchemy library underlies pandas's `read_sql`, so this ORM-level model is directly transferable knowledge.
- [[flask-web-forms]] — the chapter's running example extends the NameForm app to actually persist submitted names to the database, combining this chapter with the prior one.

## North Star Connection

- How this applies to the audit business: this is the mechanism for giving a client-facing Flask tool actual persistent storage — logging job records, storing intake-form submissions, tracking client data over time — instead of a one-off form. The migration workflow (review before applying) is the safe-change discipline that matters once a client tool is live and being iterated on, mirroring the transaction-safety caution from [[sql-inspecting-and-modifying-data]].
- Track relevance: Tech — required for any Flask tool that needs to remember data between sessions/users.
- Possible future Second Brain use: Yes — model definition + db.session CRUD + Flask-Migrate is the complete, ready-to-use persistence layer for a first client-facing tool.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Persistence is required for any client tool that needs to remember data over time, not just a one-off form. |
| Current usefulness | 4 | The ready-to-use persistence layer for a first real client tool. |
| KSU support | 2 | ORM modeling overlaps loosely with relational-database fundamentals but isn't a dedicated ISYE topic. |
| Tech-stack relevance | 5 | Flask and SQL/SQLite are both explicitly in the Top 12 stack. |
| Business audit value | 4 | Enables tracking client data (job records, intake submissions) over time for ongoing audit/retainer work. |
| Data/workflow value | 5 | The core persistence mechanism for any data-collecting client tool. |
| Reading urgency | 3 | Becomes urgent the moment a client tool needs to store more than one form submission. |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Data workflow / automation

**Use when**:
A Flask client tool needs to persist data between sessions or users — job logs, intake submissions, tracked records.

**Do not use when**:
The tool is a single-use, stateless form with no need to remember past submissions.

**Fast retrieval query**:
"Flask-SQLAlchemy model relationship migration" / tags stack/flask + use-case/data-workflow
