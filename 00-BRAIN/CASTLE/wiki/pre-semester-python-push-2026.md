---
type: plan
timeline: log
status: complete
tags: [planning, school, programming, python]
created: 2026-07-24
closed: 2026-08-23
---

# Pre-Semester Python Push — July 27 to August 23, 2026

### Four weeks, run at school pace, to enter August 24 having already seen every lecture module Chris has not yet reached.

> ## ✅ WINDOW CLOSED 2026-08-23 — outcome recorded against the success bar, not around it
>
> Closed at the semester transition on its own dated schedule. `review_trigger` removed
> rather than re-dated; a closed window has no next review.
>
> **Owner truth at close — `03-WIKIS\PYTHON\wiki\current-position.md`: Stage 4b**, reached
> 2026-07-29 when Stage 4 closed. **The resume point is C1** — `53`/`NameError` plus an
> independent `average(numbers)` — and it is **unrun since Aug 18**. Nothing here promotes it.
>
> **Against § Success bar at August 23, honestly:**
>
> | Bar | Result |
> |---|---|
> | Stage 4 functions independently fluent, proof recorded | ✅ Stage 4 closed 2026-07-29 |
> | Stage 5 lists and dictionaries *worked*, not merely read | ❌ **Not reached.** Stage 4b is where the owner sits |
> | Searching/sorting, OOP, recursion **seen** | ❌ Not reached — Weeks 3–4 of the map did not run as written |
> | One mixed cold read passed | ❌ Not recorded |
> | Course logistics confirmed against live D2L | ⏭ D2L opens **Aug 24**; carried into Phase 1's first exit criterion |
>
> **Why, and it is not a failure of the plan:** from Aug 1 the entire capacity of the system
> went into semester readiness — five syllabi, the workload/reading/schedule plans, the laptop
> build, and two `.ROOT` repairs. This lane's own § Fixed points note says it *"does not own
> the month."* It did not get the month, and § Guardrail 1 is the reason nothing above is
> rounded up: **exposure is logged as exposure; `current-position.md` moves only on
> independent performance.**
>
> **What carries forward:** C1 is the named PYTHON item in
> [[weekly-plan-2026-08-24-to-2026-08-30]]'s Sat Aug 29 lead block, and the Week 1 plan flags
> PYTHON as *the hub to look at* because week 1 otherwise gives it nothing. **Guardrail 5
> still binds** — when the live course reaches Module 5.2 in November it is taught from the
> live module, not from August's partial exposure.

## What this page is

A **sequencing map**, not a weekly plan and not learner truth. Each Sunday
review generates that week's actual checklist in `weekly-plans/` from the row
below. This page says *what module is next and what proof closes it*; the
weekly plan says *what happens Tuesday*.

Ownership, unchanged:

- `03-WIKIS\PYTHON\wiki\current-position.md` — the only home of learner truth.
- `01-NORTH_STAR\Goals & Milestones\fall_2026_semester.md` — the readiness gates.
- `03-WIKIS\PYTHON\wiki\syllabus-alignment.md` — the course pathway and reading queue.
- This page — sequencing only. It records no mastery.

## Origin

Chris's direction, 2026-07-24: use the month to "do a month worth of school
work at school pace," touching as many upcoming modules as possible — "even if
it is just to touch content so when I get into it during the semester I have
looked and thought about it already."

## The two tracks

The request contains two different depths. Keeping them separate is what makes
the push safe.

| Track | What it means | Does it move `current-position.md`? |
|---|---|---|
| **Gate** | Mastery work. Independent build, cold explain-back, proof recorded. Drawn from the `fall_2026_semester.md` readiness gates. | **Yes** — but only from independent proof. |
| **Recon** | Deliberate first exposure. Read, trace, ask questions, stop. No drill-to-mastery, no proof claim. | **No.** Logged as exposure only. |

**Priority rule:** if a week runs short, Recon is cut first. Never the reverse.
The Gate track is what Test 1 (Oct 5, Modules 1–2) and the closed-book lab
midterm actually measure.

## Position at the start

Stages 0–2 satisfied. Stage 3 (loops) active, closing at the July 26 review.
In semester terms that puts Chris at roughly **lecture Week 6** — so the four
weeks below run Modules 3 through 6, which is the remainder of the lecture
syllabus except Module 7/8 (TBD/Review) and the lab's Java week.

## Week map

| Week | Course module | Gate track | Recon track | Enrichment thread |
|---|---|---|---|---|
| **1** — Jul 27–Aug 2 | Module 3: functions, parameters, arguments | Stage 4 core. Fluency with `def`, parameters, arguments, return values, scope. Readiness gate #2. | — protect the gate | Docstrings and naming taught while writing the functions |
| **2** — Aug 3–Aug 9 | Module 4: Python libraries → Module 5.1: tuples, lists | Stage 4 stdlib bridge, then Stage 5 lists/tuples/strings-as-sequences | — | Stage 9 automation begins: pick one real task off the capability library |
| **3** — Aug 10–Aug 16 | Module 5.2: dictionaries, searching, sorting | Stage 5 dictionaries + `choosing-a-data-structure` | Searching/sorting and Big-O — touch only | SQL reps peak here: `GROUP BY` ≡ the dictionary accumulator |
| **4** — Aug 17–Aug 23 | Module 6: object-oriented programming | The mixed cold-read gate, pseudocode-before-implementation, debug-from-error. Readiness gates #3–#5. | OOP (class, instance, `__init__`, one method) and recursion — touch only | Exception handling folded into the debug gate |

