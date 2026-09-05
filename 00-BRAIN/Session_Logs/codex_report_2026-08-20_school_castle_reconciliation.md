---
type: report
timeline: log
status: complete
tags: [school, fall-2026, castle, education, engr-1000, learning]
created: 2026-08-20
surface: codex
---

# Fall 2026 School / CASTLE Reconciliation

### Session report · Thursday, August 20, 2026 · Codex · Chris / CASTLE

**Chris's instruction:** review `04-SCHOOL` through the CASTLE lens, reconcile the
live semester information, preserve `FallKSU.xlsx` as the likely human checklist,
establish where weekly readings belong, make each course's weekly focus visible,
adapt the intake method to Chris's demonstrated learning patterns, elevate
pseudocode in CSE, and use the neighboring ENGR 1000 web syllabi without treating
any of them as Chris's missing BWD syllabus.

## Outcome

The **Markdown/wiki owner chain is reconciled and validated**. The school area now
has one launch page, an explicit weekly translation rule, a reading owner, a
workload owner, current source-status boundaries, five-course weekly focus rows,
and a narrowed ENGR gap. These changes are in commit **`13bdb4e` (`school update`)**,
which is present on both local `main` and `origin/main` at report time.

The **workbook itself is not yet reconciled**. `FallKSU.xlsx` remains the preferred
human-facing checklist design, but its May-era class roster and war-room content
cannot be treated as current semester truth. This Codex surface did not have the
required spreadsheet artifact runtime, so no workbook cells, tabs, formulas, or
fonts were changed. Its reusable structure should be retained; its facts must be
repopulated from the owner files named below.

## CASTLE ruling: one human cockpit, separate factual owners

The operating model is now:

| Need | Owner |
|---|---|
| Human checklist and check-off view | `04-SCHOOL\FallKSU.xlsx` after refresh |
| Weekly load, due work, and collision risk | `04-SCHOOL\semester-workload-plan.md` |
| What to read/open and to what page | `04-SCHOOL\semester-reading-plan.md` |
| Verified dates, rooms, weights, and policies | `04-SCHOOL\SEMESTER_MAP.md` |
| Exact, provisional, and missing source status | `04-SCHOOL\SYLLABUS_STATUS.md` |
| Domain learner truth | the owning PYTHON, PHYSICS, or EDUCATION wiki |
| Today's chosen action | `NOW.md` |

`04-SCHOOL\README.md` is the new launch page connecting those owners. The workbook
is a **view and working checklist**, not a second source of truth. When its content
conflicts with an exact-section syllabus, D2L, an instructor, or a live owner page,
the workbook is corrected; the conflict is never silently resolved in its favor.

## Weekly rule now in force

Every Sunday, each current course receives one visible row:

`week → course → focus → reading/open → graded work → proof → due → status`

The weekly-plan template and the active Aug 17–23 plan now require all five course
rows. This solves the discoverability problem that prompted the request: the weekly
focus is visible in the plan, the reading detail stays in the reading plan, and the
workbook becomes the place Chris can scan and check off the translated rows.

The workbook refresh has two explicit human-interface requirements:

1. retain a checklist-first layout instead of turning the workbook into a hidden
   database; and
2. use **13-point or larger body text**, matching Chris's stated readability need.

## Reading rule and intake method

`semester-reading-plan.md` is the cross-course reading assembler. It records an
owner for each course, page-number conventions, week-by-week readings, and honest
gaps rather than invented assignments. Reading is not expected to fit only into a
short evening block: the estimated load is 6–8 hours per week, with part of it
deliberately placed in campus gaps.

The learning loop selected for Chris is:

1. **Preview the target:** name the week's focus and the proof before opening the
   source.
2. **Read narrowly:** open only the assigned section, module, or directions.
3. **Close the source and retrieve:** explain the idea from memory, draw the model,
   or write the algorithm in plain language.
4. **Write pseudocode before CSE implementation:** state inputs, outputs, decisions,
   loops, and edge cases without leaning on Python syntax.
5. **Produce cold proof:** solve, code, calculate, or outline without copying the
   example.
6. **Record the miss:** the next study block begins with the failed step, not a full
   passive reread.

This is the evidence-producing route toward 90%+ work; it is not a grade guarantee.
The crucial change for CSE is that **working code alone is no longer accepted as the
only proof**. Pseudocode exposes whether the algorithm is understood independently
of syntax and supports written quizzes, tracing, exam reasoning, and debugging. The
active weekly plan now names pseudocode as an explicit CSE proof.

## ENGR 1000 evidence reconciliation

Chris's exact registered section is **BWD (80858)** with Kamyar Raoufi. Its Fall
2026 syllabus and dated D2L execution remain missing.

Three neighboring Fall 2026 web syllabi were compared across their course-specific
sections:

| Capture | Result |
|---|---|
| BWB (80862) | Course-specific body matches BWF |
| BWF (80860) | Course-specific body matches BWB |
| BWC (80857) | Same core; omits only one redundant “no textbook required” sentence |

Their common provisional structure is unusually strong:

