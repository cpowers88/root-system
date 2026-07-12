---
type: concept
stage: 10
status: draft
source_refs: ["Automate the Boring Stuff Ch.16 (SQLite Databases)"]
prerequisites: ["dictionaries", "csv-and-json"]
tags: [stage-10, databases, sqlite]
---

# Concept: Databases and SQLite (Light Introduction)

## Plain-English Meaning

A **database** stores structured data so it can be reliably queried, filtered, and updated — even with large amounts of data or multiple programs accessing it. **SQLite** is a lightweight database that lives in a single file, built into Python's standard library (`sqlite3`) with no separate server needed.

## What Problem This Solves

CSV and JSON (Stage 9) work fine for small, simple data — but they get slow and awkward to search/filter/update as data grows large or needs structured querying ("find every student with a score above 90"). Databases are built specifically for that.

## When To Use It

When data needs to be searched, filtered, or updated efficiently, especially as it grows beyond what comfortably fits in memory, or when multiple parts of a program need reliable, structured access to the same data.

## When Not To Use It

For small, simple, one-time data, CSV/JSON (Stage 9) is simpler and sufficient — don't reach for a database just because it sounds more advanced.

## Code Shape

```python
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, score INTEGER)")
cursor.execute("INSERT INTO students VALUES (?, ?)", ("Chris", 95))
conn.commit()

cursor.execute("SELECT * FROM students WHERE score > 90")
print(cursor.fetchall())
conn.close()
```

## Tiny Working Example

```python
import sqlite3

conn = sqlite3.connect(":memory:")   # temporary, in-memory database for testing
cursor = conn.cursor()
cursor.execute("CREATE TABLE notes (text TEXT)")
cursor.execute("INSERT INTO notes VALUES (?)", ("Stage 10 notes",))
conn.commit()

cursor.execute("SELECT * FROM notes")
print(cursor.fetchall())   # [('Stage 10 notes',)]
```

## Beginner Mistakes

- Forgetting `conn.commit()` after an `INSERT`/`UPDATE` — without it, changes aren't actually saved to the database file.
- Building SQL queries with string concatenation/f-strings instead of `?` placeholders — this is both a bug risk and a real security vulnerability (SQL injection) in larger contexts.
- Forgetting `conn.close()` (or not using a context manager), similar to the file-handling lesson from Stage 6.

## Physical-World Anchor

A library's card catalog system — instead of flipping through every book to find what you need (a CSV-style search), the catalog lets you query directly by author, title, or subject.

## Required Vocabulary

- [[glossary/database]]

## Related Code Patterns

- (none required this stage — SQLite gets a light intro, not a drilled pattern; full depth is parked beyond this vault's current scope)

## Drill

- [[drills/stage-10-application-practice]]

## Explain-Back Questions

1. When would you reach for a database instead of a CSV or JSON file?
2. Why is it important to use `?` placeholders instead of building SQL queries with string concatenation?
3. What does `conn.commit()` actually do, and what happens if you forget it?

## Source Notes

- (source: Automate the Boring Stuff, 3rd Ed., Ch.16, "SQLite Databases")
