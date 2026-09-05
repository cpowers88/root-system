---
type: report
timeline: now
status: active
tags: [governance, castle, school, review, fall-2026]
---

# Pre-Semester Pathway Review — CASTLE, the August Update, and Monday Readiness

### Scope: the Aug 12 update packet, CASTLE's wiki state, ownership and read paths, and the school layer against Aug 24
### Surface: Claude Code · Hat: Operator + Software Engineer · Chris-directed, 2026-08-22 afternoon
### Status: **findings and one gate roster. Nothing was fixed.** Held so the fresh single-agent Codex session owns the edits.

---

## Why this is a separate report

Two Claude reports and one Codex plan already exist for 2026-08-22. This one does not
restate them. It was produced by a **fresh CASTLE-first load** — the exact test flag #103
still owes before tomorrow's acceptance review — and it reports only what that load
surfaced that the other three passes did not.

**Deliberately excluded because they are already owned:**

| Already covered | Owner |
|---|---|
| `register:`/`type:` vocabulary, `frontmatter_audit.py` coverage | flag #84, **closed 2026-08-22** by Codex Gate C |
| CASTLE `HOW_TO_USE.md` / `README.md` semester staleness | Codex Gate C, **done** |
| CASTLE `CODEX.md` retention decision | Codex Gate C, held for Chris |
| ENGR corpus wording, TCOM filename literals, miss-log row 1 | `claude_report_2026-08-22_engr_corpus_diff_and_tcom_filenames.md` → Codex Gate B |
| miss-log aid-defect instance count | Codex Gate B item 6 |

---

## Flag #103's last open condition — the fresh-session CASTLE-first test

**Result: PASS on ownership. FAIL on one navigation instruction.**

The load ran `AGENT.md` → `CLAUDE.md` → `CHRIS_CORE.md` → `SYSTEM_FLAGS.md` →
`NORTH_STAR.md` → `CASTLE\OPERATIONS.md` → `wiki\index.md` → `current-position.md`.

**At no point did the session have to guess where cross-domain capability state lives.**
`skill-map.md` defers correctly with "→ register" and states its own history as the
reason. `capability_development_goal.md` holds ranking only. `current-position.md` is
unambiguously the home, and its Basis column makes "unchanged" a measured claim rather
than an assumption. The ownership loop is genuinely repaired — this is the acceptance
evidence for tomorrow.

The one failure is finding P-1 below, and it is in the read path, not the ownership.

---

## P-1 🔴 — `CASTLE\wiki\log.md` has two orderings, and Local Boot reads the wrong end

**Condition.** Lines 9–110 hold **seven entries in newest-first order**, topped by
`## 2026-08-19`. From line 150 the file runs **chronologically**, ending at the three
genuinely newest entries — all `## 2026-08-22`, at lines 2006, 2024 and 2060.

**Consequence.** `CASTLE\OPERATIONS.md` § Local Boot step 2 instructs every session to read
*"the last three entries of `wiki\log.md`."* A session reading top-down gets
**Aug 19 · Aug 06 · Aug 02** and never reaches:

- the Aug 21 full reconciliation that closed flag #103's overdue pass;
- the Aug 21 return-to-cockpit closure;
- the Aug 21 Week 1 build and state-hygiene sweep;
- the Aug 21 night school-start transition (Codex);
- all three Aug 22 entries, including today's Gate C promotion.

**Six decision entries are unreachable by the documented read path.** That is flag #103's
own shape in a new location: the state was written correctly and the read path does not
arrive.

**Why no gate caught it.** `castle_freshness.py` check 4 regexes *every* `## YYYY-MM-DD`
heading and takes `max()`. It is structurally blind to ordering — it correctly reports the
newest entry as Aug 22 while no reader can find it. The check is not wrong; its scope
simply does not include "can a session read this file in order."

**Recommended fix.** Move the seven orphan entries into chronological position, then change
Local Boot step 2 to read *"the three newest entries, at the **end** of the file"*. The file
is titled "Append Only" — the append convention is already the intended one. ~15 minutes,
no judgment calls.

---

## P-2 🟠 — Two CASTLE files disagree on a dated trigger, written in the same commit

