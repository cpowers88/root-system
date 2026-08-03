---
type: log
tags: []
timeline: log
updated: 2026-07-24
---

# EDUCATION Wiki — Session Log

## 2026-07-27 (evening) — Weeks 1-6 ingestion check, TCOM + ECON, against fresh recaptures

- Codex's earlier inbox sort left two raw syllabus captures coexisting per
  course (stale July 21 at `raw/[file].md`, fresh July 27 at
  `raw/Syllabi/[file].md`) — root-level duplicates removed by Chris before
  this session, `raw/Syllabi/` is now the sole copy for TCOM, ECON, ENGR.
- Read the new TCOM and ECON syllabi's full Weeks 1-6 in this session and
  checked every deliverable/date/chapter against `courses/tcom-2010/
  semester-map.md` and `courses/econ-1000/semester-map.md`. **Both already
  accurate** — the July 21 ingestion held up; the 1,109-line raw diff on
  TCOM was mostly re-scrape formatting (a duplicated calendar table, an
  added HTML grading-rubric block), not a real schedule change.
- Added two small confirmed details each map didn't have: TCOM's real
  attendance-penalty structure (3 free unexcused absences, then ~3.5 pts/
  absence, 6=one letter grade, 9=two); ECON's Week 6 Thursday (10/1)
  post-exam review session and the online/no-extension quiz-exam policy.
- Weeks 7-14 for both courses not yet re-checked against the fresh
  captures — next pass when there's a specific need, not tonight.

## 2026-07-24 — Machine-first course architecture installed

- Installed `OPERATIONS.md` as the machine contract and reduced `CLAUDE.md`
  to a loader.
- Added the human `README.md` and replaced `HOW_TO_USE.md`.
- Rebuilt `wiki/index.md` as the sole live catalog.
- Organized knowledge into `course-briefs/`, `courses/<course>/`, `methods/`,
  and `references/`.
- Archived the pre-migration interfaces and catalog under
  `99-ARCHIVE/2026-07-24_EDUCATION_PRE_MACHINE_ARCHITECTURE/`.
- No file under `raw/` changed.

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

## 2026-07-21 (final) — TCOM 2010 activated: Educator hat, first per-course structure

- Chris loaded the real assigned textbook (*Open Technical Communication*,
  `raw/Open-TC-PDF.pdf`), its instructor ancillary package
  (`raw/Open-TC_Course-Resources/` — templates, rubrics, slides), and ~90
  per-example worked files (`raw/Linked-Resources/`, numbered by the book's
  own chapter.section scheme) into this hub's `raw/`, then asked to wear the
  Educator/TCOM hat and map the real semester against this material.
- Loaded `HAT_EDUCATOR.md` and `HAT_TCOM.md` before building. Found and
  fixed a real error in `HAT_TCOM.md`: it said "Never email assignments,"
  but the actual syllabus text explicitly requires the Business Email unit
  to be submitted by real email — only document *attachments* are barred
  for other assignments. Left the hat's claimed class time (TTh 9:35–10:55am)
  alone — the captured syllabus text has no clock time to confirm or deny it
  against.
- Built `tcom-2010-semester-map.md`: a week-by-week table mapping every real
  syllabus deliverable to its textbook chapter, ancillary template/rubric/
  slide, and worked example(s). Two genuine gaps found and left open rather
  than papered over: no ancillary template for the Week 6 Report Group
  Charter or the Week 12 Reflective Memo — both need building from adjacent
  generic templates or the syllabus's own D2L-linked samples (behind auth,
  not capturable). `Sample-Syllabi/` in the ancillary package was excluded
  from the map on purpose — publisher-generic, not Chris's real section.
- Files: `tcom-2010-semester-map.md` (new), `index.md`, `current-position.md`,
  `fall-2026-course-briefs.md`, `00-BRAIN\HATS\HAT_TCOM.md`, this log.
- Result: TCOM 2010 is the first of the six Fall courses to get real
  per-course structure, ahead of the Aug 24 semester start — justified per
  this hub's own activation rule ("build out per-course structure only when
  a course's material actually lands here") since the material genuinely
  landed today, not pre-built speculatively.
- Next: no blocking action. If Chris wants, the two gap templates (charter,
  reflective memo) could be drafted from the generic Schedule/Memo templates
  already on hand — Chris's call, not done unprompted.

## 2026-07-21 (also final) — ECON 1000 provisional map + HAT_ECON.md correction

