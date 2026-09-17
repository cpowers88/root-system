---
type: reference
tags: [school, fall-2026]
source: "ECON exact-section evidence in immutable EDUCATION raw; active TCOM exact-section copy in 04-SCHOOL/03-TCOM; ENGR neighboring Fall 2026 BWB/BWC/BWF copies in 04-SCHOOL/05-ENGR — ownership and ENGR corpus reconciled 2026-08-22"
timeline: reference
---

# Fall 2026 Course Briefs — ECON 1000 · TCOM 2010 · ENGR 1000

Study-support distillation of ECON, TCOM, and ENGR. Active official course copies Chris
receives from KSU belong in `04-SCHOOL\<course>\`; existing wiki `raw\` captures remain
immutable evidence. General course materials (notes, datasets, textbooks) also live in
`04-SCHOOL\` — this page
exists so any session supporting Chris's Fall coursework knows the structure,
the deadlines rhythm, and above all **each course's AI policy** before
touching anything. `04-SCHOOL\SYLLABUS_STATUS.md` is the
authoritative index of which source file is exact-section vs. reference-only
across all six Fall courses, including CSE and PHYS (owned by PYTHON and
PHYSICS, not this page).

## ⚠️ AI Policies — Three Courses, Three Different Rules

| Course | AI policy | Practical rule for sessions |
|---|---|---|
| ECON 1000 | **Allowed for any purpose, must be credited.** Uncredited use = cheating (KSU Code of Academic Integrity) | Support freely; every AI contribution must be acknowledged in the submission |
| TCOM 2010 | **AI-written assignments = PLAGIARISM.** AI only for editing/proofreading, and only with cited usage | Never draft; review/proofread only, and the usage must be cited |
| ENGR 1000 | **AI use prohibited** across three neighboring Fall 2026 web sections; exact BWD not yet verified | Treat submitted BWD work as AI-prohibited; concept explanation and study planning only |

These sit under the Wiki Shared Layer's academic-integrity rule: syllabi
read for topics, dates, and policies — never for producing gradeable work
beyond what each course's own policy allows.

## ECON 1000 — Contemporary Economic Issues (BAC / 80643)

**Status: exact section**, captured directly from Simple Syllabus 2026-07-21
and recaptured 2026-07-27 with exact meeting information.

- **Format:** 2 credit hours, 14 weeks, face-to-face Tue/Thu 8:00–8:50 am,
  Marietta Q-202. Instructor: Zeynep Kelani (zkelani@kennesaw.edu; office
  hours by appointment Tue 9:15–11:00).
- **Textbook (real, assigned):** *Contemporary Economic Issues*, Mathews &
  Patrono (5th ed.) — delivered as an eBook through D2L's Day One Access
  program, not an independently downloadable or linkable file. No external
  free link exists or is expected; access arrives automatically inside D2L
  once the course populates (tracks `SYSTEM_FLAGS.md` #57's Aug 24 timeline).
  OpenStax and CORE Econ (below) remain the free stand-ins until then.
- **Grading:** Exam 1 25% · Exam 2 (Final) 25% · Quizzes 50% (four quizzes,
  two lowest dropped, two highest each count 25%). Scale ~89.5 = A cutoff,
  rounded per the syllabus's own uneven boundary table.
- **Assessments:** 2 exams (40 MC, 60 min, online via D2L, NOT cumulative,
  both mandatory, zero make-ups/extensions) + 4 quizzes (10 MC, 20 min,
  same no-extension policy). All due 11:00 pm Eastern.
- **Confirmed Fall 2026 schedule spine:** Ch. 1–5 → Quiz Ch. 1-2-3 (wk 3,
  9/8) → Quiz Ch. 4-5 (wk 5, 9/22) → **Exam 1 Tue 9/29 (Ch. 1–5, online, no
  class meeting)** → Ch. 7–9 → Quiz (wk 9, 10/22) → Ch. 10–12 → Quiz (wk 12,
  11/12) → Financial Literacy special section + extra-credit quiz (wk 13) →
  **Final Exam Thu 12/3 (Ch. 7–12 only, online)**.
- **Topics:** production models, economic systems (capitalism vs socialism),
  markets/surplus/deadweight loss, GDP & growth, inflation, unemployment,
  market failure, government failure, inequality & redistribution,
  financial literacy.
- Danger-weeks note: Chapters 7–9 and 10–12 land inside Oct 5 – Nov 11 —
  the school-only window covers the entire back half of this course.
- **Provisional semester map:** [[courses/econ-1000/semester-map]] — maps the
  confirmed real schedule to CORE Econ's confirmed units, OpenStax's
  expected chapters, and the FRED datasets. Lower confidence than TCOM's
  map (real textbook is D2L-locked); re-check once D2L opens.
- **Reading/dataset prep (independent study only, not submitted work):**
  Four real FRED series (`GDP`, `GDPC1`, `CPIAUCSL` inflation, `UNRATE`
  unemployment) are already pulled and live at
  `04-SCHOOL\04-ECON\datasets\` (fetched 2026-07-21 via
  `00-BRAIN\scripts\fetch_fred.py`; re-runnable any time for current data).
  Two open textbooks are placed alongside the syllabus in the same folder:
  OpenStax *Principles of Economics 2e* and CORE Econ's *The Economy 2.0*.
  Two Federal Reserve sources now sit in this hub's immutable `raw/`: the
  FRED/BLS CPIAUCSL clipping and David Wheelock's four-page Great Depression
  overview. They are fully processed into five just-in-time reading chunks,
  a flashcard batch, and a solution-free reasoning drill at
  [[courses/econ-1000/reading-guides/great-depression-cpi]]. They unlock during Weeks
  7-14 and are not assigned course readings unless the instructor says so.
  World Bank Open Data (not yet pulled) covers the economic-systems
  cross-country comparisons. Practicing real SQL/visualization reps against
  the FRED series doubles as progress on the July weak-link list
  ([[current-position]] items #1 SQL reliability and #4 decision-facing data
  visualization) while front-loading course content. St. Louis Fed's free
  economic-education pages (https://www.stlouisfed.org/education) are a
  solid plain-language supplement to the paywalled textbook.

## TCOM 2010 — Technical Writing (Section 04 / 85633)

**Status: exact section**, captured directly from Simple Syllabus 2026-07-21
and recaptured 2026-07-27 with exact meeting information.

- **Format:** 3 credit hours (prereq ENGL 1101), Radow College. Instructor:
  Lisa Diamond (ldiamon@kennesaw.edu or lisa.diamond@kennesaw.edu — email
  only; MS Teams evening meetings by appointment).
- **Textbook (real, assigned):** *Open Technical Communication*, 4th ed.
  (Tiffani Tijerina, Tamara Powell, Jonathan Arnett, Monique Logan, Cassandra
  Race — KSU-affiliated authors), published by Affordable Learning Georgia,
  CC-BY 4.0, genuinely free — https://alg.manifoldapp.org/projects/open-technical-communication.
  Now in `raw/Open-TC-PDF.pdf`, along with its instructor ancillary package
  and per-example worked files. Full week-by-week resource map:
  [[courses/tcom-2010/semester-map]].
- **Content:** technical descriptions, instructions, proposals,
  recommendation reports; rhetorical theory, audience analysis, document
  design, visual aids, editing; at least one complete technical report,
  produced in groups. Units visible in the schedule: business email +
  memos, ethics analysis, audience analysis, elevator speech, individual
  project proposal, group technical report (with oral presentation and
  reflective memo), instructions unit with in-class usability testing.
- **This class meets in person and is not online** — attendance is
  mandatory and graded (first 3 unexcused absences free, then a
  cumulative grade penalty).
- **Grading weights:** Business Email 15 · Audience Analysis unit 5 ·
  Presentations & Proposals 15 · Technical Report Oral Presentation 15 ·
  Technical Report Written Report 20 · Instructions unit 15 · Graded
  Exercises 15 (total 100).
- **Late work:** –10%/day until the class set is graded, then closed; no
  late Discussions/Quizzes/Extra Credit.
- **Confirmed still-recycled dates:** the syllabus's own weekly calendar
  carries January/Spring due-dates (e.g. "due Tuesday, January 20th")
  inside a Fall Semester 2026 document — present in this fresh capture too,
  so it is KSU's own Simple Syllabus template issue, not a stale-source
  artifact on our side. The weekly rhythm (Tue class / Thu units) is
  reliable; **trust D2L, not the printed dates**, for real Fall 2026
  deadlines.
- Serves Area F for engineering/CS majors — the professional-writing rep
  feeds every client-facing artifact skill in the business track.
- **Reading prep:** the syllabus already links its own sample documents
  (business email, technical report, proposal, instructions) directly in
  the weekly calendar — pull those now rather than sourcing new examples.
  Given the strict AI-editing-only policy, this course is a reading-craft
  target, not a dataset-integration one.

## ENGR 1000 — Introduction to Engineering (⚠️ strong provisional pattern)

**Status: exact Fall 2026 BWD still missing.** The registrar identifies BWD as
online with no meeting time; Kamyar Raoufi is the instructor, supplied by Chris.
Three neighboring Fall 2026 web sections — BWB, BWC, and BWF — provide a measured
departmental-policy pattern. Byte comparison shows BWB/BWF share a template apart from
identifiers, while BWC omits seven blocks.

- **Common structure across all three:** no textbook; departmental quizzes 50%
  + homework/other quizzes 50%; lowest departmental quiz and lowest
  non-attendance grade dropped; no late work; no extra credit; D2L owns dates;
  AI use prohibited.
- **Common seven assignments:** Virtual Scavenger Hunt, Time Management,
  Professional Communication/resume, Engineering Ethics, Professional
  Licensure, Student Engagement, and Engineering Design.
- **Common outcomes:** engineering disciplines, advising/plan of study, campus
  resources, study/time-management skills, basic math/programming, and teamwork.
- **Still BWD-unknown:** D2L dates and weekly order, quiz and attendance behavior,
  synchronous vs. asynchronous execution, partnership requirements, and Raoufi-specific
  policy.
- Do not prepare or pre-complete neighboring-section assignments. Use the common
  structure only to establish the weekly D2L check and recognize what may appear.

## Data-Quality Flags (for Chris)

1. **ENGR 1000 BWD execution evidence remains missing despite a reasonable departmental
   pattern across three neighboring Fall 2026 web sections.** All three defer dates to D2L.
   Treat shared policy as provisional; verify BWD dates and behavior in D2L on August 24.
2. **TCOM's schedule table still shows January/Spring dates** in the fresh
   July 21 capture — confirmed as KSU's own recycled Simple Syllabus
   template, not a one-off transcription error. Trust D2L for real dates.
3. ECON's confirmed schedule has no outstanding data-quality issue as of
   this capture.

## Links

Related: [[references/ai-programs-us-2026]] (KSU degree-landscape context).
Syllabus captures: `03-WIKIS\EDUCATION\raw\Syllabi\`. General course
materials: `04-SCHOOL\`. Full six-course current-section
index: `04-SCHOOL\SYLLABUS_STATUS.md`. Calendar tagging for
these dates: `SYSTEM_FLAGS.md` #51 (Fall CASTLE calendar blocks, due before
Aug 24).
