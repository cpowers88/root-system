---
type: index
timeline: now
status: active
tags: [school, fall-2026]
created: 2026-08-20
---

# 04-SCHOOL — Fall 2026 launch page

This folder is the course-file home. **Start with `FallKSU.xlsx` for the human
checklist**, then use the live owner files below when the workbook needs facts.
The workbook is a view and working checklist; it does not become a second source
of truth.

## Open these

| Question | Open |
|---|---|
| What do I need to do and check off? | `FallKSU.xlsx` |
| What is due, how heavy is the week, and where are the collisions? | `semester-workload-plan.md` |
| **When in the day do I actually study, and what?** | **`weekly-study-schedule.md`** |
| What should I read, and to what page? | `semester-reading-plan.md` |
| What are the verified dates, rooms, weights, and course policies? | `SEMESTER_MAP.md` |
| Which syllabus/source is binding, provisional, or still missing? | `SYLLABUS_STATUS.md` |
| What is my live action today? | `..\NOW.md` |

## 🛣 There is ONE road. This is it. — added 2026-08-23, the night before launch

**Chris's question, and it was the right one: "is there more than one road map?"** The answer
is that there is one road built in **layers**, each owning a different question — and on
2026-08-23 exactly one genuine contradiction was found inside it and fixed. **Nothing below is
optional and nothing below is a second road.**

| Layer | The question it answers | The single owner |
|---|---|---|
| 1 · **Direction** | Why any of this | `01-NORTH_STAR\NORTH_STAR.md` |
| 2 · **Dates & course facts** | When is it, what is it worth, what are the rules | **`SEMESTER_MAP.md`** |
| 3 · **Load** | What is due this week and how heavy is it | **`semester-workload-plan.md`** |
| 4 · **What to study, per course** | Which sections, in which week | the **owning hub** — PHYS: **`03-WIKIS\PHYSICS\wiki\semester-pathway.md` § Phase 2** · CSE: `PYTHON\wiki\syllabus-alignment.md` · TCOM: `EDUCATION\...\tcom-2010-17-week-execution-plan.md` · ECON: `EDUCATION\...\econ-1000\semester-map.md` · ENGR: 🔴 undefined until BWD posts |
| 5 · **What to open, to what page** | The exact page number | **`semester-reading-plan.md`** (assembles layer 4; **the owner wins on conflict**) |
| 6 · **When in the day** | Which hour each block runs | **`weekly-study-schedule.md`** *(rendered view: the Powers Fall Timetable artifact — a view, never an authority)* |
| 7 · **This week specifically** | What actually happens Mon–Sun | **CASTLE `wiki\weekly-plans\weekly-plan-<dates>.md`** |
| 8 · **Right now** | The single next action | **`..\NOW.md`** |
| 9 · **Am I actually learning it** | Proof, stage, and open misses | each hub's **`current-position.md`** + **`miss-log.md`** |
| 10 · **What did I score** | Standing against the 90% target | **`FallKSU.xlsx`** § GRADE TRACKER |

**Above all ten: D2L and the exact-section instructor.** A released syllabus beats every file
here; a D2L posting beats the syllabus. **When two layers disagree, the lower-numbered layer
does not automatically win — the *named owner for that question* wins.** Say so in one line and
correct the other file in the same session.

> ### The one contradiction found, and what it teaches
>
> **`semester-reading-plan.md` named the lecture-paced `phys-2211-17-week-math-first-plan.md`
> as the owner of PHYS reading, while `semester-workload-plan.md` and PHYSICS learner truth
> named the one-week-ahead `semester-pathway.md`.** They differed by exactly one week, which
> would have made the **Sun Sep 13 Exam 1 proof gate unreachable** and put new material inside
> the Exam 1 sweep. Corrected 2026-08-23; the 17-week plan keeps its lecture→page lookup and
> loses its pacing claim.
>
> **Three instances of one defect in three days** — the Sep 7 gate, the Week 1 consumed drill,
> and this. **The pattern: a page cites an owner it did not read.** Raised as flag **#104**.
> The cheap counter-move, and the one to actually run: *before writing a date or a sequence into
> any page, open the owner it cites and compare — citing is not reading.*

## Sunday translation into the workbook

For each course, write one row with these fields:

`Week → course → focus → reading/open → graded work → proof → due → status`

1. Read the week's row in `semester-workload-plan.md`.
2. Read the matching week in `semester-reading-plan.md`.
3. Check D2L; D2L and the exact-section instructor override every local plan.
4. Put one visible weekly focus and one proof in the workbook for each course.
5. During the week, use the workbook as the checklist. Return corrections to the
   owning Markdown/wiki page instead of letting the workbook become hidden truth.

## Course folders

| Folder | Course | Live truth outside this folder |
|---|---|---|
| `01-CSE-Python\` | CSE 1321 / 1321L | `03-WIKIS\PYTHON\wiki\current-position.md` |
| `02-Physics I\` | PHYS 2211 | `03-WIKIS\PHYSICS\wiki\current-position.md` |
| `03-TCOM\` | TCOM 2010 | `03-WIKIS\EDUCATION\wiki\current-position.md` |
| `04-ECON\` | ECON 1000 | `03-WIKIS\EDUCATION\wiki\current-position.md` |
| `05-ENGR\` | ENGR 1000 | `03-WIKIS\EDUCATION\wiki\current-position.md` |
| `99-EDG\` | Deferred prior course | Not part of the Fall 2026 launch |

Graded work belongs in each course's `work\` folder. Reference material stays in
the course folder. Domain teaching and learner truth stay in the owning wiki.

## ENGR evidence boundary

The exact Fall 2026 **BWD** syllabus is still missing. Three neighboring Fall
2026 web sections (BWB, BWC, BWF) share a near-identical course core. Their common
structure is strong provisional evidence only. BWD D2L and Kamyar Raoufi remain
binding for dates, execution, delivery mechanics, and any difference in policy.