- Chris asked for the same treatment on "the other course" (ECON) after
  TCOM's activation. Checked `HAT_ECON.md` against the real exact-section
  syllabus first, same discipline as TCOM, and found real errors: it said
  four exams at 25% each with the course ending ~mid-November; the real
  structure is two exams (25%+25%) plus four quizzes (50% total, two
  lowest dropped), running the full 14 weeks through Thu Dec 3. Also fixed
  the professor's name (already confirmed as Zeynep Kelani, not "TBD"), the
  exact class time (8:00–8:50am, not 8:55am), and both real exam dates
  (9/29 and 12/3, not "TBD from D2L") — none of this needed to wait for
  D2L; it was already confirmed in the real syllabus captured earlier
  today.
- Built `econ-1000-semester-map.md`, explicitly one confidence tier below
  `tcom-2010-semester-map.md`: the real schedule/exams/quizzes are
  confirmed, CORE Econ's unit list is confirmed (fetched live), but
  OpenStax's chapter mapping past Ch. 1 is inferred from the book's known
  standard structure, not independently re-verified — flagged as such
  rather than presented with false confidence. The real assigned textbook
  (Mathews & Patrono) stays completely unmapped since it's D2L-locked; the
  page says plainly to re-check once D2L opens, not to trust this mapping
  as final.
- Files: `econ-1000-semester-map.md` (new), `index.md`, `current-position.md`,
  `fall-2026-course-briefs.md`, `00-BRAIN\HATS\HAT_ECON.md`, this log.
- Next: re-verify the OpenStax/CORE Econ chapter alignment and replace the
  provisional map with a real one once D2L populates (~Aug 24) and the
  actual Mathews & Patrono chapter structure is visible. ENGR 1000 remains
  fully blocked — no real Fall BWD syllabus exists yet to map against.

## 2026-07-21 (inbox sweep) — Two ECON-relevant sources staged; closed flag #77

