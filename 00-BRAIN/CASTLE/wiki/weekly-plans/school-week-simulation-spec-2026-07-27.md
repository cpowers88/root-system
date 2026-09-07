---
type: spec
timeline: reference
status: approved
tags: [planning, school, fall-2026, simulation-week]
created: 2026-07-26
approved_by: Chris
approved: 2026-07-26
---

# School Week Simulation — Honest Workload Spec

**Purpose.** Chris asked for a simulation of one real week of the Fall 2026 load,
with an honest assessment of how much work that actually is, built from the
syllabi rather than from our own stage plans. This spec proposed what the July
27–August 2 week should contain. Chris approved the 32-block simulation on
July 26; the live implementation is
`weekly-plan-2026-07-27-to-2026-08-02.md`.

**Sources.** Exact-section syllabi for CSE 1321 BF, CSE 1321L 04, ECON 1000 BAC,
TCOM 2010 04. PHYS 2211 §55 as pacing reference only — Chris's §54 has no
syllabus and no assigned instructor (`SYSTEM_FLAGS.md` #57). ENGR 1000 has only a
Summer W01 reference.

---

## Part 0 — What a Block Is

A block was undefined until now, which made every hour count in this spec
unverifiable. Definition, matched to Chris's real class periods (PHYS lecture is
55 minutes; ECON is 55; TCOM is 80):

> **One block = 50 minutes of single-subject focused work, then a 10-minute
> break away from the screen.**

Every block carries four things, written before it starts:

1. **Entry condition** — what must already be read or done. A block with an
   unmet entry condition is not started; the reading block is run first.
2. **One named outcome** — what this block is for, in a sentence.
3. **One artifact** — a file, a photo of handwritten work, a code file, a
   recorded score. If a block produces no artifact, it did not happen.
4. **Exit condition** — what counts as done, decided in advance so "I feel good
   with it" is never the test.

Rules that make the count honest:

- **A block is not divisible.** Twenty-five minutes of physics and twenty-five
  of email is zero blocks. Split attention is the exact condition that produced
  the Stage 3 denominator error on July 26.
- **Breaks are outside the count**, as is setup, tool fiddling, and file
  admin.
- **A block interrupted past ~10 minutes is a half block** and is recorded as
  such. Do not round up.
- **Maximum four consecutive blocks** before a real break of 30+ minutes.

At 32 blocks, that is about **27 hours of focused work plus breaks** across six
days — roughly 4.5 hours of real work per day, which is where the "is this
sustainable" question actually gets answered.

## Part 0.5 — Physics Is Handwritten. Non-Negotiable.

Chris's call, adopted here: **all physics work is done by hand — paper or iPad
digital writing.** The reasoning is not preference, it is that the work itself is
spatial and symbolic. A free-body diagram, a vector decomposition, a motion
graph, an axis choice, and a sign convention cannot be typed. Typing physics
converts a spatial problem into a transcription task and removes the exact step
being trained.

**The evidence format changes accordingly.** A physics block's artifact is a
photo or PDF export of the handwritten page, filed with the drill it belongs to.
That gives three things at once:

- diagram, work, and units are visible, so a miss can be classified by component
  rather than scored as one aggregate wrong answer;
- the page is Chris's own class notes in his own structure, not a transcription
  of someone else's; and
- the artifact is already in the shape the real course wants, since WebAssign
  entry is the last step of hand-worked problems, not a substitute for them.

**On the tool-learning stance, recorded because it is correct:** Chris's approach
is to use the iPad and let the workflow settle through use rather than optimizing
the setup first. That is the same principle the July 24 source batch states for
systems — *start simple, add complexity only to address an observed limitation.*
Do not build an iPad note-taking standard in advance. Run the week, keep whatever
Chris actually did twice, and write it down after it exists.

**Python is the opposite** and stays typed — the artifact is a runnable `.py`
file, because the skill being trained is producing working code. Pseudocode
before code may be handwritten; the code itself is not.

---

## Part 1 — The Honest Number

### Registered load: 13 credits

| Course | Credits | Scheduled contact |
|---|---:|---|
| PHYS 2211 §54 | 3 | MWF 9:10–10:05 lecture + F 11:30–12:25 breakout = **4 hrs** |
| CSE 1321 BF | 3 | ~2.5 hrs |
| CSE 1321L 04 | 1 | lab, ~2.75 hrs |
| TCOM 2010 04 | 3 | TTh 9:35–10:55 = **2.7 hrs** |
| ECON 1000 BAC | 3 | TTh 8:00–8:55 = **1.8 hrs** |
| ENGR 1000 BWD | 1 | fully online, no meeting |
| **Total** | **13** | **~14 hours in class** |

### Out-of-class expectation

The standard university ratio is 2–3 hours of outside work per credit hour.
At 13 credits that is **26–39 hours**, on top of ~14 contact hours.

> ### A realistic week is **40–53 hours**.

