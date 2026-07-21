---
type: log
tags: [log]
---

# EDUCATION Wiki — Session Log

## 2026-07-07 — Wiki created (narrow scope)

- Created as part of the `.ROOT` wiki unification. The prior `EDUCATION` folder
  was renamed to `PYTHON` (its content was already 100% Python/CS — nothing
  general-KSU existed to leave behind). This is a fresh scaffold for TCOM, ECON,
  ENGR, and other general KSU coursework support.
- Pages created: CLAUDE.md, index.md, log.md, raw/README.md, HOW_TO_USE.md
- Next action: activate when a course's staged study material is ready to move
  here — see `00-BRAIN\CASTLE\wiki\phases\` for sequencing.
- *(Entry carried over 2026-07-08 from the hub-root `log.md` when that stale
  scaffold file was archived — see the 2026-07-08 integrity-sweep entry.)*

## 2026-07-08 — First processing pass: raw/ → wiki/

- Wiki was empty (fresh scaffold after the July 7 PYTHON carve-out); created
  `index.md`, `log.md`, and the first content page.
- Processed both files in `raw/` — they form one package: the cicmap.ai web
  clipping (CIC @ Northeastern's interactive map of U.S. undergraduate AI
  programs, June 2026 data) and its companion paper arXiv:2606.12428 (April
  2026 analysis of 66 AI majors and 87 AI minors).
- Distilled both into `ai-programs-us-2026.md`: landscape counts, what AI
  majors/minors typically require, ACM CS2023 context, and KSU relevance notes.
- Note: the clipping's line 40 is a ~236KB inline SVG of the map itself —
  no data value, ignored during extraction. `raw/` untouched per the raw
  source rule.
- Chris confirmed from the map: KSU has **no AI-specific program** — only a
  BS with a Major in Computer Science. Recorded in the KSU relevance section
  of `ai-programs-us-2026.md`.
- Next: re-check cicmap.ai each semester (CIC re-scrapes roughly once a
  semester) for a new KSU AI concentration, the likeliest first arrival.

## 2026-07-08 — Pre-go-live integrity sweep (Session 2)

- Added YAML frontmatter to `index.md`, `log.md`, and `ai-programs-us-2026.md`
  (they were created after the July 8 vault-wide frontmatter batch).
- Stale hub-root `index.md` and `log.md` archived to `99-ARCHIVE\`
  (`ARCHIVED_2026-07-08_EDUCATION_root_index.md` / `_root_log.md`); the root
  log's 2026-07-07 creation entry was carried into this file first (above).
- Next: nothing pending in this hub; activates when a course lands here.

## 2026-07-09 — CLAUDE.md dedup (system-wide, Chris-approved)

- Shared blocks (academic integrity, raw rule, chunking, session protocols)
  replaced by a pointer to `00-BRAIN\AI_Agent.md § Wiki Shared Layer`. Scaffold
  otherwise unchanged. Record: `00-BRAIN\Session_Logs\DAILY_2026-07-09.md`.

## 2026-07-09 — Citation/sort audit: three Fall syllabi ingested

- Third hub in Chris's hub-by-hub citation-and-sorting sweep. Found three
  syllabus PDFs in `raw/` no session had processed (dropped ~June 20 per
  capture timestamps): ECON 1000, TCOM 2010, ENGR 1000.
- Coverage per the chunking rule: ECON all 25 pp. (text extraction);
  TCOM all 19 pp. — the PDF is a **scan with no text layer**, read
  page-by-page as rendered images; ENGR all 12 pp. (text extraction).
- Created `fall-2026-course-briefs.md` (one page, not three — none of the
  courses has activated, and the load-bearing content is comparative:
  **three different AI policies across the three courses**, deadlines
  rhythm, grading structures).
- Data-quality flags recorded on the page: ENGR syllabus is the Fall 2025
  edition (reverify AI policy against the 2026 version when posted); TCOM's
  schedule table carries recycled January/Spring dates inside a Fall 2026
  header; TCOM's weights table is cut off in the source scan.
- Index updated (page entry + raw-sources table).
- Next: when Fall 2026 ENGR syllabus posts, replace that section; per-course
  activation (current-position.md etc.) waits for actual coursework after
  Aug 24.

## 2026-07-09 — AI Index 2026 education data folded in

- Part of the flag-55(c) multi-hub ingest (Chris-directed): the Stanford
  AI Index 2026's Education chapter highlights were added as a section on
  `ai-programs-us-2026.md` — national CS-enrollment decline (−11%),
  AI-master's growth (+17%), PhD flow reversing to academia, and the
  80%-student-use vs 6%-clear-policies gap that mirrors the syllabus
  findings on `fall-2026-course-briefs.md`.
- Source PDF lives in `03-WIKIS\TECHNOLOGY\raw\`; full distillation in
  `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\ai-index-2026.md`; coverage record
  in that wiki's log (session 12).
- Next: unchanged — per-course activation waits for Aug 24; re-check
  cicmap.ai next semester.

## 2026-07-11 — current-position.md created (prelive review brief item 3)

- Created `current-position.md` per the CODEX final prelive review
  (`00-BRAIN\Session_Logs\CODEX_FINAL_PRELIVE_REVIEW_2026-07-11.md`, Execution
  Brief item 3): NORTH_STAR's monthly-review checklist and HAT_EDUCATOR both
  expect an EDUCATION progress anchor, and it was missing before the Aug 1
  monthly. This supersedes the July 9 note that activation waits for Aug 24 —
  the file is a pre-semester anchor, not per-course activation (concepts/,
  drills/ etc. still wait for actual coursework).
- Index updated with the new page entry.
- Next: update current-position when D2L opens (~July 25), at the Aug 1
  monthly, and at the Aug 24 semester start.

## 2026-07-14 — Index integrity correction

- Added the existing `learning-how-to-learn-principles.md` page to the
  exhaustive index, resolving the one EDUCATION index omission/orphan pair
  found by strict wiki lint. No learning content or Physics work changed.
- Next: normal pre-semester cadence; update current-position when D2L opens.

## 2026-07-14 — Human guide reconciled to live school authority

- Connected HOW_TO to the pre-semester plan and official-source precedence.
  Removed stale certainty around recycled course dates, incomplete weights, and
  an older ENGR policy while keeping the D2L update trigger explicit.
- Cross-reference validation found no active dead link in the guide.

## 2026-07-21 (evening) — Course briefs refreshed against real exact-section captures

- Chris pulled real, exact-section Simple Syllabus Markdown captures for ECON
  1000 and TCOM 2010 (plus CSE 1321/1321L, owned by PYTHON) on 2026-07-21,
  replacing the July 9 PDF ingest this page was built from. `fall-2026-course-briefs.md`
  rewritten against the live files in `02-LIBRARY\00-SCHOOL\` — ECON confirmed
  with no outstanding data-quality issue; TCOM's recycled January/Spring dates
  persist in the fresh capture too (confirmed as KSU's own Simple Syllabus
  template defect, not a stale-source artifact); ENGR's only available source
  turned out to be **Summer 2026** (Instructor Matt Marshall), not the "Fall
  2025" the old brief claimed — still reference-only, still not the real Fall
  BWD section, corrected in place. See `SYSTEM_FLAGS.md` #57 for the standing
  ENGR/PHYS unconfirmed-section tracking.
- Added a short reading/dataset-prep pointer per course: FRED + World Bank
  Open Data for ECON (doubles as real-data reps against the July SQL/
  data-viz weak links); the syllabus's own linked sample documents for TCOM;
  explicitly nothing yet for ENGR pending the real BWD syllabus.
- Files: `fall-2026-course-briefs.md`, `index.md` (page description + raw
  sources table), this log.
- Next: no action pending here; re-check when ENGR's real Fall BWD syllabus
  posts, and when D2L populates (~Aug 24) for the transition to per-course
  activation.

## 2026-07-21 (later) — raw/ reality sync + two unprocessed sources found

- Chris placed `.md` copies of the ECON/TCOM/ENGR exact-section syllabi
  directly into this hub's `raw/` (for ease of use, no transcription errors)
  and archived the three superseded PDFs himself. Index updated to match:
  the raw table now lists the real current files, marks them as convenience
  copies with `02-LIBRARY\00-SCHOOL\` staying canonical if the two ever
  diverge.
- Found two pre-existing files in `raw/` neither this hub's index nor any
  session had processed: `Learn To Learn in 109 minutes.md` (Justin Sung
  meta-learning transcript — encoding/retrieval, spaced retrieval, orders of
  learning; substantive, overlaps [[learning-how-to-learn-principles]]) and
  `Sharpen your thinking.md` (Obsidian.md's marketing homepage — no
  learning-methodology content, flagged as a likely mis-clip rather than
  processed). Both recorded in the index; neither absorbed into a wiki page
  yet — awaiting Chris's call on the Sung transcript, and confirmation on
  whether the Obsidian page was an intentional capture.
- **Correction, same session:** the claim above that the Sung transcript and
  Obsidian file were unprocessed was wrong — `learning-how-to-learn-principles.md`
  already fully incorporated the Sung transcript on 2026-07-12 (five-chunk
  review, dedicated Source Assessment section) and already correctly
  identifies the Obsidian file as a tool-affordance page, not a learning
  source. Caught by actually reading that page before acting further; index
  corrected in place.

## 2026-07-21 (later still) — ECON/TCOM literature fetch; raw/ write permission confirmed hard-blocked

- Fetched three open-license reading sources per Chris's request to build
  structured ECON/TCOM pathways: OpenStax *Principles of Economics 2e* (free,
  CC-BY, Ch. 1 confirmed live, full ~20-chapter structure not independently
  re-verified this pass — book landing/TOC page is SPA-rendered and returned
  no text to automated fetch); CORE Econ's *The Economy 2.0* (free, CC
  BY-NC-ND, full unit list confirmed live for both micro and macro volumes);
  Purdue OWL's Professional, Technical Writing section (free, full 18-topic
  list confirmed live).
- **Could not fetch:** a BCcampus/Pressbooks-style open technical-writing
  textbook, and St. Louis Fed / FRED educational pages — both returned
  HTTP 403 across every URL variant tried (`opentextbc.ca`,
  `ecampusontario.pressbooks.pub`, `stlouisfed.org/education`,
  `fred.stlouisfed.org`), consistent with bot/Cloudflare protection rather
  than a bad URL. Left unfetched rather than force it; Chris can grab these
  manually in a browser if wanted.
- **Structural finding:** writing into any wiki's `raw/` is denied at the
  permission-settings level, not just by convention — confirmed by an actual
  denied `Write` call to `EDUCATION\raw\`. Conversational authorization from
  Chris does not override this; it is a deliberate hard guard on raw
  immutability. The three fetched files were written to the session
  scratchpad instead, for Chris to copy into `raw/` himself, matching how he
  placed the syllabus copies and the two meta-learning clippings earlier
  this session.
- Also confirmed, and did not act on: Chris authorized removing the
  Obsidian stray clip and asked whether the ECON/TCOM/ENGR syllabi now
  duplicated between this hub's `raw/` and `02-LIBRARY\00-SCHOOL\` should
  be resolved by removing one copy. Both are file-removal actions inside
  `raw/`, which AI cannot perform directly per the finding above — left for
  Chris, with the duplicate-resolution direction itself still ambiguous in
  his own wording pending a chat clarification.
- Next: Chris copies the three scratchpad files into `raw/` if he wants
  them there; Chris removes/archives the Obsidian clip himself; Chris
  confirms which copy (library vs. this hub's `raw/`) should be the sole
  surviving one for the three syllabi.

## 2026-07-21 (final pass) — Real FRED datasets pulled for ECON 1000

- Chris set up a FRED API key at `C:\Users\chris\.root-secrets\FRED.env`
  (external to `.ROOT`, same convention as the YT Outlier Scanner project).
  Built `00-BRAIN\scripts\fetch_fred.py` to read the key at runtime (never
  printed/logged) and pull four series via the live FRED API: `GDP`,
  `GDPC1` (real GDP), `CPIAUCSL` (CPI/inflation), `UNRATE` (unemployment).
  All four confirmed live and current — data through 2026-01 (quarterly) /
  2026-06 (monthly).
- Output: `02-LIBRARY\00-SCHOOL\04-ECON\datasets\` (4 CSVs + README
  documenting source, license, and refresh instructions).
  `fall-2026-course-briefs.md`'s ECON reading/dataset-prep bullet updated to
  point at the real local files instead of the earlier abstract FRED
  recommendation.
- Next: no action pending; World Bank Open Data (economic-systems
  cross-country comparisons) remains an unfetched recommendation if Chris
  wants it later.
