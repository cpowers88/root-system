---
type: contract
timeline: now
status: live
register: human-context
tags: [school, fall-2026, governance]
updated: 2026-09-09
---

# Semester Tutor Plan — making `.ROOT` teach the actual course

Audit and rebuild plan, 2026-09-09 (Week 3 of 15). Supersedes nothing yet; it names what
must change and in what order. `SYLLABUS_STATUS.md` remains the provenance index. This file
is the **defect record and the build order**.

---

## PART 1 — Syllabus audit: what the existing review missed

`SYLLABUS_STATUS.md` closed on 2026-08-24 with the verdict *"all five courses now have
exact-section sources."* Every claimed path was checked against the filesystem on
2026-09-09 and **every file exists.** The provenance claim is true.

It is also the wrong test. The index verifies **which section a document came from**. It
never verified **which semester the document describes**. Three of five failed that second
test, and one is not machine-readable at all.

### Verified defects

| # | Course | Defect | Consequence |
|---|---|---|---|
| **1** | **CSE 1321L 04 (86703)** | Course Calendar is a **Spring** calendar. Week 1 = "Jan 12–18"; "Jan 19: Martin Luther King Jr. Day"; "Mar 9–15 Spring Break"; midterm "Mar 2–8". **Zero Fall dates in the table.** | Every Lab and Assignment due date `.ROOT` derived from this file is wrong by roughly seven months. The lab is 40% homework + 10% lab exercises — the largest single date-driven grade block in the schedule. |
| **2** | **TCOM 2010 04 (85633)** | Course Calendar is a **Spring** calendar. "Ethics Analysis assignment due on Friday, **January 16th**"; "Business Email Draft due Tuesday, **January 20th**"; "Resume Extra Credit due Tuesday, January 20th". Eight January references, **zero** Fall-month references. | The Week-N / Tuesday-Thursday **sequence** is reusable. The **dates** are not. This is the direct cause of the entry in `NOW.md`: *"The workbook now reflects that list instead of the stale derived TCOM sequence."* Chris hand-supplied Week 3 on Sept 6 because the file could not. |
| **3** | **CSE 1321 BF (81262)** | Two contradictory grading tables printed back to back with no ruling: **(a)** Quiz 25 / Test 1 25 / Test 2 25 / Final 25, and **(b)** Quiz 40 / Midterm 20 / Final 40. Table (b) also names a "Midterm" the course does not have — the calendar has Test 1 and Test 2. Calendar row 15 reads "Module 8: Review (**May 4th, 2026**, Last Day of Classes)" inside an otherwise-correct Fall table. | Grade forecasting in `FallKSU.xlsx` is unreliable until one table is ruled binding. The weekly Fall dates *are* correct and usable; the grading block is not. |
| **4** | **ENGR 1000 BWD (80858)** | `Course Schedule FA26.pdf` is **one page containing one image and zero characters of extractable text.** A scan, not a document. | Every ENGR date in `.ROOT` — the fourteen weekly due dates, the Tuesday 11:59 PM rule, the ten assignments — was transcribed by eye from a picture and **nothing in the vault can re-verify it**. `SYLLABUS_STATUS.md` calls this course "evidence-complete." It is evidence-*captured*, unverifiable. |
| **5** | **PHYS 2211 54 (83722)** | Two different instructor addresses in one document: header says Farhan Islam / `fislam7@kennesaw.edu`; Email Policy says *"send your messages to `kpemasir@kennesaw.edu`."* Template residue, same class of error as the already-logged "Monday, Wednesday, and Thursday" header contradiction. | Minor, but it is the third proven internal contradiction in this file. Treat the prose as unreliable and the **dated schedule table** as the trustworthy part. |

### Clean — and the standard the others must be raised to

| Course | Why it works |
|---|---|
| **ECON 1000 BAC** | Full Fall 2026 calendar: `Week 3 / Tuesday / 9/8/26 / Practice Chapter 1-2-3`. Every session dated, every chapter named, both exams and all four quizzes placed. |
| **PHYS 2211 §54** | `Aug 26 → Motion in 1D → Serway 2.1–2.4`. Date → topic → **exact textbook sections**, all fifteen weeks, all four unit exams (Sep 21, Oct 12, Nov 4, Nov 18). |

Those two rows are the target shape: **date → topic → source location → assessment.**
A tutor that has that can teach. A tutor that has a syllabus PDF cannot.

### The rule this produces

> A syllabus is not accepted because it came from the right section. It is accepted when
> its calendar dates fall inside this term's academic calendar, its grading table is
> singular, and its text is machine-readable. Right section, wrong semester is the failure
> mode that survived four months of syllabus hunting.

Add that as a second gate in `SYLLABUS_STATUS.md`. It costs one grep and would have caught
three of five files in August.

