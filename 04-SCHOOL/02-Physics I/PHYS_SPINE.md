---
type: contract
timeline: now
status: live
register: human-context
tags: [school, physics, fall-2026]
updated: 2026-09-09
---

# PHYS 2211 §54 — Course Spine

**The only file in `.ROOT` that states a PHYS 2211 date.** Everything else about this course
either teaches (`03-WIKIS\PHYSICS\wiki\`) or records what Chris can actually do
(`03-WIKIS\PHYSICS\wiki\current-position.md`). If another file disagrees with this one about a
date, this one wins and that file is wrong.

**Source:** `04-SCHOOL\02-Physics I\Syllabus.pdf` — Farhan Islam, §54, exact-section copy
received 2026-08-18, *Tentative Course Schedule*, all 45 dated rows. Every row below is a
verbatim transcription of that table. Nothing here is inferred.

**Meeting:** Mon / Wed / Fri 9:10–10:05, Academic Building 200 · Recitation §54 Fri
11:30–12:25, Atrium 1116.
**Homework:** WebAssign, weekly, **no late submissions accepted** — answer keys post at the
deadline. Extensions must be requested *before* the deadline, through WebAssign, with penalty.
**Exams:** four unit exams, **lowest dropped**. A missed exam becomes the dropped one.

**Known WebAssign dates** (from `77-INBOX\PHYS_due_dates.md`, D2L/WebAssign export 2026-09-02):

| Item | Date |
|---|---|
| HW2 | due **Sep 8**, 11:59 PM — closed |
| HW3 | due **Sep 14**, 11:59 PM |
| Module 3 — Work & Energy | opens **Sep 17**, 6:00 PM |
| Module 4 — Linear Momentum & Collisions | opens **Sep 30** |
| Module 5 — Rotational Kinematics & Dynamics | opens **Oct 18** |
| Module 6 — Static Equilibrium | opens **Oct 31** |
| Module 7 — Oscillations & Waves | opens **Nov 16** |

⚠ **Module 3 opens Sep 17 — four days before Unit Exam 1, and it is not on that exam.** Work and
Energy is Serway 7, Week 6 material. Opening early is not an instruction to start early. Finish
HW3 (due Sep 14), then run the exam cold set. Module 3 waits until Sep 22.

> **Syllabus reliability note.** This document contradicts itself three times: the header says
> "Monday, Wednesday, and Thursday" (all 45 dates say Friday), and the Email Policy gives
> `kpemasir@kennesaw.edu` while the header gives `fislam7@kennesaw.edu`. **The dated schedule
> table is the trustworthy part of this file. The prose is not.** Confirm policy questions with
> Islam directly.

---

## The spine

`Proof` names the drill that must be passed **cold — no notes, no worked example open** —
before the week counts as closed. Paths are relative to `03-WIKIS\PHYSICS\wiki\`.

| Wk | Dates | Class topic (Islam) | Serway | Stage | Proof — pass cold | Assessment |
|---|---|---|---|---|---|---|
| 1 | Aug 24 · 26 · 28 | Measurements · Motion in 1D · Motion in 1D w/ constant acceleration | 1.1–1.6, 2.1–2.9 | `stages/stage-1-physics-and-measurement`, `stages/stage-2-motion-in-one-dimension` | `drills/sig-fig-drill`, `drills/unit-conversion-drill`, `drills/dimensional-analysis-drill`, `drills/motion-graphs-drill`, `drills/constant-acceleration-drill` | WebAssign wk 1 |
| 2 | Aug 31 · Sep 2 · Sep 4 | Vectors · Motion in 2D · Projectile motion & uniform circular motion | 3.1–3.4, 4.1–4.2, 4.4–4.5 | `stages/stage-3-vectors`, `stages/stage-4-motion-in-two-dimensions` | `drills/vector-components-drill`, `drills/vector-addition-drill`, `drills/polar-cartesian-conversion-drill`, `drills/projectile-motion-drill` | WebAssign wk 2 |
| 3 | ~~Sep 7 Labor Day~~ · Sep 9 · Sep 11 | Concept of force & Newton's First Law · Newton's Second and Third Laws | 5.1–5.4, 5.6 | `stages/stage-5-laws-of-motion` | `drills/fbd-drawing-drill`, `drills/newtons-second-law-drill` | WebAssign wk 3 |
| **4** | **Sep 14 · 16 · 18** | **Gravitational force & free-body diagrams · Friction & connected systems · Uniform circular motion** | **5.5, 5.7, 5.8, 6.1–6.2** | `stages/stage-5-laws-of-motion`, `stages/stage-6-circular-motion` | `drills/friction-problems-drill`, `drills/inclined-plane-drill`, `drills/circular-motion-forces-drill` | WebAssign wk 4 |
| **5** | **Sep 21** · 23 · 25 | **UNIT EXAM 1** · Motion in accelerated frames · Motion under resistive forces | 6.3, 6.4 | `common-errors/stage-1` … `stage-6`, then `concepts/accelerated-reference-frames`, `concepts/terminal-velocity` | Exam-1 cold set — see below · then `drills/terminal-velocity-drill` | **Unit Exam 1 — Sep 21** |
| 6 | Sep 28 · 30 · Oct 2 | Applications & problem-solving in dynamics · Work by constant and variable force · Kinetic energy & work–energy theorem | 5.7, 7.1–7.5 | `stages/stage-7-energy-of-a-system` | `drills/work-calculation-drill`, `drills/work-energy-theorem-drill` | WebAssign wk 6 |
| 7 | Oct 5 · 7 · 9 | Conservative & non-conservative forces, potential energy · Conservation of mechanical energy & power · Linear momentum & impulse | 7.6–7.9, 8.1–8.5, 9.1–9.3 | `stages/stage-7-energy-of-a-system`, `stages/stage-8-conservation-of-energy`, `stages/stage-9-linear-momentum` | `drills/energy-conservation-drill`, `drills/spring-energy-drill`, `drills/power-drill`, `drills/momentum-impulse-drill` | WebAssign wk 7 |
| 8 | **Oct 12** · 14 · 16 | **UNIT EXAM 2** · Collisions in one dimension · Collisions in two dimensions | 9.4, 9.5 | `stages/stage-9-linear-momentum` | Exam-2 cold set · `drills/collision-drill` | **Unit Exam 2 — Oct 12** |
| 9 | Oct 19 · 21 · 23 | Center of mass & systems of many particles · Rotation of rigid bodies, angular variables · Torque & moment of inertia | 9.6–9.7, 10.1–10.5 | `stages/stage-9-linear-momentum`, `stages/stage-10-rotation` | `concepts/center-of-mass` explain-back, `concepts/moment-of-inertia` explain-back | WebAssign wk 9 |
| 10 | Oct 26 · 28 · 30 | Moment of inertia & rotational kinetic energy · Conservation of energy in rotational motion · Angular momentum & torque | 10.6–10.9, 11.1–11.2 | `stages/stage-10-rotation`, `stages/stage-11-angular-momentum` | `problem-types/rolling-without-slipping`, `drills/angular-momentum-drill` | WebAssign wk 10 |
| 11 | Nov 2 · **Nov 4** · Nov 6 | Conservation of angular momentum · **UNIT EXAM 3** · Static equilibrium of rigid objects | 11.2–11.4, 12.1 | `stages/stage-11-angular-momentum`, `stages/stage-12-static-equilibrium` | Exam-3 cold set · `problem-types/angular-momentum-conservation` | **Unit Exam 3 — Nov 4** |
| 12 | Nov 9 · 11 · 13 | Applications of static equilibrium · Simple harmonic motion · Energy in simple harmonic motion | 12.3, 15.1–15.3, 15.5 | `stages/stage-12-static-equilibrium`, `stages/stage-15-oscillatory-motion` | `drills/equilibrium-drill`, `drills/shm-equations-drill`, `drills/shm-energy-drill` | WebAssign wk 12 |
| 13 | Nov 16 · **Nov 18** · Nov 20 | Damped & forced oscillations · **UNIT EXAM 4** · Wave propagation & traveling waves | 15.6–15.7, 16.1–16.2 | `stages/stage-15-oscillatory-motion`, `stages/stage-16-wave-motion` | Exam-4 cold set · `concepts/wave-model` explain-back | **Unit Exam 4 — Nov 18** |
| — | Nov 23–29 | *Thanksgiving break — no classes* | — | — | — | — |
| 14 | Nov 30 · Dec 2 · Dec 4 | Wavelength, frequency & wave speed · Comprehensive review · Comprehensive review | 16.3 | `stages/stage-16-wave-motion` | Mixed cold set across all four exam blocks | WebAssign wk 14 |
| 15 | Dec 7 | Final exam preparation & course wrap-up | — | — | — | Final exam — **date `NEED D2L`** |

**Final exam date is not in the syllabus.** It comes from the KSU final-exam schedule and D2L.
That blank stays blank until Chris fills it — the spine does not guess dates.

---

## What this reveals — read this part

### 1. Four stages in the wiki are not on this course

The PHYSICS wiki was built from Serway's table of contents. Islam's course does not follow
Serway's table of contents. These four stages have **no row in the schedule above**:

| Stage | Serway | Status |
|---|---|---|
| `stage-13-universal-gravitation` (11,553 b) | Ch 13 | **Not scheduled.** Also has `drills/gravitation-drill`, flashcards, common-errors, `problem-types/orbital-motion`, `worked-examples/orbital-period-example`, `equations/newtons-law-of-gravitation`, `equations/orbital-mechanics`, `calculus-links/gravitational-potential-integral`. |
| `stage-14-fluid-mechanics` (5,112 b) | Ch 14 | **Not scheduled.** Plus fluids concepts, `equations/density`, `drills/stress-strain-drill`. |
| `stage-17-superposition` (12,282 b) | Ch 17 | **Not scheduled.** Plus `drills/standing-waves-drill`, `drills/beat-frequency-drill`. |
| `stage-18-relativity` (13,512 b) | Ch 18 | **Not scheduled** — though the course *description* promises special relativity. Plus `drills/relativity-lorentz-drill`. |

That is roughly **30% of the stage material aimed at chapters this course never reaches**, and
the wiki gives no signal that it is off-syllabus. A tutoring session told "PHYS, teach me the
next thing" could walk Chris straight into universal gravitation two weeks before an exam that
does not contain it.

**Action:** mark those four `status: parked` with the reason `off-syllabus PHYS 2211 §54 Fall
2026`, or move them to `wiki/parked-advanced/` (the folder already exists and is empty). Do not
delete — they are correct physics and PHYS 2212 or a later course may need them.

**One thing to verify with Islam:** the course description says the student will "explain the
basic ideas of special relativity," but the schedule ends at 16.3 plus review. Either relativity
is dropped this term or it is coming and the schedule is short a row. One email settles it, and
it decides whether `stage-18` is parked or promoted.

### 2. Chapters 13 and 14 being skipped changes the Week 9–11 load

The course jumps 12 → 15, skipping gravitation and fluids entirely, and compresses rotation
(Ch 10), angular momentum (Ch 11) and static equilibrium (Ch 12) into Weeks 9–11 with **Unit
Exam 3 landing mid-block on Nov 4**. That is the densest stretch of the term. It is also the
stretch where the wiki's stage-10 and stage-12 files are the largest (6,780 b and 15,520 b),
which suggests earlier sessions already found it hard.

### 3. Unit Exam 1 is Monday, September 21 — twelve days out

It covers **Chapters 1 through 6**: measurement, 1D motion, vectors, 2D motion and projectiles,
Newton's laws with friction and connected systems, and uniform circular motion.

`work-energy-25min-review.md` (last touched Sep 6) shows recent work in **Chapter 7** — one
chapter past the exam's coverage. Chapter 7 is Week 6 material and is not on this exam.

**Exam-1 cold set — the drills that map to the six chapters, in order:**

```
Ch 1   drills/sig-fig-drill · drills/unit-conversion-drill · drills/dimensional-analysis-drill
Ch 2   drills/motion-graphs-drill · drills/constant-acceleration-drill · drills/free-fall-drill
Ch 3   drills/vector-components-drill · drills/vector-addition-drill
       drills/polar-cartesian-conversion-drill
Ch 4   drills/projectile-motion-drill · drills/relative-velocity-drill
Ch 5   drills/fbd-drawing-drill · drills/newtons-second-law-drill
       drills/friction-problems-drill · drills/inclined-plane-drill
Ch 6   drills/circular-motion-drill · drills/circular-motion-forces-drill
```

Seventeen drills, six school days before the exam. Run them cold, in that order. Every drill
that misses goes to `04-SCHOOL\miss-log.md` with its error class and gets re-aimed — that
mechanism already works and needs no change.

Then read `common-errors/stage-1` through `stage-6` **the night before**, not earlier. They are
error catalogues; they are worth most when the material is already loaded.

`worked-examples/projectile-first-principles-example.md` (12,082 b — the largest worked example
in the wiki) covers the single most exam-likely problem type in Chapters 3–4. Work it before the
projectile drill, not after.

---

## Rules for this file

1. **One owner.** No other `.ROOT` file may state a PHYS 2211 date. Files that currently do —
   `semester-pathway.md`, `phys-2211-17-week-math-first-plan.md`, `pacing-trigger-map.md`,
   `syllabus-coverage-ledger.md`, `learning-path.md`, `04-SCHOOL\SEMESTER_MAP.md`,
   `semester-workload-plan.md`, `semester-reading-plan.md`, `weekly-study-schedule.md` — are
   superseded on this course's dates and get archived per the approved retirement.
2. **Cited or blank.** A row's dates come from Islam's schedule table or the row says
   `NEED D2L`. Nothing is inferred, interpolated, or carried over from a prior term.
3. **It points, it does not teach.** Every cell is a path into the wiki. A spine row that
   restates physics is a defect — the wiki page owns the content.
4. **D2L still wins.** This is a *tentative* schedule and Islam may move it. A live D2L
   announcement supersedes this file; when it does, edit this file and nothing else.
5. **Position lives elsewhere.** What Chris can actually do belongs in
   `wiki/current-position.md`, and it moves only on independent performance. This spine says
   what the course covers; it never claims he has it.

---

## Open items

| # | Item | Owner | Unblocks |
|---|---|---|---|
| 1 | Final exam date | D2L / KSU final-exam schedule | Week 15 row |
| 2 | Is special relativity taught this term? | Email Islam | Park or promote `stage-18` |
| 3 | Park the four off-syllabus stages | Next session | Stops off-syllabus tutoring |
| 4 | Archive the superseded PHYS planning files | Approved 2026-09-09 | Makes this the single owner |
