---
type: contract
timeline: now
status: live
register: human-context
tags: [school, cse-1321, fall-2026]
updated: 2026-09-09
---

# CSE 1321 BF + CSE 1321L 04 — Course Spine

**The only file in `.ROOT` that states a CSE 1321 or 1321L date.** Teaching content lives in
`03-WIKIS\PYTHON\wiki\`; what Chris can actually do lives in that hub's `current-position.md`.

**Sources, in precedence order:**

1. **D2L quiz windows** — `77-INBOX\CSE_lecture_due_dates.md`, captured 2026-09-02. **Live system, wins on any conflict.**
2. **Lecture syllabus PDF** — `Fall-Semester-2026-CSE-1321-BF-(81262)...pdf`, 16 pp., verified Fall calendar.
3. **Lab syllabus PDF** — `Fall-Semester-2026-CSE-1321L-04-(86703)...pdf`. **Its calendar is a Spring calendar** (Jan/Feb/Mar/Apr, Spring Break, "Midterm Mar 2–8"). Not a bad capture — the instructor's own posted document is wrong-term. **No lab date below comes from it.**

**Meeting:** Lecture Mon/Wed 4:10–5:30 PM, Academic Building 203 · Lab Tue 5:45–7:35 PM, Atrium 2120.
**Submission:** lecture quizzes and tests in D2L (Respondus LockDown Browser + webcam for tests); labs and assignments in **Gradescope**.
**AI: prohibited on all submitted work, both courses.** Practice and explanation only.

---

## Grading — resolved

The two grading tables that looked contradictory in the Markdown capture are **not** contradictory.
The PDF carries the column headers the Markdown capture dropped:

| | Spring **and Fall** Semesters | Summer Semester |
|---|---|---|
| Quiz Average | **25%** | 40% |
| Test 1 | **25%** | — |
| Test 2 | **25%** | — |
| Midterm | — | 20% |
| Final Exam | **25%** | 40% |

**Fall 2026 governs: Quiz 25 / Test 1 25 / Test 2 25 / Final 25.** No instructor email needed.
Lowest quiz dropped.

**Lab (1321L):** Homework Assignments 40% · Lab Exercises 10% · Midterm 20% · Final 30%.
Lowest lab assignment and lowest lab exercise dropped.

> **Lesson worth keeping:** the `.md` syllabus captures in `raw\syllabi\` lose table headers.
> Three of the five courses' key facts live in tables. **Keep the PDF as the authority for any
> table; use the Markdown only for prose search.**

---

## Lecture spine — CSE 1321 BF

Wiki paths relative to `03-WIKIS\PYTHON\wiki\`. Quiz windows are D2L's, which differ from the
syllabus in Weeks 10–13 — see the discrepancy note below.

| Wk | Class dates | Module / topic | Stage | Proof — pass cold | Assessment (D2L window) |
|---|---|---|---|---|---|
| 1 | Aug 24 – 30 | M0 — Welcome, decomposition, algorithms & abstraction, computers vs. programs | `stages/stage-00-setup-and-orientation` | `drills/cse-module-0-algorithmic-thinking` | Syllabus & Policy quizzes — open through **Dec 7**, unlimited attempts · Respondus setup quiz |
| 2 | Aug 31 – Sep 6 | M1 — I/O, data types, operators, arithmetic, boolean expressions, assignment | `stages/stage-01-python-atoms` | `drills/stage-01-input-and-conversion` | **Quiz 1** — Basics/Variables/Types/IO/Expressions · Aug 31 → **Sep 6, 11:59 PM** · 3 attempts |
| **3** | **Sep 7 – 13** | **M2 — Selection statements (branching)** | `stages/stage-02-decisions-and-boolean-logic` | `drills/stage-02-decision-rules` | — |
| 4 | Sep 14 – 20 | M2 — Selection statements | `stages/stage-02-decisions-and-boolean-logic` | `drills/stage-02-decision-rules` cold | **Quiz 2** — Selection · opens **Sep 14**, closes **Sep 20, 11:59 PM** · 3 attempts |
| 5 | Sep 21 – 27 | M2 — Repetition statements (loops) | `stages/stage-03-loops-and-repetition` | `drills/stage-03-loop-tracing` | — |
| 6 | Sep 28 – Oct 4 | M2 — Repetition statements | `stages/stage-03-loops-and-repetition` | `drills/stage-03-loop-tracing` cold | **Quiz 3** — Repetition · Sep 28 → **Oct 4, 11:59 PM** |
| 7 | Oct 5 – 11 | **TEST 1 (Modules 1–2)** · M3 — Defining functions, parameters, arguments | `stages/stage-04-functions-parameters-return` | Test-1 cold set — see below | **Test 1 — Oct 5** (MW section) · Respondus + webcam |
| 8 | Oct 12 – 18 | M3 — Functions | `stages/stage-04-functions-parameters-return` | `drills/stage-04-function-writing` | **Quiz 4** — Functions · Oct 12 → **Oct 18, 11:59 PM** |
| 9 | Oct 19 – 25 | M4 — Python libraries | `stages/stage-04b-python-libraries` | `drills/stage-04-library-basics` | **Quiz 5** — Libraries · Oct 19 → **Oct 25, 11:59 PM** |
| 10 | Oct 26 – Nov 1 | M5.1 — Tuples, lists | `stages/stage-05-data-shapes` | `drills/stage-05-data-structure-practice` | **Quiz 6** — Tuples, lists · Oct 26 → **Nov 1, 11:59 PM** ⚠ |
| 11 | Nov 2 – 8 | M5.2 — Dictionaries, searching & sorting | `stages/stage-05b-searching-and-sorting` | `drills/stage-05-data-structure-practice` cold | **Quiz 7** — Tuples/lists/dict/search/sort · Nov 2 → **Nov 8, 11:59 PM** ⚠ |
| 12 | Nov 9 – 15 | **TEST 2 (Modules 1–5)** · M6 — Object-oriented programming | **gap — see below** | Test-2 cold set | **Test 2 — Nov 9** (MW section) |
| 13 | Nov 16 – 22 | M6 — Object-oriented programming | **gap** | `drills/stage-08-algorithms-and-classes-practice` | **Quiz 8** — OOP I · Nov 16 → **Nov 22, 11:59 PM** ⚠ |
| — | Nov 23 – 29 | *Fall break — no classes* | — | — | — |
| 14 | Nov 30 – Dec 6 | TBD (syllabus) | — | — | **Quiz 9** — OOP · Nov 30 → **Dec 6, 11:59 PM** |
| 15 | Dec 7 | M8 — Review · last day of classes | — | mixed cold set | **Quiz 10** — Course review · Nov 30 → **Dec 7, 11:59 PM** |
| 16 | Dec 8 – 24 | Finals week | — | — | Final exam — date **`NEED D2L`** |

⚠ **D2L and the syllabus disagree on Quizzes 6–8.** The syllabus table says *Quiz 6 due Nov 8*
and *Quiz 7 & Quiz 8 due Nov 19*. D2L says Quiz 6 closes **Nov 1**, Quiz 7 closes **Nov 8**, and
Quiz 8 closes **Nov 22**. **The D2L windows above govern** — a quiz that closes a week earlier
than expected is the exact shape of an avoidable zero. Re-verify in D2L in late October.

Two more syllabus artifacts, recorded so nobody re-investigates them: the Week 15 row reads
*"Module 8: Review (May 4th, 2026, Last Day of Classes)"* — Spring residue in an otherwise
correct Fall table; the Dec 7 date is right. And Test dates come from the **FYE site**, not D2L
assignments — the D2L capture notes this, and it is why Test 1 and Test 2 appear only in the
syllabus.

### Gap: no OOP stage exists

Module 6 (object-oriented programming) runs Weeks 12–13, carries **Quiz 8 and Quiz 9**, and is on
the final. `03-WIKIS\PYTHON\wiki\stages\` has thirteen stage files and **none of them covers
classes and objects.** The nearest asset is `drills/stage-08-algorithms-and-classes-practice`,
which is a drill, not a stage.

That is the single largest teaching gap in the CSE hub, and it is nine weeks out — enough runway
to build it properly rather than the night before Quiz 8.

### Off-syllabus PYTHON stages

`stage-06-files-errors-debugging`, `stage-07-program-design`, `stage-08-think-python-readiness`,
`stage-09-automation-bridge`, `stage-10-application-thinking` — none map to a scheduled CSE 1321
module (Week 14 is "TBD" and may absorb one). They are useful for the self-directed track and for
the business build, **not** for exam prep. Tag them so a tutoring session does not treat them as
"next."

### Test 1 cold set — Oct 5, covers Modules 1–2

```
M1  drills/stage-01-input-and-conversion   — input(), casting, operators, expressions
M2  drills/stage-02-decision-rules         — if / elif / else, boolean logic, nesting
M2  drills/stage-03-loop-tracing           — while / for, accumulators, trace-by-hand
```

Trace-by-hand is the skill Test 1 punishes hardest and the one that most resembles the exam:
closed-book, no interpreter. Run `stage-03-loop-tracing` on paper.

---

## Lab spine — CSE 1321L 04

**Dates are not yet known and are not guessed.** The posted lab syllabus carries a Spring
calendar; the authoritative Fall document is the FYE schedule
(`cse1321l_schedule_fall_26_due_dates_v2-1.docx`) or the Gradescope due dates.

Module sequence below is from the FYE course page and is reliable. Counts disagree between
sources — the syllabus body says **13 labs and 7 assignments**, the FYE page lists **Labs 1–12
and Assignments 1–6**. Resolve when the schedule lands.

| Module | Labs | Assignment | Stage | Proof |
|---|---|---|---|---|
| M0 — Intro, IDE, Gradescope | — | — | `stages/stage-00-setup-and-orientation` | Submit one file to Gradescope successfully |
| M1 — I/O, variables, data types, operators | Labs 1–3 | Assignment 1 | `stages/stage-01-python-atoms` | `drills/stage-01-input-and-conversion` |
| M2 — Flow control: selection, repetition | Labs 4–6 | Assignments 2–3 | `stages/stage-02…`, `stages/stage-03…` | `drills/stage-02-decision-rules`, `drills/stage-03-loop-tracing` |
| M3 — Functions | Lab 7 | Assignment 4 | `stages/stage-04-functions-parameters-return` | `drills/stage-04-function-writing` |
| — | **Midterm — in class, closed book, no resources** | | | date **`NEED`** |
| M4 — Python libraries | Lab 8 | — | `stages/stage-04b-python-libraries` | `drills/stage-04-library-basics` |
| M5.1 — Tuples, lists | Lab 9 | Assignment 5 | `stages/stage-05-data-shapes` | `drills/stage-05-data-structure-practice` |
| M5.2 — Dictionaries, searching, sorting | Lab 10 | Assignment 6 | `stages/stage-05b-searching-and-sorting` | `drills/stage-05-data-structure-practice` |
| M6 — Object-oriented programming | Labs 11–12 | — | **gap** | `drills/stage-08-algorithms-and-classes-practice` |
| — | **Final — in class, closed book, no resources** | | | date **`NEED`** |

**All lab dates: `NEED` — Chris is bringing them back from class.** When they arrive, they fill
the table above and nothing else in `.ROOT` changes.

---

## Rules for this file

1. **One owner.** No other `.ROOT` file states a CSE date. `PYTHON\wiki\syllabus-alignment.md` and
   `cse-1321-17-week-mastery-plan.md` are superseded on dates.
2. **Precedence:** D2L / Gradescope → lecture syllabus PDF → FYE site. **Never the lab syllabus calendar.**
3. **For any table, the PDF is the authority.** The Markdown captures dropped headers and produced
   a false contradiction that cost real investigation time.
4. **It points, it does not teach.** Every cell is a path into the PYTHON hub.

## Open items

| # | Item | Owner | Unblocks |
|---|---|---|---|
| 1 | Lab & assignment due dates, midterm, final | Chris — after class / FYE `.docx` / Gradescope | Whole lab spine |
| 2 | Lecture final exam date | KSU finals schedule | Week 16 |
| 3 | Build an OOP stage | Next build session | Module 6, Quizzes 8–9, final |
| 4 | Re-verify Quiz 6–8 windows in D2L | Late October | Prevents an early-close zero |
| 5 | 13 labs / 7 assignments vs 12 / 6 | FYE schedule | Lab count |