---

## PART 2 — Obtain now: the two authoritative files

The exact Fall 2026 CSE schedules exist and are public. They are `.docx`, so they cannot be
pulled through this session's web tooling — Chris downloads them, and they become the
replacements for defects #1 and #3.

**Download both, save into `04-SCHOOL\01-CSE-Python\`:**

1. **CSE 1321L lab & assignment due dates (Fall 26, v2-1)**
   `https://campus.kennesaw.edu/colleges-departments/ccse/first-year-experience/cse1321l_python/schedules/cse1321l_schedule_fall_26_due_dates_v2-1.docx`

2. **CSE 1321 lecture tentative schedule (Fall 26, v40)**
   `https://campus.kennesaw.edu/colleges-departments/ccse/first-year-experience/cse1321_python/schedules/cse1321_tentative_schedule_fall26_v40.docx`

The same FYE pages carry the **official lecture slide decks, Modules 0–7** — the actual
material the exams are written from. Those are the primary teaching sources for CSE and
currently the vault does not have them; it has CS50P instead, which is a different course.

### Still owed, and only Chris can get them

| Need | Where | Why it cannot be inferred |
|---|---|---|
| TCOM 2010 real Fall dates | D2L (Diamond) | The syllabus is a Spring document. Sequence survives, dates do not. |
| CSE 1321 grading ruling | One email to the instructor | Two printed tables; no document in existence resolves them. |
| ENGR 1000 BWD schedule as text | D2L — re-download, or photograph and transcribe | Current copy is an image. |

---

## PART 3 — Diagnosis: why `.ROOT` is not already the tutor

**The vault is not short of material.** PHYSICS alone holds 18 stage files, ~60 concept
pages, ~45 equation pages, ~38 drills, ~22 worked examples, per-stage flashcards and
per-stage common-error pages. PYTHON holds stages, drills, glossary, code patterns,
mini-projects, a source-page map. That is a real tutor's worth of content.

**The vault is short of one thing: a single owner of "what am I studying this week."**

Fifteen files currently make a dated claim about the semester:

```
04-SCHOOL\SEMESTER_MAP.md                     40,875 b
04-SCHOOL\semester-workload-plan.md           37,512 b
04-SCHOOL\semester-reading-plan.md            22,083 b
04-SCHOOL\week-zero-plan.md                   15,222 b
04-SCHOOL\weekly-study-schedule.md            13,105 b
04-SCHOOL\weekly-study-schedule.html          44,904 b
04-SCHOOL\FallKSU.xlsx                        62,068 b
PHYSICS\wiki\semester-pathway.md              24,906 b
PHYSICS\wiki\learning-path.md                 25,172 b
PHYSICS\wiki\phys-2211-17-week-math-first-plan.md
PHYSICS\wiki\syllabus-coverage-ledger.md
PHYSICS\wiki\pacing-trigger-map.md
PYTHON\wiki\cse-1321-17-week-mastery-plan.md  26,483 b
PYTHON\wiki\syllabus-alignment.md             32,753 b
EDUCATION\wiki\pre-semester-coverage-plan.md  13,716 b
```

Roughly 400 KB of planning. **Every one of them was authored before August 24** — before a
single class met — and three of them were built on syllabi that turned out to describe the
previous spring. A "17-week plan" written in July cannot know that Islam moves Unit Exam 1
to Sep 21, that ENGR closes everything at Tuesday 11:59 PM, or that TCOM's real sequence
only became visible in class.

This is why the system asked Chris for the Week 3 list instead of telling him.

**In construction terms:** there are fifteen sets of drawings on the job and no one has
stamped a set *Issued for Construction*. The framer works off one, the electrician off
another, and the inspector fails the rough-in. The fix was never a sixteenth set. It is one
stamped set, a revision block, and everything else marked *reference only*.

---

## PART 4 — The fix: one file per course

**Recommendation: retire the semester planning layer and build a `COURSE_SPINE.md` per
course. Five files. Nothing else may state a date.**

Each spine is a table with one row per graded week, and every row points at teaching
material that already exists in the wiki. Nothing is generated that a stage file already
holds — the spine is the *index*, not the content.

```markdown
## PHYS 2211 §54 — Spine
| Wk | Dates | Class topic | Source | Wiki | Proof | Assessment |
|----|-------|-------------|--------|------|-------|------------|
| 4 | Sep 14,16,18 | Gravity & FBD · Friction · Uniform circ. | Serway 5.5,5.7,5.8,6.1-6.2 | stages/stage-5-laws-of-motion, stages/stage-6-circular-motion | drills/fbd-drawing-drill, drills/friction-problems-drill | WebAssign HW wk4 |
| 5 | Sep 21 | **UNIT EXAM 1** | — | common-errors/stage-1..6 | cold set, no notes | Unit Exam 1 |
```