### What our current plan simulates

`weekly-plan-2026-07-27-to-2026-08-02.md` schedules **20 blocks of about one
hour**. That is **roughly 40–50% of a real week**, and the plan currently
describes itself as "one honest simulation of the registered Fall course mix."

**That description is wrong and should be corrected.** Twenty hours is a
legitimate ramp — it is not the load. Two honest options:

- **Option A — keep 20 blocks, relabel.** Call it a 40% ramp. Low risk, but it
  will not tell Chris whether he can carry a real week.
- **Option B — run one deliberately heavy week.** 30–35 blocks, ~60–70% of real
  load, which is the most that fits around Ben Care and family without becoming
  a fiction. This is the only version that produces the answer Chris actually
  wants, which is *"can I do this?"*

**Recommendation: Option B, once.** One hard week now, six weeks before classes,
with a full stop if it collides with family. The purpose of a simulation is to
find the ceiling while the cost of finding it is zero.

---

## Part 2 — Where Chris Actually Sits Against the Real Calendar

This is the most useful thing the syllabi gave us.

### Physics — Chris is ~5 weeks ahead

| Course week | Date | Content | Chris's stage |
|---|---|---|---|
| 1 | Aug 24–28 | Ch 1 Measurement, Ch 2 Motion 1D | Stages 1–2, provisionally cleared |
| 2 | Sep 2 | Ch 3 Vectors | **Stage 3 — CLOSED July 16** |
| 2–3 | **Sep 4, Sep 9** | **Ch 4 Motion in 2D / Projectile** | **Stage 4 — ACTIVE** |
| 3–5 | Sep 11–23 | Ch 5 Force, Newton's Laws, FBD, Friction | Stage 5 — ready, not active |
| 5 | **Sep 25** | **EXAM 1** | — |

**The calibration that matters: the real course spends two lecture days on all of
Chapter 4.** F Sep 4 and W Sep 9. Then it moves to Ch 5.

Our Stage 4 plan allocates a full seven-day deep dive to the same chapter. That
is not wrong for building durable understanding — but it means **our pace is
roughly 3× slower than the course's**, and Chris should know that number. When
the semester starts, one chapter per week with a homework set and a quiz is the
actual metronome.

### Python — Chris is ~9 weeks ahead

| Course week | Module | Chris's stage |
|---|---|---|
| 1 | Module 0 — algorithms, decomposition, abstraction | covered |
| 2 (Quiz 1, Sep 6) | Module 1 — I/O, data types, operators, booleans | covered |
| ~4–5 | Module 2 — Selection (branching) | covered |
| **6 (Sep 28–Oct 4, Quiz 3)** | **Module 2 — Repetition (loops)** | **Stage 3 — CLOSED July 26** |
| ~7–8 | **Module 3 — Defining functions, parameters, arguments** | **Stage 4 — ACTIVE** |
| ~9 | Module 4 — Python Libraries | Stage 4b — correctly split already |
| later | 5.1 tuples/lists · 5.2 dicts, search/sort · 6 OOP | not built |

Chris closed the loops gate today. **The course does not reach loops until the
week of September 28.** Our Stage 4/4b split already matches Modules 3 and 4
exactly — that decision was made before we read this schedule and it holds.

**Implication for the simulation:** Chris cannot simulate "this week's real
coursework," because he is far ahead of it. What he can simulate is **the weekly
rhythm and volume** at his own position on the path. That is the correct target
and it is what the plan below does.

---

## Part 3 — The Real Weekly Rhythm

From the syllabi, the recurring obligations that define a week:

**Physics (§55 reference):**
- WebAssign homework set assigned weekly, **due the following Monday 11:59 pm**
- 15-minute quiz released **Friday**, due **Sunday 11:59 pm**, lockdown browser
- In-class + breakout participation (graded, 10%)
- Grading: HW 10 · Quiz 5 · In-class/Recitation 10 · 3 Exams 45 · Final 30

**CSE 1321:**
- ~1 module per week; **10 quizzes** across the term, lowest dropped
- Grading: Quiz avg 25 · Test 1 25 · Test 2 25 · Final 25
- All quizzes and exams online through D2L, Respondus LockDown Browser
- Text: Think Python 2nd ed. (free FYE PDF)

**CSE 1321L (lab, separate grade):** Quiz avg 40 · Midterm 20 · Final 40

So one honest week is: **one chapter or module of new material, one problem set,
one timed closed-book quiz, per hard subject.** That is the unit to simulate.

---

## Part 4 — Proposed Simulation Week (Option B, 32 blocks)

Blocks are ~1 hour. Chris may move blocks between days.