- no textbook;
- seven assignments: Virtual Scavenger Hunt, Time Management, Professional
  Communication/resume, Engineering Ethics, Professional Licensure, Student
  Engagement, and Engineering Design;
- departmental quizzes 50% and homework/other quizzes 50%;
- lowest departmental quiz and lowest non-attendance grade dropped;
- no late work and no extra credit;
- D2L owns due dates; and
- AI use is prohibited.

**Boundary:** this does not establish BWD dates, weekly order, quiz mechanics,
synchronous/asynchronous execution, partnership requirements, or Raoufi-specific
instructions. No neighboring prompt is treated as Chris's assignment. The three
captures remain in `77-INBOX`; nothing was placed into immutable `raw` by AI.

Until BWD says otherwise, submitted ENGR work is treated as **AI-prohibited**. The
safe preparation is administrative: open the exact BWD shell, identify every item,
record the date/status, and build the twice-weekly D2L check habit. Do not pre-do a
neighboring section's work.

## Course-policy corrections preserved

- **PHYS 2211 §54:** exact syllabus received Aug 18. AI may support explanation,
  guided technique, examples, and clarification, but may not produce submitted
  work or WebAssign answers.
- **TCOM 2010 §04:** AI may edit/proofread Chris's existing writing with cited use;
  it may not draft the assignment.
- **CSE 1321 / 1321L:** AI remains prohibited on submitted work.
- **ECON 1000:** AI is permitted when credited, subject to the exact assignment and
  instructor directions.
- **ENGR 1000:** treat as prohibited until exact BWD evidence says otherwise.

## Files reconciled

The implementation touched the following owner chain:

- `04-SCHOOL\README.md` — new launch page and Sunday translation rule.
- `04-SCHOOL\semester-reading-plan.md` — reading assembler and ENGR standing row.
- `04-SCHOOL\semester-workload-plan.md` — corrected planning relationship.
- `04-SCHOOL\SEMESTER_MAP.md` and `SYLLABUS_STATUS.md` — current authority and gap
  boundaries.
- PHYS, TCOM, and ENGR `work\README.md` files — course-local execution boundaries.
- CASTLE's weekly-plan template and active Aug 17–23 plan — required five-course
  focus/reading/graded/proof view; pseudocode elevated.
- EDUCATION `OPERATIONS.md`, current position, Fall course briefs, index, log, and
  source map — ownership and evidence chain reconciled.
- `HAT_EDUCATOR.md` and `HAT_ENGR1000.md` — execution stance and current instructor.
- `SYSTEM_FLAGS.md` and `SYSTEM_FLAGS_DETAIL.md` — flag #57 narrowed to the exact
  ENGR BWD gap.

A dead PHYSICS wikilink found by validation was repaired to the live owner page.

## Validation and repository state

After the repair:

- frontmatter audit: **CLEAN, 0 findings**;
- Markdown link integrity: **PASS** after repairing the one dead active-plan link;
- `git diff --check`: **PASS**;
- final canonical `root_health.py`: **PASS** across boot/governance, wiki
  navigation, frontmatter, skill mirrors, whitespace, and Markdown integrity; and
- the implemented reconciliation is committed and synchronized as **`13bdb4e`**.

The health gate does not prove semantic freshness, cadence completion, source
ownership decisions, or duplicate-source disposition. Those were reviewed manually
for the school owner chain described in this report.

## Open items and next exact actions

1. **Refresh `FallKSU.xlsx`.** Preserve the dashboard/checklist concept and 13-point
   readability, but replace the May roster and content with the current five-course
   owner data. Add the weekly schema above. Do not copy facts back into owner pages
   merely because they appear in the workbook.
2. **Aug 21:** check for Raoufi's reply / exact BWD syllabus. Keep flag #57 open if
   nothing arrives.
3. **Aug 24:** reconcile exact D2L shells for all courses. Highest-value checks are
   ENGR BWD dates and quiz mechanics, ECON book/page access, TCOM derived dates, and
   CSE posted dates.
4. **CSE schedule follow-up:** today's earlier Session Log records an official Fall
   FYE schedule that resolves the final date and reports quiz-date drift in weeks
   10–13. Those findings were not incorporated into the owner pages by this
   reconciliation pass and need a dedicated source-to-owner correction before the
   older quiz rows are trusted.
5. **Weeks 1–3:** measure real reading time and replace the current estimates. Grade
   protection depends on adapting from observed proof and error patterns, not
   defending a forecast.

## Details not to forget

- `FallKSU.xlsx` is valuable because it matches Chris's visual/checklist preference;
  value of the interface does not validate its stale facts.
- `99-EDG` is deferred prior-course material, not a Fall 2026 active course.
- ENGR has no safe provisional textbook reading. Its weekly “reading” is the exact
  D2L announcement, module/video, assignment directions, and quiz instructions.
- The neighboring ENGR agreement is evidence about shared structure only. BWD and
  Raoufi remain binding.
- Pseudocode is now part of CSE intake and proof, not an optional decoration added
  after the code works.
