---
type: report
timeline: now
status: active
tags: [governance, school, education, review, fall-2026, skills]
---

# Teaching-Readiness Audit — can `.ROOT` carry Chris to five A's?

### Scope: the full teaching and guidance layer against the 90%-in-five-courses target
### Surface: Claude Code · Hat: none (CASTLE audit) · Chris-directed, 2026-08-22 evening
### Status: **audit delivered, then two changes implemented on Chris's rulings in the same session.** `root_health.py` PASS.

---

## 1. Verdict

**The preparation layer is elite. The execution-feedback layer is unproven and structurally
thin — and it is the one that decides A versus B.** A world-class map, a barely-tested engine.

| Layer | Score | Basis |
|---|:--:|---|
| Requirements & dates | 9.5/10 | 4 exact syllabi + the official CCSE departmental schedule; the week→date conversion is *proven by counting*, not derived; every date carries a confidence mark; four recycled-Spring-date defects caught |
| Grading-structure exploitation | 9.5/10 | Every drop rule quantified; ECON's top-2-of-4; CCSE tutoring = 5% free on both CSE finals, verified on disk |
| Collision & load mapping | 9/10 | Week 12 named eight weeks early; PHYS sweeps moved off two collisions; TCOM's four checkpoints identified as the 35% lever |
| Time model | 8/10 | Built from the real calendar, not blank time. 30.1 h vs ~28 h needed — three stacked unverified assumptions under it |
| Teaching method | 9/10 | Trigger-fired methods, retrieval matched to required performance, `passed (immediate)` vs `proven (durable)`, error classes with *re-aimed* reps |
| **Execution capture** | **4/10** | Risk 1 |
| **Leading indicators on exams** | **3/10** | Risk 2 |

Scores are judgment, not measurement.

## 2. What is genuinely top-1%

1. **The semester is known better than the syllabi know it.** `May 4th, 2026` found in a Fall
   syllabus; a missing CSE quiz week; two quizzes stacked on a wrong date; a 353-page web
   print-out separated from the 634-page textbook every page number refers to.
2. **The free-points inventory is real and dated** — 5% on both CSE finals for tutoring visits,
   ECON quizzes 1–2 as free diagnostics, five drop-rule buffers reserved for collision weeks
   rather than spent early.
3. **The AI audits its own teaching material.** `hat-performance-log.md` records four instances
   of the vault teaching a wrong rule and reproducing it in Chris's failed reps; the miss log now
   carries *check the aid before the learner* as a Sunday step.
4. **Integrity is encoded at the strictest reading.** TCOM §04's blanket AI prohibition, caught
   2026-08-19, retired two scheduled "Business Email draft" blocks that would have been
   plagiarism by the instructor's own definition.

## 3. The five risks that cost A's

### 🔴 Risk 1 — the instruments are excellent and their data entry is unowned

`FallKSU.xlsx` § GRADE TRACKER, `04-SCHOOL\miss-log.md` and the 91-row ASSIGNMENT TRACKER are
all read every Sunday. Every one depends on manual entry at the moment a score returns or a rep
fails — and `session-close` is far too heavy to run after a 45-minute WebAssign block. Friction
is highest exactly when load peaks. The miss log holds five rows, all from a low-load rehearsal
week; it has never been tested against a 26-hour week.

**→ Addressed this session. See §5.**

### 🔴 Risk 2 — nothing sees exam risk until an exam has already been graded

PHYS is 37% of the outside-class load and 75% exam-weighted. The GRADE TRACKER's own rule says
standing is meaningless below ~20% graded. Before Unit Exam 1 the only possible PHYS entries are
WebAssign (10), worksheet (10) and quizzes (5) — **none of which predict closed-book exam
performance.** Chris can read 100% on Sep 20 and take a B on Sep 21.

The only true leading indicator is the miss-log plus durability-check system, and both open PHYS
defects are *habit*, not knowledge:

- **Answer-completion not firing** — content arrives instantly when asked, never volunteered.
  Twice, five days apart.