| File | Claim |
|---|---|
| `wiki\current-position.md:60` | OPP-20260714-02 — *"⏰ Its `check_at` is **2026-08-23**"* |
| `wiki\current-position.md` § Reconciliation record | *"OPP-20260714-02 `check_at` **Aug 23**"* |
| `wiki\opportunity-queue.md` OPP-20260714-02 row | Review date **2026-09-21** |

Both files were written in `9099f29` (2026-08-21). The queue is the owner; `current-position`
should **cite** the date, not restate it — restating is what let the two drift inside one
session.

**Second, smaller instance in the same file.** The queue's italic preface still reads
*"every row now points at the **Aug 23** pre-semester review."* Live rows now read Sep 21 ×3,
Aug 23 ×2, Aug 30 ×1. The prose was true when written on Aug 19 and was not updated when the
rows were re-dated on Aug 21.

**Consequence for tomorrow:** Sunday's due-checks return will read the queue and find only
**two** rows due (OPP-20260716-02, OPP-20260727-01), while `current-position` tells the same
session that OPP-20260714-02 is also due. One of them is wrong and the reviewer has to
adjudicate it live.

---

## P-3 🟠 — The August 12 update packet still declares `.ROOT` PAUSED

| Artifact | Live text |
|---|---|
| `SESSION_INDEX.md` frontmatter | `timeline: now` · `status: active` |
| `SESSION_INDEX.md` title | *"`.ROOT` Update — August 2026 (**OPEN**)"* |
| `SESSION_INDEX.md` § Authority | *"`.ROOT` is **PAUSED** until he gives the completed `OK TO START`."* |
| `UPDATE_PLAN.md` frontmatter | `timeline: now` · `status: active` |
| `UPDATE_PLAN.md` header | *"This is the controlling plan for the current update. It is **LIVE** and evolves."* |
| `SYSTEM_FLAGS.md` banner | *"`.ROOT` **IS RUNNING**. Chris gave `OK TO START` on 2026-08-17… That file is now the update's **historical record, not a live queue**."* |

`SESSION_INDEX.md` explicitly instructs a fresh session — *"including one in a new chat
window"* — to read `UPDATE_PLAN.md` **before proposing any update work**. A session that
obeys that instruction before reaching the flag register starts the semester believing the
system is paused and the plan is live. Chris is opening a new Codex window; this is the
document that window is pointed at.

**P-4 🟠 folds in here.** `OPERATIONS.md` Session Close 7 (written 2026-08-19) states:
*"A multi-day update names this gate in its `SESSION_INDEX.md` as an explicit final step."*
**The Aug 12 packet's `SESSION_INDEX.md` does not name it.** The rule has been applied to
sessions since Aug 19 but never to the one artifact it names by file class.

**Recommended fix.** Close the packet: banner stating it is historical, `timeline: log` /
`status: complete`, and the Session Close 7 line as its final step. Then carry its six
"Open going into Aug 24" rows to live owners — three already are (#57, the Drive link, the
`S4U` run); **row 6, the deferred Phase D `AGENT.md` slim, has no live owner anywhere and
would be orphaned by the close.** It belongs in `SYSTEM_FLAGS.md` as 🟢, post-semester.

---

## P-5 🟠 — Three of five courses have no writable syllabus, and Monday is D2L day

`SYLLABUS_STATUS.md`'s own ownership rule, **reconciled 2026-08-22 — today**:

> *"`WHERE_IT_GOES.md` governs new official course material: the working copy Chris receives
> from KSU lives in the matching `04-SCHOOL` course folder."*

Live state — `find 04-SCHOOL -iname "*yllab*"` returns four files:

| Course | Active source named by the index | In its `04-SCHOOL` course folder? |
|---|---|---|
| TCOM 2010 | `04-SCHOOL\03-TCOM\TCOM 2010 04 (85633)…md` | ✅ yes |
| PHYS 2211 §54 | `04-SCHOOL\02-Physics I\Syllabus.pdf` | ✅ yes |
| **CSE 1321** | `03-WIKIS\PYTHON\raw\syllabi\…` | ❌ **none** |
| **CSE 1321L** | `03-WIKIS\PYTHON\raw\syllabi\…` | ❌ **none** |
| **ECON 1000** | `03-WIKIS\EDUCATION\raw\Syllabi\…` | ❌ **none** |

