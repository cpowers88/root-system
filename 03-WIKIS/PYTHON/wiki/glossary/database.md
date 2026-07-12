---
type: glossary-entry
stage: 10
status: draft
aliases: ["SQLite", "sqlite3"]
related_terms: ["csv", "json"]
---

# Database

## Plain-English Definition

A system for storing structured data so it can be reliably queried, filtered, and updated, even at large scale. SQLite is a lightweight database built into Python (`sqlite3`), living in a single file with no separate server.

## What Problem It Helps Solve

CSV and JSON work for small, simple data, but get slow and awkward to search/filter/update as data grows. Databases are built specifically for efficient, structured querying.

## When Chris Will See It

When data needs filtering/searching beyond what a CSV/JSON file comfortably supports, or when multiple parts of a program need shared, reliable access to the same data.

## Code Example

```python
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students WHERE score > 90")
print(cursor.fetchall())
conn.close()
```

## Common Confusion

Forgetting `conn.commit()` after inserting or updating data means the change is never actually saved — a very common Stage 10 mistake.

## Physical-World Anchor

A library's card catalog — query directly by author or subject instead of flipping through every book by hand.

## Related Terms

- [[glossary/csv]]
- [[glossary/json]]

## Flashcard Q/A

**Front:** What does `conn.commit()` do, and what happens if you forget it?

**Back:** It saves pending changes to the database. Forgetting it means inserts/updates are never actually persisted.
