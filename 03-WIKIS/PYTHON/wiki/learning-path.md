---
type: plan
tags: [programming]
timeline: now
---

# Learning Path

## Purpose

This page is the active reading and practice sequence. It prevents the vault from becoming a pile of book summaries.

Chris should always be able to open this page and know what to read, practice, and build next.

---

## Current Position

**Generated through**: Stage 10 — Application Thinking
**Current study stage**: Stage 4 — Functions
**Stage 0 status**: Satisfied
**Stage 1 status**: Satisfied (2026-07-13) — worked independently with Codex 2026-07-12, verified in session (explained type-conversion reasoning, correctly predicted/confirmed a `TypeError`, explained `+`-concatenation vs. f-strings). Evidence: `02-LIBRARY\00-SCHOOL\01-CSE-Python\Stages\Stage-01-python-atoms\`.
**Stage 2 status**: Satisfied (2026-07-16) — correction and cold explain-back
verified; evidence and exact proof history live in `wiki/current-position.md`.
**Stage 3 status**: Satisfied (2026-07-26) — fresh loop-and-accumulator gate
passed with correction across normal, exact-boundary, and decimal tests.
**Next action**: Resume the exact Stage 4 cold functions baseline recorded in
`wiki/current-position.md`; do not maintain a second drill-position copy here.

The curriculum is fully generated through Stage 10, but that describes what exists in the vault, not where Chris is. Chris has satisfied Stages 0-3. **Do not read "generated through Stage 10" as an instruction to start at Stage 10.**

**Current Concept:** function definition/call, parameter, argument, return value,
and local scope (Stage 4)
**Next Reading / Drill / Vocabulary / Blocker:** follow `wiki/current-position.md`,
the sole owner of live learner truth.
**Parked Advanced Material:** see `wiki/parking-lot.md` (consolidated 2026-06-24)

**Intake note (2026-07-13):** Four late raw-source files were classified. They
added future support/reference options only and did not change the stage sequence;
the live learner has since advanced to the Stage 3 frontier recorded above.

## Fall 2026 Course Overlay

[[syllabus-alignment]] now carries the detailed CSE 1321/1321L semester pathway:
the week/module-to-stage map, code-reader competency ladder, module playbooks,
assessment preparation, and the trigger-based reading queue through the final.

The routing rule is simple:

```text
current-position = what Chris reads and proves now
syllabus-alignment = when later course reading unlocks
this page = durable Stage 0–10 sequence
```

Every meaningful session begins with `Read now`, `Read next after proof`, and
`Do not read yet`. Required local pages and *Think Python* sections come first;
support books open only when the first explanation or fresh attempt does not land.
Reading must end in a trace, skeleton, drill, or explain-back.

This hub is the independent CSE learning lane. Vibe coding and AI-generated
implementation are out of scope here and do not count as mastery evidence.

---

## Source Roster (finalized 2026-06-24)

Full per-book detail lives in `wiki/source-map.md`. This is the quick per-stage lookup.

| Stage | Spine | Support / Practice | Mini-Project Source |
|---|---|---|---|
| 0 | Think Python Ch.1 | ATBS Ch.0, PCC Ch.1 | Invent Ch.1-2 |
| 1 | Think Python Ch.1-2 (+ `input()` from Ch.5) | ATBS Ch.1, PCC Ch.2, Python Workout Ch.2-3 | Invent Ch.1-2, 4 |
| 2 | Think Python Ch.5 (non-recursive) | ATBS Ch.2, PCC Ch.5 | Invent Ch.3, 5 |
| 3 | Think Python Ch.7 (+ for-loop from Ch.8) | ATBS Ch.3, PCC Ch.4 & 7 | Invent Ch.3 (extend) |
| 4 | Think Python Ch.3 + Ch.6 | ATBS Ch.4, PCC Ch.8, Python Workout Ch.7, Python docs Modules opening | Function toolbox + standard-library bridge |
| 5 | Think Python Ch.8, 10, 11, 12 | ATBS Ch.6-8, PCC Ch.3-4 & 6, Python Workout Ch.4-5 | Invent Ch.8-14 |
| 6 | Think Python Ch.14, Ch.20 | ATBS Ch.5 & 10, PCC Ch.10, Python Workout Ch.6 | Invent Ch.6 |
| 7 | Think Python Ch.4, 9, 13 (case studies) | Invent Ch.7 (flowcharts); Think Like a Programmer (strategy only, no C++ code) | Invent Ch.7 |
| 8 | Think Python Ch.5 recursion, Ch.15-18, Ch.21 | PCC Ch.9, Grokking Algorithms Ch.1-5, Data Structures & Algorithms Ch.1-9, Python Workout Ch.10, ATBS Ch.9 | Invent Ch.15-16 |
| 9 | ATBS Ch.11, 14, 15, 17-20, App. A | Python Workout Ch.9, `raw/docs/library/csv.txt` & `datetime.txt` (reference) | ATBS automation chapters |
| 10 | ATBS Ch.12, 13, 16 | PCC Ch.11 + Part II, `raw/docs/howto/argparse.txt` | Invent Ch.17-21, PCC Part II |

---

## Stage 0 — Current Baseline and Setup

**Status: complete.** Chris can already create/run `.py` files in VS Code and terminal, use `print()`, and recognize strings.

- **Purpose:** confirm environment works; establish baseline.
- **Prerequisites:** none.
- **Vocabulary:** program, source code, interpreter, script, IDE, terminal.
- **Common mistakes:** wrong working directory; Python 2 vs 3 confusion; indentation mangled by copy-paste.
- **Mastery check:** create, save, and run a `.py` file from both VS Code and terminal without help. (Already met.)
- **Parked:** everything below.

---

## Stage 1 — Python Atoms

**Status: packet generated 2026-06-24.** See `wiki/stages/stage-01-python-atoms.md` for the full packet (concept pages, glossary, flashcards, code pattern, drill, mini-project, common errors).

- **Purpose:** values, expressions, variables, assignment, strings, numbers, `print()`, `input()`, type conversion.
- **Prerequisites:** Stage 0.
- **Vocabulary:** value, variable, assignment, expression, string, integer, float, type, type conversion, comment, concatenation, `print()`, `input()`.
- **Mini-project:** short personal-info / "About Me" program using input, conversion, and formatted output.
- **Common mistakes:** forgetting quotes around strings; mixing `str` + `int` without converting; confusing `=` (assignment) with `==` (comparison); forgetting `input()` always returns a string.
- **Do not move on until:** Chris can write a short program from memory that takes input, converts its type, stores it in variables, and prints formatted output — without notes.
- **Parked:** conditionals, loops, functions, data structures.

---

## Stage 2 — Decisions

**Status: packet generated 2026-06-24.** See `wiki/stages/stage-02-decisions-and-boolean-logic.md` for the full packet.

- **Purpose:** comparisons, Boolean logic, `if` / `elif` / `else`.
- **Prerequisites:** Stage 1.
- **Sources:** Think Python Ch.5 (Boolean Expressions, Logical Operators, Conditional/Alternative/Chained/Nested Execution — recursion sections held for Stage 8); ATBS Ch.2; PCC Ch.5; Invent Ch.3 (Guess the Number), Ch.5 (Dragon Realm).
- **Vocabulary:** condition, Boolean, comparison operator, `and`/`or`/`not`, `if`/`elif`/`else`, branch, truthy/falsy.
- **Required code pattern:** `if-elif-else-decision-chain`.
- **Drill:** translate plain-English rules ("if it's raining and I have no umbrella...") into `if` chains.
- **Mini-project:** a branching text adventure (Dragon Realm style) or a number-guessing game with hints (Guess the Number style).
- **Common mistakes:** using `=` instead of `==`; missing colon; indentation mismatch; reaching for nested `if` when `elif` would be cleaner; forgetting `else` as a catch-all.
- **Do not move on until:** Chris can read a plain-English decision rule and write the matching `if`/`elif`/`else` chain from memory, and explain why he chose `elif` vs. nested `if`.
- **Parked:** loops, recursion, functions with return values.

---

## Stage 3 — Repetition

**Status: satisfied 2026-07-26.** See `wiki/current-position.md` for the final
fresh loop-and-accumulator gate evidence.

- **Purpose:** `for`, `while`, `range()`, counters, accumulators, loop tracing.
- **Prerequisites:** Stage 2.
- **Sources:** Think Python Ch.7 (Reassignment, Updating Variables, `while`, `break`, Algorithms) + "Traversal with a for Loop" pulled forward from Ch.8; ATBS Ch.3; PCC Ch.7 (while/input) and Ch.4 (for, pulled forward); reinforced via Invent Ch.3.
- **Vocabulary:** loop, iteration, iterable, `for` loop, `while` loop, `range()`, counter, accumulator, `break`, `continue`, infinite loop.
- **Required code patterns:** `for-loop-over-range`, `while-loop-until-condition`.
- **Drill:** loop tracing (predict output by hand) + write-a-loop-from-scratch drills.
- **Mini-project:** accumulator program (running total/average calculator) or an extended number-guessing loop with limited attempts.
- **Common mistakes:** off-by-one in `range()`; infinite `while` loop from forgetting to update the condition; confusing `break` vs `continue`.
- **Do not move on until:** Chris can trace a loop's output by hand and write a counter/accumulator loop from memory.
- **Parked:** nested loops over complex data, recursion as a loop alternative.

---

## Stage 4 — Functions

**Status: active 2026-07-26.** See
`wiki/stages/stage-04-functions-parameters-return.md` for the full packet.

- **Purpose:** `def`, calls, parameters, arguments, return values, scope basics,
  then a short standard-library import/use bridge in the same order as both syllabi.
- **Prerequisites:** Stage 3.
- **Sources:** Think Python Ch.3 (Function Calls, Composition, Parameters/Arguments, Stack Diagrams, Fruitful vs. Void) + Ch.6 (Return Values, Boolean Functions); ATBS Ch.4; PCC Ch.8; Python Workout Ch.7.
- **Vocabulary:** function, `def`, call, parameter, argument, return value, scope, local variable, fruitful/void function.
- **Required code patterns:** `function-with-parameter`, `function-with-return-value`, `import-and-call-standard-library`.
- **Drill:** Python Workout Ch.7 exercises; write 3 small functions from a plain-English spec; then complete `stage-04-library-basics`.
- **Mini-project:** a small "toolbox" program combining 3-4 functions that call each other.
- **Common mistakes:** confusing parameter names with argument values; forgetting `return` (expecting `print()` inside a function to hand back a value); scope confusion (changing a local variable doesn't change anything outside the function).
- **Do not move on until:** Chris can write a function with parameters and a return value from memory, explain parameter vs. argument, and import/call one standard-library function while explaining import vs. installation.
- **Parked:** default/keyword arguments depth, `*args`/`**kwargs`, decorators.

---

## Stage 5 — Data Shapes

**Status: packet generated 2026-06-24.** See `wiki/stages/stage-05-data-shapes.md` for the full packet.

- **Purpose:** strings as sequences, lists, indexing/slicing, dictionaries, tuples, sets, choosing the right structure.
- **Prerequisites:** Stage 4.
- **Sources:** Think Python Ch.8 (Strings), Ch.10 (Lists), Ch.11 (Dictionaries), Ch.12 (Tuples); ATBS Ch.6-8; PCC Ch.3-4 & 6; Python Workout Ch.4-5; Invent Ch.8-14 (Hangman through Caesar Cipher) as mini-project material.
- **Vocabulary:** list, index, slice, mutable/immutable, dictionary, key, value, tuple, set, nested structure.
- **Required code patterns:** `list-loop-and-index`, `dictionary-lookup`.
- **Drill:** Python Workout Ch.4-5 exercises.
- **Mini-project:** pick one from Invent — Hangman (strings/lists), Tic-Tac-Toe (lists/2D thinking), or Caesar Cipher (string manipulation).
- **Common mistakes:** off-by-one indexing; treating strings as mutable (they aren't); `KeyError` from a missing dictionary key; aliasing confusion (a list assigned to a new name is a reference, not a copy).
- **Do not move on until:** Chris can choose correctly between a list and a dictionary for a given problem and explain why, plus debug one indexing mistake unassisted.
- **Parked:** comprehensions (Python Workout Ch.8 / Think Python Ch.19), advanced set operations.

---

## Stage 6 — Files, Errors, and Debugging

**Status: packet generated 2026-06-24.** See `wiki/stages/stage-06-files-errors-debugging.md` for the full packet.

- **Purpose:** read/write files, understand exceptions and tracebacks, debug systematically.
- **Prerequisites:** Stage 5.
- **Sources:** Think Python Ch.14 (Files), Ch.20 (Debugging); ATBS Ch.5 (Debugging) & Ch.10 (Reading and Writing Files); PCC Ch.10; Python Workout Ch.6; Invent Ch.6 (Using the Debugger).
- **Vocabulary:** file path (relative/absolute), open/read/write/close, exception, traceback, `try`/`except`, syntax/runtime/semantic error.
- **Required code patterns:** `file-read-with-context-manager`, `try-except-block`.
- **Drill:** Python Workout Ch.6 exercises; "read this traceback and find the bug" drills.
- **Mini-project:** a simple file-based note-saver or running score-tracker.
- **Common mistakes:** forgetting to close a file (not using `with`); wrong relative path; bare `except:` that swallows real errors; reading a traceback top-to-bottom instead of bottom-to-top.
- **Do not move on until:** Chris can read a Python traceback, identify the failing line and error type, and fix a basic bug without help.
- **Parked:** databases, advanced exception hierarchies, context manager internals.

---

## Stage 7 — Program Design

**Status: packet generated 2026-06-24.** See `wiki/stages/stage-07-program-design.md` for the full packet.

- **Purpose:** decomposition, pseudocode, flowcharts, planning before coding.
- **Prerequisites:** Stage 6.
- **Sources:** Think Python Ch.4, Ch.9, Ch.13 (the three Case Study chapters model incremental development and testing); Invent Ch.7 ("Designing Hangman with Flowcharts" — a direct model for this stage); Think Like a Programmer — **strategy/discussion only, never the C++ code itself** (see `wiki/parking-lot.md`).
- **Vocabulary:** decomposition, pseudocode, flowchart, algorithm, test case, incremental development.
- **Drill:** given a plain-English problem, write pseudocode or a flowchart before any code.
- **Mini-project:** plan (flowchart or pseudocode) AND build a multi-step program of Chris's choosing, built incrementally and tested at each step.
- **Common mistakes:** trying to write the whole program in one pass instead of building incrementally; skipping the planning step; combining untested pieces and debugging everything at once.
- **Do not move on until:** Chris can take a new plain-English problem, decompose it into steps on paper first, and build it incrementally.
- **Parked:** formal software engineering methodology, design patterns.

---

## Stage 8 — Algorithms and Data Structures (Beginner Depth)

**Status: packet generated 2026-06-24.** See `wiki/stages/stage-08-think-python-readiness.md` for the full packet.

- **Purpose:** basic OOP and sorting/searching as required by the syllabus, with
  recursion and Big O intuition as useful CS/spine enrichment rather than explicit
  Fall 2026 syllabus mandates.
- **Prerequisites:** Stage 7.
- **Sources:** Think Python Ch.5 recursion sections, Ch.15-18 (Classes/Objects/Methods/Inheritance), Ch.21 (Analysis of Algorithms); PCC Ch.9 (Classes); Grokking Algorithms Ch.1-5 (intro, selection sort, recursion, quicksort, hash tables); Data Structures & Algorithms Ch.1-9 (Big O, sorting, hash tables, stacks/queues — code language unconfirmed, treat as concept reference); Python Workout Ch.10 (Objects); Invent Ch.15-16 (Reversegam + AI); ATBS Ch.9 (Regex, lighter-weight addition).
- **Vocabulary:** recursion, base case, class, object, attribute, method, instance, Big O, sorting, searching, hash table.
- **Mini-project:** a small class-based program (e.g., a `Dog` or `Card` class with a couple of methods) plus one sorting/searching exercise implemented from scratch.
- **Common mistakes:** infinite recursion from a missing/wrong base case; forgetting `self`; confusing a class attribute with an instance attribute.
- **Do not move on until:** Chris can write a simple class with `__init__` and one method from memory, and trace a recursive function by hand to find its base case.
- **Parked:** trees, Dijkstra's algorithm, dynamic programming, k-nearest neighbors, deep inheritance/polymorphism, regex beyond basics.

---

## Stage 9 — Automation Bridge

**Status: packet generated 2026-06-24.** See `wiki/stages/stage-09-automation-bridge.md` for the full packet.

- **Purpose:** files/folders at scale, CSV/JSON, spreadsheets, scheduling — turning Python into a tool that does real chores.
- **Prerequisites:** Stage 8 (or Stage 6 minimum for the file-handling parts).
- **Sources:** ATBS Ch.11 (Organizing Files), Ch.14 (Excel), Ch.15 (Google Sheets), Ch.17 (PDF/Word), Ch.18 (CSV/JSON/XML), Ch.19 (Scheduling), Ch.20 (Email/Texts), Appendix A (installing packages); Python Workout Ch.9 (Modules/Packages); `raw/docs/library/csv.txt` and `datetime.txt` as fallback reference.
- **Vocabulary:** module, package, `pip`, CSV, JSON, automation script, scheduling.
- **Mini-project:** a file-organizing script or a CSV report generator.
- **Common mistakes:** hardcoded file paths that break on another machine; not handling a missing/malformed file; forgetting to `pip install` a needed package.
- **Do not move on until:** Chris can write a script that reads structured data from a file, processes it, and writes a result, without copying a recipe verbatim.
- **Parked:** advanced email/SMS/push-notification integrations, complex scheduling, business tooling (`03-WIKIS\BUSINESS` / `03-WIKIS\TECHNOLOGY` — formerly FORGE).

---

## Stage 10 — Application Thinking

**Status: packet generated 2026-06-24 — final stage of the original path.** See `wiki/stages/stage-10-application-thinking.md` for the full packet.

- **Purpose:** CLI tools, testing, databases, and a first taste of web/app architecture.
- **Prerequisites:** Stage 9.
- **Sources:** ATBS Ch.12 (CLI programs), Ch.13 (Web Scraping), Ch.16 (SQLite); Python Crash Course Ch.11 (Testing with `pytest`) + Part II (Pygame game, data visualization); Invent Ch.17-21 (graphics, sound, collision detection) as an alternative project track; `raw/docs/howto/argparse.txt` as reference.
- **Vocabulary:** CLI, argument parsing, unit test, database, web request, API (introductory only).
- **Mini-project:** Chris's choice — a CLI tool with arguments, a small Pygame game, or a tested module with a `pytest` suite.
- **Common mistakes:** not testing edge cases; tightly coupling logic to input/output so it can't be tested; skipping input validation.
- **Do not move on until:** Chris can build and explain a small end-to-end program (input → processing → output) with at least one automated test.
- **Parked:** Flask/FastAPI, SQLAlchemy, Docker, CI/CD, cloud deployment, NumPy/pandas, OCR, keyboard/mouse automation, text-to-speech, business applications (`03-WIKIS\BUSINESS` / `03-WIKIS\TECHNOLOGY` — formerly FORGE). See `wiki/parking-lot.md`.

---

## Stage Unlock Rules

Do not move forward just because a page exists.

A concept is ready when Chris can:

- define the term in plain English,
- recognize it in code,
- write a small example from memory,
- explain when to use it,
- debug one common mistake,
- complete one drill,
- explain the concept back verbally or in writing.

---

## Next Required Claude Operation

All 11 stages (0-10) now have complete packets. The originally-planned path is fully generated. Chris works through remaining stages at his own pace. When he reaches the end, or asks what's next, options to discuss: deeper practice/repetition within Stages 1-10, a bridge toward business applications (`03-WIKIS\BUSINESS` / `03-WIKIS\TECHNOLOGY` — formerly FORGE, retired July 7, 2026), or genuinely new advanced material beyond this path. Do not generate further stages speculatively — ask Chris first.