- **Reasonableness check not firing** — Chris's own ruling: *"my form is 100% careless."*

With the equation sheet supplied at every exam, marks will be lost to unchecked substitution,
not to unknown formulas. The system diagnosed this correctly and gave it **no scheduled home** —
both habits close by "firing unprompted," which appears in no block in the weekly schedule.

**→ Partly addressed: the Saturday block is now a named lead/habit block. The standing
reasonableness habit still has no gate.**

### 🟠 Risk 3 — the two "+2 weeks ahead" claims were measured on different rulers

**→ Corrected this session on Chris's ruling. See §4.**

The sharper half: PYTHON is at Stage 4b, resume at C1, unrun since Aug 18, and Week 1 gave it
nothing. The Aug 1 timed closed-book quiz scored **2 pass / 1 partial / 3 miss, with two
regressions on items previously verified PASS** — direct evidence that this hub's explain-back
verdicts do not survive timed conditions. CSE is 25% quizzes plus three closed-book exams under
LockDown Browser. **The course with the most demonstrated durability failures was receiving the
least scheduled time.**

### 🟠 Risk 4 — three unverified assumptions sit under the load-bearing number

30.1 h/week clears ~28 h with ~4 h margin, and that margin depends on three new blocks that have
never run, a Tuesday the plan itself flags as optimistic, and a laptop carrying ~58% of study
time whose endurance was tested against 2h15 against a real 6-hour requirement. Seven collision
weeks; the worst needs ~26 h.

### 🟠 Risk 5 — two of five courses have no learner hub

The Sunday alignment gate names PHYSICS, PYTHON, EDUCATION — three hubs for five courses. ECON
and ENGR have course maps but no `current-position.md`: no proof frontier, no resume point, no
durability obligations. ECON's structure is unforgiving — two mandatory exams, 25% each, 60
minutes, one sitting, no logout, no make-up.

## 4. Change 1 — the lead, re-based (Chris's ruling)

Chris: *"the two week rule may be over extended right now… we all start Monday at zero and it is
impossible to be 2 weeks ahead."*

Correct, and the defect is worse than a stale number. **That lead was measured against lecture
delivery, and nothing is graded on lecture delivery.** Unit Exam 1 covers Ch 1–5 + 6.1–6.2
whether or not those chapters have been lectured. Against the assessment, PHYS holds Ch 1–3
proven, **Ch 4 open**, Ch 5 and 6.1–6.2 untouched — roughly 60% of Exam 1's scope, four weeks
out. A normal position, and not a lead in any unit.