`04-SCHOOL\01-CSE-Python\` and `04-SCHOOL\04-ECON\` contain no syllabus at all.

**Why this bites Monday specifically.** Those three point at `raw\`, which is immutable and
AI-write-prohibited. When D2L supplies real CSE quiz dates and the real ECON chapter
numbering — both named as Week 1 reconciliation items — **there is no writable working copy
to correct.** The reconciliation ran on two of five courses and stopped.

**Recommended fix.** Copy (never move) the three files from `raw\` into their course folders
and repoint the index's Active Source column. Reading `raw\` is permitted; only writing is
not. ~5 minutes. **Sequencing note:** the Codex plan records that Chris moved and deleted
files under `raw\` during today's concurrent reviews, so this must run inside Gate A's live
baseline, not from this report's snapshot.

---

## P-6 🟠 — The weekly cadence has been silent two weeks, one week before load doubles

Last filed: `WEEKLY_AUGUST3-9.md` (2026-08-12). **Aug 10–16 has no weekly report**; Aug 17–23
closes tomorrow. Twelve DAILY files sit live in `Session_Logs\`. Rotation keys on a filed
weekly, so nothing has rotated since Aug 13.

This is the July 20–26 problem recurring — the gap the Aug 13 monthly-authority clause was
written to prevent — arriving one week before the semester doubles the load.

**Addressed this session:** `WEEKLY_AUGUST10-23.md` is filed alongside this report and
authorizes the rotation. See its Completion Sweep.

---

## P-7 🟢 — `castle_freshness.py` check 4 is coarser than the rule it enforces

`LOG_WINDOW = 14`. Session Close 7 requires a log line **per review session**; the detector
tolerates fourteen days of total silence against CASTLE commits. It cannot see a single
missing entry, only a dead file.

This is a defensible design — deterministic, near-zero false positives — and it should not be
tightened. The problem is that a PASS reads as *"every review was logged"* when it means
*"the file is not dead."* One line in the docstring and in `root_health.py`'s
not-evaluated list closes the gap, consistent with the S-2 lesson closed today: **the
docstring is part of the instrument.**

---

## P-8 🟢 — Flag #101, instance 12, produced live in this session

A `for` loop reading five named files' frontmatter with `sed`/`grep` — read-only, five
explicit paths, no wildcards, zero writes — was denied for being a loop. Completed with
`Grep` instead, which was the better tool anyway.

Identical in shape to instances 6 and 11. **No new information; the count moves to 12.**
The recommendation on file is unchanged: exempt an explicit read-only verb set in
`.claude\hooks\require_safe_shell.py`, and do **not** widen `ALLOWED_SCRIPTS`.

---

# The D2L Day One Gate — Monday, August 24, 2026

Chris's direction, 2026-08-22: *put the gate on Monday now, so work blocked behind it stops
blocking everything else.*

**Rule: nothing on this roster is a blocker before Monday.** Each row is D2L-gated by
external fact, not by anything `.ROOT` can do. Anything **not** on this roster that is
waiting on "when D2L opens" is mis-filed and should be worked now.

**Execution home:** Monday 10:15–12:30 in
`CASTLE\wiki\weekly-plans\weekly-plan-2026-08-24-to-2026-08-30.md`, against
`04-SCHOOL\FallKSU.xlsx` → **D2L DAY ONE** tab. This roster is the completeness check over
that block, not a second checklist.

| # | Blocked item | Currently filed at | Answer returns to |
|---|---|---|---|
| 1 | **TCOM Ethics Analysis SUBMISSION section — format AND filename.** Due Fri Aug 28; printed nowhere in the syllabus | `NOW.md`, Week 1 plan, `SEMESTER_MAP.md` | `04-SCHOOL\03-TCOM\`, miss-log row 1 |
| 2 | **ENGR 1000 BWD dates, weekly order, quiz windows, attendance-quiz behavior, sync/async, drop rules, Raoufi policy** | flag **#57** 🟠, `SYLLABUS_STATUS.md` punch list | `SYLLABUS_STATUS.md`; **#57 closes or converts to one dated question to Raoufi** |
| 3 | **CSE Syllabus & Policy quiz real dates** (`SEMESTER_MAP.md` anomaly 1 — the syllabus prints a template error) + Lab 1 mechanics | Week 1 plan 🟡 rows | `03-WIKIS\PYTHON\wiki\cse-1321-17-week-mastery-plan.md` |
| 4 | **ECON assigned-text alignment** — real Mathews & Patrono chapter numbering against the OpenStax substitute mapping | Week 1 plan, `fall_2026_semester.md` § Current next action | `04-SCHOOL\04-ECON\`, `semester-reading-plan.md` |
| 5 | **Verified Fall 2026 course data into the tracker** | `phase-1…md` **exit criterion 1** (inherited from Phase 0) | `CASTLE\wiki\proof-projects\ksu-academic-tracker.md` |
| 6 | **SQL/SQLite proof frontier** — *"use verified tracker data when D2L populates"* | `current-position.md` SQL row | `current-position.md` Capability table |
| 7 | **Respondus LockDown Browser install + practice quiz** | `SEMESTER_MAP.md` row 8 | `04-SCHOOL\01-CSE-Python\` |
| 8 | **TCOM Group Charter samples** (five weeks of lead time behind D2L auth) | `SEMESTER_MAP.md` | `04-SCHOOL\03-TCOM\Course Resources\` |
| 9 | **Brightspace read-only All Calendars and Tasks iCal feed** — check availability; does not replace twice-weekly D2L verification | CASTLE log 2026-08-22 (Codex) | `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\` |
| 10 | **Course-performance instruments go live** — GRADE TRACKER rows 40–45 begin receiving real scores | `current-position.md` Course-performance row | `FallKSU.xlsx`, read at the Sun Aug 30 return |

**Not on this roster and therefore not D2L-blocked** — work these whenever there is capacity:

- **PYTHON C1** — unrun since Aug 18, thirteen days held. Week 1 gives it nothing but the
  Saturday float. **This is the roster's real point: C1 has been sitting behind a semester
  that has not started.**
- **PHYS row 3 durability re-run** and the fresh cold circular-motion problem (miss-log 5b) —
  own material, own drills, zero external dependency.
- **P-1 through P-7 above**, all seven.
- **The five-part semester transition** — Chris-owned, tomorrow, needs no external input.
- **`verify_backup_restore.py`** — still unrun; the mirror check does not substitute for it.

**Gate close condition.** By Monday 12:30, every row above is either answered and returned to
its owner, or recorded as *absent from D2L on day one* — which is itself the finding, and
which converts row 2 into one specific dated question to Raoufi rather than a second week of
waiting.

---

## Recommended disposition

| Item | Priority | When | Owner |
|---|---|---|---|
| P-1 log ordering + Local Boot step 2 | 🔴 before Monday | tonight or Aug 23 | Codex Gate A/C |
| P-5 three syllabus working copies | 🟠 before Monday | Gate A live baseline | Codex Gate A |
| P-2 OPP date reconciliation | 🟠 | Aug 23 due-checks return | CASTLE |
| P-3 + P-4 close the update packet | 🟠 | Aug 23 review | Chris rules, Codex executes |
| P-6 weekly + DAILY rotation | 🟠 | **done this session** | — |
| P-7 docstring scope | 🟢 | Sep monthly | Codex |
| P-8 flag #101 instance 12 | 🟢 | at any `.claude\` change | Chris |

**None of P-1…P-8 blocks Monday.** P-1 and P-5 are recommended before Monday because both
bite on day one: P-1 breaks the first fresh session of the semester, P-5 breaks the first D2L
capture for three of five courses.

---

## The one structural observation worth carrying

`.ROOT` now owns four staleness detectors — `castle_freshness.py`, `root_health.py`,
`validate_boot_chain.py`, `stale_overwrite_guard.py` — and **every one of them checks a file
against a date, or against itself.** None checks file A against file B.

P-2 and P-3 are both that class. So was flag #103's root cause. So was the Aug 21
REVENUE_LAB return-path failure. **Four instances, which clears the AI-initiated evidence
threshold in `AGENT.md` § System Evolution Authority.**

**Recommendation: do not build it before the semester settles.** Log it as a proposal with a
`check_at` at the September 21 monthly, alongside the next full reconciliation. The semester
maintenance budget says CASTLE work does not grow during a semester, and this is exactly the
kind of attractive system build that Execution Discipline 1 exists to hold back.

---

*Written by: Claude Code, 2026-08-22 · Chris-directed pre-semester review*
*Companion: `WEEKLY_AUGUST10-23.md`, filed the same session*
*Check moment: the August 23 pre-semester review*
