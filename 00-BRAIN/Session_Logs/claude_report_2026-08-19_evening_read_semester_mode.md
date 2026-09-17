---
type: report
timeline: log
status: complete
tags: [governance, school, fall-2026, learning]
created: 2026-08-19
surface: claude-code
---

# Evening Read → Semester Mode, and the Week-1 Reading Question

### Session report · Wednesday, August 19, 2026 (evening) · Claude Code · Operator/CASTLE

**Chris's instruction:** load into CASTLE, rework the evening read to reflect the school
semester, pause the technology side unless it ties to school — and answer what he needs to
read to be ready for week 1, start fast, and hold pace all term.

Governance change, Chris-directed. Under `AGENT.md` § System Evolution Authority that path
is impact review → approval → implementation → validation → named check date; the
repeated-friction evidence threshold does not apply. Chris's approval is the instruction
itself.

---

## 1. What shipped

| # | Change | File |
|---:|---|---|
| 1 | Technology block paused for the semester; three-part tie test defined | `00-BRAIN\EVENING_READING_INSTRUCTIONS.md` |
| 2 | Course rotation rebuilt on the registrar's timetable | same |
| 3 | Format contract updated — one block or two, never a stub | same |
| 4 | Generator prompt updated; output sanitiser hardened | `00-BRAIN\scripts\run_evening_reading.ps1` |
| 5 | Week-1 reading for all five courses + the three pace mechanisms | `04-SCHOOL\semester-workload-plan.md` §2 |
| 6 | Tonight's brief corrected twice — format, then assignment | `EVENING_READING.md` |
| 7 | Decision record | `CASTLE\wiki\log.md`, `DAILY_2026-08-19.md`, `NOW.md` |

---

## 2. The pause, exactly as written

**Default brief is now one block: School.** The Technology block returns only when **all
three** are true:

1. The reading serves a **named course deliverable, exam, or module** — not general
   interest, not "business-relevant," not continuity with last night's source.
2. That item is **due within 7 days**, or is the next unrun item in the owning course's
   queue.
3. The **FOCUS line names the course and the deliverable.** If it cannot, the tie does not
   exist.

**When the test fails, the heading is omitted.** No stub, no apology, no "paused" note —
the brief is the assignment, not a status page. This turned out to matter within the hour
(§5).

**Named as not qualifying:** `AI_engineering.pdf`, agent frameworks, MCP, REVENUE_LAB
sources. Their queue positions are **held, not lost** — the AIAS Ch. 7 position survives in
`raw-source-coverage.md` and resumes when the mode lifts.

**Named as qualifying:** Word/document-design tooling before TCOM's Document Redesign
(week 6), a FRED or spreadsheet method before an ECON data discussion, a calculator or
plotting technique before a PHYS set. A Python/CSE reading is **already the School block** —
the rule forbids running one lane twice by relabelling it.

**Freed time is capped, not open.** School cap rises 20 → **30 minutes in a 🟡/🔴 week**,
stays 20 in a 🟢 week. A quiet night does not become a licence to read further ahead than
the one-week lead.

**Ends Dec 9, 2026, or when Chris lifts it.** Explicitly not retired because a week looks
light.

---

## 3. The rotation was backwards, and the fix is load-derived

The July table ran **TCOM 2 / ECON 2 / Python 1 / Physics 1**. Set before the buffer was
measured and before the registrar's real timetable was reconciled into
`semester-workload-plan.md` §1.

**Measured load, outside class:** PHYS ~37% · CSE ~28% · TCOM ~22% · ECON ~9%.
The old table gave the 37% course one night and the 9% course two.

**New table, live from Sun Aug 23:**

| Night | Lane | The real reason |
|---|---|---|
| Sunday | **PHYS** | Mon 9:10 lecture — and **three of four unit exams plus both CSE tests are Mondays** |
| Monday | **TCOM** | Tue 9:35 class. Tuesday runs ECON → TCOM → 17:45 lab, 11.5 h on campus |
| Tuesday | **CSE** | Wed 16:10 lecture and the current module |
| Wednesday | **ECON** | Thu 8:00 — earliest class of the week, easiest to arrive at unread |
| Thursday | **PHYS** | Fri lecture **and the recitation worksheet, 10% of the grade, produced in that room** |
| Friday | **CSE** | **CSE quizzes close Sunday.** Last night that deadline is cheap |
| Saturday | **TCOM** | Tuesday's deliverable and, from week 8, the report checkpoint |