Seven columns. **`Proof` is the column that makes it a tutor and not a reading list** — it
names the drill that must be passed cold before the week is closed.

### Rules that keep it from rotting

1. **One owner.** The spine is the only file in `.ROOT` allowed to state a school date.
   Every other planning file gets `status: superseded` and a pointer, or moves to
   `99-ARCHIVE`. This is the existing one-live-truth rule, applied to the layer that broke it.
2. **Dates come only from a verified source.** A spine row cites the document it came from.
   A row with no citation is marked `NEED D2L` and stays unfilled. `.ROOT` never invents a
   date — that boundary is already in `README.md` and the spine is what finally enforces it.
3. **The spine points; it never copies.** Wiki pages stay the owner of teaching content. A
   spine row that restates physics is a bug.
4. **Weekly close writes one line.** Actual hours, what passed cold, what missed. Misses
   route to `04-SCHOOL\miss-log.md`, which already works and needs no change.

### What "the only source of knowledge outside class" can and cannot mean

Direct correction, because the goal as stated is not achievable and chasing it will cost
weeks: **`.ROOT` cannot be the only source.** WebAssign is where PHYS homework is graded.
Gradescope is where CSE labs are submitted. D2L is where every date actually lives, and the
syllabi just proved that local copies drift. Serway and *Think Python* are the texts the
exams are drawn from.

What `.ROOT` can be — and this is the version worth building — is **the only place you have
to think about.** One file per course tells you what this week covers, where the material
is, which drill proves you have it, and what is due. It routes you to WebAssign; it does
not replace it.

That distinction is also an academic-integrity boundary. CSE 1321/1321L and ENGR 1000
prohibit AI on submitted work outright. PHYS permits AI as a tutoring resource and forbids
it in submissions. TCOM allows editing your existing writing only. A system that positions
itself as *the source of answers* walks into those policies. A system that positions itself
as *the source of practice and proof* does not.

---

## PART 5 — Build order

Three passes. Verify each before the next. The whole thing is roughly one working session,
and pass 1 alone changes how next week runs.

### Pass 1 — the two courses whose data is already clean (today, ~90 min)

Build `PHYS_SPINE.md` and `ECON_SPINE.md`. Both syllabi are verified clean, both carry
date → topic → source, and PHYSICS has 18 stages and 38 drills sitting ready to be indexed.
Nothing needs to be obtained first.

**These two are also the semester's real risk.** PHYS is calculus-based mechanics with four
unit exams and the lowest dropped — Unit Exam 1 is **Sep 21, twelve days out**, covering
Serway 1–6, and the vault's `work-energy-25min-review.md` shows Week 3 was spent on Chapter
7 material. That gap is the highest-value thing on this list.

*Success test:* a cold session, told only "PHYS, ninety minutes," opens the spine, lands on
Week 4, and runs the right drill without being told where anything is.

### Pass 2 — CSE, once the two downloads land (~45 min)