Reading for each row is already sequenced in `syllabus-alignment.md`'s Semester
Reading Queue. Do not re-derive it here.

## The weekly ritual — one week of school, imitated

A real course week is one topic, one lab, an assignment about every other week,
and a quiz about every other week. Five moves reproduce that, and every artifact
they need already exists in the PYTHON packets:

1. **Lecture** — read the stage page, then its concept pages, then the assigned
   *Think Python* sections. Local map before book.
2. **Lab** — the stage's drill from `wiki/drills/`.
3. **Assignment** — the stage's mini-project from `wiki/mini-projects/`.
4. **Quiz** — closed-book retrieval from `wiki/flashcards/`. Closed book is the
   point; the real lab midterm and final are closed book, closed notes, no
   outside resources.
5. **Cold read** — one unseen short program: locate, trace, predict output, then
   run and explain the gap. Ladder levels R1–R3 in `syllabus-alignment.md`.

Close each week by logging error classes to `wiki/errors/` and advancing
`current-position.md` **only** where independent proof was recorded.

## Two syllabus-required topics that get taught in place

The July 24 wiki audit found no page anywhere in the hub teaching either of
these, though the lecture course description names both. Rather than bolt on
standalone pages, each is taught in the week where it arises naturally:

- **Good programming style and proper documentation** → Week 1. Docstrings,
  naming, and comment conventions are taught while writing the Stage 4
  functions, which is where they belong.
- **The relationship between correct code and security** → Week 3. The SQL
  strand already carries the lesson: `sql-grouping-and-aggregate-functions.md`
  shows sentinel values (`-1`, `-3`) silently corrupting a `SUM` unless filtered
  with `WHERE ... >= 0`. Input validation, taught from a real failure.

If either lands well, a durable page is written into the PYTHON hub afterward —
authored from the worked example, not ahead of it.

## Deliberately deferred

**pandas and NumPy.** These teach the vectorized replacement for the loop —
`numpy-ufuncs-pseudorandom-and-vectorized-logic.md` states plainly that
`np.where` exists to avoid an if/else loop over elements. Chris's loop
construction is still stabilizing and is exactly what the closed-book
assessments measure. Revisit at the August 23 review, or once loop construction
is cold-automatic — whichever is first. The source summaries are already
parked and ready; nothing is lost by waiting.

## Fixed points inside the window

- **Aug 1** — monthly weak-link review; re-rank `capability_development_goal.md`.
- **Aug 2, Aug 9** — weekly reviews; each generates the next weekly plan.
- **~Aug 14** — Revenue Lane A prediction check.
- **Aug 16** — monthly synthesis and system-direction review.
- **Aug 23** — final pre-class review. Confirm D2L, Gradescope, Respondus,
  webcam/microphone, and the real Fall lab calendar (readiness gate #6).
- **Aug 24** — semester begins.

This lane shares the month with Physics, the revenue items, and the reviews. It
does not own the month.

## Guardrails

1. **Recon is not mastery.** Exposure gets logged as exposure. `current-position.md`
   moves only from independent performance — the rule that has kept the Stage 1–3
   evidence trustworthy.
2. **Capacity is declared, not inferred.** Per `fall_2026_semester.md`'s workload
   gate, Chris states available capacity and the week is sized to it. Open
   calendar space is not capacity.
3. **Academic integrity is unchanged.** All of this is private pre-semester
   practice on fresh examples. CSE 1321/1321L prohibit AI-assisted submitted
   work; nothing here is submitted, and no live course prompt enters this lane.
4. **A slipped Gate week stops the push.** If Module 3 fluency has not landed,
   Week 2 does not start on schedule — the sequence re-plans rather than
   accumulating debt.
5. **Touching a module does not license skipping it later.** When the live
   course reaches Module 5.2 in November, it is taught from the live module, not
   from August's exposure.

## Success bar at August 23

Not "finished every packet." The bar is:

- Stage 4 functions independently fluent, with proof recorded.
- Stage 5 lists and dictionaries worked, not merely read.
- Searching/sorting, OOP, and recursion **seen** — enough that November's
  lecture is a second look, not a first one.
- One mixed cold read passed: unseen program, traced, output predicted,
  construct choice explained, one failure mode named.
- Course logistics confirmed against live D2L.

## Open

- Week 1's start assumes Stage 3 closes at the July 26 review. If it does not,
  the whole map shifts by the amount Stage 3 still needs.
- Whether to write durable PYTHON pages for style/documentation and
  correct-code/security, or leave them as worked examples. Decide after Week 3.

---
*Created 2026-07-24 · Source: Chris's direction plus the July 24 PYTHON wiki
audit · Feeds `weekly-plans/` each Sunday · Review: August 23, 2026.*
