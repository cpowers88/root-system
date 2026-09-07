---
type: report
timeline: log
status: complete
tags: [school, governance, syllabus, audit]
---

# Course Hat and Syllabus Alignment Audit — Codex

## Purpose

Review every active Fall 2026 course hat against the live exact-section or
reference-only syllabus evidence now registered in
`02-LIBRARY\00-SCHOOL\SYLLABUS_STATUS.md`. The review covers the EDUCATION
course hats plus the PHYSICS and PYTHON subject hats and their controlling wiki
owners.

This is the review record for the school-content commit that follows this drop.
It does not claim that the corrections below are already implemented.

## Evidence Boundary

Exact-section Fall 2026 evidence exists for:

- CSE 1321 BF / CRN 81262
- CSE 1321L 04 / CRN 86703
- ECON 1000 BAC / CRN 80643
- TCOM 2010 04 / CRN 85633

Reference-only evidence exists for:

- PHYS 2211 Sections 51 and 55; neither is Chris's registered Section 54
- ENGR 1000 Summer 2026 W01 / CRN 51735; this is not Chris's Fall BWD / CRN 80858

Chris's registration record independently confirms the real Fall sections,
meeting times, locations, and currently listed instructors. PHYS 2211 Section 54
and ENGR 1000 BWD still show no specified instructor.

## Verdict by Hat

| Hat | Verdict | Required correction |
|---|---|---|
| `HAT_EDUCATOR.md` | Minor correction | Describe ENGR's no-AI rule as a protective default pending the real BWD syllabus; route course-specific policy to the subject hats |
| `HAT_EDUCATOR_PLAYBOOKS.md` | Pass | No syllabus-bearing course facts |
| `HAT_ENGINEERING_PLAYBOOKS.md` | Pass | No syllabus-bearing course facts |
| `HAT_ECON.md` | Material correction | Add the exact AI-credit rule; remove old makeup exceptions; record the announced extra-credit opportunity accurately |
| `HAT_TCOM.md` | Material correction | Add the editing/proofreading-only AI rule; remove the false single submission channel and universal filename; remove the invented Day 1 subject fallback; clear the stale missing-weights caveat |
| `HAT_ENGR1000.md` | Rewrite course-facts block | Separate verified Fall BWD registration truth from the Summer W01 reference; stop presenting W01 policies as confirmed BWD facts |
| `HAT_PHYSICS.md` | Critical correction | Remove Dr. Behera as Chris's confirmed instructor; label Section 51/55 policy, platform, grading, and pacing as provisional neighbor evidence |
| `HAT_PYTHON.md` | Pass with minor verification | Preserve the course alignment; reverify `.py`-only/all-files and IDE claims against the live FYE/D2L guidance or label their source explicitly |

## Exact Corrections Required

### ECON 1000

`HAT_ECON.md` correctly reflects the new two-exam/four-quiz structure, textbook,
meeting time, and Fall dates. Three issues remain:

1. The exact syllabus permits GenAI for any purpose only when its contribution is
   credited. Uncredited use is cheating. The hat currently omits this rule.
2. The hat carries three makeup exceptions from older evidence. The exact BAC
   syllabus says no makeup exams, quizzes, or assignments; a missed deadline earns
   zero.
3. The syllabus offers up to five extra-credit points through assignments announced
   in D2L. Record this without converting it into a guaranteed assignment schedule.

### TCOM 2010

`HAT_TCOM.md` needs a policy-and-submission correction:

1. AI-written assignments are plagiarism. AI may only edit or proofread, and the
   usage must be cited.
2. D2L is not the only submission channel outside the Business Email unit. The
   schedule also routes the group Progress Report through email and includes at
   least one email-based extra-credit activity. Follow the live assignment's exact
   channel.
3. The syllabus uses multiple filename patterns for individual work, drafts,
   finals, and group submissions. `LastName_04_AssignmentName.docx` is not a safe
   universal rule.
4. The fallback subject `Powers 04 Day 1 Check-In` is not present in the captured
   syllabus and should be removed. Follow the live Week 1 instruction.
5. The complete grading weights are now available; the old cut-off-table caveat is
   stale. The recycled January/Spring calendar warning remains valid.
6. Reconcile the textbook author line with the live EDUCATION brief/source record.