Build `CSE_SPINE.md` from the two `.docx` schedules, covering lecture and lab in one table.
Pull the official Module 0–7 slide decks into `PYTHON\raw\`. Mark the grading ruling
`NEED INSTRUCTOR` until the email is answered.

*Also settles a live question:* the lecture calendar puts Modules 2 and 3 (selection, loops,
functions) across Weeks 3–8, and Test 1 on **Oct 5**. PYTHON's stages currently run to
Stage 3 conditionals. The spine will show exactly how far ahead of the wiki the course is.

### Pass 3 — TCOM and ENGR, after D2L (~45 min)

These two are blocked on documents only Chris can produce. Build the spines with the
sequence known and dates left as `NEED D2L`, so the blanks are visible instead of guessed.

### Then the retirement — and it is the part that actually fixes the system

Archive or mark superseded: `semester-workload-plan.md`, `semester-reading-plan.md`,
`week-zero-plan.md`, `weekly-study-schedule.md` + `.html`, `pre-semester-coverage-plan.md`,
both 17-week plans. Reduce `SEMESTER_MAP.md` to the syllabus-fact record it is good at and
strip its dated scheduling. `FallKSU.xlsx` keeps grades and submission status — the two
things a markdown table is genuinely worse at — and stops carrying a derived schedule.

**Skipping this step is how the problem comes back.** Five new files beside fifteen old ones
is sixteen owners, not one.

---

## Scope flags

Three things sit next to this work and are **not** part of it. Named here so they stay named.

- **Rebuilding the wiki content.** PHYSICS and PYTHON already hold enough to teach from. The
  spine indexes what exists. Writing new stage pages before a single spine is used is the
  same pre-semester planning move that produced the fifteen files.
- **ROOT2.** The build guide in this project is a rewrite of the whole vault. It is the right
  long-term call and the wrong thing to start in Week 3 with Unit Exam 1 twelve days out. The
  spine is compatible with it — a spine is exactly what a hub's `notes/path.md` becomes.
- **CASTLE.** Syllabi and course schedules do not belong in CASTLE, and loading them there
  would repeat the two-owners error this plan exists to fix. CASTLE is the strategy and
  decision lane; course sources belong to `04-SCHOOL` and the subject wikis, which is what
  `WHERE_IT_GOES.md` already says. `NOW.md` currently reads *"CASTLE remains out unless a
  specific system decision appears."* That is correct — leave it out.

---

## Decision required

Pass 1 needs no inputs and can start immediately. Passes 2 and 3 need the two downloads and
a D2L pull. The retirement step needs approval because it archives files.

---

## RESOLUTION LOG — 2026-09-09, same day

Chris routed the missing documents through `77-INBOX` the same session. Status of the five
defects and the build:

| # | Defect | Status |
|---|---|---|
| 1 | CSE 1321L Spring calendar | **Confirmed at source, not a bad capture.** The official Simple Syllabus PDF also carries the Spring calendar — Feb/Mar/Apr dominant, zero Fall months. Lab dates must come from the FYE `.docx` or Gradescope. Chris is retrieving them. **Still open.** |
| 2 | TCOM Spring calendar | **CLOSED.** `TCOMassignments.md` is the live Fall calendar, Aug 25 → Dec 3, every session dated. `TCOM_SPINE.md` built from it. |
| 3 | CSE 1321 contradictory grading tables | **CLOSED — not a contradiction.** The PDF carries the column headers the Markdown capture dropped: one table is *Spring and Fall Semesters*, the other *Summer Semester*. **Fall governs: Quiz 25 / Test 1 25 / Test 2 25 / Final 25.** No instructor email needed. |
| 4 | ENGR scanned-image schedule | **CLOSED, and it had cost something.** The D2L export supplies all dates machine-readably — **and proves the hand-read transcription was wrong.** Student Engagement Assignment was recorded as Nov 3; D2L says **Nov 17**. That is the one item requiring physical event attendance. |
| 5 | PHYS duplicate instructor email | Open, cosmetic. Treat the dated schedule table as authoritative and the prose as unreliable. |

### The generalizable lesson, and it is worth more than the five fixes

**The Markdown syllabus captures lose table structure.** Defect #3 was never a real contradiction
— it was two labeled columns flattened into two unlabeled tables. Grading weights, course
calendars, and assignment schedules all live in tables, so the `.md` captures in `raw\syllabi\`
are lossy for exactly the facts that matter most.

> **Rule: for any table, the PDF is the authority. Use the Markdown only for prose search.**

Add that beside the term-check gate in `SYLLABUS_STATUS.md`.

### Built this session

```
04-SCHOOL\01-CSE-Python\CSE_SPINE.md    lecture complete; lab structure known, dates NEED
04-SCHOOL\02-Physics I\PHYS_SPINE.md    15 weeks + WebAssign windows + Exam 1 cold set
04-SCHOOL\03-TCOM\TCOM_SPINE.md         every session Aug 25 - Dec 3
04-SCHOOL\04-ECON\ECON_SPINE.md         every quiz and exam window
04-SCHOOL\05-ENGR\ENGR_SPINE.md         all 15 Tuesday deadlines
04-SCHOOL\RETIRE_SUPERSEDED.ps1         dry-run by default; -Execute to move
```

Passes 1, 2 and 3 are complete except the CSE lab dates. The build order in PART 5 was written
expecting three sessions; the inbox collapsed it into one.

### Teaching gaps the spines exposed

1. **No OOP stage in the PYTHON hub.** CSE Module 6 runs Weeks 12–13, carries Quizzes 8 and 9,
   and is on the final. Thirteen stage files, none covering classes and objects. Nine weeks of
   runway — build it deliberately.
2. **Four PHYSICS stages are off-syllabus** — gravitation, fluids, superposition, relativity.
   ~30% of stage material aimed at chapters this course never reaches, with nothing marking it so.
3. **Five PYTHON stages are off-syllabus** — files/errors, program design, Think Python readiness,
   automation bridge, application thinking. Valuable for the business track; not exam material.

### Still owed

| Item | Owner |
|---|---|
| CSE 1321L lab & assignment dates, lab midterm, lab final | Chris — after class |
| CSE 1321 lecture final exam date | KSU finals schedule |
| PHYS final exam date | D2L |
| Confirm ENGR Sep 8 quiz + Time Management were submitted | **D2L, now — window closed, no late work** |
| Is special relativity taught in PHYS this term? | Email Islam |
| Confirm ECON Ch 14 is on the final | D2L |
