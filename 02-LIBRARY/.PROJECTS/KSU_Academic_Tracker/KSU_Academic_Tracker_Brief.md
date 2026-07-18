---
type: project
timeline: now
status: ready
tags: [project]
---

# KSU Academic Tracker — Project Brief
### Python + SQLite + Markdown
### Build target: July 5–24, 2026 (before D2L access opens ~July 25)
### Last updated: July 15, 2026 — live-path and purpose reconciliation

---

## Purpose

A lightweight command-line tool that tracks readings, assignments,
tests, and study material across Fall 2026 KSU courses.

SQLite holds the structured data — dates, status, grades.
Markdown files hold the actual content — notes, study sheets,
chapter summaries.

The program connects them. You run it in the morning and know
exactly what needs attention.

---

## D2L Access Note

D2L access opens approximately one month before classes begin —
around July 25, 2026. KSU starts August 24, 2026.

Important: Some professors load all material before the semester.
Others load assignments and readings week by week as the course
progresses. Do not expect the full semester to be visible on
day one. This is how it worked at Chattanooga State and KSU
is likely the same.

Practical approach:
- July 25: Log in, enter whatever is available into the tracker
- Enter syllabus dates first — tests and major deadlines are
  usually posted early even when weekly work is not
- Add readings and assignments as professors post them
- The tracker works with partial data — enter what exists,
  fill in the rest as the semester moves

---

## Courses — Fall 2026

| Code       | Course                         | Format       |
|------------|--------------------------------|--------------|
| PHYS 2211  | Principles of Physics I        | MWF 9:10am   |
| CSE 1321   | Programming Problem Solving I  | MW 4:10pm    |
| CSE 1321L  | Programming Problem Solving Lab | Tue 5:45pm   |
| ENGR 1000  | Intro to Engineering           | Online async |
| TCOM 2010  | Technical Writing              | TTh 9:35am   |
| ECON 1000  | Contemporary Economic Issues   | TTh 8:00am   |

---

## What the Program Does

Two functions only:

1. Show what needs attention today or this week — assignments
   due, tests coming up, readings not yet completed.

2. Link structured data to markdown notes — when you query
   "what do I need for the Physics test," it returns the test
   date, chapters covered, and the path to your study file
   in Obsidian.

No dashboard. No web interface. A Python script run from
the terminal.

---

## Data Model — Four Tables

### courses
```
course_id     INTEGER PRIMARY KEY
code          TEXT        -- e.g. PHYS2211
name          TEXT        -- Physics I
professor     TEXT
credit_hours  INTEGER
```
Entered once at setup. Never changes mid-semester.

---

### assignments
```
assignment_id  INTEGER PRIMARY KEY
course_id      INTEGER     -- foreign key to courses
name           TEXT        -- e.g. Problem Set 3
due_date       TEXT        -- YYYY-MM-DD
status         TEXT        -- pending / submitted / graded
grade          REAL        -- filled in when returned
notes_file     TEXT        -- relative path to .md if exists
```

---

### tests
```
test_id           INTEGER PRIMARY KEY
course_id         INTEGER     -- foreign key to courses
name              TEXT        -- e.g. Exam 1
test_date         TEXT        -- YYYY-MM-DD
chapters_covered  TEXT        -- e.g. CH 1-3, CH 5
study_status      TEXT        -- not started / in progress / ready
notes_file        TEXT        -- relative path to study sheet .md
```

---

### readings
```
reading_id  INTEGER PRIMARY KEY
course_id   INTEGER     -- foreign key to courses
chapter     TEXT        -- e.g. CH 3
pages       TEXT        -- e.g. 45-78
due_date    TEXT        -- YYYY-MM-DD
completed   INTEGER     -- 0 or 1
notes_file  TEXT        -- relative path to chapter notes .md
```

---

## Command Line Queries

python tracker.py --week
Returns everything due in the next 7 days, sorted by date.

python tracker.py --today
Returns only today's items.

python tracker.py --tests
Returns all upcoming tests with study status and chapters.

python tracker.py --course PHYS2211
Returns everything for one course.

python tracker.py --overdue
Returns anything past due date still marked pending.

---

## Markdown Connection

Every `notes_file` field stores a path relative to `.ROOT`, under the official
course-file home:

  02-LIBRARY\00-SCHOOL\02-Physics I\Notes\01-Chapter 1 Measurements.md
  02-LIBRARY\00-SCHOOL\01-CSE-Python\Notes\CS50P\Lecture 1.md
  02-LIBRARY\00-SCHOOL\04-ECON\Econ 1000syllabi.md

The program displays the path when it shows that item.
You open the file in Obsidian. The program does not read
the markdown — it only knows where it lives.

---

## Python Concepts Covered

- sqlite3 module — database creation, queries, updates
- argparse — command line argument handling
- datetime — date math, due-in-X-days logic
- Functions and conditional logic
- String formatting for clean terminal output
- File path handling

Walking into CSE 1321 having already built this is a
real advantage. Every concept they introduce will have
prior context.

---

## Build History

### V1 — Shipped July 8, 2026
Built and tested:
- --week
- --courses
- --tests
- --today
- --course PHYS2211
- --overdue
- --add-test
- --add-assignment
- --add-reading

Next action:
- Enter real D2L/syllabus data around July 25, 2026.
- Do not add edit/delete/update features yet. V2 is parked unless real use exposes the need.

---

## File Location in Second Brain

`02-LIBRARY\.PROJECTS\KSU_Academic_Tracker\`

- `KSU_Academic_Tracker_Brief.md`
- `tracker.py`
- `academic.db`

Chris approved small project code living inside `.ROOT` for this tracker-class work. Larger repos, environments, dependency folders, and product code still need the normal local/GitHub discipline unless the system rules change again.

---

## Connection to North Star

This is a small school-support proof project that also exercises permanent Python,
SQL, CLI, date-logic, and structured-data capability. Its value is measured by
whether it reduces semester friction with verified course data—not by assigning it
to a retired track or treating it as a product roadmap.

POL remains parked. The tracker does not automatically reactivate POL or any other
build; a later weak-link/current-strategy review must explicitly justify that work.
The capability compounds even when the projects remain separate.

---

Owner: Chris Powers
Build start: July 5, 2026
Status: V1 shipped — awaiting real D2L/syllabus data
Only active next action: around July 25, enter the verified D2L/syllabus data that
is actually available and test the real workflow. Add no V2 feature unless that use
exposes the need.
