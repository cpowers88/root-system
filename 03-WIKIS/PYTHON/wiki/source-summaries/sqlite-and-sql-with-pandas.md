---
type: source-summary
timeline: reference
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [programming, sql-strand, data-analysis-strand]
---

# SQLite and SQL with pandas

**Summary**: The basic mechanics of getting data out of a SQL database and into a pandas DataFrame — directly relevant per the wiki's tech priority list ("SQLite and SQL for structured data storage"). Covers Python's built-in `sqlite3` driver and the much cleaner `pandas.read_sql` + SQLAlchemy path.

**Sources**: PythonforDataAnalysis.pdf (Wes McKinney, 3rd ed.), Chapter 6, section 6.4 ("Interacting with Databases")

**Last updated**: 2026-06-20

---

## The Raw sqlite3 Path (More Manual)

```python
import sqlite3
con = sqlite3.connect("mydata.sqlite")
con.execute("CREATE TABLE test (a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);")
con.commit()

stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)   # data = a list of tuples
con.commit()

cursor = con.execute("SELECT * FROM test")
rows = cursor.fetchall()                                   # list of tuples
df = pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
```

This works, but notice the friction: you have to manually fetch rows as tuples, then manually rebuild a DataFrame from `cursor.description`. This pattern (raw driver → manual reassembly into a DataFrame) is the same shape across most database drivers, which is exactly the friction `pandas.read_sql` exists to remove.

## The Clean Path — SQLAlchemy + read_sql

```python
import sqlalchemy as sqla
db = sqla.create_engine("sqlite:///mydata.sqlite")
df = pd.read_sql("SELECT * FROM test", db)
```

One line, no manual column-name wiring. **This should be the default approach** for any database read in an audit tool — SQLAlchemy's connection-string format (`"sqlite:///path.sqlite"`, or equivalent strings for PostgreSQL/MySQL/etc.) means the same `read_sql` call works against essentially any SQL database by just changing the connection string, not the surrounding code.

## Connects to

- [[reading-writing-csv-with-pandas]] / [[reading-excel-html-and-web-apis]] — `read_sql` is the database-flavored sibling of `read_csv`/`read_excel`; all three land in the same DataFrame structures from [[pandas-series-dataframe-fundamentals]].

## Pathway Placement

- **Role**: reference bridging the two parked strands (data-analysis + SQL fundamentals); the direct extension of [[concepts/databases-and-sqlite]] once pandas is in play.
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s SQLite intro plus pandas basics from the parked data-analysis strand.
- **Status**: parked per [[parking-lot]] (pandas + SQLAlchemy rows). Not part of the active Stage 0-10 path.
