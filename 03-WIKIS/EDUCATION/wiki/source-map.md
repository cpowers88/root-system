---
type: map
timeline: reference
status: live
tags: [school, education]
created: 2026-07-24
---

# Source Map — EDUCATION

Per-source disposition for everything in this hub's `raw/`. Restored 2026-07-24:
the July 24 instruction-set migration archived the source-to-page table that had
lived inside `wiki\index.md` and pointed future sessions at the archive instead
of replacing it. That table was this hub's coverage ledger, so it belongs live.

Standard this follows: every source carries an explicit disposition — ingested,
covered by a named page, deferred with a reason, or intentionally excluded with
a reason. **Presence in `raw/` is not coverage.**

`raw/` is immutable. Nothing here authorizes changing it.

## Course sources

| Source | What it is | Disposition |
|---|---|---|
| `raw/ECON 1000 BAC (80643) Fall 2026 Syllabus.md` | Exact-section capture, 2026-07-21 | Covered — [[course-briefs/fall-2026-course-briefs]], [[courses/econ-1000/semester-map]]. **No longer byte-identical** to the `04-SCHOOL\04-ECON\` copy: the school-library file was recaptured 2026-07-27 and adds official meeting information plus the explicit statement that attendance is not graded. See flag #85 and the canonical-copy note below. |
| `raw/TCOM 2010 04 (85633) Fall 2026 Syllabus.md` | Exact-section capture, 2026-07-21 | Covered — [[course-briefs/fall-2026-course-briefs]], [[courses/tcom-2010/semester-map]]. **No longer byte-identical** to the `04-SCHOOL\03-TCOM\` copy: the school-library file was recaptured 2026-07-27 and adds exact meeting information. See flag #85 and the canonical-copy note below. |
| `raw/ENGR 1000 W01 (51735) Summer 2026 Syllabus - Reference Only.md` | **Wrong term and section** — Summer 2026 W01, not Fall 2026 BWD | Covered as reference only — [[course-briefs/fall-2026-course-briefs]]. Cannot control deadlines, grading, instructor policy, or AI use. Open flag #57. |
| `raw/Open-TC-PDF.pdf` | The real assigned TCOM 2010 textbook, *Open Technical Communication* 4th ed. (CC-BY 4.0) | Covered — [[courses/tcom-2010/semester-map]] |
| `raw/Open-TC_Course-Resources/` | Instructor ancillary package: slides, assignment templates, rubrics | Covered — [[courses/tcom-2010/semester-map]]. `Sample-Syllabi/` **intentionally excluded** — publisher-generic, not Chris's section. |
| `raw/Linked-Resources/` | ~130 per-example worked files referenced throughout the textbook, numbered by chapter.section (`2-1_`, `4-7_`, `10_`) | Covered as a set — [[courses/tcom-2010/semester-map]]. Indexed by number, not individually summarized. |
| `raw/lesson--great-depression-introduction-essay-wheelock.pdf` | Federal Reserve Bank of St. Louis essay — output, unemployment, deflation, banking panics, recovery, policy | Ingested — [[courses/econ-1000/reading-guides/great-depression-cpi]] plus ECON flashcards and drill |
| `raw/Consumer Price Index for All Urban Consumers All Items in U.S. City Average.md` | FRED/BLS CPIAUCSL clipping — definition, scope, seasonal adjustment, limitations, citation | Ingested — [[courses/econ-1000/reading-guides/great-depression-cpi]] plus ECON flashcards and drill |

## Learning-method sources

| Source | What it is | Disposition |
|---|---|---|
| `raw/Learn To Learn in 109 minutes.md` | Justin Sung meta-learning transcript — encoding/retrieval, spaced retrieval, orders of learning | **Fully ingested 2026-07-12** (five-chunk review) — [[methods/learning-how-to-learn-principles]]. A later session wrongly called this unprocessed; that was corrected in the archived index and the correction is carried forward here. |
| `raw/Sharpen your thinking.md` | Obsidian.md marketing homepage | **Intentionally excluded** — no learning-methodology content; confirmed a stray clip by Chris 2026-07-21. Assessed as a tool-affordance pointer in [[methods/learning-how-to-learn-principles]]. Chris to remove or archive it himself; AI cannot write to `raw/`. |

## Missing and relocated — provenance gaps

`wiki\references\ai-programs-us-2026.md` was built from two sources that are no
longer in this hub's `raw/`. Found 2026-07-24; the page's source block has been
corrected to say so.

| Source | Status |
|---|---|
| `AI Programs in U.S. Universities.md` | **Missing from `.ROOT` entirely.** Web clipping of cicmap.ai captured 2026-07-08. Its extracted claims are not re-verifiable against a local copy — treat them as dated to that capture and re-clip before relying on a figure. |
| `2606.12428v1.pdf` | **Relocated** to `03-WIKIS\BUSINESS\raw\2606.12428v1.pdf`. Not lost; the citation just no longer resolves from this hub. |

## Canonical-copy question — open, do not resolve unilaterally

The exact-section syllabi existed byte-identically in this hub's `raw/` and
in `04-SCHOOL\` until the school-library copies were recaptured on
2026-07-27. This hub recorded on 2026-07-21 that the `raw/` copies are
*convenience copies* and `04-SCHOOL\` stays canonical.

`03-WIKIS\PYTHON` decided the **opposite** on 2026-07-23 for its own syllabi:
`raw\syllabi\` is canonical and the `02-LIBRARY` copy is "Chris's personal
workspace, not wiki-governed, and not the citation target."

Two sibling school hubs therefore hold opposite rules for the same class of
file, and the copies **now diverge**. This hub's own log also records Chris
asking which copy should be the sole source, with the answer still pending.
System flag **#85** is now HIGH; do not resolve it inside one hub.

## Update rule

Add a row when a source arrives in `raw/`. Change a disposition only from real
work, not from intent. If a source leaves or moves, record it here rather than
letting a derived page keep asserting a path that no longer resolves.
