---
type: map
timeline: reference
tags: [programming, governance, education]
---

# CSE 1321 / 1321L Syllabus Alignment

## Purpose

This page is the authoritative bridge between the official Fall 2026 course
syllabi and the staged Python path. The Markdown files in `raw\SYLLABI\` are useful
topic-table extracts, but they omit policies, learning outcomes, assessment
structure, tools, and required/recommended materials.

Official sources reviewed visually as PDFs on 2026-07-15 and replaced in the
active school library by direct Simple Syllabus Markdown captures on 2026-07-21:

- `02-LIBRARY\00-SCHOOL\01-CSE-Python\CSE 1321 BF (81262) Fall 2026 Syllabus.md`
  — CSE 1321 lecture, Chris's registered section.
- `02-LIBRARY\00-SCHOOL\01-CSE-Python\CSE 1321L 04 (86703) Fall 2026 Syllabus.md`
  — CSE 1321L lab, Chris's registered section.

## Non-Negotiable Academic-Integrity Boundary

Both official syllabi say **AI use is prohibited**. Work submitted for either
course must be Chris's own; content created or assisted by a generative-AI tool is
treated as cheating. This hub may explain concepts, create private study drills,
and assess Chris's own practice, but it must not draft, solve, rewrite, or debug
submitted course work. When a task might be graded, stop and ask before touching
the work. (sources: both active Markdown syllabi, academic-integrity/AI-policy sections)

## Course Controls That Matter Here

### CSE 1321 lecture

- 3 credit hours; concurrent prerequisite: CSE 1321L.
- *Think Python* by Allen B. Downey is the recommended, no-cost course book.
- Learning outcomes: computational problem solving; correct use of data types and
  expressions; selection and repetition; collections; functions and classes.
- 10 quizzes and 3 exams. Fall/spring weighting: quiz average 25%, Test 1 25%,
  Test 2 25%, final 25%; lowest quiz dropped.
- Exams use Respondus LockDown Browser and require a webcam, microphone, and
  reliable internet access.
- Up to 5% can be added to the lecture and lab final-exam scores through ten C-CSE
  Tutoring Center visits (0.5% each).

(source: active CSE 1321 Markdown syllabus, course and assessment sections)

### CSE 1321L lab

- 1 credit hour; concurrent prerequisite: CSE 1321.
- *Think Python* is the no-cost course book.
- 13 labs and 7 assignments; work is submitted through Gradescope.
- Weighting: assignments 40%, lab exercises 10%, midterm 20%, final 30%; lowest
  assignment and lowest lab exercise are dropped.
- Midterm and final are in class, closed book, closed notes, with no outside
  resources.

(source: active CSE 1321L Markdown syllabus, course and assessment sections)

## Topic-to-Path Map

| Official topic or outcome | Primary path coverage | Alignment decision |
|---|---|---|
| IDE, run, debug, test | Stage 0; debugging deepens in Stage 6 | Direct match |
| Decomposition, algorithms, abstraction | A small plan-before-code habit begins in Stages 1-2; full mastery is Stage 7 | Thread early; do not move Stage 7 |
| Input/output, variables, data types, operators, expressions | Stage 1 | Direct match |
| Selection / branching | Stage 2 | Direct match |
| Repetition / loops | Stage 3 | Direct match |
| Functions, parameters, arguments | Stage 4 | Direct match |
| Python libraries | Stage 4 course bridge: standard-library import/use; packages and `pip` stay in Stage 9 | Gap repaired without reordering stages |
| Tuples and lists | Stage 5 | Direct match |
| Dictionaries | Stage 5 | Direct match |
| Searching and sorting | Stage 8 | Direct match |
| Classes / OOP | Stage 8 | Direct match |
| Exception handling | Stage 6 | Named in course description, though not calendar table |
| Arrays | Stage 5 terminology bridge | Python `list` is the beginner course collection; NumPy arrays remain parked |
| Documentation, correct code, and security | Comments begin in Stage 1; test cases and explicit assumptions deepen in Stage 7 | Cross-cutting habit, not a new stage |
| Intro to Java (lab only) | Parked course bridge after Python OOP | Do not dilute the Python foundation now |

## What Is Required vs. Helpful Enrichment

- Explicitly named by the official course: data types/expressions, selection,
  repetition, collections, functions, Python libraries, searching/sorting, classes,
  exception handling, IDE/debug/run/test habits, documentation, and basic security
  awareness.
- Helpful but **not explicitly named as a course requirement**: recursion, Big O
  notation, regex, `pytest`, automation, APIs, SQL, pandas, and web applications.
  These remain valuable pathway content at their existing prerequisites, but must
  not be presented as syllabus mandates.

## Schedule Reliability Warning

The lab syllabus title says Fall 2026, but its calendar uses January-May dates and a
spring-break week. Treat its topic order, outcomes, policies, and assessment
structure as useful; do **not** treat those lab dates as Fall 2026 truth. D2L or a
corrected instructor schedule must control live due dates.

## Readiness Gate

Before class begins, the high-value target remains Stages 1-4 plus the small
standard-library bridge at the end of Stage 4. Stages 5 and 8 then mirror the
course's later collection, algorithm, and OOP modules. Learner progress still lives
only in [[current-position]]; this page maps curriculum coverage, not mastery.
