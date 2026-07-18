---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.
### Last updated: July 17, 2026 (flag #77 — inbox sort pending decisions logged)

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
| 57 | **EDUCATION syllabus data-quality gaps** (recorded on `fall-2026-course-briefs.md`): the ENGR 1000 syllabus in raw/ is the **Fall 2025 edition** — its policies (including the total AI prohibition) must be reverified against the real Fall 2026 syllabus when KSU posts it; TCOM 2010's schedule table carries recycled January/Spring dates inside a Fall 2026 header (weekly rhythm probably right, printed dates wrong — trust D2L); TCOM's assignment-weights table is cut off in the source scan — pull the real table from D2L in week 1. | July 9 | MEDIUM | Update `03-WIKIS\EDUCATION\wiki\fall-2026-course-briefs.md` when Fall 2026 ENGR syllabus + D2L are available; hard ceiling Aug 24 | OPEN |
| 16 | Spin rule / right-hand rule needs physical anchor from Atlas. Covers: cross product, torque, angular velocity, and future magnetic field direction. Curl fingers in direction of rotation, thumb points to vector. Must be anchored before these topics appear in PHYS 2211. | June 9 | LOW | Atlas / Physics sessions | OPEN — **approaching**: Chris is now working Vectors (Serway Ch 3) per castle current-position (July 8); cross product is next door. Atlas should anchor it in the next physics session that touches vector products. |
| 68 | Raw-file naming defects found during the July 12 Claude Code + OpenAI docs pack ingest (`03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\`): (a) 12 files in `OPEN_AI-CHATGPT_CODEX_FILES\` (`OpenAI API.md`–`OpenAI API 9.md`, `OpenAI AP15I (1)/(2).md`) share a collided literal page title from capture — SHA-256 confirmed none are duplicates, all 12 genuinely distinct, all now routed into wiki pages, but raw filenames stay generic/unsearchable; (b) `CLI_USE.md` (Claude pack) and `Node reference  OpenAI API.md` (OpenAI pack) are mislabeled — actual content is computer use and the Agent Builder node catalog, not CLI usage or a Node SDK reference. All four already correctly routed in wiki pages despite misleading raw filenames. | July 12 | LOW | Informational only — raw/ is immutable; no fix needed unless Chris wants to rename for future searchability | OPEN |
| 69 | `Agents SDK  OpenAI API 1.md` in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical (SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed flag #63 (mis-saved duplicate). Content read once, not double-summarized. | July 12 | LOW | Chris's call whether to remove the duplicate; both remain in raw pending decision | OPEN |
| 77 | `77-INBOX` sort (July 17 evening): two named PDFs moved and confirmed as new material — `Process Mining Handbook.pdf` → `03-WIKIS\SYSTEMS\raw\` (deepens existing BPMN/XES/PM4Py lane; ties to MCP Bootcamp Day 1 Systems Audit) and `AI in Business and Economics.pdf` → `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\` (ties to Day 7 Product & Value). Neither has a ledger row or synthesis page yet — full/selective ingestion deliberately deferred (780 combined pages, late session, standing "don't reopen large source books as a reading queue" discipline). Four other inbox PDFs are confirmed duplicates of already-compiled sources (`Entrepreneurship.pdf`, `The Goal, GOLDRATT.pdf`, `Foundations of Scalable Systems.pdf`, `Hacking APIs.pdf`) sitting untouched in `77-INBOX` pending Chris's delete-or-leave call. `TheLeanStartup,RIES.pdf` is genuinely new/uncovered (no home decision made). `Programming Logic and Design Comprehensive.pdf` is parked, not ingested — matches Chris's own stated read on Python fundamentals ("good for now, will ask if it gets advanced"), no live build boundary needs it. | July 17 | LOW | `77-INBOX` (4 duplicates) / `03-WIKIS\SYSTEMS\raw\` + `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\` (2 unregistered new sources) | OPEN |

---

## CLOSED FLAGS

Closed flags live in the monthly ledger:
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` (current month:
`CLOSED_FLAGS_2026-07.md`, 13 rows migrated July 15). Pre-ledger history
(June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`.

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Last updated: July 17, 2026*