**PHYS 2 · TCOM 2 · CSE 2 · ECON 1.**

**Why PHYS specifically moved to two nights:** its pre-class reading is *graded*. WebAssign
and D2L reading quizzes plus unannounced in-class quizzes
(`PHYSICS\wiki\semester-pathway.md` §5). It is the only course of the five where arriving
unread is directly scorable.

**Rebalance trigger is buffer-based, not dated.** PHYS and CSE hold +2 weeks as of
2026-08-18. If either drops below +1 week it takes a third night from ECON. If the TCOM
report checkpoints slip, Saturday becomes a second TCOM night in weeks 8–11. The pre-semester
table is retained and scoped to "through Sat Aug 23" rather than deleted.

**ENGR 1000** takes Saturday the week its syllabus lands — absent until then, not silently
folded in.

---

## 4. The reading answer

`semester-workload-plan.md` §3's week-1 row listed what is **graded**. Nothing anywhere said
what to **read**. That gap is now closed in §2 of that page.

### Run-in, Aug 19–23 — three readings, ~3 hours

| # | Read | By | Why |
|---:|---|---|---|
| 1 | **TCOM §2.13 Emails & Memos** | Aug 23 | Instructor email goes out **Tue Aug 25**; Business Email is 15% of the course |
| 2 | **TCOM Ch 3 Ethics** + one case from `raw\Linked-Resources\` | Aug 26 | **Ethics Analysis is graded, due Fri Aug 28**, and its format appears nowhere in the syllabus |
| 3 | **ECON — OpenStax Ch 1** | Aug 23 | Acknowledged **substitute**. Mathews & Patrono is D2L-locked; re-anchor Aug 24 |

**No PHYS or CSE run-in reading assigned.** Both are +2 ahead; re-reading covered ground
buys nothing, and PHYS's slot in week 1 is week *2*'s material under the one-week-ahead rule.

**⛔ Never `2e_Word\`** for a TCOM chapter — its Ch 3 is *Library and Internet Research*, not
*Ethics*. That defect was live in two `.ROOT` study pages until this morning and had already
reproduced in Chris's failed reps.

### The reading that decides week 1 and is not a textbook

Five courses, five late policies, five naming conventions, five AI policies — and **week 1
grades three quizzes on exactly this**:

- **TCOM policies + file naming** → `EDUCATION\wiki\courses\tcom-2010\concepts\course-policies-and-file-naming.md`. Two graded quizzes, **no late credit ever**. Today's cold diagnostic: **~3 of 8**, and both confident misses were **PHYS rules imported into TCOM**.
- **CSE 1321 + 1321L policy sections** → `PYTHON\raw\syllabi\`. Two more graded quizzes. Note the two conflicting grade tables.
- **PHYS §54 syllabus** → two lines only: the **WebAssign extension rule** (request *before* the deadline, or a miss is a flat zero) and the **Day One Access opt-out, Fri Aug 28 11:45 PM**.

**This is the highest-value hour in the run-in.** The cross-course contamination error class
is already measured, and it is the one week-1 failure mode that costs points on material
Chris actually knows.

### Week 1 proper, Aug 24–30

| Course | Read | By |
|---|---|---|
| **PHYS** | Serway **3.1–3.4**, **4.1–4.2, 4.4–4.5** — *week 2's* material (`raw\textbook\physic(full_book).pdf`, PDF runs **+30 pages** ahead of printed) | across the week |
| **TCOM** | Finish Ch 3 Ethics; then §5.2 Audience Analysis + §2.12 Oral Presentations | Ch 3 by Aug 26 |
| **CSE** | *Think Python* Ch 1 + Ch 4 "A Development Plan"; then Module 1 spine (Ch 1, Ch 2, Ch 5 "Keyboard Input") | Ch 1/4 Aug 24; Module 1 Aug 30 — **Quiz 1 is Sun Sep 6** |
| **ECON** | **Mathews & Patrono Ch 1** the moment D2L opens; check numbering against the OpenStax mapping | Aug 27 — **quiz Ch 1-2-3 Tue Sep 8** |
| **ENGR** | ⛔ **The syllabus is the reading.** It does not exist | **Aug 24, D2L** — flag #57 |

### Holding pace — nothing new was built

Three mechanisms already exist and only have to run:

1. **The rotation above** — the daily instrument.
2. **The PHYS one-week-ahead rule.** Its payoff is that every pre-exam week converts to pure
   retrieval instead of first-pass learning. **Move the two red sweeps forward** — Exam 2's to
   Oct 1–2 (before CSE Test 1 eats the weekend), Exam 4's into week 11 — or they land on top
   of CSE Test 1 and on week 12.
3. **TCOM's four ungraded report checkpoints** — Oct 13, Oct 20, Oct 27, Nov 3. The only thing
   between 35% of that grade and the worst week of the semester. **Being ungraded is precisely
   why they get skipped.**

---

## 5. Two defects found in this session's own output

### 5a. The 5 p.m. job leaked commentary into the published brief

The scheduled run fired **mid-edit**. It read the new instructions correctly, applied
semester mode, and omitted the Technology block — then emitted a stray ` ``` ` fence followed
by a paragraph *explaining why* the block was omitted. § Semester mode forbids exactly that,
and § Format forbids commentary.

