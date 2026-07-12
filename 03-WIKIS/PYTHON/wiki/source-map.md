---
type: map
tags: [reference, programming]
---

# Source Map

## Purpose

This page inventories all raw sources and decides how each source should be used in the learning pathway.

Do not deep-ingest many books until this map exists.

---

## Status: Intake Finalized (2026-06-24)

Source intake is closed for now. Eight sources (two syllabi + six books) are mapped across all 11 stages. **For the quick per-stage spine/support/mini-project table, see `wiki/learning-path.md` → "Source Roster."** This page holds the full per-book detail and reasoning. Do not add more sources without a specific reason (a real gap found during generation, not "let's see what else exists").

---

## Source Intake Status

| Source | Location | Type | Status | Role | Difficulty | Current Use | Notes |
|---|---|---|---|---|---|---|---|
| CSE lab syllabus | `raw/syllabi/CSE_lab_syllabus.md` | syllabus | ingested | school-policy | n/a | topic order + schedule alignment | schedule-only file; no textbook, no grading breakdown, no AI policy text present |
| CSE lecture syllabus | `raw/syllabi/CSE_lecture_syllabus.md` | syllabus | ingested | school-policy | n/a | topic order + schedule alignment | schedule-only file; no textbook, no grading breakdown, no AI policy text present |
| Think Python, 2nd Ed. (Allen Downey) | `raw/books/thinkpython.pdf` | book | ingested (TOC-level) | spine | beginner-friendly | active spine for Stages 1-8 | course textbook Chris added 2026-06-24; subtitle "How to Think Like a Computer Scientist" is the literal source of the vault's CS-thinking framing |

### Syllabus Extraction Notes (2026-06-24)

- **AI policy:** Not stated in either file. Chris confirmed AI assistance is allowed for this course. Course is **not** marked `ai-restricted`, but the vault's standing rule still applies — stop and ask before doing graded work for him.
- **Required books/tools:** None listed in either syllabus file. Chris will add the official textbook to `raw/books/` later. Treated as **pending** in the evaluation matrix below until added.
- **Grading categories:** Not present in either file (no weights, exam dates, or rubric info available yet).
- **Lecture topic order (15 weeks):** decomposition/algorithms/abstraction → data types/operators/Boolean/assignment → selection (2 wks) → iteration/loops (2 wks) → functions/parameters/arguments (2 wks) → Python libraries → tuples/lists → dictionaries + searching/sorting → OOP (2 wks) → TBD → review.
- **Lab topic order (13 weeks):** intro/IDE+Gradescope → I/O and variables → data types/operators/expressions → selection → repetition (2 wks) → functions → Python libraries → tuples/lists → dictionaries + searching/sorting → OOP (2 wks) → intro to Java.
- **Lab/lecture relationship:** Lab runs roughly in lockstep with lecture, one topic per week, with lab trailing slightly (e.g., lecture spends 2 weeks each on selection/iteration/functions; lab compresses repetition into 2 weeks but functions into 1). Lab is the only place Java appears (final week) — flagged as out of scope for this Python-track vault unless Chris asks to bridge it later.
- **Topics Chris must master before class begins:** everything through functions/parameters/arguments — i.e., vault Stages 1–4 (atoms, decisions, loops, functions). This lines up with Weeks 1–4 of the existing 8-Week Python Foundation Plan draft in `learning-path.md`.
- **Topics that arrive early in the course but are later in the vault's stage order:** Python Libraries (lecture wk 9 / lab wk 8) arrives before tuples/lists/dictionaries in both syllabi, ahead of vault Stage 5. Flagged — vault will still teach data shapes first since libraries depend on fluency with data shapes to be useful, but Chris should expect "Python Libraries" lecture content to look unfamiliar until Stage 5 is done.
- **OOP** appears in both syllabi (weeks 11–13ish) — matches vault's parked placement at Stage 8 ("objects... as required by syllabus"). No prerequisite gap.

---

## Source Role Definitions

- `spine` — main teaching source for a stage.
- `support` — clarifies or reinforces a concept.
- `practice` — source of exercises and drills.
- `reference` — lookup material only.
- `advanced` — useful later, parked now.
- `school-policy` — syllabus, timeline, topic order, policy only.
- `capability-map` — explains what code can solve.
- `project-source` — supports mini-projects or applied builds.

