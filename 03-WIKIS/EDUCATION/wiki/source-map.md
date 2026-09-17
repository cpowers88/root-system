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
| `04-SCHOOL/03-TCOM/TCOM 2010 04 (85633) Fall 2026 Syllabus.md` | **Controlling active exact-section copy**, recaptured 2026-07-27 and read end to end 2026-08-19 | Covered — [[course-briefs/fall-2026-course-briefs]], [[courses/tcom-2010/semester-map]], [[courses/tcom-2010/tcom-2010-17-week-execution-plan]]. Existing raw copies are immutable historical evidence. Printed January dates are recycled and do not control Fall dates. |
| `04-SCHOOL/05-ENGR/ENGR 1000 BWB (80862) Introduction to Engineering.md`, `...BWC (80857)...`, and `...BWF (80860)...` | Fall 2026 neighboring web sections; active course-reference copies | Covered as provisional departmental-policy evidence — [[course-briefs/fall-2026-course-briefs]]. BWB/BWF share a template apart from identifiers; BWC omits seven blocks. All defer dates to D2L. None can control BWD dates or execution. Open flag #57. |
| `raw/Open-TC_Course-Resources/Open-TC-PDF.pdf` | ✅ **THE reading copy.** The assigned 2019 decimal-numbered edition of *Open Technical Communication*, **634 pages, no page offset** — every page number in [[courses/tcom-2010/open-tc-page-map]], `semester-reading-plan.md` and `FallKSU.xlsx` is a page in this file | Covered — [[courses/tcom-2010/semester-map]]. |
| `raw/Textbook Doc Files/Open Technical Communication.pdf` | ⚠ **Same edition, different artifact — do not read pages from it.** A **353-page SoftChalk web print-out**; chapters match, pagination does not, and it carries no page numbers of its own (its p149 is *Writing Process*, not *2.13 Memos and Emails*). 🔴 **Corrected 2026-08-21** — this row previously listed it alongside `Open-TC-PDF.pdf` as an aligned copy, which sent page citations to the wrong file | Keep as a chapter-level fallback only. Never a page source. |
| `raw/Textbook Doc Files/2e_Word/` | ⛔ **Trap.** A later flat 0–29 renumbering, missing chapters 25–28 | Do not navigate by it; its numbering conflicts with the syllabus. |
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
