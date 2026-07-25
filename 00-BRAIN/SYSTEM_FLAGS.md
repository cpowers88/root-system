---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.
### Last updated: July 25, 2026 (flag #82 closed after dependency-folder exclusions restored the reviewed health baseline)

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
| 57 | **EDUCATION syllabus data-quality gaps** (recorded on `course-briefs/fall-2026-course-briefs.md`): the ENGR 1000 syllabus in raw/ is the **Fall 2025 edition**; TCOM 2010's schedule table carried recycled January/Spring dates inside a Fall 2026 header. **Extended July 21:** D2L is accessible but the courses themselves remain unpopulated — real course content is not expected before Aug 24, the first day of classes. Chris pulled real, exact-section Simple Syllabus Markdown captures for four of six courses (CSE 1321, CSE 1321L, ECON 1000, TCOM 2010 — now in `02-LIBRARY\00-SCHOOL\`, see `SYLLABUS_STATUS.md`), resolving this flag's TCOM/CSE portion. **Two courses remain genuinely unconfirmed:** PHYS 2211 Section 54 (Chris's actual enrolled section, confirmed via `Clippings\View Registration Information.md`) has no matching syllabus — only neighboring Sections 51 (instructor Krishna Rana Magar) and 55 (instructor Swayamprabha Behera) exist, filed as reference-only since neither establishes Section 54's real instructor, dates, or grading; ENGR 1000 only has a Summer 2026 reference, not Chris's Fall BWD section. **PHYS portion cross-referenced July 21:** both neighbor syllabi are now registered in `03-WIKIS\PHYSICS\wiki\source-map.md` and cross-checked against the 18-stage path in `syllabus-coverage-ledger.md` and `learning-path.md` — confirms Stage 1-12/15 order, surfaces an open question on Ch 13/14/16/17/38 scheduling, still pending real Section 54 confirmation. **Further narrowed July 21 (later):** Chris's official KSU registration record (`02-LIBRARY\00-SCHOOL\View Registration Information.md`, moved there from `Clippings\` this session) confirms real meeting times/locations for both remaining gaps — PHYS 2211 §54: Friday 11:30–12:25pm breakout (Atrium 1116) + MWF 9:10–10:05am lecture (Academic Building 200), Marietta Campus; ENGR 1000 BWD: fully online, no meeting time. **Both still show "No specified Instructor" directly on the registrar record itself** — the registrar confirming the gap is real, not a capture failure. Same record confirmed TCOM 2010 meets TTh 9:35–10:55am exactly as `HAT_TCOM.md` states, and surfaced a minor 5-minute discrepancy for ECON 1000 (registration says ends 8:55am; the real syllabus text says 8:50am) — immaterial, defer to whichever the professor states in class. | July 9 (extended July 21) | MEDIUM | Update `03-WIKIS\EDUCATION\wiki\course-briefs\fall-2026-course-briefs.md` once real PHYS 2211 Section 54 and ENGR 1000 Fall BWD syllabi post with an assigned instructor — realistically Aug 24 onward, not before; the July 26 pre-semester boundary should track this gap, not assume D2L will have resolved it | OPEN — reviewed July 21; TCOM/CSE/ECON resolved with real captures; PHYS neighbor syllabi now put to use in the PHYSICS wiki; PHYS §54 and ENGR BWD now have confirmed real meeting times/locations but still no assigned instructor per the registrar itself, pending Aug 24 |
| 16 | Spin rule / right-hand rule needs physical anchor from Atlas. Covers: cross product, torque, angular velocity, and future magnetic field direction. Curl fingers in direction of rotation, thumb points to vector. Must be anchored before these topics appear in PHYS 2211. | June 9 | LOW | Atlas / Physics sessions | OPEN — **approaching**: Chris is now working Vectors (Serway Ch 3) per castle current-position (July 8); cross product is next door. Atlas should anchor it in the next physics session that touches vector products. |
| 68 | Raw-file naming defects found during the July 12 Claude Code + OpenAI docs pack ingest (`03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\`): (a) 12 files in `OPEN_AI-CHATGPT_CODEX_FILES\` (`OpenAI API.md`–`OpenAI API 9.md`, `OpenAI AP15I (1)/(2).md`) share a collided literal page title from capture — SHA-256 confirmed none are duplicates, all 12 genuinely distinct, all now routed into wiki pages, but raw filenames stay generic/unsearchable; (b) `CLI_USE.md` (Claude pack) and `Node reference  OpenAI API.md` (OpenAI pack) are mislabeled — actual content is computer use and the Agent Builder node catalog, not CLI usage or a Node SDK reference. All four already correctly routed in wiki pages despite misleading raw filenames. | July 12 | LOW | Informational only — raw/ is immutable; no fix needed unless Chris wants to rename for future searchability | OPEN |
| 80 | `run_evening_reading.ps1` (new today) wrote `EVENING_READING.md` with every em dash mis-encoded as `ΓÇö` — a UTF-8/codepage mismatch between the captured Claude output and `[System.Text.UTF8Encoding]::new($false)`'s write. Content is fully readable; only the dash glyphs are garbled. **Related finding July 23 (see closed flag #81):** both `EVENING_READING.md` and `MORNING_BRIEF.md` also carry a leading UTF-8 BOM despite the `$false` (no-BOM) constructor argument, which was independently causing `frontmatter_audit.py` to misreport them as missing frontmatter entirely — the read-side symptom is now fixed (#81), but the write-side still emits a BOM it isn't supposed to, most likely because Windows PowerShell 5.1's `-Encoding UTF8` on `Out-File`/`Set-Content` always adds a BOM regardless of a custom `UTF8Encoding` object used elsewhere in the same script, and there is no `utf8NoBOM` option in 5.1 (that arrived in PowerShell 6+) — the fix needs `[System.IO.File]::WriteAllText()` with the `UTF8Encoding(false)` object doing the actual write, not a cmdlet defaulting back to BOM-on. | July 22 | LOW | `00-BRAIN\scripts\run_evening_reading.ps1` and whatever generates `MORNING_BRIEF.md` | OPEN — first observed run, July 22 17:00 task; fix by reading the captured `$result` as UTF-8 explicitly (or stripping non-ASCII em dashes to `-`) before write, then verify on the next scheduled run; also confirm both scripts write via `WriteAllText`, not a cmdlet, to actually suppress the BOM |
| 69 | `Agents SDK  OpenAI API 1.md` in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical (SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed flag #63 (mis-saved duplicate). Content read once, not double-summarized. | July 12 | LOW | Chris's call whether to remove the duplicate; both remain in raw pending decision | OPEN |
| 85 | **Two school hubs hold opposite canonical-copy rules for the same class of file.** The exact-section Fall 2026 syllabi exist byte-identically in both a hub's immutable `raw/` and `02-LIBRARY\00-SCHOOL\`. **EDUCATION** recorded 2026-07-21 that its `raw/` copies are convenience copies and `02-LIBRARY\00-SCHOOL\` stays canonical. **PYTHON** decided the opposite 2026-07-23 — `raw\syllabi\` is canonical, the `02-LIBRARY` copy is "Chris's personal workspace, not wiki-governed, and not the citation target" — on the reasoning that citing an ungoverned personal folder ties hub governance to a location that can be reorganized without the wiki knowing. Nothing is broken while the copies match; they disagree the moment one diverges. EDUCATION's own log also records Chris asking which copy should be the sole source, with the answer still pending a clarification that never happened. Needs one rule applied to both hubs (and to PHYSICS when its Section 54 syllabus lands), not a per-hub choice. | July 24 | MEDIUM | One decision from Chris, then align `03-WIKIS\EDUCATION\wiki\source-map.md` + `course-briefs\fall-2026-course-briefs.md` and `03-WIKIS\PYTHON\wiki\syllabus-alignment.md` + `source-map.md` to match | OPEN — surfaced during the EDUCATION audit; not resolved inside one hub by design |
| 84 | **`register:` is deployed in 50 live files with 6 values but is undefined in the metadata authority.** `WHERE_IT_GOES.md § Metadata Standard` calls itself "One Copy, Defined Here" and says "never invent a second metadata scheme — extend this one," yet does not mention `register:` at all. Live values: `human-context` (18), `ai-directive` (17), `ai-loader` (10), `compatibility-pointer` (2 — `00-BRAIN\AI_OS_CORE.md` and `03-WIKIS\BUSINESS\wiki\ai-integration-company\index.md`), `ai-profile` (2 — `00-BRAIN\CLAUDE.md`, `CODEX.md`), `knowledge-index` (1 — `03-WIKIS\BUSINESS\wiki\index.md`). Origin: `vault-skeleton-design.md` §7.1 proposed it as a **binary** (`ai-directive` / `human-context`); §8.5 said add it "only after structural and behavioral validation rules are defined." Neither gate was met — it propagated by sibling precedent across the July 24 hub conversions instead. The last two values look misapplied to wiki *content* pages rather than instruction files. **Chris's working hypothesis (2026-07-24): `register:` may be CASTLE-scoped only, even though it currently touches every wiki** — he wants to dig into that before anything is written into `WHERE_IT_GOES.md`. Nothing was changed pending his decision. | July 24 | MEDIUM | Decision first (Chris), then either `00-BRAIN\WHERE_IT_GOES.md § Metadata Standard` to define the approved value set, or a removal pass across the 50 files if the property turns out to be CASTLE-scoped | OPEN — deferred by Chris same day; no files edited. Cost of the deferral is bounded: the property is inert metadata, so a later narrowing or removal is a mechanical pass, not a rewrite |
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