---

## Multi-Book Evaluation Matrix

When books are added, fill this table.

| Source | Beginner fit 1-5 | CS thinking 1-5 | Python mechanics 1-5 | Practice value 1-5 | School alignment 1-5 | Application value 1-5 | Recommended role |
|---|---:|---:|---:|---:|---:|---:|---|
| Think Python, 2nd Ed. | 5 | 5 | 5 | 4 (has end-of-chapter exercises) | 5 (chapter topics match both syllabi almost 1:1, including OOP and searching/sorting near the end) | 2 (no CLI/web/API/automation content) | **spine** for Stages 1-8; will need a **support/project-source** added later for Stages 9-10 |

### Think Python -> Vault Stage Mapping (TOC-level, 2026-06-24)

Book chapter order does not match vault Stage order (book teaches basic function calls before conditionals and loops, and bundles recursion with conditionals). Vault Stage order is kept as-is per `CLAUDE.md`; sections are pulled from the book non-sequentially.

| Vault Stage | Book chapters / sections used |
|---|---|
| Stage 0 — Setup | Ch.1 "Running Python," "The First Program" |
| Stage 1 — Atoms | Ch.1 (Values and Types, Arithmetic Operators), Ch.2 (Assignment, Variable Names, Expressions, Order of Operations, String Operations, Comments) — note: book doesn't teach `input()` until Ch.5 ("Keyboard Input"), so that piece is pulled forward out of order |
| Stage 2 — Decisions | Ch.5 (Boolean Expressions, Logical Operators, Conditional/Alternative/Chained/Nested Execution) — recursion sections of Ch.5 held back for Stage 8 |
| Stage 3 — Loops | Ch.7 (Reassignment, Updating Variables, `while`, `break`, Algorithms) + "Traversal with a for Loop" pulled forward from Ch.8 |
| Stage 4 — Functions | Ch.3 (Function Calls, Composition, Parameters/Arguments, Stack Diagrams, Fruitful vs. Void) + Ch.6 (Return Values, Boolean Functions) |
| Stage 5 — Data shapes | Ch.8 Strings, Ch.10 Lists, Ch.11 Dictionaries, Ch.12 Tuples |
| Stage 6 — Files/errors/debugging | Ch.14 Files (incl. Catching Exceptions), Ch.20 Debugging (syntax/runtime/semantic errors) |
| Stage 7 — Program design | Ch.4, Ch.9, Ch.13 (the three "Case Study" chapters model decomposition, incremental development, and testing) |
| Stage 8 — Think Python / course readiness | Ch.5 recursion sections, Ch.15-18 Classes/Objects/Methods/Inheritance (matches syllabus OOP weeks), Ch.21 Analysis of Algorithms (matches syllabus searching/sorting week) |
| Stage 9 — Automation bridge | **not covered by this book** — needs a separate source later |
| Stage 10 — Application thinking | Ch.19 Goodies partially relevant (comprehensions, sets); CLI/web/API/DB content **not covered** — needs a separate source later |

---

## Spine Selection

**Active spine:** Think Python, 2nd Ed. (Allen Downey) — for Stages 1-8  
**Reason:** official course textbook; chapter topics match both syllabi closely; subtitle matches the vault's CS-thinking framing  
**Support sources:** none yet  
**Practice sources:** Think Python end-of-chapter exercises (Stages 1-8 only)  
**Parked advanced sources:** none added yet (see `wiki/parking-lot.md` for topic-level parking)

---

## Automate the Boring Stuff with Python, 3rd Ed. (Al Sweigart) — added 2026-06-24

