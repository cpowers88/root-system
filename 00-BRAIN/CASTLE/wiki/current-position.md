---
type: map
timeline: now
status: active
tags: [baseline]
---

# Current Position — August 2026 Monthly Baseline

> **✅ FULL RECONCILIATION RUN 2026-08-21, closing flag #103's overdue pass.** Every row
> below was checked against its owner this session — not re-asserted. **Method, because it
> is the part worth repeating:** `git log --since=2026-07-19` over the owner files, then a
> read of every owner that actually moved. A row whose owner has not been touched since the
> July baseline keeps its July assessment **and now says so explicitly**, which is a
> different claim from "current" and was the ambiguity that made this file drift.
>
> **The headline finding is that eleven of thirteen rows genuinely did not move, and that
> is correct rather than neglectful.** Since Aug 1 the entire capacity of the system went
> into semester readiness — five syllabi, the workload/reading/schedule plans, the laptop
> build, and two `.ROOT` repairs. **The rows that should have moved did: both learner rows.**
> Recording eleven honest "unchanged, owner untouched since <date>" entries is the outcome
> of a reconciliation, not the absence of one.
>
> `castle_freshness.py` **PASS (2026-08-21)** — and it now actually runs from a session; it
> had been absent from the bulk gate's `ALLOWED_SCRIPTS` since it shipped Aug 19, so every
> direct invocation was denied. Fixed and measured the same session.

### Reconciled: August 21, 2026 (full pass) · previous full pass July 19, 2026
### Sources: NORTH_STAR.md, CURRENT_STRATEGY.md, owner current-position files, capability_development_goal.md, and active proof owners
### Cadence: monthly; current actions and temporary pauses live in .ROOT\NOW.md

## Fixed Baseline and Material Constraints

- **Destination:** October 8, 2031 remains the hard measurement date; the KSU BS in Industrial & Systems Engineering and $500K–$1M annual floor remain fixed.
- **School:** Degree Works (audited July 19) records 41 completed degree-applicable credits plus 13 registered Fall 2026 credits: 54 completed-or-in-progress credits applied toward the 121-credit degree, with a minimum of 67 additional credits needed. Fall classes begin August 24. Fixed deadlines and academic-integrity rules constrain the field.
- **Business:** Advisor-Builder is the active strategy hypothesis, not identity. Clients: zero.
- **Financial continuity:** additional income before Spring 2027 enrollment is a material constraint. REVENUE_LAB owns lane evidence and approvals.
- **Human governance:** Chris owns direction, timing, capacity, consequential decisions, and final quality.

## Capability and Proof Frontier

**Reconciliation basis column** added 2026-08-21: every row states the date its owner was
last actually touched, so "unchanged" is a measured claim rather than an assumption.

