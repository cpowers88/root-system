---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.
### Last updated: July 29, 2026 (flag #85 closed — full syllabus review filed all six Fall courses and reconciled EDUCATION's canonical rule with reality; flag #57 updated with a dated pre-semester punch list)

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
| 68 | Raw-file naming defects found during the July 12 Claude Code + OpenAI docs pack ingest (`03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\`): (a) 12 files in `OPEN_AI-CHATGPT_CODEX_FILES\` (`OpenAI API.md`–`OpenAI API 9.md`, `OpenAI AP15I (1)/(2).md`) share a collided literal page title from capture — SHA-256 confirmed none are duplicates, all 12 genuinely distinct, all now routed into wiki pages, but raw filenames stay generic/unsearchable; (b) `CLI_USE.md` (Claude pack) and `Node reference  OpenAI API.md` (OpenAI pack) are mislabeled — actual content is computer use and the Agent Builder node catalog, not CLI usage or a Node SDK reference. All four already correctly routed in wiki pages despite misleading raw filenames. | July 12 | LOW | Informational only — raw/ is immutable; no fix needed unless Chris wants to rename for future searchability | OPEN |
| 69 | `Agents SDK  OpenAI API 1.md` in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical (SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed flag #63 (mis-saved duplicate). Content read once, not double-summarized. | July 12 | LOW | Chris's call whether to remove the duplicate; both remain in raw pending decision | OPEN |
| 88 | **`02-LIBRARY`'s reference-domain folders drifted from the docs that describe them.** `WHERE_IT_GOES.md`, `02-LIBRARY\README.md`, and `vault_map.md` all still documented uppercase `00-SCHOOL`/`REF-<NAME>` (the July 15, 2026 rename), but the live folders have been lowercase `00-school`/`ref-<name>` since as early as July 13 (ref-health, ref-field-operations) — never reconciled, including through the July 25 naming-case resolution. **Fixed 2026-07-29:** all three docs corrected to match the live lowercase tree (documentation-only, no folders renamed). `ref-AI-automation`'s internal-casing inconsistency (should be `ref-ai-automation`) was **checked, not fixed**: 34 files reference it by exact path, including `00-BRAIN\scripts\path_reference_baseline.json` and its `TECHNOLOGY_LIBRARY_STRATEGY.md` spine — not the cheap rename `WHERE_IT_GOES.md`'s own rule requires; leave it alone unless a dedicated link-safe rename pass is scoped. `02-LIBRARY\coding_toolkit\` (created July 27, currently just an empty `python_code\` subfolder) is still undocumented — confirm its purpose or archive it. | July 29 | LOW | `02-LIBRARY\coding_toolkit\` | OPEN — docs reconciled; `ref-AI-automation` rename downgraded to won't-fix absent a dedicated pass; `coding_toolkit` disposition still pending Chris's call |
| 86 | **The evening-reading rotation and the teaching loop contradict each other whenever the next day's first block is a cold gate.** Both were adopted 2026-07-25. `EVENING_READING_INSTRUCTIONS.md` § Course Rotation says each night "primes the next day's first block" (Sunday = Python). The PYTHON teaching loop requires a **cold attempt before instruction**. On 2026-07-26 the rotation fired correctly and assigned *Think Python* pp. 43–52 the night before Monday's Python **cold baseline** — which would have replaced the measurement with the reading. Caught before Chris opened it; `EVENING_READING.md` was rewritten to physics-only plus an explicit "read nothing for Python tonight" with the reason stated. **Not a Codex error — Codex followed the standing instruction exactly.** This is the fourth instance in July of correct output produced against a stale rule, and the first that would have cost a real measurement rather than a file edit. **Proposed fix when this is worked:** add override 0 to `EVENING_READING_INSTRUCTIONS.md`, ahead of the existing two — *never prime a cold gate; if the next day's first block is a cold baseline, mastery gate, or timed quiz, that course gets no reading, and the omission is stated explicitly with its reason.* | July 26 | LOW | `00-BRAIN\EVENING_READING_INSTRUCTIONS.md` § Course Rotation | OPEN — deliberately deferred by Chris 2026-07-26: contained, documented, and worked around for the one night it fired. Escalate to MEDIUM if it recurs on any future cold-gate morning. |
---

## CLOSED FLAGS

Closed flags live in the monthly ledger:
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` (current month:
`CLOSED_FLAGS_2026-07.md`, 13 rows migrated July 15). Pre-ledger history
(June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`.

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Last updated: July 22, 2026*
