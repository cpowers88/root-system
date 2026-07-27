---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.
### Last updated: July 25, 2026 (flag #84 closed — `register:` scoped to instruction-interface files and defined in `WHERE_IT_GOES.md`; flag #82 closed earlier the same day)

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
| 57 | **EDUCATION syllabus data-quality gaps** (recorded on `course-briefs/fall-2026-course-briefs.md`): D2L is accessible but PHYS 2211 Section 54 and ENGR 1000 Fall BWD remain unpopulated. Exact-section CSE 1321, CSE 1321L, ECON 1000, and TCOM 2010 captures are live in `02-LIBRARY\00-SCHOOL\`. Chris's registration record confirms PHYS 2211 §54 meets Friday 11:30–12:25pm plus MWF 9:10–10:05am and ENGR BWD is fully online. Neighboring PHYS Sections 51 and 55 remain reference-only and cannot establish Section 54 grading, dates, or policy. **July 27 update:** a fresh Section 51 recapture identifies Farhan Islam, and Chris reports the current online listing also names Farhan for his Section 54. Farhan is therefore the provisional likely instructor, but the exact-section syllabus remains missing. TCOM's recycled schedule dates and ECON's minor 8:50/8:55 discrepancy remain subject to D2L/instructor confirmation. | July 9; updated July 27 | MEDIUM | Update the EDUCATION and PHYSICS owners when real PHYS 2211 Section 54 and ENGR 1000 Fall BWD sources post; confirm Farhan through D2L or an exact-section source | OPEN — four exact-section sources live; PHYS §54 likely instructor identified provisionally; PHYS §54 syllabus and ENGR BWD source still missing |
| 16 | Spin rule / right-hand rule needs physical anchor from Atlas. Covers: cross product, torque, angular velocity, and future magnetic field direction. Curl fingers in direction of rotation, thumb points to vector. Must be anchored before these topics appear in PHYS 2211. | June 9 | LOW | Atlas / Physics sessions | OPEN — **approaching**: Chris is now working Vectors (Serway Ch 3) per castle current-position (July 8); cross product is next door. Atlas should anchor it in the next physics session that touches vector products. |
| 68 | Raw-file naming defects found during the July 12 Claude Code + OpenAI docs pack ingest (`03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\`): (a) 12 files in `OPEN_AI-CHATGPT_CODEX_FILES\` (`OpenAI API.md`–`OpenAI API 9.md`, `OpenAI AP15I (1)/(2).md`) share a collided literal page title from capture — SHA-256 confirmed none are duplicates, all 12 genuinely distinct, all now routed into wiki pages, but raw filenames stay generic/unsearchable; (b) `CLI_USE.md` (Claude pack) and `Node reference  OpenAI API.md` (OpenAI pack) are mislabeled — actual content is computer use and the Agent Builder node catalog, not CLI usage or a Node SDK reference. All four already correctly routed in wiki pages despite misleading raw filenames. | July 12 | LOW | Informational only — raw/ is immutable; no fix needed unless Chris wants to rename for future searchability | OPEN |
| 80 | `run_evening_reading.ps1` (new today) wrote `EVENING_READING.md` with every em dash mis-encoded as `ΓÇö` — a UTF-8/codepage mismatch between the captured Claude output and `[System.Text.UTF8Encoding]::new($false)`'s write. Content is fully readable; only the dash glyphs are garbled. **Related finding July 23 (see closed flag #81):** both `EVENING_READING.md` and `MORNING_BRIEF.md` also carry a leading UTF-8 BOM despite the `$false` (no-BOM) constructor argument, which was independently causing `frontmatter_audit.py` to misreport them as missing frontmatter entirely — the read-side symptom is now fixed (#81), but the write-side still emits a BOM it isn't supposed to, most likely because Windows PowerShell 5.1's `-Encoding UTF8` on `Out-File`/`Set-Content` always adds a BOM regardless of a custom `UTF8Encoding` object used elsewhere in the same script, and there is no `utf8NoBOM` option in 5.1 (that arrived in PowerShell 6+) — the fix needs `[System.IO.File]::WriteAllText()` with the `UTF8Encoding(false)` object doing the actual write, not a cmdlet defaulting back to BOM-on. | July 22 | LOW | `00-BRAIN\scripts\run_evening_reading.ps1` and whatever generates `MORNING_BRIEF.md` | **NARROWED July 25 — root cause found and fixed, pending one scheduled run to confirm.** The earlier hypothesis was wrong: the script *already* wrote correctly via `[System.IO.File]::WriteAllText` with `UTF8Encoding($false)`, so the write side was never the defect. The real cause is that **PowerShell decodes a native process's stdout using the console output codepage** — under the default OEM codepage every UTF-8 em dash was already corrupted to `ΓÇö` inside `$result`, before `WriteAllText` ever saw it. Fixed by setting `[Console]::OutputEncoding` to UTF-8 around the `claude.exe` call and restoring it in `finally`. `EVENING_READING.md` is now clean (0 mojibake, 0 BOM, 9 correct em dashes) but was hand-written this session, so **the fix is unproven until the next 5:00 p.m. scheduled run**. Remaining separate issue: `MORNING_BRIEF.md` still carries a UTF-8 BOM and **no script in `00-BRAIN\scripts\` generates it** — that half belongs to whatever session or external task writes it, and is not fixed by this change. |
| 69 | `Agents SDK  OpenAI API 1.md` in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical (SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed flag #63 (mis-saved duplicate). Content read once, not double-summarized. | July 12 | LOW | Chris's call whether to remove the duplicate; both remain in raw pending decision | OPEN |
| 86 | **The evening-reading rotation and the teaching loop contradict each other whenever the next day's first block is a cold gate.** Both were adopted 2026-07-25. `EVENING_READING_INSTRUCTIONS.md` § Course Rotation says each night "primes the next day's first block" (Sunday = Python). The PYTHON teaching loop requires a **cold attempt before instruction**. On 2026-07-26 the rotation fired correctly and assigned *Think Python* pp. 43–52 the night before Monday's Python **cold baseline** — which would have replaced the measurement with the reading. Caught before Chris opened it; `EVENING_READING.md` was rewritten to physics-only plus an explicit "read nothing for Python tonight" with the reason stated. **Not a Codex error — Codex followed the standing instruction exactly.** This is the fourth instance in July of correct output produced against a stale rule, and the first that would have cost a real measurement rather than a file edit. **Proposed fix when this is worked:** add override 0 to `EVENING_READING_INSTRUCTIONS.md`, ahead of the existing two — *never prime a cold gate; if the next day's first block is a cold baseline, mastery gate, or timed quiz, that course gets no reading, and the omission is stated explicitly with its reason.* | July 26 | LOW | `00-BRAIN\EVENING_READING_INSTRUCTIONS.md` § Course Rotation | OPEN — deliberately deferred by Chris 2026-07-26: contained, documented, and worked around for the one night it fired. Escalate to MEDIUM if it recurs on any future cold-gate morning. |
| 85 | **School hubs hold opposite canonical-copy rules for the same class of file, and the copies materially diverged, then partially reconciled.** EDUCATION recorded 2026-07-21 that its immutable `raw/` syllabus copies are convenience copies and `02-LIBRARY\00-SCHOOL\` stays canonical. PYTHON decided the opposite 2026-07-23: `raw\syllabi\` is canonical and the school-library copy is not the citation target. On 2026-07-27, fresh Simple Syllabus captures for CSE 1321, CSE 1321L, ECON 1000, TCOM 2010, and neighboring PHYS 2211 Section 51 replaced the school-library working copies, briefly diverging from each hub's still-July-21 `raw/`. **PYTHON resolved same day:** Chris authorized a raw exception, and CSE 1321/1321L's `raw/syllabi/` files were replaced outright with the July 27 captures (library duplicates removed, not left in parallel) — consistent with PYTHON's own "raw is canonical" rule. `wiki/source-map.md` and `wiki/current-position.md` updated with the newly confirmed instructors (Eun Sik Kim, lecture; Muhammad Usman, lab) and meeting times. **PHYSICS and EDUCATION remain open:** their `raw/` copies are still the July 21 captures while `02-LIBRARY\00-SCHOOL\` holds the July 27 versions (PHYS Section 51 now names Farhan Islam; ECON states attendance isn't graded) — the underlying canonical-copy disagreement between EDUCATION and PYTHON's original rules is still unresolved for those two hubs. | July 24; materialized July 27; PYTHON resolved July 27 | HIGH | Chris decides whether `02-LIBRARY\00-SCHOOL\` or hub `raw/` is canonical for PHYSICS and EDUCATION's official course files, then align those two hubs the same way PYTHON just was | OPEN — narrowed 2026-07-27: PYTHON's divergence is closed via a Chris-authorized raw replacement; PHYSICS and EDUCATION still hold newer library copies against stale `raw/`, and the original two-hubs-disagree question is unresolved for them |
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