**Root cause:** `run_evening_reading.ps1` stripped a fence only when it sat at the very end
of the content (`(?s)\r?\n```\s*$`). Here content followed the fence, so both survived into
`EVENING_READING.md`.

**Fix:** cut from the **first bare fence onward** — the output contract never contains a code
fence, so anything at or after one is wrapper or trailing prose. Verified against the exact
malformed shape (validator passes, correct body preserved); `ParseFile` clean.

**Worth naming:** the model half of the pipeline followed the new rule on its first exposure.
The failure was the sanitiser being narrower than the contract it enforces.

### 5b. Tonight's assignment was wrong, and I let it stand once before correcting it

The job assigned **ECON Ch 1**, reasoning that TCOM "already ran its session today." I
accepted that in my first pass as a defensible override-3 pick.

**It was not.** Override 3 states an explicit order — **TCOM first, then ECON** — and the test
is whether the *reading* has run, not whether the course was touched. Today's TCOM block was a
**policy-retrieval drill**, not §2.13. Independently, `NOW.md` names §2.13 as the reading
block in plain text. Two sources agreed and I deferred to the generated output over both.

**Corrected:** tonight's brief is **TCOM §2.13 Emails & Memos**, capped at 20 minutes,
stopping before Ch 3 Ethics (Saturday's block). ECON Ch 1 moves to a later run-in night;
four remain before Aug 23, so both still fit.

**The generalisable lesson, offered not adopted:** an override that names an *order* needs to
name its *completion test* too, or a session will substitute a plausible one. This is the same
shape as flag #94 — a rule whose trigger is missing is a rule that does not fire. If it
recurs, it belongs in the instruction file as an explicit clause.

---

## 6. Validation

- `root_health.py` → **PASS WITH DEBT**, 0 blockers, 1 pre-existing wiki-link review item
  against an expected 697. Unchanged baseline; nothing in this session moved it.
- `run_evening_reading.ps1` → `Parser::ParseFile` clean; sanitiser tested against the real
  malformed output.
- `EVENING_READING.md` → satisfies the contract's validator (frontmatter, READ, FOCUS, STOP),
  one block, no Technology heading.

---

## 7. Open, and check moments

| # | Item | When |
|---:|---|---|
| 1 | **First live night of the semester rotation — should assign PHYS** | **Sun Aug 23** |
| 2 | Semester mode reviewed against a real week | Aug 23 pre-semester review, then week 1 close |
| 3 | Whether override 3's completion test needs writing into the instruction file | If it recurs |
| 4 | ENGR enters the rotation and `semester-workload-plan.md` §2 | The day its syllabus lands (flag #57, check Fri Aug 21) |
| 5 | ECON's real Ch 1 replaces the OpenStax substitute | Aug 24, D2L |

**Not done, deliberately:** no new page was created for the week-1 reading. It went into
`semester-workload-plan.md` §2, where §7 already tells Chris to read the week's row on Sunday —
`CASTLE\OPERATIONS.md` Standing Rule 5, depth before sprawl.

---

*Files changed: `00-BRAIN\EVENING_READING_INSTRUCTIONS.md` · `00-BRAIN\scripts\run_evening_reading.ps1` ·
`04-SCHOOL\semester-workload-plan.md` · `EVENING_READING.md` · `NOW.md` ·
`00-BRAIN\CASTLE\wiki\log.md` · `00-BRAIN\Session_Logs\DAILY_2026-08-19.md`*
