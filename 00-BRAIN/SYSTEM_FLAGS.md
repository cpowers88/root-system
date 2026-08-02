---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.
### Last updated: August 2, 2026, weekly review (flag #90 retired by Chris as an accepted operating limitation; moved to CLOSED_FLAGS_2026-08.md)

---

## The Rule

Every system improvement flag lands here the moment it is raised — in a session, a handoff, a weekly, anywhere.

**Timing by priority:**
- **HIGH** — fix in the session that raised it. Do not close the session with an open HIGH flag.
- **MEDIUM** — fix at the next weekly review.
- **LOW** — fix at the next monthly review.

A flag leaves this file only when the fix is verified in the target file. "I'll remember" is not a status.

If the same flag is re-raised after being closed, it comes back as HIGH.

**History rule (updated July 15, 2026):** this file holds OPEN flags only. When
a flag closes, its row moves in the same session to the monthly ledger at
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` — no weekly
migration step to forget. Pre-ledger history (June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`. This file is
read at every session start — history in it is a per-session context tax.

---

## OPEN FLAGS

| # | Flag | Raised | Priority | Target | Status |
|---|---|---|---|---|---|
| 57 | **EDUCATION syllabus data-quality gaps.** D2L is accessible but PHYS 2211 Section 54 and ENGR 1000 Fall BWD remain unpopulated. Exact-section CSE 1321, CSE 1321L, ECON 1000, and TCOM 2010 captures are all filed and current (see `02-LIBRARY\00-school\SYLLABUS_STATUS.md`). Neighboring PHYS Sections 51 and 55 remain reference-only and cannot establish Section 54 grading, dates, or policy. **2026-07-29:** `02-LIBRARY\00-school\fall_KSU_schedule.md` (Chris's actual Outlook registration confirmation) independently confirms **Farhan Islam** and PHYS 2211 §54's exact meeting times/CRN 83722 — stronger than the prior provisional online-listing match, but still not the syllabus content (grading, exams, policy, calendar). A dated punch list with an Aug 17 escalation trigger for both remaining gaps now lives in `SYLLABUS_STATUS.md`'s Pre-Semester Punch List. | July 9; updated July 29 | MEDIUM | Recheck D2L/Simple Syllabus weekly from mid-August; if nothing posts by **Aug 17**, email the instructor directly. Full detail and owner in `SYLLABUS_STATUS.md`. | OPEN — four of six courses fully filed and current; PHYS §54 instructor confirmed via two independent sources, syllabus content still missing; ENGR BWD source still missing |
| 16 | Spin rule / right-hand rule needs physical anchor from Atlas. Covers: cross product, torque, angular velocity, and future magnetic field direction. Curl fingers in direction of rotation, thumb points to vector. Must be anchored before these topics appear in PHYS 2211. | June 9 | LOW | Atlas / Physics sessions | OPEN — **approaching**: Chris is now working Vectors (Serway Ch 3) per castle current-position (July 8); cross product is next door. Atlas should anchor it in the next physics session that touches vector products. |
| 69 | `Agents SDK  OpenAI API 1.md` in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical (SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed flag #63 (mis-saved duplicate). Content read once, not double-summarized. **2026-08-02:** Chris reviewed the full 85-line content (OpenAI Agents SDK docs clipping) and decided: archive the duplicate. Blocked on execution — `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\` is under a sandbox-level write guard that no available tool can pass, even with Chris's explicit approval in-session; this is a structural boundary, not a missing permission click. | July 12; decided Aug 2 | LOW | Chris to move `Agents SDK  OpenAI API 1.md` to `99-ARCHIVE\ARCHIVED_2026-08-02_AI_AUTOMATION_SYSTEMS_raw_Agents-SDK-OpenAI-API-duplicate.md` himself, outside the sandbox guard | OPEN — decision made, execution blocked by raw-folder sandbox guard, needs Chris to run the move directly |
| 91 | **Python stage progression doesn't reliably reach Chris, so sessions stall on already-closed material.** Chris-reported, direct: "python never progresses as I don't open the plan and we stay stuck on the same material over and over." Real closures ARE happening underneath — Stage 3 closed 2026-07-16, Stage 4 closed 2026-07-29 — but nothing pushes "stage closed, here is the new frontier" to a surface Chris actually reads (`NOW.md`/`MORNING_BRIEF.md`), so the felt experience is stalling even while the wiki itself advances. Concrete same-day supporting evidence: `03-WIKIS\PYTHON\wiki\current-position.md` is internally self-contradictory right now — its own "Stage 4 — CLOSED (2026-07-29)" section confirms closure, but the file's own bottom "Current Next Action" section still names the already-closed common-error debug rep as the next action instead of Stage 4b. So the failure isn't only "Chris doesn't open the file" — the file itself doesn't always get its own summary section updated at closure time, which would mislead even a session that does open it. **2026-08-02 (root-cause interview, same session):** Confirmed as a real gap, not an expectation mismatch — `03-WIKIS\PYTHON\OPERATIONS.md`'s own final operating principle states "Chris should never open this wiki and wonder what to read next," and its QUERY protocol requires the AI to state the next reading lines as part of the session, not on Chris's initiative. Root cause is confirmed as surfacing failure: stages close correctly in the wiki, but "here's what's next" isn't reliably reaching `NOW.md`/`MORNING_BRIEF.md`, which is the only place Chris is expected to look. Second, compounding root cause, also Chris-stated: the teaching loop (cold-attempt → explain-back → PASS WITH CORRECTION mastery gate, per `wiki\teaching-loop.md`) is calibrated for "second nature" mastery, but the pre-semester goal is lighter — "see and understand," not full mastery — so every stage currently takes a heavier gate to close than the current phase actually calls for. Proposed two-part fix, pending Chris's go-ahead to implement: (1) a stage-closure/frontier-change line surfaces in `NOW.md`/`MORNING_BRIEF.md` automatically; (2) `current-position.md` § Teaching Method gets an explicit pre-semester "survey mode" (read once, one walked example, one light check) that supersedes the full mastery-gate loop until 2026-08-24, when real grades make the heavier loop appropriate again. | Aug 2 | MEDIUM | `03-WIKIS\PYTHON\wiki\current-position.md` § Teaching Method (survey-mode addition); `NOW.md`/`MORNING_BRIEF.md` (stage-closure surfacing rule) | OPEN — root cause confirmed, fix designed, awaiting Chris's approval to implement |
---

## CLOSED FLAGS

Closed flags live in the monthly ledger:
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` (current month:
`CLOSED_FLAGS_2026-08.md`). Pre-ledger history
(June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`.

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Last updated: August 1, 2026*
