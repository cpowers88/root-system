---
type: index
timeline: now
tags: [school, syllabus, fall-2026]
---

# Syllabus Status — Fall 2026

**Active-copy ownership, reconciled 2026-08-22:** `WHERE_IT_GOES.md` governs new official
course material: the working copy Chris receives from KSU lives in the matching `04-SCHOOL`
course folder. Existing wiki `raw\` captures remain immutable evidence; this reconciliation
does not move or rewrite them. This file is the cross-course source-status index.
Classes start **August 24, 2026** — see the Pre-Semester Punch List at the
bottom for what has to close before then.

## Current-Section Sources

| Course | Registered section | Active Markdown source | Status |
|---|---|---|---|
| CSE 1321 | BF (81262) | `03-WIKIS\PYTHON\raw\syllabi\CSE 1321 BF (81262) Fall 2026 Syllabus.md` | Exact section |
| CSE 1321L | 04 (86703) | `03-WIKIS\PYTHON\raw\syllabi\CSE 1321L 04 (86703) Fall 2026 Syllabus.md` | Exact section |
| ECON 1000 | BAC (80643) | `03-WIKIS\EDUCATION\raw\Syllabi\ECON 1000 BAC (80643) Fall 2026 Syllabus.md` | Exact section |
| TCOM 2010 | 04 (85633) | `04-SCHOOL\03-TCOM\TCOM 2010 04 (85633) Fall 2026 Syllabus.md` | Exact section, active course copy |
| **PHYS 2211** | **54 (83722)** | **`03-WIKIS\PHYSICS\raw\syllabus\Syllabus.pdf`** | ✅ **Exact section — received 2026-08-18** direct from Farhan Islam. Byte-identical working copy at `04-SCHOOL\02-Physics I\Syllabus.pdf` (hash verified). Lists recitations 51–54 under one lecture, **including §54 (Fri 11:30–12:25, Atrium 1116)** |

## Reference-Only Sources

| Course | Registered section | Available Markdown source | Use boundary |
|---|---|---|---|
| ~~PHYS 2211~~ | ~~54 (83722)~~ | **Superseded 2026-08-18 — see the exact-section row above.** The `raw/` §51 capture stays as immutable evidence; the two `04-SCHOOL` working copies (§51 and §55) were archived to `99-ARCHIVE\ARCHIVED_2026-08-18_PHYS_neighbour_syllabi\` because they sat beside the real `Syllabus.pdf`. `99-ARCHIVE\ARCHIVED_2026-07-29_PHYS 2211 54 (52148)…md` remains a Summer-term scope corroboration only | **No longer used for pacing.** §51 is now known to be a *sibling recitation of Chris's own lecture*, which is why it paced the course well; §55 is Behera's separate lecture |
| ENGR 1000 | BWD (80858) | Three neighboring Fall 2026 web captures in `04-SCHOOL\05-ENGR\`: BWB (80862), BWC (80857), BWF (80860) | None is BWD. BWB/BWF share a template apart from identifiers; BWC omits seven blocks. Use the shared departmental policy provisionally, never BWD dates or execution |

## Missing Current Sources — **one real gap left**

- ✅ **PHYS 2211 Section 54 — CLOSED 2026-08-18.** Chris obtained the exact syllabus direct
  from Farhan Islam. Grading weights, all four unit-exam dates plus the final, the AI policy,
  and a clean internally-consistent 15-week calendar are all now known. **The registration
  record's MWF 9:10–10:05 + Fri 11:30–12:25 is confirmed** — note the syllabus header
  mistakenly says "Monday, Wednesday, and Thursday", contradicted by all 45 of its own dates.
  Full reconciliation: `03-WIKIS\PHYSICS\wiki\semester-pathway.md`.
- **ENGR 1000 Section BWD** still has no exact-section source. The remaining actionable gap is
  its D2L-owned dates and execution evidence; every neighboring syllabus defers dates to D2L.
- D2L opens **Aug 24**; course content is not populated before then, which is expected.

Recheck Simple Syllabus and D2L when the courses populate. Exact-section materials supersede reference-only sources when they become available.

## ENGR 1000 — byte-compared 2026-08-22 against three Fall 2026 web sections

The live BWB (80862), BWC (80857), and BWF (80860) files are canonical course copies in
`04-SCHOOL\05-ENGR`. Byte comparison shows BWB and BWF share the same template apart from
section/CRN/instructor identifiers. BWC is a shorter variant that omits seven blocks present
in the other two. Across two instructors, all three still agree on:

- the same seven assignments;
- departmental quizzes 50% and homework/other quizzes 50%;
- the lowest departmental quiz and lowest non-attendance grade dropped;
- no late work, no extra credit, no textbook, and D2L-owned dates;
- the same learning outcomes; and
- AI use prohibited.

**Ruling:** this is strong provisional common structure. It does not establish
BWD dates, weekly order, quiz mechanics, synchronous/asynchronous execution,
attendance-quiz behavior, partnership requirements, or Raoufi-specific policy.

### Earlier references no longer live

The previously cited Fall 2025 BD and §05 paths are absent from the live tree and were never
Git-tracked, so they are not valid active evidence. The Summer W01 reference was deleted in
the July 27 archive commit and is recoverable from Git history, but restoring it is outside
this reconciliation. No conclusion here depends on those three files.

Kamyar Raoufi is Chris's BWD instructor, supplied by Chris on August 17. The registrar record
lists no meeting time; the course code and neighboring web sections support online delivery,
but D2L must establish how Raoufi actually runs it.

**Consequence for the escalation email:** the question to Raoufi is no longer
"what is the general course structure?" It is **when BWD work opens/closes and
how the 50% departmental-quiz component operates in his section** — details the
neighboring sections cannot answer.

**Index correction, updated 2026-08-22:** this table previously pointed ENGR at
`ENGR 1000 W01 (51735) Summer 2026 Syllabus - Reference Only.md`. **That file does not
exist anywhere in the live tree** — a broken reference the index carried since the
July 27 recapture note recorded archiving it as a duplicate. The reference row now names
the three Fall 2026 neighboring-section files that actually live in `04-SCHOOL\05-ENGR`.

## July 27 Recapture

Fresh Simple Syllabus captures replaced the July 21 working copies for CSE
1321, CSE 1321L, ECON 1000, and TCOM 2010. The course requirements did not
change; the new captures add exact meeting information. ECON also explicitly
states that attendance is strongly encouraged but not graded. The July 21
working copies are preserved under
`99-ARCHIVE/04-SCHOOL/SYLLABI_REPLACED_2026-07-27/`.

The ENGR 1000 W01 file delivered with this batch was body-identical to the
existing Summer reference. It was archived as a duplicate and does not close
the missing Fall BWD source gap.

## Physics Neighbor-Section Comparison

The two PHYS 2211 files are not duplicates and neither governs Chris's Section 54.

Shared course-level signals that may support provisional preparation:

- Calculus-based mechanics, waves, and special relativity.
- Serway and Jewett, 10th edition.
- WebAssign-supported homework.
- A broad mechanics sequence beginning with measurement, one- and two-dimensional motion, vectors, and forces.

Material section differences:

| Control | Section 51 | Section 55 |
|---|---|---|
| Instructor evidence | July 27 recapture names Farhan Islam and `fislam7@kennesaw.edu`; supersedes the July 21 capture's missing instructor block | Instructor block and faculty profile name Swayamprabha Behera |
| Unit exams | Four tests; best three count | Three exams stated in grading and calendar, although one prose line inconsistently mentions four |
| Final weight | 25% | 30% |
| Participation structure | Attendance 7.5% plus recitation 7.5% | Participation 10% |
| Calendar reliability | Contains conflicting final-exam dates and other section-specific entries | Contains recycled/impossible entries, including a January opt-out deadline and an August MLK holiday label |

Safe use: triangulate prerequisite concepts and broad topic coverage. Unsafe use: Section 54 deadlines, instructor policy, grade weights, exam count, attendance rules, or pacing.

## Replacement Record

On 2026-07-21, active school-library syllabus PDFs were replaced by Markdown captures for easier search and use. The retired PDFs and the stale ECON Markdown copy were preserved under:

`99-ARCHIVE/04-SCHOOL/SYLLABI_REPLACED_2026-07-21/`

Unrelated PDFs, including textbooks, lecture slides, and document examples, were not moved. Immutable wiki `raw/` evidence was not changed.

**2026-07-29 addendum:** six older, pre-July-21 legacy syllabus captures that
were sitting loose at the `99-ARCHIVE` root without the `ARCHIVED_YYYY-MM-DD_`
prefix — `CSE_lab_syllabus.md`, `CSE_lecture_syllabus.md`, `ECON_syllabus.pdf`,
`ENGR_syllabus.pdf`, `TcomSyllabus.PDF`, `physics-ARCHIVED.pdf` — were
confirmed superseded by the current captures above and renamed with the
`ARCHIVED_2026-07-29_` prefix in place. No content changed.

## Pre-Semester Punch List — before August 24, 2026

**One gap remains.** Everything else in this file is filed and current.

| Gap | Owner | Next check | Trigger |
|---|---|---|---|
| ~~PHYS 2211 §54 exact syllabus~~ | — | ✅ **CLOSED 2026-08-18.** The Aug 17 escalation email to Islam worked — the syllabus arrived the next morning | — |
| **ENGR 1000 BWD D2L dates and execution evidence** | Chris — D2L, then Kamyar Raoufi (`kraoufi@`) if details are absent | Verify BWD in D2L **Aug 24**: dates, weekly order, quiz windows, attendance-quiz behavior, synchronous/asynchronous execution, drop rules, and any instructor variation. Until then use the departmental pattern provisionally and treat AI as prohibited | `SYSTEM_FLAGS.md` #57 |

**The escalation is worth recording as evidence, not just as a closed row.** Both emails
went out Mon Aug 17 after `SEMESTER_MAP.md` established that D2L would not open until Aug
24 and email was therefore the only path. PHYS answered within a day. That converted the
semester's largest unknown into its best-documented course with six days to spare.

**AI policies, all five courses:**

| Course | Policy |
|---|---|
| CSE 1321 / 1321L | Prohibited on submitted work |
| ENGR 1000 | Treat as prohibited on submitted work; all three neighboring Fall 2026 web sections prohibit it, exact BWD still pending |
| **PHYS 2211 §54** | **Permitted as a tutoring resource** (explanations, guided technique, examples, clarification); **prohibited in submitted work.** WebAssign is graded — no AI-produced answers |
| ECON 1000 | Permitted if credited |
| TCOM 2010 | AI may edit/proofread Chris's existing writing only, with cited usage; it may not draft assignments |

Nothing else blocks Aug 24 readiness — CSE 1321, CSE 1321L, ECON 1000, TCOM 2010 and now
PHYS 2211 all have exact-section sources in hand.
