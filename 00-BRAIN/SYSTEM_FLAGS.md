---
type: flags
tags: [now, governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.
### Last updated: July 15, 2026 (post-migration residual audit complete)

---

## The Rule

Every system improvement flag lands here the moment it is raised — in a session, a handoff, a weekly, anywhere.

**Timing by priority:**
- **HIGH** — fix in the session that raised it. Do not close the session with an open HIGH flag.
- **MEDIUM** — fix at the next weekly review.
- **LOW** — fix at the next monthly review.

A flag leaves this file only when the fix is verified in the target file. "I'll remember" is not a status.

If the same flag is re-raised after being closed, it comes back as HIGH.

**History rule (added July 11, 2026):** this file holds OPEN flags plus the current week's closes only. Older closed flags move to `99-ARCHIVE\` at the weekly review (current archive: `ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`, June 8 – July 11). This file is read at every session start — history in it is a per-session context tax.

---

## OPEN FLAGS

| # | Flag | Raised | Priority | Target | Status |
|---|---|---|---|---|---|
| 57 | **EDUCATION syllabus data-quality gaps** (recorded on `fall-2026-course-briefs.md`): the ENGR 1000 syllabus in raw/ is the **Fall 2025 edition** — its policies (including the total AI prohibition) must be reverified against the real Fall 2026 syllabus when KSU posts it; TCOM 2010's schedule table carries recycled January/Spring dates inside a Fall 2026 header (weekly rhythm probably right, printed dates wrong — trust D2L); TCOM's assignment-weights table is cut off in the source scan — pull the real table from D2L in week 1. | July 9 | MEDIUM | Update `03-WIKIS\EDUCATION\wiki\fall-2026-course-briefs.md` when Fall 2026 ENGR syllabus + D2L are available; hard ceiling Aug 24 | OPEN |
| 16 | Spin rule / right-hand rule needs physical anchor from Atlas. Covers: cross product, torque, angular velocity, and future magnetic field direction. Curl fingers in direction of rotation, thumb points to vector. Must be anchored before these topics appear in PHYS 2211. | June 9 | LOW | Atlas / Physics sessions | OPEN — **approaching**: Chris is now working Vectors (Serway Ch 3) per castle current-position (July 8); cross product is next door. Atlas should anchor it in the next physics session that touches vector products. |
| 68 | Raw-file naming defects found during the July 12 Claude Code + OpenAI docs pack ingest (`03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\`): (a) 12 files in `OPEN_AI-CHATGPT_CODEX_FILES\` (`OpenAI API.md`–`OpenAI API 9.md`, `OpenAI AP15I (1)/(2).md`) share a collided literal page title from capture — SHA-256 confirmed none are duplicates, all 12 genuinely distinct, all now routed into wiki pages, but raw filenames stay generic/unsearchable; (b) `CLI_USE.md` (Claude pack) and `Node reference  OpenAI API.md` (OpenAI pack) are mislabeled — actual content is computer use and the Agent Builder node catalog, not CLI usage or a Node SDK reference. All four already correctly routed in wiki pages despite misleading raw filenames. | July 12 | LOW | Informational only — raw/ is immutable; no fix needed unless Chris wants to rename for future searchability | OPEN |
| 69 | `Agents SDK  OpenAI API 1.md` in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical (SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed flag #63 (mis-saved duplicate). Content read once, not double-summarized. | July 12 | LOW | Chris's call whether to remove the duplicate; both remain in raw pending decision | OPEN |

---

## CLOSED THIS WEEK

| # | Flag | Raised | Closed | Fix |
|---|---|---|---|---|
| 51 | Castle's "calendar-encoded capacity" (OPERATIONS.md rule 8) had no CASTLE/FLOAT tagging from Fall semester start onward — semester week template had only class-meeting blocks. | July 7 | July 15 | Corrected Chris's real Ben Care hours on the North Star Calendar (Sun 7-10am/6-8pm, Mon-Fri 7-9am/5-8pm, Sat 7am-2pm — replacing stale Thu/Fri-only evening + Sat/Sun 3hr-block pattern) and built the full Launch Pad → CASTLE → Flash Card → Lunch → CASTLE/FLOAT → Session Close rotation into every remaining open window, Aug 24–Dec 15, 2026 (57 calendar operations: 2 deletes, 2 updates, 53 creates, all on the North Star Calendar). New confirmed capacity: ~29h45m/wk CASTLE + ~36h55m/wk FLOAT — the July 7 baseline (~24-26h/~10h) is superseded; OPERATIONS.md rule 8 updated. Three Ben-Care/class overlaps (Tue/Thu ECON 8-8:55am; Mon/Wed CSE Lecture tail; Tue CSE Lab) left visible and unresolved, pending Chris's childcare conversation with Heather (~2 weeks from July 15). |
| 75 | Residual semantic-interface drift re-raised the class closed under #74: live technology pointers still named retired North Star Track 2, the monthly skill tracker described completed work as not started, active project space held empty scaffolds, and the scanner secret was inside the synced vault | July 15 | July 15 | Treated HIGH under the re-raise rule. Reconciled active technology, skill, CASTLE, Revenue Lab, project, and proof language to the permanent-capability/current-strategy model; replaced the 126-line stale cockpit with a one-screen `NOW.md` while preserving the exact prior file; added missing field-note metadata; archived one superseded plan, two exact duplicate mislabeled notes, three zero-byte placeholders, two header-only stubs, and two empty/parked project scaffolds after inbound-reference and hash checks. Moved the scanner credential to `C:\Users\chris\.root-secrets\YT_Outlier_Scanner.env` without displaying it and updated/tested the loader. Boot, strict wiki lint, frontmatter, shared-skill, direct-path, duplicate, empty-file, secret-location, and stale-interface checks pass. |
| 74 | Semantic interface drift across PYTHON, TECHNOLOGY, CASTLE source/count ownership, and Watchtower placement | July 14 | July 14 | Reconciled PYTHON to Stage 2; TECHNOLOGY to its live 107-page/four-landscape inventory with index ownership; removed non-decision-useful CASTLE scale claims and central-source-registration wording; added `...projectSuccess` to placement authority; installed the evidence-home → Watchtower → CASTLE test → outcome → CURRENT_STRATEGY Ratchet contract. |
| 73 | NORTH_STAR income timeline did not reflect the July 14 school-funding cut | July 14 | July 14 | Added the continuity-income constraint, a before-Spring-2027 revenue milestone, and a funding-continuity risk. March 2027 is now explicitly the first consulting-client target, not the first-dollar target; Revenue Lab remains the evidence-first test surface. |
| 72 | `frontmatter_audit.py` omitted `88-JOURNAL` from its exclusion set, so a read-only metadata audit could traverse the private journal boundary | July 13 | July 13 | Added `88-JOURNAL` to the script's excluded path components; rerun must confirm the audit no longer reports or traverses journal paths. No journal content was surfaced in the audit output. |
| 70 | Codex CLI native Windows sandbox was missing its setup helper and the Drive workspace could not complete ACL setup | July 12 | July 13 | Reinstall restored the helper; Chris established `C:\Users\chris\.ROOT` as the canonical local workspace, and this unelevated session is operating there. Drive ACL compatibility is no longer a working-tree blocker. `approval_policy = "on-request"` and network denial remain intentional safeguards. |
| 71 | C: local-root cutover needed a verified cloud backup without restoring G: as a working tree | July 13 | July 13 | Chris confirmed Drive for desktop is syncing exactly `C:\Users\chris\.ROOT` under **Computers → this PC → .ROOT** and the live folder/files display green sync marks. `G:\My Drive\.ROOT` remains a legacy recovery snapshot only. |
| 67 | Agent/eval maturity lacked a concrete gate | July 12 | July 12 | Added `AGENT.md § Agent Evaluation Gate`: single-agent first; five representative cases; full action-trace review; human approval for consequential actions; DAILY evidence and regression rollback. Five-case supervised baseline passed. |
| 66 | `.claude/settings.local.json` held a stale broad allowlist with no deterministic private/raw deny layer | July 12 | July 12 | Archived original; replaced atomically with Manual-mode least privilege. Auto/bypass disabled; `88-JOURNAL` tool+sandbox read/write denies; eight raw roots write-denied; boot validator now verifies the controls. |
| 65 | Wiki lint reported 759 equal-severity findings, hiding real link/index hygiene | July 12 | July 12 | Enhanced existing `wiki_lint.py` with blocker/review/expected classes and strict mode; neutralized 33 stale FORGE-era links. Final: 0 blockers, 0 review debt, 714 expected items. |
| 62 | SYSTEM_FLAGS.md itself was ~90% closed-flag history (~4,200 words re-read every session start) — flagged by the July 11 Claude-docs review as the system's biggest always-on context tax | July 11 | July 11 | Closed-flags table (83 rows, June 8 – July 11) archived to `99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`; history rule added above; live file now OPEN + current-week closes only (~4,200 → ~1,600 words). Chris pre-approved via plan (review + quick wins). |
| 64 | PYTHON (565) and PHYSICS (295) hub CLAUDE.mds exceeded the ~200-line always-load budget | July 11 | July 11 | Chris approved the full slim pass same evening. PYTHON 565→145 (new `wiki/authoring-standards.md` + `wiki/protocols.md`; baseline merged into `current-position.md`); PHYSICS 295→130 (new `wiki/authoring-standards.md`; tag fixed now→reference). Same pass also slimmed NORTH_STAR 557→310, WHERE_IT_GOES 279→195, vault_map 159→114 (+ new LOCAL_MACHINE_MAP.md), HAT_OPERATOR 173→92 + HAT_EDUCATOR 205→136 (+ two PLAYBOOKS files), ATLAS 66→31, CODEX 130→96, START_HERE bug fix. All originals archived. Full report: `Session_Logs\SLIM_PASS_2026-07-11.md`. |
| 63 | Duplicate raw file in `CASTLE\raw\books\CLAUDE_FILES\`: `EXPLORE_THE_.CLAUDE_DIRECTORY.md` was byte-identical (MD5 match) to `HOW_CLAUDE_CODE_WORKS.md` — mis-saved download | July 11 | July 11 | Chris removed the duplicate manually same night; absence verified against the live tree (only `HOW_CLAUDE_CODE_WORKS.md` remains). Optional leftover: the real ".claude directory" docs page was never captured — re-download into the same folder if wanted. |

**All older closed flags (June 8 – July 11, 83 rows):** `99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Last updated: July 15, 2026*