- Chris restructured `77-INBOX\READY_FOR_CHRIS_RAW_PLACEMENT\` into one
  subfolder per active hub (CASTLE deliberately excluded — not a raw-intake
  hub) and asked for the loose files in `77-INBOX\` and `Clippings\` to be
  sorted. Classified and moved three files:
  - `lesson--great-depression-introduction-essay-wheelock.pdf` (St. Louis
    Fed education essay — GDP, inflation/deflation, unemployment, banking,
    government's economic role) → staged in `READY_FOR_CHRIS_RAW_PLACEMENT\EDUCATION\`.
    Strong direct match to ECON 1000's real topic list.
  - `Consumer Price Index for All Urban Consumers All Items in U.S. City
    Average.md` (FRED CPI web clipping, same series as `CPIAUCSL.csv`) →
    same staging folder — a reading companion to the dataset already pulled.
  - `View Registration Information.md` (Chris's real OwlExpress
    registration record, all six Fall 2026 CRNs/times/locations/instructors)
    → moved to `02-LIBRARY\00-SCHOOL\` directly, not staged for any wiki
    `raw/` — it's an official academic record like `Ellucian Degree Works
    Dashboard.md`, not domain source material.
  - The registration record materially narrowed `SYSTEM_FLAGS.md` #57:
    confirmed real meeting times/locations for PHYS 2211 §54 and ENGR 1000
    BWD (both still show no assigned instructor, per the registrar itself);
    confirmed TCOM's class time was already stated correctly in
    `HAT_TCOM.md`; surfaced a harmless 5-minute schedule discrepancy for
    ECON 1000 between the syllabus and the registration record, noted in
    `HAT_ECON.md`.
  - Flag #77 closed — its four original files are confirmed gone from the
    old flat staging location (Chris's own disposition); moved to
    `Closed Flags\CLOSED_FLAGS_2026-07.md`.
- Files: `SYSTEM_FLAGS.md`, `Closed Flags\CLOSED_FLAGS_2026-07.md`,
  `HAT_ECON.md`, this log. Two files remain staged in `raw/`'s inbox
  waiting room, not yet in `raw/` itself (AI cannot write there directly).
- Next: Chris moves the two staged EDUCATION files into this hub's `raw/`
  when ready; the other seven hub subfolders in the staging area remain
  empty — nothing further to route this pass.

## 2026-07-21 (processed intake) — CPI and Great Depression ECON support

- Chris moved the two staged ECON sources into EDUCATION `raw/`: David C.
  Wheelock's four-page Federal Reserve Bank of St. Louis Great Depression essay
  and the FRED/BLS CPIAUCSL clipping. Raw files were read only and not modified.
- Used the PDF inspection workflow: extracted all four pages, rendered all four to
  PNG in the system temporary directory, and visually confirmed clean, complete,
  readable pages with intact headings, footnotes, and transitions.
- Built [[econ-1000-great-depression-cpi-reading-guide]] as five just-in-time
  chunks for Weeks 7-14: CPI measurement; GDP/output contraction; money, banking,
  and deflation; recovery/government action; and final integration. Each chunk has
  an unlock point, reading boundary, misconception control, and explain-back proof.
- Added [[glossary/econ-1000-macro-terms]],
  [[flashcards/econ-1000-gdp-inflation-unemployment]], and
  [[drills/econ-1000-cpi-and-depression-reasoning]]. The drill is private,
  solution-free practice and is explicitly not a substitute for graded work.
- Recorded two critical boundaries: CPI index level is not the inflation rate, and
  the local CPI series starts in 1947 so it cannot directly graph or verify the
  essay's 1929-1933 claims. The Wheelock essay's monetary interpretation is framed
  as an argument to analyze, not the only accepted causal account.
- Inserted the sources into [[econ-1000-semester-map]], the course brief, current
  position, HOW_TO_USE, and the exhaustive index. Removed legacy `reference` tags
  from the ECON and TCOM semester maps, clearing both maps' new schema regressions.
- Validation: strict wiki lint passes with 0 blockers and 0 review debt; whitespace
  check passes; EDUCATION contributes no new frontmatter debt. The canonical vault
  remains separately blocked by five concurrent PHYSICS timeline findings.
- Next: do not broad-read the new packet now. The first unlock is Week 7 after the
  initial GDP lesson; before then, use only light pre-semester GDP/inflation/
  unemployment vocabulary retrieval if it fits the priority plan.

## 2026-07-24 (evening) — Hub audit after the machine-architecture migration (Claude Code)

- Mechanically clean: 12 pages, 0 dead links, 0 orphans, 0 frontmatter gaps,
  index matches tree, live structure matches what `OPERATIONS.md` claims.
  `current-position.md` and `course-briefs/fall-2026-course-briefs.md` are both
  accurate and current, including flag #57's ENGR/PHYS source-quality state.
  The missing ENGR 1000 course folder is correctly justified, not a gap.
- **Regression found and repaired.** The July 24 migration archived the
  source-to-page table that lived inside `wiki\index.md` and pointed future
  sessions at the archived copy instead of replacing it. That table was this
  hub's coverage ledger — the artifact the architecture evidence refinery names
  as the standard (explicit per-source disposition: ingested / covered by a
  named page / deferred with reason / intentionally excluded with reason).
  Restored live as NEW `wiki\source-map.md`, reconciled against the current
  `raw/` tree rather than copied forward, and linked from `index.md`.
- **Provenance break found.** `wiki\references\ai-programs-us-2026.md` claimed
  "Sources (in `raw/`)" for two files that are no longer there:
  `AI Programs in U.S. Universities.md` is **missing from `.ROOT` entirely**,
  and `2606.12428v1.pdf` now lives in `03-WIKIS\BUSINESS\raw\`. The page's
  source block now states both accurately; its cicmap-derived figures are
  marked as dated to the 2026-07-08 capture and not re-verifiable locally.
- **Not resolved, by design.** The three exact-section syllabi are byte-identical
  in this hub's `raw/` and in `02-LIBRARY\00-SCHOOL\`. This hub recorded
  2026-07-21 that `02-LIBRARY` stays canonical; PYTHON recorded the opposite for
  its own syllabi on 2026-07-23. Chris's own question about which copy should be
  the sole source is still open in this log. Raised as system flag **#85** rather
  than settled inside one hub.
- **Reported, not fixed:** `raw\README.md` still says "Nothing here yet —
  populate per course as it activates," while `raw/` now holds roughly 200 files
  including the whole Open-TC textbook package. `raw/` is immutable, so this is
  Chris's call.
- Validation: `wiki_lint.py` 0 blockers; `frontmatter_audit.py` no new findings
  in EDUCATION; `validate_boot_chain.py` PASS.
- **Next action:** Chris decides flag #85 (one canonical-copy rule for all school
  hubs) and whether to correct `raw\README.md`.

## 2026-07-26 — Pre-semester block coverage plan (Claude Code)

- Chris asked what this hub's school blocks run on going forward. Booted the
  full chain, then answered against the July 27 CASTLE weekly plan, which
  assigns this hub 9 of 32 blocks (TCOM 4, ECON 3, ENGR 2).
- **Chris's decisions this session:** the ENGR plan-of-study substitution is the
  right shape, **but ENGR is held entirely until Aug 24** — KSU shows no course
  content before then. Line the pre-semester weeks up against the real course
  weeks and front-load Week 1 work where possible; report what cannot be filled
  so it can be placed elsewhere.
- Built [[pre-semester-coverage-plan]] covering four weeks (Jul 27 – Aug 23).
  It states what is *workable*; CASTLE keeps ownership of placing blocks into
  days. **Verdict: 36 planned blocks, 22–26 fillable, 10–14 released.**
- **TCOM — 16 blocks, fully fillable, real course Weeks 1–3.** Every source is
  local. Verified against the PDF rather than trusting the semester map: Ch 2.13
  Memos and Emails pp. 149–163, Ch 3 Ethics pp. 174–190, Ch 5.2 Audience Analysis
  pp. 304–310, Ch 2.12 Oral Presentations pp. 139–148, Ch 5.10 Peer Review from
  p. 448, Ch 8 Technical Editing from p. 590 — **printed page numbers equal PDF
  page numbers, no offset** (spot-checked pp. 149, 174, 304). All ancillary and
  Linked-Resources paths confirmed present. Stop line set before the Week 4–5
  Individual Project Proposal — real graded project work.
- **ECON — 6 of 12 fillable.** Weeks A–B only (Ch 1 foundations, scarcity,
  gains from specialization, PPF graph reading). Weeks C–D released on purpose:
  Week 3 Economic Systems is exactly where the substitute maps are least
  trustworthy, and the macro packet's first unlock is Week 7. Week A's third
  block retargeted from "second foundations block" to cold vocabulary retrieval,
  matching this hub's own stated pre-semester ceiling.
- **ENGR — 8 blocks released.** Also recorded that the original Friday block was
  unrunnable regardless: the Summer W01 reference syllabus defers its assignment
  list to a D2L schedule PDF that is not in the vault.
- Two small corrections: the TCOM semester map named the resume peer-review
  ancillary `PeerReview.docx`; the real filename is
  `Resume+CoverLetter_PeerReview.docx`. Fixed. Block-evidence table added to the
  new plan so TCOM/ECON proof has somewhere to land — this hub had no learner
  proof ledger, unlike PYTHON and PHYSICS.
- Files: new `wiki\pre-semester-coverage-plan.md`; `index.md`,
  `current-position.md`, `courses\tcom-2010\semester-map.md`, this log.
- **Still open for Chris:** flag #85 (one canonical-copy rule for school hubs,
  MEDIUM, due at a weekly review) and where the 10–14 released blocks go —
  recommended to Python and Physics, but that is CASTLE's call, not this hub's.

## 2026-07-27 — Exact-section syllabus recapture routed from 77-INBOX (Codex)

- Replaced the school-library working copies for ECON 1000 and TCOM 2010 with
  fresh Simple Syllabus captures. Requirements did not change; both add exact
  meeting information, and ECON explicitly says attendance is encouraged but
  not graded.
- Preserved the July 21 working copies under
  `99-ARCHIVE/02-LIBRARY/00-SCHOOL/SYLLABI_REPLACED_2026-07-27/`.
- The delivered ENGR W01 Summer file was body-identical to the existing
  reference and was archived as a duplicate. Fall BWD remains missing.
- The immutable EDUCATION `raw/` captures remain dated July 21 and now diverge
  from the school-library files. Corrected `source-map.md` and escalated flag
  #85 to HIGH rather than silently selecting a canonical-copy rule.

**Next action:** Chris chooses one canonical home for official course files;
until then, use the July 27 school-library captures as the newest official
evidence and keep the divergence explicit.

## 2026-07-27 — Raw-syllabus preparation plan activated (Codex)

- Re-read the exact-section ECON 1000 and TCOM 2010 syllabi directly from
  EDUCATION `raw/`, plus the ENGR Summer reference and both live semester maps.
- Updated [[pre-semester-coverage-plan]] rather than creating a competing plan.
  TCOM remains 16 fully sourced blocks. ECON moved from six blocks limited to
  Weeks A–B to eight bounded blocks across all four weeks.
- ECON now prepares Chapters 1–3 durable reasoning only: scarcity, incentives,
  opportunity cost, specialization, comparative advantage, PPF interpretation,
  neutral economic-system comparison, fresh-case classification, and a cold
  readiness gate. It does not claim the substitute books match Mathews/Patrono.
- Added three pre-semester gates: TCOM Week 1 message-analysis readiness, ECON
  Chapters 1–3 readiness, and a D2L verification handoff.
- ENGR remains held because the only syllabus is Summer W01 and its assignment
  schedule is absent.

**Next exact action:** run ECON Week A Block 1 in the next CASTLE ECON slot:
OpenStax Chapter 1 orientation followed by a closed-source definition of
scarcity, incentives, opportunity cost, and tradeoff.

## 2026-08-02 — ECON Week B disambiguation line (Fable, evening close)

- Applied the one remaining verified fix from today's plan reconciliation:
  `pre-semester-coverage-plan.md` § Week B — specialization and production
  choices now states only E1 (one block) is scheduled Aug 3–9; the listed
  items roll to Weeks C–D, deferred rather than missed. Matches the TCOM
  disambiguation already in place; no scope or gate change.

**Next exact action:** unchanged — E1 runs Friday Aug 7 per the CASTLE
weekly plan, or earlier via its Move-On Gate queue.