**From Aug 24 the lead is a target, measured per course in the unit that course grades**
(Chris's ruling on the offered options):

| Course | Unit | Two-week gate |
|---|---|---|
| PHYS 2211 | **Proof** | Exam scope proven cold 14 days before the sitting. Exam 1 → **Sun Sep 7** |
| CSE 1321 / 1321L | **Proof** on the *Think Python* spine | Capped by D2L on course-shell material |
| TCOM 2010 | **Deliverable** | Report due Thu Nov 12, finishable Tue Nov 3 |
| ECON 1000 | **Reading** | Chapter read before its quiz window |
| ENGR 1000 | 🔴 TBD | Set in week 1 from the real BWD list |

**No conflict with the PHYS one-week-ahead rule** — that governs *lecture* priming for graded
reading quizzes; this governs *assessment* readiness. Different rulers.

**The build window is weeks 1–4 and it closes Sep 21.** §3's estimates leave ~16 · 12 · 14 · 13
surplus hours against a ~30 h schedule — **~55 h as a ceiling, 35–45 h realistically**, and
near zero from week 5. If the lead is not built by Sep 21, it does not get built.

**Files changed:** `04-SCHOOL\semester-workload-plan.md` (new § The lead; two other assertions
re-based) · `00-BRAIN\EVENING_READING_INSTRUCTIONS.md` (claim corrected; **rebalance trigger
re-based**) · `04-SCHOOL\week-zero-plan.md` · `CASTLE\OPERATIONS.md` (Reviews item **4d**, inside
item 4's existing budget, plus header date) · `weekly-plan-2026-08-24-to-2026-08-30.md` (second
weekly goal, per-course week-1 lead work, Saturday float converted to a named lead block,
`study-close` wired in, Aug 30 return gains 4d).

**The highest-value single fix in that set:** the evening-reading rebalance trigger read *"if
either falls below +1 week"* against a baseline never measured on a running course — **armed
against a phantom, so it could not have fired correctly.** Flag #94 / #103 shape: a rule whose
trigger does not exist.

**`check_at`: Sunday 2026-09-06** — the last Sunday where action on the Exam 1 gate is still
possible. First live read is the Aug 30 return.

## 5. Change 2 — the `study-close` skill (Chris's ruling, overriding the morning recommendation)

**This session's 10:35 entry recommended waiting for Week 1 evidence.** Chris ruled to build it
before Monday. Recorded as an override, not a convergence.

Canonical: `00-BRAIN\SKILLS\study-close\SKILL.md`. Mirrored to `.claude\skills` and
`.agents\skills` by `sync_shared_skills.py --sync`; validation **PASS**, 7 canonical skills.

Written against `writing-for-agents`. The design decisions that matter:

- **The fast path is the default.** Two gates — *anything come back graded? anything fail cold?*
  Both no, it closes on hours plus resume point. Most blocks end there. This is the single
  feature that decides whether it survives week 12.
- **It hands over the cell rather than writing the workbook.** `FallKSU.xlsx` carries live
  formulas and the conditional formatting that reddens overdue rows; an `openpyxl` round-trip
  drops that silently and Excel locks the file anyway. **Written into the skill so a future
  session does not "helpfully" automate it.**
- **The re-aim carries the demand** — named as *not a re-run*, per the miss log's own rule.
- **Check the aid before the learner fires before any miss is logged.**
- **Hours are captured**, closing the gap that `semester-workload-plan.md` §7.4 names — every
  hour figure in that file is an estimate with no capture path.
- Explicitly not the session close; step 5 says when to escalate, including the
  `hat-performance-log.md` row when AI taught in the block.

## 6. What was deliberately not done

- **PHYSICS wiki pages and `HAT_PHYSICS` were not touched.** Their one-week-ahead rule is a
  different and sound instrument. **`semester-pathway.md` was not read in full, so whether its
  phase structure conflicts with a Sep 7 proof gate is unverified.** Worth a check before Sunday.
- **No new flag filed.** Risks 2, 4 and 5 are findings for Chris's Aug 23 review, not `🔴`s that
  would bind a session on the rehearsal Saturday against the Aug 19 school-first ruling.
- **The standing reasonableness-check habit still has no scheduled gate.** Named, not fixed.
- **Flag #101, instance 13:** a read-only `for` loop running `ls` over three skill directories,
  denied for being a loop; completed with `Read`. Count only.
- **Pre-existing, not introduced here:** `sync_shared_skills.py` warns that
  `SKILLS\_staged\handoff\` carries an unvalidated `SKILL.md` needing disposition.

## 7. Verification

`sync_shared_skills.py --check` **PASS** (7 canonical, 2 mirrors) · `root_health.py` **PASS**
twice, before and after the governance edits — boot and governance, wiki links, frontmatter,
CASTLE freshness, shared skill mirrors, whitespace, 1,600-file text integrity, all clean.

**Instruction-file edits do not alter an already-loaded session** (`AGENT.md` File Safety 10).
The evening-reading and `OPERATIONS.md` changes need a fresh session to test.

---
*Owner: `04-SCHOOL` for the lead definition; `00-BRAIN\SKILLS` for the skill. Companion:
`claude_report_2026-08-22_castle_instruction_layer_review.md` and
`claude_report_2026-08-22_pre-semester_pathway_review.md` — three passes, same day, different
scopes.*
