---
type: map
timeline: now
status: active
reference_priority: core
tags: [physics, school]
---

# Pacing Trigger Map

## Purpose

Answers one question: **"today is [date] — what should I be reading, and by
when?"** Two kinds of triggers, not just a calendar:

1. **Date triggers** — tied to the real semester calendar, telling you what
   to read ahead of lecture.
2. **State triggers** — tied to what you've actually mastered or how an exam
   is approaching, independent of the calendar.

Cross-reference: [[current-position]] is the live truth for where you
actually are. This page is the *schedule pressure* against that truth — if
they disagree, current-position wins and this page tells you how far behind
or ahead of pace you are.

## Controlling Source and Limits — rewritten 2026-08-18

**The exact Section 54 syllabus arrived.** `raw/syllabus/Syllabus.pdf` (Fall 2026,
Farhan Islam) now supplies every date this page used to estimate. The estimate columns
are gone.

| Now confirmed from the §54 syllabus | Still open |
|---|---|
| Lecture **Mon/Wed/Fri 9:10–10:05 AM**, Academic Building 200 — *the syllabus header says "Monday, Wednesday, and Thursday", but all 45 scheduled dates are M/W/F and the registrar agrees. Treat "Thursday" as a typo* | **Where and when §54 sits the four unit exams.** They print at 10:20–11:15, which is the §51/52/53 recitation slot, not Chris's Friday 11:30 |
| **Recitation §54 Friday 11:30 AM–12:25 PM**, Atrium 1116 | Whether the instructor shifts anything once D2L opens |
| Semester **Aug 24 – Dec 14, 2026**; **Thanksgiving break Nov 23–29** | |
| **Farhan Islam**, `fislam7@kennesaw.edu` *(the Email Policy paragraph's `kpemasir@` is boilerplate debris — use `fislam7@`)* | |
| **Exact topic-by-day schedule for all 15 weeks** | |
| **All four unit exam dates + the final**: Sep 21, Oct 12, Nov 4, Nov 18, and **Wed Dec 9, 8:00–10:00 AM** | |
| **Grading**: exams 45% (4, lowest dropped) · final 30% · HW 10% · recitation worksheet 10% · quizzes 5%. **No attendance component** | |
| **Scope**: Ch 1–12, 15, 16.1–16.3. **Ch 13, 14, 17, 38 are not on this course** | |

The path source is **`raw/syllabus/Syllabus.pdf`**. Its schedule is internally consistent
across all 15 weeks — unlike the neighbour captures, nothing past Week 8 is scrambled.
The two `04-SCHOOL` neighbour working copies were archived 2026-08-18; the `raw/` §51
capture stays as immutable evidence but is no longer a pacing source.

**Full detail, exam coverage, and the study-window table live in [[semester-pathway]].**
This page keeps the *trigger* logic; that page keeps the calendar.

## Trigger Rule 1 — The Weekend Read-Ahead

Lecture happens Monday, Wednesday, Friday. The controlled-path way to never
be caught flat-footed:

> **Every Sunday evening, read the concept page(s) for whatever chapter/section
> is expected in the coming week's table row below** — not to master it cold,
> just to have seen the vocabulary and the model once before lecture says it
> out loud. Full drilling still happens after, at the stage's normal pace.

This trigger fires every week of the semester, calendar gaps and all — it
doesn't require the exam dates or Fall Break date to be correct, only the
topic estimate.

## Trigger Rule 2 — Exam Approach

> **The Sunday one week before an exam date, stop new-material reading and run a
> pre-exam sweep**: `common-errors/` and `flashcards/` for every stage covered since
> the last exam, plus a cold pass on that range's mastery checklists.

**The four real dates, and the Sunday each sweep starts** (confirmed 2026-08-18):

| Exam | Date | Sweep begins | Covers |
|---|---|---|---|
| Unit Exam 1 | **Mon Sep 21** | Sun **Sep 13** | Ch 1–5 + 6.1–6.2 |
| Unit Exam 2 | **Mon Oct 12** | Sun **Oct 4** | Ch 6.3–6.4, 7, 8, 9.1–9.3 |
| Unit Exam 3 | **Wed Nov 4** | Sun **Oct 25** | Ch 9.4–9.7, 10, 11 |
| Unit Exam 4 | **Wed Nov 18** | Sun **Nov 8** | Ch 12.1, 12.3, 15 |
| **Final** | **Wed Dec 9, 8–10 AM** | Sun **Nov 29** | **Comprehensive** |

**Sweep content is weighted differently now that the equation sheet is supplied at every
exam.** Flashcard formula recall drops in value; cold *classification* — reading a worded
problem and naming the model, chapter, and setup — is what the exam actually tests. See
[[semester-pathway]] § "The equation sheet is supplied."

## Trigger Rule 3 — Mastery, Not Calendar, Moves the Active Stage

> **The moment a stage's full mastery checklist passes cold (no notes), update
> [[current-position]] and move to the next stage immediately** — do not wait
> for the calendar row below to "authorize" it. The table shows pressure, not
> permission. Chris has repeatedly moved faster than the July build-ahead
> assumed (Stage 3 closed cold in one session); this vault is not allowed to
> slow that down.

## Trigger Rule 4 — Stall Check

> **If more than 7 real days pass with no forward movement on the active
> stage**, that's a signal to reassess — either the stage packet has a real
> gap (flag it), or competing commitments need CASTLE-level sequencing, not
> just more physics time. Don't silently let the gap grow.

## Trigger Rule 5 — Real Dates Land

> **The first day Section 54 shows real content in D2L**, treat that as a
> hard trigger to re-run the syllabus cross-check: update `source-map.md`,
> `syllabus-coverage-ledger.md`, `learning-path.md`, [[semester-pathway]], and this
> page in one pass.

**This trigger already fired once, early and from a better surface.** On 2026-08-18 the
exact §54 syllabus arrived from the instructor rather than from D2L, and the full
cross-check ran that day. **It fires again on Aug 24** when D2L opens — the instructor
outranks the PDF, and the two day-one questions below need answers.

## Week-by-Week Path — real §54 dates, confirmed 2026-08-18

**This is the actual lecture schedule**, read from `raw/syllabus/Syllabus.pdf`. It is no
longer an estimate and no longer a neighbour section's topic order.

**Read this table as "what class is doing."** What *Chris* studies each week is one week
ahead of it — that pairing lives in [[semester-pathway]] § Phase 2.

| Week of | Class days | Topic | Serway | Stage | Sunday read-ahead |
|---|---|---|---|---|---|
| Aug 24 | M W F | Measurements → Motion in 1D (both halves) | 1.1–1.6, 2.1–2.9 | 1–2 | Already held — read ahead to Ch 3–4 |
| Aug 31 | M W F | Vectors → 2D motion → projectile + UCM | 3.1–3.4, 4.1–4.2, 4.4–4.5 | 3–4 | [[stages/stage-5-laws-of-motion]] |
| Sep 7 | **W F only** — Labor Day Mon Sep 7 | Force, Newton's 1st → 2nd and 3rd | 5.1–5.4, 5.6 | 5 | Weight/FBD, friction, UCM |
| Sep 14 | M W F | Weight and FBD → friction and connected systems → **uniform circular motion** | 5.5, 5.7, 5.8, 6.1–6.2 | 5→6 | 🔴 **EXAM 1 SWEEP** — retrieval, not new material |
| Sep 21 | M W F | 🔴 **UNIT EXAM 1 (Mon)** → accelerated frames → resistive forces | 6.3, 6.4 | 6 | [[stages/stage-7-energy-of-a-system]] |
| Sep 28 | M W F | Dynamics applications → work, constant and variable force → KE and work–energy theorem | 5.7, 7.1–7.5 | 7 | Ch 7.6–9.3 |
| Oct 5 | M W F | Conservative/nonconservative forces and PE → mechanical energy and power → momentum and impulse | 7.6–7.9, 8.1–8.5, 9.1–9.3 | 7–9 | 🔴 **EXAM 2 SWEEP** |
| Oct 12 | M W F | 🔴 **UNIT EXAM 2 (Mon)** → collisions in 1D → collisions in 2D | 9.4, 9.5 | 9 | [[stages/stage-10-rotation]] |
| Oct 19 | M W F | Centre of mass → rotation and angular variables → **torque and moment of inertia** | 9.6–9.7, 10.1–10.5 | 9→10 | ⚠ **flag #16 — right-hand rule anchor is due before Oct 23** |
| Oct 26 | M W F | Moment of inertia and rotational KE → energy conservation in rotation → angular momentum and torque | 10.6–10.9, 11.1–11.2 | 10–11 | 🔴 **EXAM 3 SWEEP** + [[stages/stage-12-static-equilibrium]] |
| Nov 2 | M W F | Conservation of angular momentum → 🔴 **UNIT EXAM 3 (Wed)** → static equilibrium | 11.2–11.4, 12.1 | 11–12 | [[stages/stage-15-oscillatory-motion]] |
| Nov 9 | M W F | Applications of static equilibrium → SHM → energy in SHM | 12.3, 15.1–15.3, 15.5 | 12→15 | 🔴 **EXAM 4 SWEEP** |
| Nov 16 | M W F | Damped and forced oscillations → 🔴 **UNIT EXAM 4 (Wed)** → wave propagation and traveling waves | 15.6–15.7, 16.1–16.2 | 15→16 | [[stages/stage-16-wave-motion]] |
| Nov 23 | **Thanksgiving — no classes Nov 23–29** | — | — | — | Consolidation only |
| Nov 30 | M W F | Wavelength, frequency, wave speed → comprehensive review → comprehensive review | 16.3 | 16 | Full-course retrieval |
| Dec 7 | M only | Final exam prep and wrap-up. **Last day of classes** | — | review | Final sweep |
| **Dec 9** | **🎓 FINAL EXAM, Wed 8:00–10:00 AM** | **Comprehensive** | 1–12, 15, 16.1–16.3 | all | — |

**Thanksgiving break is confirmed: Nov 23–29.** The old "check D2L for Fall Break" item is
closed.

**Chapters 13 (universal gravitation), 14 (fluids), 17 (superposition), and 38–39
(relativity) are not on this course.** Their stage packets stay built as durable
reference; do not activate them for PHYS 2211. This shrink is authorised by the exact
§54 calendar, satisfying [[syllabus-coverage-ledger]]'s standing rule against shrinking
the path on neighbour evidence alone.

## Two day-one questions this schedule cannot answer

1. **Where and when does §54 sit the unit exams?** They print at 10:20–11:15 AM, which is
   the §51/52/53 recitation slot — not Chris's Friday 11:30. No timetable conflict either
   way, but he needs the room.
2. **Is the meeting pattern MWF or M/W/Th?** All 45 dates say MWF; one header line says
   Thursday. Confirm and stop re-litigating it.

## Last Updated

**2026-08-18** — rebuilt on the exact Section 54 syllabus obtained from Farhan Islam.
Every estimated date replaced with a printed one; scope shrunk to Ch 1–12, 15, 16.1–16.3;
neighbour-section pacing retired. D2L and the instructor still supersede this page.
