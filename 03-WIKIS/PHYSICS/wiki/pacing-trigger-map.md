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

## What Is Confirmed vs. Estimated

| Confirmed, real (do not verify further) | Estimated (neighbor-syllabus evidence, verify in D2L) |
|---|---|
| PHYS 2211 Section 54 meets **Mon/Wed/Fri 9:10–10:05 AM**, Academic Building Room 200, Marietta Campus | Which chapter is lectured on which specific day |
| Friday **breakout/recitation 11:30 AM–12:25 PM**, Atrium Building Room 1116 | Exam dates (soft estimate: ~Sep 25, ~Oct 30, ~Nov 20) |
| Semester runs **Aug 24 – Dec 14, 2026** | Fall Break's exact date (both source syllabi are silent/unclear on it) |
| Labor Day (Mon Sep 7) and Thanksgiving Break (Mon–Fri Nov 23–27) are no-class | Instructor identity (registrar still shows "No specified Instructor" as of 2026-07-21) |

Source for the confirmed column: `02-LIBRARY\00-SCHOOL\View Registration
Information.md` (official Owl Express record). Source for the estimated
column: the two neighbor syllabi in `raw/syllabus/` — see
[[syllabus-coverage-ledger#Cross-Section Verification, 2026-07-21]]. **The
day D2L populates Section 54's real syllabus (target: Aug 24 or shortly
after), replace the Topic/Chapter column below with the real one and delete
this caveat block.**

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

> **The Sunday one week before an estimated exam date, stop new-material
> reading and run a pre-exam sweep**: `common-errors/` and `flashcards/` for
> every stage covered since the last exam, plus a cold pass on that range's
> mastery checklists.

Applies to the three soft exam dates below whenever a real one is confirmed
in D2L — shift the trigger date to match.

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
> `syllabus-coverage-ledger.md`, `learning-path.md`, and this page's Topic
> column in one pass, the same way the two neighbor syllabi were reconciled
> on 2026-07-21.

## Week-by-Week Table (Aug 24 – Dec 14, 2026)

All dates are real Mondays (confirmed lecture pattern). Topic/Chapter and
exam dates are the **estimated** column — see caveat above.

| Week of | Real class days | Estimated topic | Ch | Stage | Sunday read-ahead trigger |
|---|---|---|---|---|---|
| Aug 24 | M W F | Intro, Measurements → Motion in 1D | 1–2 | 1–2 | Read [[stages/stage-1-physics-and-measurement]] before Aug 24 (first class) |
| Aug 31 | (M date-label suspect — see [[source-map#Syllabus Data-Quality Gate]]) W F | Vectors → Motion in 2D / Projectile | 3–4 | 3–4 | [[stages/stage-3-vectors]], then [[stages/stage-4-motion-in-two-dimensions]] |
| Sep 7 | **Labor Day, no class M** · W F | Projectile Motion cont. → Concept of Force | 4–5 | 4–5 | [[stages/stage-5-laws-of-motion]] |
| Sep 14 | M W F | Newton's Laws → FBDs → Friction | 5 | 5 | Stage 5 drills/worked examples |
| Sep 21 | M W · **F ~Exam 1** | Newton's Law problems, Friction | 5 | 5 close-out | Pre-exam sweep (Trigger Rule 2) |
| Sep 28 | M W F | Circular Motion → Nonuniform Circular Motion | 6 | 6 | [[stages/stage-6-circular-motion]] incl. accelerated frames §6.3 |
| Oct 5 | M W F | Work and Energy → Work-Energy Theorem | 7–8 | 7 | [[stages/stage-7-energy-of-a-system]] |
| Oct 12 | M W F | Conservative/Nonconservative Forces → Conservation of Energy → Power | 7–8 | 7–8 | [[stages/stage-8-conservation-of-energy]] |
| Oct 19 | M W F | Linear Momentum → Impulse → Collisions 1D | 9 | 9 | [[stages/stage-9-linear-momentum]] |
| Oct 26 | M W · **F ~Exam 2** | Collisions 2D → Rotation of a Rigid Object | 9–10 | 9→10 | Pre-exam sweep, then [[stages/stage-10-rotation]] |
| Nov 2 | M W F | Moment of Inertia → Torque → Rotational KE, Rolling | 10 | 10 | Stage 10 drills |
| Nov 9 | M W F | Angular Momentum → Conservation of Angular Momentum → Static Equilibrium | 11–12 | 11–12 | [[stages/stage-11-angular-momentum]], [[stages/stage-12-static-equilibrium]] |
| Nov 16 | M W · **F ~Exam 3** | Static Equilibrium cont. → SHM | 12, 15 | 12→15 | Pre-exam sweep, then [[stages/stage-15-oscillatory-motion]] |
| Nov 23 | **Thanksgiving Break, no class all week** | — | — | — | Optional catch-up / rest; no new-material trigger fires |
| Nov 30 | M W F | Simple Pendulum, Energy in SHM → Damped/Forced Oscillations → Final Review | 15 | 15 | Stage 15 drills; §15.6-15.7 now leans toward assessed — see [[parking-lot]] |
| Dec 7 | Finals window (through Dec 14) | Final Review / Final Exam (exact date/time not yet confirmed) | all | 1–15 review | Full-course flashcard + common-errors sweep, all stages studied to date |

**Fall Break:** neither neighbor syllabus gives a confirmed date (Section 51
lists it as an unlabeled calendar row; Section 55 doesn't show it at all).
Not placed in the table above — check D2L/the official KSU academic calendar
and slot it in once known.

**Stages 16–18** (waves, superposition, relativity) do not appear in either
neighbor's calendar at all — see the open question logged in
[[syllabus-coverage-ledger#Cross-Section Verification, 2026-07-21]]. No
pacing row exists for them yet; this table stops at what the two real
neighbor calendars actually show.

## Last Updated

2026-07-21 — built from the two neighbor syllabi and the real Section 54
registrar record. Supersede the estimated column the moment real Section 54
content appears in D2L (Trigger Rule 5).
