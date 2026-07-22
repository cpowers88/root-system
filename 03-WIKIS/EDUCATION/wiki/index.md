---
type: map
tags: [reference, school]
---

# EDUCATION Wiki — Index

General KSU coursework support (TCOM, ECON, ENGR, and anything without its own wiki).
Operating rules: this folder's `CLAUDE.md`. Raw sources live in `raw/` (immutable).

## Pages

- [ai-programs-us-2026.md](ai-programs-us-2026.md) — Distilled reference: CIC's cicmap.ai
  interactive map + arXiv 2606.12428 status report on undergraduate AI majors/minors
  in U.S. CS departments (data as of April–June 2026). Sources: `raw/AI Programs in
  U.S. Universities.md`, `raw/2606.12428v1.pdf`.
- [fall-2026-course-briefs.md](fall-2026-course-briefs.md) — ECON 1000 / TCOM 2010 /
  ENGR 1000 syllabus distillation: **the three courses' three different AI policies**,
  grading structures, schedule spines, and data-quality flags. Refreshed 2026-07-21
  against the real exact-section Simple Syllabus captures (ECON, TCOM confirmed
  exact-section; ENGR's only source remains reference-only — Summer 2026, not the
  real Fall BWD section).
- [current-position.md](current-position.md) — Progress anchor for EDUCATION (required
  by NORTH_STAR monthly review + HAT_EDUCATOR). Pre-semester state until Aug 24;
  update at the Aug 1 monthly, when D2L/course modules populate, and at semester start.
- [[learning-how-to-learn-principles]] — Practical
  secondary-source guidance on encoding, retrieval, application, prioritization,
  and attention; numerical/neuroscience claims remain explicitly unverified.
- [tcom-2010-semester-map.md](tcom-2010-semester-map.md) — **TCOM 2010 activated
  2026-07-21.** Week-by-week map from the real syllabus schedule to the actual
  textbook chapters, the instructor ancillary templates/rubrics/slides, and
  the per-example worked files — plus the two real gaps found (no ancillary
  template for the Report Group Charter or the Reflective Memo).
- [econ-1000-semester-map.md](econ-1000-semester-map.md) — **ECON 1000
  provisional map, 2026-07-21.** Real confirmed schedule/exams/quizzes mapped
  to CORE Econ's confirmed unit list, OpenStax's expected-but-not-fully-verified
  chapters, and real FRED datasets. Lower confidence tier than TCOM's map —
  the real assigned textbook is D2L-locked, so chapter alignment is a
  substitute-based guess to be re-checked once D2L opens.

- [econ-1000-great-depression-cpi-reading-guide.md](econ-1000-great-depression-cpi-reading-guide.md)
  — Five just-in-time reading chunks connecting CPI, GDP, unemployment,
  deflation, banking, and policy to ECON Weeks 7-14; includes source limits and
  an exam-style causal-reading frame.
- [flashcards/econ-1000-gdp-inflation-unemployment.md](flashcards/econ-1000-gdp-inflation-unemployment.md)
  — Later-semester retrieval batch for GDP, CPI/inflation, unemployment,
  banking panics, deposit insurance, and causal claims.
- [glossary/econ-1000-macro-terms.md](glossary/econ-1000-macro-terms.md)
  — Plain-English term bank covering GDP, CPI, inflation/disinflation/deflation,
  unemployment, banking, policy failure, and causation.
- [drills/econ-1000-cpi-and-depression-reasoning.md](drills/econ-1000-cpi-and-depression-reasoning.md)
  — Private, solution-free reasoning drill unlocked in pieces during Chapters
  8-11 and final review.

## Raw sources

| File | What it is | Processed into |
|---|---|---|
| `raw/AI Programs in U.S. Universities.md` | Web clipping of cicmap.ai (June 2026 data) | `ai-programs-us-2026.md` |
| `raw/2606.12428v1.pdf` | Muzny et al. arXiv paper, "Mapping AI Programs in the U.S." | `ai-programs-us-2026.md` |
| `raw/ECON 1000 BAC (80643) Fall 2026 Syllabus.md` | Convenience copy of the exact-section capture; canonical original is `02-LIBRARY\00-SCHOOL\04-ECON\` | `fall-2026-course-briefs.md` |
| `raw/TCOM 2010 04 (85633) Fall 2026 Syllabus.md` | Convenience copy of the exact-section capture; canonical original is `02-LIBRARY\00-SCHOOL\03-TCOM\` | `fall-2026-course-briefs.md`, `tcom-2010-semester-map.md` |
| `raw/ENGR 1000 W01 (51735) Summer 2026 Syllabus - Reference Only.md` | Convenience copy of the reference-only capture; canonical original is `02-LIBRARY\00-SCHOOL\05-ENGR\` | `fall-2026-course-briefs.md` |
| `raw/Learn To Learn in 109 minutes.md` | Justin Sung meta-learning transcript | fully processed into [[learning-how-to-learn-principles]] on 2026-07-12 (five-chunk review) — a prior session this pass wrongly called this unprocessed; corrected |
| `raw/Sharpen your thinking.md` | Obsidian.md's marketing homepage, confirmed a stray clip (Chris, 2026-07-21) | already correctly assessed as a tool-affordance pointer, not a learning source, in [[learning-how-to-learn-principles]]; Chris to remove/archive this file himself — AI cannot write to `raw/` (permission-denied by design) |
| `raw/Open-TC-PDF.pdf` | The real assigned TCOM 2010 textbook, *Open Technical Communication* 4th ed. (CC-BY 4.0) | `tcom-2010-semester-map.md` |
| `raw/Open-TC_Course-Resources/` | Instructor ancillary package for the same textbook — presentation slides, assignment templates, rubrics (`Sample-Syllabi/` subfolder deliberately excluded from the map, publisher-generic) | `tcom-2010-semester-map.md` |
| `raw/Linked-Resources/` | ~90 per-example worked files referenced throughout the textbook, numbered by chapter.section (e.g. `2-1_`, `4-7_`, `10_`) | `tcom-2010-semester-map.md` |
| `raw/lesson--great-depression-introduction-essay-wheelock.pdf` | Federal Reserve Bank of St. Louis introductory essay on output, unemployment, deflation, banking panics, recovery, and policy | `econ-1000-great-depression-cpi-reading-guide.md`, ECON flashcards and drill |
| `raw/Consumer Price Index for All Urban Consumers All Items in U.S. City Average.md` | FRED/BLS CPIAUCSL clipping; index definition, scope, seasonal adjustment, limitations, and citation | `econ-1000-great-depression-cpi-reading-guide.md`, ECON flashcards and drill |

The three old syllabus PDFs (ECON/TCOM/ENGR) Chris archived on 2026-07-21 are
preserved at `99-ARCHIVE\` per raw immutability — superseded, not deleted.
`02-LIBRARY\00-SCHOOL\` stays the canonical source of truth if the `raw/`
convenience copies and the library ever diverge for ECON/ENGR (TCOM's
textbook/ancillary set now lives natively in this hub's `raw/`, not
duplicated in the library).

TCOM 2010 is the first course to activate real per-course structure (ahead
of the Aug 24 semester start, on real landed material). ECON and ENGR remain
pre-semester reference until their own material lands the same way.