| Capability or track | CASTLE state | Proof frontier | Owner truth | Basis (2026-08-21) |
|---|---|---|---|---|
| **Course performance — all five, Fall 2026** | **NEW ROW 2026-08-21.** No graded work exists yet; classes begin Aug 24 | **The target is 90% in every course.** Standing is computed in `04-SCHOOL\FallKSU.xlsx` § GRADE TRACKER rows 40–45 and read at the Sunday return (`OPERATIONS.md` § Reviews, item 4). `WATCH` (< 90) earns a named corrective block; `ACTION` (< 87) reaches `MORNING_BRIEF` | `04-SCHOOL\FallKSU.xlsx` + `04-SCHOOL\miss-log.md` | **Created this session.** CASTLE tracked capability monthly and grades not at all; grades move weekly and are the actual target |
| Physics | building — Stage 4 open at circular-motion drills 1–4 | **Next rep: read §4.4 and §§6.1–6.2, then circular motion worked → faded → fresh cold transfer.** The 2026-08-21 cold attempt got the 5.0 m/s² magnitude but missed precise inward direction and the real force; Problems 1–2 are now lesson material and Problems 3–4 remain untouched cold. **Row 2 `proven (durable)` 2026-08-18. Row 3 ❌ MISSED AGAIN 2026-08-21**, reopened Sun Aug 23 – Mon Aug 24; error class *equation choice/units* | PHYSICS wiki current-position + math-readiness-path | ✅ **MOVED.** Owner rewritten 2026-08-21 (this morning, parallel session). Reconciled against it |
| Python | building — **Stage 4b** (Stage 4 closed 2026-07-29) | **C1** — `53`/`NameError` plus an independent `average(numbers)`; then import one standard-library module and wrap one library call in his own function | PYTHON wiki current-position | ✅ **VERIFIED.** Owner last moved 2026-07-29 (Stage 4 → 4b). Resume point C1 unchanged and unrun — PYTHON has had no rep since Aug 18 |
| SQL/SQLite | building — July weak link; guided two-table fixture verified July 21 | Independently query or extend the Bootcamp fixture; use verified tracker data when D2L populates | [[sql]] + [[ksu-academic-tracker]] + TECHNOLOGY owner | **Unchanged.** [[sql]] still `status: building`; its only touch since July was the Aug 12 path repoint. ⏰ **Its proof unblocks Aug 24** — the tracker's own next action is "enter verified course data when D2L populates" |
| Data visualization | building — first rep verified | A justified visual another person can trace and use for a decision | Technology Strategy + live proof vehicle | **Unchanged**, owner untouched since the July baseline |
| Field observation | building | First approved live observation; two tested live sessions move it to working | BUSINESS method + 05-BUSINESS\02-Field Notes | **Unchanged.** [[field-observation]] touched Aug 12 by the path repoint only; no live observation has occurred |
| Systems and flow thinking | building | Apply a flow or constraint model so it improves a real decision or finding | SYSTEMS wiki + coursework | **Unchanged**, owner untouched since the July baseline |
| Technology landscape | building | Problem-led category and Recommendation Ladder rep with constraints and rejection logic | Technology Strategy + TECHNOLOGY wiki | **Unchanged**, owner untouched since the July baseline |
| Recommendation Ladder | building | Evidence-based keep, simplify, buy, integrate, or build decision | Technology Strategy | **Unchanged**, owner untouched since the July baseline |
| Git/GitHub discipline | building | Understandable repository history and successful recovery or review | active repositories | ⬆ **Evidence accrued, state held.** Two-machine sync, the gitdir relocation (flag #102) and daily commit/push have run since Aug 16 without incident. Not promoted — the stated proof is *successful recovery or review*, and no recovery has been exercised. `verify_backup_restore.py` against the live D: backup is the Aug 23 test |
| Agentic delivery | working | Measure one assisted delivery end-to-end; time/quality evidence plus Chris explain-back moves it toward proven | approved projects + AI system | **Unchanged at `working`.** Substantial assisted delivery ran Aug 17–21, but none of it was *measured* end-to-end with time/quality evidence, which is the stated gate. Promotion still requires measurement plus Chris's explain-back |
| Technical writing and communication | building | Audience-specific finding or handoff that supports a decision or operation | TCOM/EDUCATION + real artifacts | **Unchanged, but its owner moved.** EDUCATION's `current-position` was rewritten Aug 19–21; TCOM course *setup* advanced, no writing artifact was produced. ⏰ First real evidence is the graded instructor email, **Tue Aug 25** |
| Advisor-Builder strategy | active hypothesis | Live workflow observation, qualified conversations, willingness to pay, and measured outcomes | CURRENT_STRATEGY.md + BUSINESS evidence | **Unchanged at hypothesis.** Clients still zero; no qualified conversation has occurred. Correctly dormant under the Aug 19 school-first ruling |
| Financial continuity | material constraint | Only approved evidence tests; no copied lane mechanics here | REVENUE_LAB + NOW.md | ✅ **Open conflict CLOSED this pass.** REVENUE_LAB's log has asked since 2026-07-24 whether Lane A is paused or active and named CASTLE as owner. **It is `parked`** — [[opportunity-queue]] OPP-20260714-02 already says so and `NOW.md` does not contradict it. The reconciliation had been done; **the answer was never returned to the hub that asked.** Returned this session. ⏰ Its `check_at` is **2026-08-23** |

**This table is the single home of cross-domain capability state (ruled by Chris
2026-08-19, closing flag #103's ownership loop).** [[skill-map]] holds horizons and
activation criteria only; `capability_development_goal.md` holds the weak-link *ranking*
only; neither carries state. Temporary sprint pauses and exact drill positions do not
change these monthly states. Any hub fact quoted here carries its as-of date and owner
link — cite stage numbers, never restate them bare (the 2026-07-19 rule: gates +
pointers, no copied state).

## Current Priority Routing

The cross-domain weak-link ranking is owned only by
`01-NORTH_STAR\Goals & Milestones\capability_development_goal.md`; CASTLE does
not reproduce it here. Chris ruled on 2026-08-19 that the Fall semester overlay
selects fixed school deadlines and current course proof before optional
capability, business, project, or system work. `04-SCHOOL\semester-workload-plan.md`
owns course load and collision truth, and `.ROOT\NOW.md` owns the immediate
action. The full capability-state reconciliation runs Friday Aug 21.

## Durable Advantages

- Construction workflow experience and credibility.
- Warm access through Heather's network without treating one market as identity.
- Strong spatial, numerical, verbal, and systems reasoning.
- A human-governed AI operating system and working agentic-delivery practice.
- Domain knowledge across BUSINESS, SYSTEMS, TECHNOLOGY, PYTHON, and PHYSICS.
- A shipped tracker and other bounded internal proof vehicles.
- A commitment to real use, explain-back, evidence, and maintainable systems.

## Owner Pointers

- Current action and temporary pauses: .ROOT\NOW.md
- School learner truth: 03-WIKIS\PYTHON\wiki\current-position.md and 03-WIKIS\PHYSICS\wiki\current-position.md
- Degree and registration evidence: 04-SCHOOL\Ellucian Degree Works Dashboard.md
- Monthly weak-link decision: 01-NORTH_STAR\Goals & Milestones\capability_development_goal.md
- Technology frontier: 02-LIBRARY\ref-AI-automation\TECHNOLOGY_LIBRARY_STRATEGY.md
- Business strategy: 01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md
- Revenue evidence: 03-WIKIS\REVENUE_LAB\wiki\
- Capability states and next proof: **owned here**, in the Capability and Proof Frontier
  table above (ruled 2026-08-19, flag #103). [[skill-map]] holds horizons and activation
  criteria only and must never be cited as the state home — this line pointed outward until
  2026-08-19 and was the last surviving half of the repaired ownership loop.

## Reconciliation record — August 21, 2026

**Ran:** the full pass this file has owed since August 1. **Method:** `git log --since`
over every owner named in the table, then a read of each owner that moved. Eleven rows
verified unchanged with their owner's last-touch date recorded; two learner rows moved and
were reconciled against owners rewritten the same morning; one row added.

**What the pass changed beyond dates:**

1. **A new Course-performance row.** CASTLE tracked capability monthly and grades not at
   all — while the actual target is 90% in five courses, which moves weekly. The
   instruments (`FallKSU.xlsx` § GRADE TRACKER standing block, `04-SCHOOL\miss-log.md`)
   and the cadence that reads them (`OPERATIONS.md` § Reviews item 4) were built this
   session.
2. **REVENUE_LAB's month-old question answered.** Its log has asked since 2026-07-24
   whether Lane A is paused or active and named CASTLE as the owner of that
   reconciliation. The queue already said `parked`; **the answer simply never went back to
   the hub that asked.** That is a return-path failure, not a state conflict — and it is
   the same shape as flag #103: work completed in one place and never propagated to the
   place that needed it.
3. **Two rows held deliberately against accrued evidence** — Git/GitHub discipline and
   Agentic delivery both saw real activity this month and neither was promoted, because
   their stated gates (*successful recovery or review*; *measured* end-to-end delivery) were
   not met. Recording that explicitly is the point of a gate.

**Next full reconciliation: September 21, 2026.** Acceptance checkpoint for this one:
**August 23, 2026**, alongside flag #102's close check and the backup review.

**⏰ Three dated items this pass surfaced for the Aug 23 Sunday return:**
OPP-20260714-02 `check_at` **Aug 23** · the tracker's real-data proof unblocks when D2L
populates **Aug 24** · `verify_backup_restore.py` against the live D: backup, **Aug 23**.
