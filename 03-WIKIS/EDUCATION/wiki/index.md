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
  update when D2L opens (~July 25), at the Aug 1 monthly, and at semester start.
- [[learning-how-to-learn-principles]] — Practical
  secondary-source guidance on encoding, retrieval, application, prioritization,
  and attention; numerical/neuroscience claims remain explicitly unverified.

## Raw sources

| File | What it is | Processed into |
|---|---|---|
| `raw/AI Programs in U.S. Universities.md` | Web clipping of cicmap.ai (June 2026 data) | `ai-programs-us-2026.md` |
| `raw/2606.12428v1.pdf` | Muzny et al. arXiv paper, "Mapping AI Programs in the U.S." | `ai-programs-us-2026.md` |
| `raw/ECON 1000 BAC (80643) Fall 2026 Syllabus.md` | Convenience copy of the exact-section capture; canonical original is `02-LIBRARY\00-SCHOOL\04-ECON\` | `fall-2026-course-briefs.md` |
| `raw/TCOM 2010 04 (85633) Fall 2026 Syllabus.md` | Convenience copy of the exact-section capture; canonical original is `02-LIBRARY\00-SCHOOL\03-TCOM\` | `fall-2026-course-briefs.md` |
| `raw/ENGR 1000 W01 (51735) Summer 2026 Syllabus - Reference Only.md` | Convenience copy of the reference-only capture; canonical original is `02-LIBRARY\00-SCHOOL\05-ENGR\` | `fall-2026-course-briefs.md` |
| `raw/Learn To Learn in 109 minutes.md` | Justin Sung meta-learning transcript | fully processed into [[learning-how-to-learn-principles]] on 2026-07-12 (five-chunk review) — a prior session this pass wrongly called this unprocessed; corrected |
| `raw/Sharpen your thinking.md` | Obsidian.md's marketing homepage, confirmed a stray clip (Chris, 2026-07-21) | already correctly assessed as a tool-affordance pointer, not a learning source, in [[learning-how-to-learn-principles]]; Chris to remove/archive this file himself — AI cannot write to `raw/` (permission-denied by design) |
| OpenStax *Principles of Economics 2e*, CORE Econ *The Economy 2.0* | Open-license ECON reading recommendations, fetched 2026-07-21 and placed in `02-LIBRARY\00-SCHOOL\04-ECON\` | Chris to copy into this hub's `raw/` |
| Purdue OWL *Professional, Technical Writing* | Open-license TCOM reading recommendation, fetched 2026-07-21 and placed in `02-LIBRARY\00-SCHOOL\03-TCOM\Textbook Doc Files\` | Chris to copy into this hub's `raw/` |

The three old syllabus PDFs (ECON/TCOM/ENGR) Chris archived on 2026-07-21 are
preserved at `99-ARCHIVE\` per raw immutability — superseded, not deleted.
`02-LIBRARY\00-SCHOOL\` stays the canonical source of truth if the `raw/`
convenience copies and the library ever diverge; `fall-2026-course-briefs.md`
cites the library path, not this folder.

No course has activated per-course structure yet (courses start Aug 24, 2026);
the course-briefs page is pre-semester reference, not activation.