The same submission nuance should be reflected in
`03-WIKIS\EDUCATION\wiki\tcom-2010-semester-map.md`, which currently describes the
Business Email as the email exception but does not surface the Progress Report
exception in its operating note.

### ENGR 1000

`HAT_ENGR1000.md` currently conflates two distinct records:

- Verified Fall truth: BWD / CRN 80858, fully online, no meeting time, no specified
  instructor.
- Reference only: Summer 2026 W01 / CRN 51735, instructor Matt Marshall.

The hat must stop calling the source Fall 2025. No textbook, no late work, no extra
credit, grading weights, content sequence, and AI prohibition are all W01 evidence
and remain unverified for BWD. Continue using no AI-assisted submitted work as the
protective default until BWD's real policy arrives, but do not present it as a
confirmed BWD syllabus fact. Remove the advisor-warning scenario that treats the
Summer syllabus as a mislabeled CRN 80858 shell.

### PHYS 2211

The PHYSICS learning path is substantially aligned and its cross-section ledger
correctly distinguishes Sections 51, 54, and 55. The live instructor identity is
not aligned:

- `HAT_PHYSICS.md` names Dr. Behera as Chris's instructor.
- `03-WIKIS\PHYSICS\wiki\current-position.md` identifies the course as Dr.
  Behera's.
- The opening course-facts block in `03-WIKIS\PHYSICS\wiki\source-map.md` does the
  same.

Dr. Behera belongs to neighboring Section 55. Chris is registered for Section 54,
whose instructor remains unspecified. Section 51/55 evidence may support provisional
topic, textbook, platform, policy, and pacing preparation, but it cannot bind Section
54's instructor, weights, exam count, deadlines, or operational rules. The AI rule
from Section 55 should be retained as a conservative study-support boundary, clearly
labeled provisional until Section 54 posts.

### CSE 1321 / CSE 1321L

`HAT_PYTHON.md` and `03-WIKIS\PYTHON\wiki\syllabus-alignment.md` are close to the
new exact-section evidence. Instructor details, schedules, module order, Gradescope,
and the submitted-work AI prohibition align. The wiki correctly records the second
unlabeled lecture grading table, copied lecture-calendar text, and the Spring lab
calendar embedded in the Fall capture.

The exact Simple Syllabus captures do not themselves state `.py files only`, submit
all relevant files on every upload, or the PyCharm/OneCompiler/Colab list. These may
come from linked FYE guidance, but the hat should cite that owner or mark them for
D2L/FYE verification rather than imply that the new captures prove them.

## Commit Scope for This Drop

Recommended commit subject:

`school: reconcile Fall 2026 course pathways and syllabus controls`

Recommended commit body:

- align ECON, TCOM, ENGR, PHYSICS, and PYTHON course controls with current evidence
- preserve exact-section versus reference-only boundaries
- add the CSE semester pathway and course-core reinforcement
- add EDUCATION semester maps and just-in-time ECON study support
- preserve unresolved PHYS 2211 Section 54 and ENGR 1000 BWD instructor/policy gates
- record the Codex course-hat audit and acceptance conditions

The commit should include this report and the matching DAILY pointer. It should only
claim a hat as corrected after the corresponding live file has been patched and
reviewed. Do not sweep machine-local configuration into this school-content commit.

## Acceptance Bar Before Commit

1. Apply the hat and Physics-owner corrections above.
2. Search all live hats and course-owner pages for stale `Dr. Behera`, `Fall 2025`,
   universal TCOM submission/filename language, and old ECON makeup exceptions.
3. Verify the exact-section/reference-only boundary remains explicit everywhere.
4. Run the frontmatter audit because instruction and wiki files are being edited.
5. Run strict wiki lint for EDUCATION, PHYSICS, and PYTHON as supported by the
   canonical validator.
6. Run canonical root health and report `BLOCKER` or `PASS WITH DEBT` honestly.
7. Confirm both staged and unstaged whitespace checks pass.
8. Review the staged diff and exclude unrelated or machine-local configuration.

## Current State and Next Exact Action

The audit is complete; the correction patch is not. Next: update the five affected
course hats, `HAT_EDUCATOR.md`, and the three PHYSICS owner references, then run the
acceptance bar and create the intentional school checkpoint commit.