Chris provided this book pre-split into chapter files. Originally dropped loose in `raw/`; moved (with Chris's approval) into `raw/books/automate-the-boring-stuff/` to keep `raw/` organized.

**Status:** TOC-level ingest (file names/chapter titles only, not deep-read).
**Gap closed (2026-07-09):** Chapter 10 ("Reading and Writing Files") was missing from the original set; Chris added it July 9, 2026 — the book is now complete in `raw/books/automate-the-boring-stuff/` (Ch. 0–24 + both appendices). Found during the July 9 citation/sort sweep.

**Role:** This book fills the exact Stages 9-10 gap left open by Think Python (no automation/application content there). Chapters 1-9 also double as **support/practice** for Stages 1-6 since they cover the same basics from a different angle. Recommended scores: Beginner fit 4, CS thinking 2 (practical/applied, not theory-heavy), Python mechanics 4, Practice value 5 (loaded with practice projects + Appendix B answer key), School alignment 2 (syllabus doesn't cover automation), Application value 5.

### Chapter -> Vault Stage Mapping

| Chapter | Title | Vault Stage | Role |
|---|---|---|---|
| 0 | Introduction | Stage 0 | support |
| 1 | Python Basics | Stage 1 | support/practice |
| 2 | if-else and Flow Control | Stage 2 | support/practice |
| 3 | Loops | Stage 3 | support/practice |
| 4 | Functions | Stage 4 | support/practice |
| 5 | Debugging | Stage 6 | support/practice (placed early in this book, used later in vault order) |
| 6 | Lists | Stage 5 | support/practice |
| 7 | Dictionaries and Structuring Data | Stage 5 | support/practice |
| 8 | Strings and Text Editing | Stage 5 | support/practice |
| 9 | Text Pattern Matching with Regular Expressions | Stage 8 | support (regex is intermediate; introduce once core fluency is solid) |
| **10** | **MISSING from provided files** | — | gap — ask Chris if he wants it added |
| 11 | Organizing Files | Stage 9 | **spine** (automation bridge) |
| 12 | Designing and Deploying Command Line Programs | Stage 10 | **spine** (application thinking) |
| 13 | Web Scraping | Stage 10 | spine, requires internet/HTML basics — not yet in parking-lot, added below |
| 14 | Excel Spreadsheets | Stage 9 | **spine** |
| 15 | Google Sheets | Stage 9 | spine (note: requires API credentials setup — slightly more advanced than Excel chapter) |
| 16 | SQLite Databases | Stage 10 | spine (matches vault's "databases" line in Stage 10 description) |
| 17 | PDF and Word Documents | Stage 9 | **spine** |
| 18 | CSV, JSON, and XML Files | Stage 9 | **spine** (also fills the JSON prerequisite the APIs unlock in `prerequisite-map.md` needs) |
| 19 | Keeping Time, Scheduling Tasks, and Launching Programs | Stage 9 | spine |
| 20 | Sending Emails, Texts, and Push Notifications | Stage 9 | spine (needs external account/API setup) |
| 21 | Making Graphs and Manipulating Images | Stage 10 | parked — niche/optional |
| 22 | Recognizing Text in Images (OCR) | parked-advanced | niche/optional, revisit only if Chris wants it |
| 23 | Controlling the Keyboard and Mouse | parked-advanced | niche/optional, revisit only if Chris wants it |
| 24 | Text-to-Speech and Speech Recognition | parked-advanced | niche/optional, revisit only if Chris wants it |
| Appendix A | Installing Third-Party Packages | Stage 9 | support (pip basics, needed once any automation chapter requires a package) |
| Appendix B | Answers to the Practice Questions | practice | self-study answer key — fine to use freely, this is not a graded school source |

**Net effect on the active path:** Think Python remains spine for Stages 1-8. This book becomes spine for Stages 9-10, resolving the gap flagged on 2026-06-24. No change to current Stage 1 next action.

---

## Python Crash Course, 3rd Ed. (Eric Matthes) — added 2026-06-24

`raw/books/PythonCrashCourse.pdf`. TOC-level ingest (Part I fully read, Part II read through Ch.15; later Part II chapters not yet checked — likely a web-app project per the book's known structure, unconfirmed).

**Role:** **support/practice** for Stages 1-7, layered alongside the Think Python spine. Not replacing Think Python as spine (Think Python is the assigned course textbook — school alignment wins), but PCC is more exercise-dense (numbered drills after nearly every subsection) which directly serves the Drill Rule and Chris's explain-example-drill learning profile. Also the first source to cover automated testing (Ch.11, `pytest`), filling the "testing" prerequisite-map row.

### Chapter -> Vault Stage Mapping

| Chapter | Title | Vault Stage | Role |
|---|---|---|---|
| 1 | Getting Started | Stage 0 | support |
| 2 | Variables and Simple Data Types | Stage 1 | support/practice |
| 3-4 | Lists / Working with Lists | Stage 5 | support/practice (book teaches lists earlier than vault order; pulled forward as reinforcement, not first exposure) |
| 5 | if Statements | Stage 2 | support/practice |
| 6 | Dictionaries | Stage 5 | support/practice |
| 7 | User Input and while Loops | Stage 3 | support/practice |
| 8 | Functions | Stage 4 | support/practice |
| 9 | Classes | Stage 8 | support (OOP, held with Think Python's OOP chapters) |
| 10 | Files and Exceptions | Stage 6 | support/practice |
| 11 | Testing Your Code | Stage 7 | support — new content, fills the "testing" prerequisite-map gap |
| 12-14 | Alien Invasion (Pygame game project) | Stage 10 | parked project-source — fun mini-project once fundamentals are solid, requires Pygame (third-party package) |
| 15 | Generating Data (Matplotlib/Plotly) | Stage 10 | parked project-source — requires third-party packages, data-shapes fluency |
| 16+ (unconfirmed) | likely a web-app project | Stage 10 / parked-advanced | not yet checked — flag to Chris if he wants this scoped |

**Net effect on the active path:** No change to current Stage 1 next action. Think Python stays primary spine; PCC becomes the go-to source whenever a stage needs more worked exercises than Think Python or Automate the Boring Stuff provide. Part II project chapters are parked until Stage 10.

---

## Think Like a Programmer (V. Anton Spraul) — added 2026-06-24

`raw/books/ThinkLikeaProgrammer.pdf`. TOC/intro-level ingest only.

**Language mismatch flagged:** this book's stated prerequisite is familiarity with C++ syntax, and all code examples are in C++ — not Python. This is otherwise a well-regarded book specifically about problem-solving *strategy* (decomposition, working with constraints, choosing approaches) rather than language mechanics, which is exactly what the vault's "think like a computer scientist" framing needs. But the code can't be handed to Chris directly.

**Role:** support, for **strategy/discussion only** — read the problem-solving narrative, skip or mentally re-derive the C++ code. Best used at Stage 7 (program design/decomposition) once Chris has enough Python fluency to translate a C++ snippet's logic into Python himself, or used purely conceptually (no code) even earlier. Not a spine, not a code-reading source for Chris yet.

---

## Grokking Algorithms, 2nd Ed. (Aditya Bhargava) — added 2026-06-24

`raw/books/GrokkingAlgorithms.pdf`. TOC-level ingest (brief contents only).

**Role:** support/practice for Stage 8, specifically the algorithms portion. Visual, heavily illustrated, Python-based code examples — a strong fit for Chris's "visual structure is critical" learning requirement. Covers exactly the syllabus's Week 11 "searching and sorting algorithms" topic.

### Chapter -> Vault Stage Mapping

| Chapter | Title | Vault Stage | Role |
|---|---|---|---|
| 1 | Introduction to Algorithms | Stage 8 | support — matches syllabus |
| 2 | Selection Sort | Stage 8 | support — matches syllabus ("sorting") |
| 3 | Recursion | Stage 8 | support, alongside Think Python Ch.5 recursion sections |
| 4 | Quicksort | Stage 8 | support — matches syllabus ("sorting") |
| 5 | Hash Tables | Stage 8 | support — reinforces dictionaries, matches syllabus ("searching") |
| 6 | Breadth-First Search | parked-advanced | beyond syllabus scope, optional enrichment |
| 7-8 | Trees / Balanced Trees | parked-advanced | beyond syllabus scope, optional enrichment |
| 9 | Dijkstra's Algorithm | parked-advanced | beyond syllabus scope, optional enrichment |
| 10 | Greedy Algorithms | parked-advanced | beyond syllabus scope, optional enrichment |
| 11 | Dynamic Programming | parked-advanced | beyond syllabus scope, optional enrichment |
| 12 | K-Nearest Neighbors | parked-advanced | intro ML — well beyond this vault's current scope |
| 13 | Where to Go Next | parked-advanced | not relevant until Stage 10+ |

**Net effect on the active path:** Stage 8 (Think Python/course readiness) now has a second, more visual algorithms source alongside Think Python Ch.21. Chapters 6-13 parked — they go beyond what either syllabus requires.

---

## A Common-Sense Guide to Data Structures and Algorithms, 2nd Ed. (Jay Wengrow) — added 2026-06-24

`raw/books/DataStructuresandAlgorithms.pdf`. TOC-level ingest only. **Code language not yet confirmed** — TOC was read, not the code samples. Treat as a concept/Big-O reference until language is verified; don't assume it's Python-ready code for Chris.

**Role:** support for Stage 8, complementing Grokking Algorithms with more rigor on Big O notation (Ch.3-7) plus structures Grokking Algorithms doesn't cover early on: stacks/queues (Ch.9), linked lists (Ch.14), binary search trees (Ch.15+). Chapters on dynamic programming and deep recursion overlap with Grokking Algorithms — use whichever explanation clicks better for Chris. Same syllabus-scope caveat as Grokking Algorithms: only sorting/searching/hash-tables/recursion are required by the syllabus; the rest is enrichment.

---

## Invent Your Own Computer Games with Python, 4th Ed. (Al Sweigart) — added 2026-06-24

`raw/books/InventYourOwnComputerGamesWithPython.pdf`. Brief contents read. Python, beginner-friendly, project-based — same author as Automate the Boring Stuff.

**Role: primary mini-project source, spanning Stages 2-8 and into Stage 10.** This is the strongest fit yet for the vault's Mini-Project Rule — small, complete, real programs at each fluency level, including a chapter literally titled "Designing Hangman with Flowcharts" (Ch.7) that models decomposition for Stage 7.

### Chapter -> Vault Stage Mapping

| Chapter | Title | Vault Stage |
|---|---|---|
| 1-2 | Interactive Shell, Writing Programs | Stage 1 |
| 3 | Guess the Number | Stage 2-3 (conditionals + loops) |
| 4 | A Joke-Telling Program | Stage 1-2 |
| 5 | Dragon Realm | Stage 2 (conditionals) |
| 6 | Using the Debugger | Stage 6 |
| 7 | Designing Hangman with Flowcharts | **Stage 7** — decomposition/planning model |
| 8-9 | Writing/Extending Hangman | Stage 5 (strings, lists) |
| 10 | Tic-Tac-Toe | Stage 5 (lists, 2D thinking) |
| 11 | The Bagels Deduction Game | Stage 5-7 (logic + design) |
| 12-13 | Cartesian Coordinates, Sonar Treasure Hunt | Stage 5-7 |
| 14 | Caesar Cipher | Stage 5 (strings) |
| 15-16 | Reversegam (Othello) + AI | **Stage 8** (basic game AI, decision logic) |
| 17-19 | Creating/Animating Graphics, Collision Detection | Stage 10 (parked, requires graphics library) |
| 20-21 | Sounds/Images, Dodger Game | Stage 10 (parked) |

**Net effect:** fills the vault's Mini-Project Rule requirement at nearly every stage with ready-made, scoped projects instead of having to invent them. Strongly recommended as the go-to mini-project source.

---

## Python Workout, 2nd Ed. (Reuven M. Lerner) — added 2026-06-24

`raw/books/PythonWorkout.pdf`. Brief contents + exercise list read. **Pure drill book** — 50 exercises (some multi-part, ~200 total), each designed to take about 10 minutes. Directly serves the vault's Drill Rule.

**Role:** drill bank across Stages 1, 4, 5, 6, 8, 9-10.

| Chapter | Title | Vault Stage |
|---|---|---|
| 1 | Improving Your Python with Practice | Stage 0 (framing) |
| 2 | Numeric Types | Stage 1 |
| 3 | Strings | Stage 1 / Stage 5 |
| 4 | Lists and Tuples | Stage 5 |
| 5 | Dictionaries and Sets | Stage 5 |
| 6 | Files | Stage 6 |
| 7 | Functions | Stage 4 |
| 8 | Functional Programming with Comprehensions | parked-advanced (Stage 10ish — list comprehensions are Think Python's "Goodies" chapter territory) |
| 9 | Modules and Packages | Stage 9-10 |
| 10 | Objects | Stage 8 (OOP) |
| 11 | Iterators and Generators | parked-advanced |
| 12 | Where to from Here? | parked |

**Net effect:** every stage now has a ready-made supply of short, focused drills instead of Claude needing to author all of them from scratch.

---

## Official Python Documentation (`raw/docs/`, added 2026-06-24)

Chris dropped in the full CPython documentation source tree (docs.python.org). This is a large reference dump, not a teaching source — classified by subtree rather than file-by-file. Not deep-ingested; inventoried at folder level only.

| Subtree | Role | Status | Notes |
|---|---|---|---|
| `raw/docs/tutorial/` | support | available, not yet used | Official Python Tutorial. Overlaps Think Python topics (controlflow, datastructures, errors, classes, inputoutput, modules) but terser, no exercises/scaffolding. Useful as a secondary reference per stage, **not** a replacement for Think Python as spine — Chris's learning profile needs the explain→example→drill structure Think Python and the vault provide. |
| `raw/docs/library/` | reference | parked | Hundreds of standard-library module references. Almost all advanced/out of scope now. A few modules are candidate **support** sources once Stage 9 (automation bridge) starts: `csv.txt`, `datetime.txt`, possibly `shutil.txt`/`os.path.txt`. |
| `raw/docs/howto/` | reference / advanced | parked | argparse, logging, regex, sockets, asyncio, descriptors, etc. All post-foundation topics. `argparse.txt` is a candidate support source for Stage 10 (CLI tools). |
| `raw/docs/reference/` | reference / advanced | parked | Formal language reference (grammar, data model, lexical analysis). Too formal/advanced for beginner stages; possible Stage 7+ citation only if Chris asks "what's the *actual* rule." |
| `raw/docs/c-api/` | out of scope | parked indefinitely | C extension API — not relevant to this Python-learning track at all. |
| `raw/docs/whatsnew/` | reference | parked | Per-version changelogs (Python 2.0 through 3.14). Not teaching content. No action needed. |
| `raw/docs/installing/`, `raw/docs/distributing/` | reference / advanced | parked | Packaging topics — relevant only at Stage 9-10 if Chris starts distributing tools. |
| top-level files (`about.txt`, `glossary.txt`, `bugs.txt`, `contents.txt`, `copyright.txt`, `license.txt`) | reference | parked | Meta-pages about the documentation project itself. `glossary.txt` is a candidate **QA reference** to cross-check the vault's own glossary wording for accuracy later — not a generation source. |

**Net effect on the active path: none.** Think Python remains the spine for Stages 1-8. This doc set is now available as a fallback reference and as a candidate support source once Stages 9-10 (automation/application) start, since Think Python doesn't cover that material.

---

## Python for Data Analysis, 3rd Ed. (Wes McKinney) — added 2026-07-07

`raw/books/PythonforDataAnalysis.pdf` (PDF copied into `raw/books/` on 2026-07-07
from FORGE's raw/; content arrived pre-ingested as 44 source-summary pages from
FORGE's retirement, see note below).
Scoped ingest already done by FORGE: Ch.2 (IPython/Jupyter) + Ch.5-10 (pandas Series/
DataFrame, file I/O, cleaning, merging/reshaping, visualization, groupby aggregation).
Ch.1, 3-4 (Python/NumPy basics) and Ch.11-12 (time series, modeling intro) were
explicitly out of scope for the original ingest.

**Status:** source-summary pages exist in `wiki/source-summaries/`, added to
inventory only — **not yet built into concept/glossary/drill/flashcard pages**, per
Chris's explicit instruction (2026-07-07) not to touch the closed, already-complete
Stage 0-10 curriculum without a specific reviewed reason. This is that reason,
flagged for a future curriculum-building session, not acted on yet.

**Role:** fills the genuine Stage 9-10 gap Automate the Boring Stuff leaves open —
that book covers CSV/Excel/SQLite at a basic level but not pandas/NumPy data
manipulation, cleaning, merging, or groupby aggregation. Recommended role: **spine**
for a new "data analysis" strand of Stage 9-10, once Chris is ready to add it.

| Pages (in `source-summaries/`) | Topic |
|---|---|
| `ipython-and-jupyter-basics.md` | Ch.2 — IPython/Jupyter setup |
| `pandas-*.md` (9 pages) | Ch.5-8 — Series/DataFrame, arithmetic, missing data, categorical, merge/concat/reshape |
| `numpy-*.md` (5 pages) | Ch.4-adjacent — ndarray basics, indexing, ufuncs, linear algebra |
| `reading-writing-csv-with-pandas.md`, `reading-excel-html-and-web-apis.md` | Ch.6 — data loading |
| `matplotlib-figures-axes-and-styling.md`, `seaborn-statistical-plots.md` | Ch.9 — visualization |
| `groupby-*.md` (4 pages), `pivot-tables-and-cross-tabulation.md` | Ch.10 — aggregation |
| `string-manipulation-and-regex-in-pandas.md` | Ch.7 — text cleaning |
| `python-for-data-analysis.md` | book-level source-summary hub |

## Practical SQL, 2nd Ed. (Anthony DeBarros) — added 2026-07-07

`raw/books/PracticalSQL.pdf` (PDF copied into `raw/books/` on 2026-07-07 from
FORGE's raw/ — see note above; content arrived pre-ingested from FORGE). 12 `sql-*.md` pages plus `sqlite-and-sql-with-pandas.md`
and a `practical-sql.md` book-level hub, covering table design, SELECT/WHERE,
joins, grouping/aggregation, dates, statistical functions, and import/export.

**Status:** same as above — inventoried only, not yet built into the active curriculum.

**Role:** fills the SQL half of the Stage 9-10 "databases" line in the vault's own
Stage 10 description, which Automate the Boring Stuff's SQLite chapter only touches
lightly. Recommended role: **spine** for a "SQL fundamentals" strand of Stage 9-10.

## Python Crash Course — chapters 16-17 resolved (2026-07-07)

The "16+ (unconfirmed)" flag in this book's existing entry above is now partially
resolved: `data-visualization-python.md` (Ch.15-16, Matplotlib/Plotly generating
data — Ch.15 was already flagged parked-project-source; Ch.16 newly confirmed) and
`working-with-apis-python.md` (Ch.17, working with web APIs) both arrived as
source-summary pages via the same FORGE retirement. Chapter 18+ (the book's likely
web-app project) remains unconfirmed. Both new pages filed in
`wiki/source-summaries/` alongside the Python for Data Analysis and Practical SQL
material above — not yet built into the curriculum.

## Note on This Batch's Origin (2026-07-07)

These 44 pages arrived as part of FORGE's retirement (`03-WIKIS\CLAUDE.md` execution
brief), not a fresh Chris-initiated intake — FORGE had already ingested them from the
two books above (plus two Python Crash Course chapters) months ago under its own
ingest protocol. A parallel batch of 22 pages from the same FORGE folder was
**archived, not migrated**, because they duplicated content already fully built into
this vault's Stage 1-8 curriculum (Think Python chapters, plus additional Python
Crash Course/general-mechanics pages covering the same ground) — see
`99-ARCHIVE\ARCHIVED_2026-07-07_FORGE_technology_python_duplicates\`.

## Required Next Update

- Stages 9-10 now have a source (Automate the Boring Stuff, see above) — no longer blocked.
- Chapter 10 of Automate the Boring Stuff has been added — gap resolved (2026-06-24).
- No further syllabus extraction needed — both files are schedule-only and have been fully ingested.
- **New (2026-07-07):** Python for Data Analysis and Practical SQL are inventoried as
  candidate Stage 9-10 spines for a "data analysis" and "SQL fundamentals" strand.
  Building them into actual concept/glossary/drill/flashcard pages needs Chris's
  go-ahead first, per this vault's closed-intake rule — flag at next session start.
- **Update (2026-07-09):** all 44 FORGE-migrated pages in `wiki/source-summaries/`
  were reshaped to this vault's conventions (vault frontmatter with `parked` status,
  FORGE-era North Star/Ranking/Retrieval sections replaced with a Pathway Placement
  section; technical content unchanged). Verified none of the material belongs in
  the active Stage 0-10 path — see the 2026-07-09 log entry.
