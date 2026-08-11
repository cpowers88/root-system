---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.
### Last updated: August 11, 2026 — flags #92 and #95 closed (OS-level write deny built and proven; config controls now tested for enforcement, not presence). No HIGH flags open.

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
| 93 | **HIGH-flag-before-close rule is prose, not enforced.** `.claude\skills\session-close\SKILL.md` (lines 38-39) states a HIGH flag must be fixed or explicitly handed to Chris before session close — but nothing currently checks this; a session can skip it. Full analysis and proposed target (`.claude\hooks\` or equivalent, firing on session-close/stop) in `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\system-evolution\proposals\2026-07-12_session-close-high-flag-hook.md`. Chris approved moving forward 2026-08-07. | July 12; approved Aug 7 | MEDIUM | Codex to design the actual hook mechanics (trigger event, block vs. warn) per the proposal's Risk/Blast Radius note, then Claude Code or Codex implements. | OPEN — approved, needs Codex hook-mechanics design before implementation |
| 94 | **Teaching-hat methods load conditionally, so teaching quality varies by session.** `HAT_EDUCATOR.md` (line 50) names seven methods — Skeleton First, One Concept at a Time, Term Anchoring, Explain-It-Back, Cold Checks, Physical Anchors, Short Corrections — but their substance sits in `HAT_EDUCATOR_PLAYBOOKS.md` behind a judgment-call load ("Load when running a teaching session"). None of the five subject hats (`HAT_PHYSICS`, `HAT_PYTHON`, `HAT_TCOM`, `HAT_ECON`, `HAT_ENGR1000`) reference the playbooks, so after the educator hat nothing in the chain mentions the methods again. When the playbook loads, teaching follows the method; when it doesn't, the agent has seven bare names and improvises — the same hat behaving as two different teachers. Cause is the July 11, 2026 slim pass, which moved substance behind a conditional load to save ~300 words. Chris reports the hats are "iffy sometimes" and has re-tested them; this had never been recorded as a flag, which is why he could not tell whether it had been acted on. | August 10 | MEDIUM | Decide after Codex's structure review: inline the seven method definitions back into `HAT_EDUCATOR.md` (~300 words, recommended — hats are already an optional load, so the base boot chain is untouched), or make the playbook load mandatory and add the pointer to all five subject hats. Keep the four SKILL procedures in the playbook either way; those are genuinely situational. | OPEN — diagnosed, fix deferred pending Codex structure review |
---

## CLOSED FLAGS

Closed flags live in the monthly ledger:
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` (current month:
`CLOSED_FLAGS_2026-08.md`). Pre-ledger history
(June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`.

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Current date stamp lives once, in the header above — do not add a second here.*