| Lane | Blocks | Weekly outcome |
|---|---:|---|
| **Physics** | **10** | Finish Ch 4 §4.1–4.6 at course pace, one WebAssign-style problem set, one timed quiz |
| **Python** | **10** | Module 3 functions: lecture, lab, mini-project, one timed quiz |
| **CSE Lab** | **3** | Lab-style graded exercise under lab conditions |
| **TCOM** | **4** | Week 1–2 readings, memo/email structure analysis, ethics |
| **ECON** | **3** | Week 1 foundations + explain-back |
| **ENGR** | **2** | Orientation and source verification only |
| **Total** | **32** | ~65% of a real week |

### The two hard subjects, in detail

**Physics — 10 blocks, Ch 4 complete**
1. §4.1–4.2 x/y independence; write the four equations from memory
2. §4.3 angled launch; drill Problems 1–4
3. §4.4 uniform circular motion; drill 1–4
4. §4.5 tangential/radial split; drill 1–3
5. §4.6 relative velocity; drill 1–5
6. Mixed problem set — **12 problems, timed, WebAssign conditions**, no worked examples open
7. Error classification pass on every miss → each becomes a retest item
8. **Timed 15-minute closed-book quiz**, lockdown conditions (no notes, no restarts)
9. Cold Stage 4 gate attempt — all 13 mastery-checklist items
10. Reserve / gate retry on failed categories only

**Python — 10 blocks, Module 3 functions**
1. Cold baseline: define and call one function; explain parameter, argument, return
2. Think Python pp. 43–52, 83–87; closed-book explain-back
3. Function-writing lab A: `fahrenheit_to_celsius(f)`, `is_even(n)` — must return, not print
4. Function-writing lab B: `shout(message)`, calling code, three scope self-checks
5. Function Toolbox design pass — requirements and pseudocode first
6. Function Toolbox implementation, several inputs including one boundary case
7. Closed-book flashcard quiz: function, call, parameter, argument, local variable, scope, return
8. **Timed quiz, D2L conditions** — closed book, one attempt, no restarts
9. Cold read: unseen functions program, trace and predict, then one function built cold
10. Reserve / error-class retest

### What makes this a real simulation and not just more practice

Four conditions that do not exist in our current plan:

1. **Timed, closed-book, single-attempt quizzes in both hard subjects.** The real
   courses use lockdown browsers with one attempt per question. Untimed practice
   has never tested this.
2. **A problem set under homework conditions** — 12 problems, no worked examples
   open, submitted before the answer key is seen.
3. **A hard weekly deadline.** Physics homework is due Monday; the quiz closes
   Sunday. The simulation should honor a real cutoff, not slide.
4. **Volume.** 32 blocks in six days is the point. Twenty blocks does not
   generate the fatigue that a real week generates, and fatigue is the variable
   Chris is actually trying to measure.

---

## Part 5 — The Other Three Courses

Deliberately light. These are not the risk.

- **TCOM (4):** Open TC Ch 2.13 emails/memos, Ch 3 ethics, Week 2 audience
  analysis. One poor-vs-improved message comparison with sources closed. No AI
  drafting — reading and analysis only.
- **ECON (3):** OpenStax Ch 1 or CORE Unit 1. Closed-source explain-back of
  scarcity, incentives, opportunity cost, one real tradeoff.
- **ENGR (2):** Confirm section remains BWD, confirm only the Summer W01
  reference exists, record the questions the real syllabus must answer. Invent no
  Fall coursework. Restrictive no-AI boundary until the real policy exists.

---

## Part 6 — What This Cannot Simulate

Stated so no one over-reads the result:

- **No real deadlines exist.** Every cutoff here is self-imposed and can be
  ignored without consequence. That is the largest gap and it cannot be closed
  before August 24.
- **No lectures.** Four hours of physics contact time is replaced by reading. The
  real course front-loads delivery Chris will not have practiced receiving.
- **No instructor, no cohort, no office hours, no tutoring center.**
- **Section 54 is unconfirmed.** All physics pacing here derives from §55, a
  neighboring section with a different instructor. Treat exam dates and weights
  as indicative only.
- **Nothing here is graded**, so the measured variable is capacity and rhythm —
  not performance under real stakes.

## Success measures

| Measure | Target |
|---|---|
| Blocks completed of 32 | **27+ (85%)** |
| Physics timed quiz | completed under real conditions, score recorded honestly |
| Python timed quiz | completed under real conditions, score recorded honestly |
| Stage 4 physics gate | attempted cold; pass or a classified miss list — **both are valid outcomes** |
| Stage 4 Python gate | attempted cold; same standard |
| Every miss | converted to a named retest item |
| Optional `.ROOT` work displacing a block | **0** |
| Chris's own capacity verdict | one honest sentence: could this be sustained for 15 weeks? |

---

## Approval record

1. Chris approved **Option B: 32 blocks** on July 26.
2. Physics remains in textbook order; a calendar does not force mastery.
3. Timed closed-book checks remain in both hard subjects.
4. The later EDUCATION owner review released ENGR entirely until August 24.
   CASTLE reconciled the live allocation without rewriting this decision record.
