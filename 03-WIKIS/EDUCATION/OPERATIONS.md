---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [school, education, governance]
created: 2026-07-24
---

# EDUCATION_WIKI — OPERATIONS

## Function

Maintain reusable study support for KSU subjects that do not have a dedicated
wiki. Convert verified course requirements and source material into course
briefs, resource maps, explanations, retrieval aids, and private practice.

## Authority

| Owns | Authority |
|---|---|
| Permanent direction and AI limits | `01-NORTH_STAR\NORTH_STAR.md` |
| Semester outcomes and priorities | `01-NORTH_STAR\Goals & Milestones\fall_2026_semester.md` |
| Official syllabus captures (ECON, TCOM, ENGR) | `03-WIKIS\EDUCATION\raw\Syllabi\` — corrected 2026-07-29 to match where captures actually land; general course materials (assignments, notes, records, D2L pulls) stay in `02-LIBRARY\00-SCHOOL\` |
| Cross-course syllabus status | `02-LIBRARY\00-SCHOOL\SYLLABUS_STATUS.md` |
| General course-support knowledge | this wiki |
| Python and CSE learning systems | `03-WIKIS\PYTHON\` |
| Physics learning system | `03-WIKIS\PHYSICS\` |
| Current sequencing and next actions | CASTLE and `NOW.md` |

An official course source overrides every derivative page here.

## Structure

```text
raw/                 immutable supporting sources
wiki/
  index.md            canonical catalog
  current-position.md cross-course status and verification gaps
  course-briefs/      semester-wide policy and requirement comparisons
  courses/<course>/   course-specific maps and study aids
  methods/            reusable learning methods
  references/         education-system research
  log.md              append-only operational history
```

Create a course folder only after real course material or a real study need
exists. A subject with enough durable staged material SHOULD graduate to its
own wiki.

## Operations

### INGEST

1. Identify the course and exact learning question.
2. Verify the authoritative course file and its date/section.
3. Check the course AI policy before assisting.
4. Read supporting sources completely in bounded chunks.
5. Update the existing course page before creating another.
6. Separate confirmed requirements, provisional mappings, guidance, and
   unknowns.
7. Update the catalog, current position, and log when their state changes.

### QUERY

1. Read `wiki\current-position.md`.
2. Load the relevant course folder only.
3. Consult shared methods or references only when required.
4. Answer at the level allowed by the course policy.
5. End with a concrete study action or verification need.

### LINT

Check official-source precedence, course-policy visibility, ownership,
duplicated PYTHON or PHYSICS content, stale course facts, premature study
aids, unresolved links, index drift, and missing evidence of learning.

## Academic integrity

AI MAY explain concepts, generate private practice, review Chris's reasoning,
and help plan independent work. AI MUST NOT produce prohibited graded
submissions or bypass a course-specific restriction. When policy is unclear,
use the most restrictive verified interpretation until Chris resolves it.

## Raw boundary

`raw\` is immutable. AI MUST NOT create, edit, move, rename, archive, or delete
anything under it without Chris explicitly authorizing a named exception.

## Proof and close

Proof is successful explain-back, retrieval, problem solving, or later course
performance—not page creation. Close by recording changed status, evidence,
the next study action, and any fact still requiring official verification.
