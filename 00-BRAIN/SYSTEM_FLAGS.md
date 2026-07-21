---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.
### Last updated: July 21, 2026 (flag #79 added; flag #57 extended)

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
| 79 | Mechanical Codex boundary for `.ROOT`: journal must be unreadable; every current `raw` evidence folder must remain readable but non-writable; ordinary workspace work and explicitly granted outside reads must still function. Chris approved implementation July 21 after a controlled test proved the prior `workspace-write` sandbox could create a file in `00-BRAIN\CASTLE\raw`. | July 21 | MEDIUM | Validate normal write, raw read/raw write denial, journal denial without exposure, network denial, and scoped outside-read recovery in a fresh session | OPEN — elevated Windows sandbox installed and `root_guarded` activated July 21; current-chat nested test hung and was terminated, so no protection claim until post-restart tests pass |
| 78 | Google Drive's `.ROOT` sync was retired July 17, and `00-BRAIN\scripts\backup_to_d_drive.ps1` was written as the replacement, but no live record confirms its first manual run or verifies `D:\BACKUPS\.ROOT`. The script uses mirror behavior, so it must not be run or scheduled without Chris's explicit approval and a checked target. | July 20 | MEDIUM | Chris-approved manual test of `backup_to_d_drive.ps1`; verify the resolved D: target and resulting backup contents before scheduling or calling the replacement complete | OPEN — review by July 26; Git/GitHub protects committed history, not current uncommitted work |
| 57 | **EDUCATION syllabus data-quality gaps** (recorded on `fall-2026-course-briefs.md`): the ENGR 1000 syllabus in raw/ is the **Fall 2025 edition**; TCOM 2010's schedule table carried recycled January/Spring dates inside a Fall 2026 header. **Extended July 21:** D2L is accessible but the courses themselves remain unpopulated — real course content is not expected before Aug 24, the first day of classes. Chris pulled real, exact-section Simple Syllabus Markdown captures for four of six courses (CSE 1321, CSE 1321L, ECON 1000, TCOM 2010 — now in `02-LIBRARY\00-SCHOOL\`, see `SYLLABUS_STATUS.md`), resolving this flag's TCOM/CSE portion. **Two courses remain genuinely unconfirmed:** PHYS 2211 Section 54 (Chris's actual enrolled section, confirmed via `Clippings\View Registration Information.md`) has no matching syllabus — only neighboring Sections 51 (instructor Krishna Rana Magar) and 55 (instructor Swayamprabha Behera) exist, filed as reference-only since neither establishes Section 54's real instructor, dates, or grading; ENGR 1000 only has a Summer 2026 reference, not Chris's Fall BWD section. | July 9 (extended July 21) | MEDIUM | Update `03-WIKIS\EDUCATION\wiki\fall-2026-course-briefs.md` once real PHYS 2211 Section 54 and ENGR 1000 Fall BWD syllabi are available — realistically Aug 24 onward, not before; the July 26 pre-semester boundary should track this gap, not assume D2L will have resolved it | OPEN — reviewed July 21; TCOM/CSE/ECON resolved with real captures, PHYS Section 54 and ENGR BWD remain unconfirmed pending Aug 24 |
| 16 | Spin rule / right-hand rule needs physical anchor from Atlas. Covers: cross product, torque, angular velocity, and future magnetic field direction. Curl fingers in direction of rotation, thumb points to vector. Must be anchored before these topics appear in PHYS 2211. | June 9 | LOW | Atlas / Physics sessions | OPEN — **approaching**: Chris is now working Vectors (Serway Ch 3) per castle current-position (July 8); cross product is next door. Atlas should anchor it in the next physics session that touches vector products. |
| 68 | Raw-file naming defects found during the July 12 Claude Code + OpenAI docs pack ingest (`03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\`): (a) 12 files in `OPEN_AI-CHATGPT_CODEX_FILES\` (`OpenAI API.md`–`OpenAI API 9.md`, `OpenAI AP15I (1)/(2).md`) share a collided literal page title from capture — SHA-256 confirmed none are duplicates, all 12 genuinely distinct, all now routed into wiki pages, but raw filenames stay generic/unsearchable; (b) `CLI_USE.md` (Claude pack) and `Node reference  OpenAI API.md` (OpenAI pack) are mislabeled — actual content is computer use and the Agent Builder node catalog, not CLI usage or a Node SDK reference. All four already correctly routed in wiki pages despite misleading raw filenames. | July 12 | LOW | Informational only — raw/ is immutable; no fix needed unless Chris wants to rename for future searchability | OPEN |
| 69 | `Agents SDK  OpenAI API 1.md` in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical (SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed flag #63 (mis-saved duplicate). Content read once, not double-summarized. | July 12 | LOW | Chris's call whether to remove the duplicate; both remain in raw pending decision | OPEN |
| 77 | Weekly intake is not fully cleared. Four classified files remain under `77-INBOX\READY_FOR_CHRIS_RAW_PLACEMENT\`: BUSINESS — `TheLeanStartup,RIES.pdf`; TECHNOLOGY — `metadata – OAPEN A world of scholarly books Open to all, built to last.md`, `Mixture of SMB wedges and enterprise stacks.md`, and `readthis.md`. AI may inspect routing state but may not place files into immutable `raw\`; the duplicates named in the July 17 row are no longer present. | July 17 | LOW | Chris decides whether to place or decline each staged file; after placement, the owning hub records intake/coverage before any synthesis queue opens | OPEN — current state verified July 20; awaiting Chris raw-placement decision |

---

## CLOSED FLAGS

Closed flags live in the monthly ledger:
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` (current month:
`CLOSED_FLAGS_2026-07.md`, 13 rows migrated July 15). Pre-ledger history
(June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`.

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Last updated: July 21, 2026*
