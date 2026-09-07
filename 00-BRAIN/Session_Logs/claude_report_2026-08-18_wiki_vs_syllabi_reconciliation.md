---
type: report
timeline: now
status: active
tags: [school, fall-2026, syllabus, wiki, reconciliation, d2l, review]
created: 2026-08-18
session_date: 2026-08-18
---

# Wiki folders vs. the workload plan and the exact-section syllabi — full reconciliation

### Written 2026-08-18, Claude Code, CASTLE session. **Nothing was edited.** This is a findings report against four hub maps, two cross-course indexes, one plan, four exact-section syllabi, and the registrar record. Every claim below cites the file and line that produced it.

**Why this exists.** `04-SCHOOL\semester-workload-plan.md` §8 lists seven D2L
reconciliation checks — the shortest description of what is still unverified across the
five courses. This session started there and worked outward, checking every wiki page that
feeds it against the primary sources. The seven are all still open and correctly
prioritized. This report adds **three more**, and finds **seven defects** in the pages that
were supposed to be already reconciled.

**Nothing here is a discovered emergency.** The pattern that produced almost all of it is
one already named in the vault: *a claim written from memory of a source rather than from
the source.* It has now been caught four times (ECON Aug 13, TCOM Aug 18, and twice more
below), which is enough repetitions to be worth naming as a class rather than fixing case
by case. See § The error class, at the end.

---

## Method and authority stack

Read in this order, per `AGENT.md` § Session Start Protocol and § Course → hat routing:

1. `00-BRAIN\AGENT.md` → `00-BRAIN\CLAUDE.md` → `CHRIS_CORE.md` → `SYSTEM_FLAGS.md` →
   `01-NORTH_STAR\NORTH_STAR.md` → `00-BRAIN\CASTLE\OPERATIONS.md`
2. CASTLE local boot: `wiki\index.md`
3. The plan under review: `04-SCHOOL\semester-workload-plan.md`
4. The two authorities that outrank the syllabi:
   - **`04-SCHOOL\fall_KSU_schedule.md`** — registrar record. CRNs, credit hours, meeting
     times, rooms, instructors. This is the record that caught PHYS being logged as 4
     credits when it is 3.
   - **The PHYS 2211 §54 syllabus** — exact section, received direct from Farhan Islam
     2026-08-18.
5. The three remaining exact-section syllabi, read from `raw\` and not from any summary:
   - `03-WIKIS\EDUCATION\raw\Syllabi\TCOM 2010 04 (85633) Fall 2026 Syllabus.md`
   - `03-WIKIS\EDUCATION\raw\Syllabi\ECON 1000 BAC (80643) Fall 2026 Syllabus.md`
   - `03-WIKIS\PYTHON\raw\syllabi\CSE 1321 BF (81262) Fall 2026 Syllabus.md`
   - `03-WIKIS\PYTHON\raw\syllabi\CSE 1321L 04 (86703) Fall 2026 Syllabus.md`
6. The wiki pages under review:
   - `03-WIKIS\EDUCATION\wiki\courses\tcom-2010\semester-map.md`
   - `03-WIKIS\EDUCATION\wiki\courses\econ-1000\semester-map.md`
   - `03-WIKIS\EDUCATION\wiki\course-briefs\fall-2026-course-briefs.md`
   - `03-WIKIS\EDUCATION\wiki\current-position.md`
   - `03-WIKIS\EDUCATION\wiki\source-map.md`, `pre-semester-coverage-plan.md`
   - `03-WIKIS\PHYSICS\wiki\semester-pathway.md`
   - `03-WIKIS\PYTHON\wiki\syllabus-alignment.md`
   - `04-SCHOOL\SEMESTER_MAP.md`, `04-SCHOOL\SYLLABUS_STATUS.md`
   - `NOW.md`

**No `raw\` file was written, moved, or modified.** All reads only. No wiki page was edited
— these are three hubs' owner truth plus `04-SCHOOL`, and `CASTLE\OPERATIONS.md` §
Operating Authority forbids CASTLE rewriting another realm's owner truth. The fix ledger at
the end names each edit and its owner.

---

## Correction to the session's own premise

The session brief carried forward that *"TCOM's `semester-map.md` covers weeks 1–14 by range
but has no weeks 11–15 rows in the numbered sense."*

**That is not what the file says.** `tcom-2010\semester-map.md` has discrete numbered rows
for weeks **11, 12, 13 and 14** (lines 38–42). Its real structural gaps are:

- **Weeks 7, 8 and 9** — swallowed by the single `6–12` technical-report range row (line 36).
  The syllabus has distinct, differently-graded content in each of those three weeks.
- **Week 15** — genuinely absent.

**Week 15 is not a wiki defect.** The TCOM syllabus's own schedule table ends at
`**Week 14: Thursday**` (line 179) while its prose at line 207 states *"This course is
delivered over 15 weeks."* The source is short a week. The map faithfully reproduces a
source that stops early. That belongs on the D2L list, not on a fix list.

Recording this because the brief's version would have sent a fixer to the wrong rows.

---

## 🔴 HIGH — fix before Monday Aug 24

### 1. `semester-workload-plan.md` §3 is missing four labs and two assignments, and they fall in the weeks already rated 🔴

**Evidence.** The CSE 1321L schedule table
(`CSE 1321L 04 (86703) Fall 2026 Syllabus.md:142`) assigns lab and assignment work in this
sequence:

| Source slot | Topic | Lab due | Assignment due |
|---|---|---|---|
| 1 | Module 0 — Intro, Syllabus/IDE/Gradescope | — | — |
| 2 | Module 1 — Input/Output and Variables | **Lab 1 & Lab 2** | — |
| 3 | Module 1 — Data Types, Operators, Expressions | Lab 3 | **Assignment 1** |
| 4 | Module 2 — Selection Structures | Lab 4 | — |
| 5 | Module 2 — Repetition Structures | **Lab 5** | **Assignment 2** |
| 6 | Module 2 — Repetition Structures | **Lab 6** | **Assignment 3** |
| 7 | Module 3 — Functions | **Lab 7** | Assignment 4 |
| — | **MIDTERM EXAM week** — all sections, in their regular lab time | — | — |
| — | *(Spring Break in the source)* | — | — |
| 9 | Module 4 — Python Libraries | **Lab 8** | — |
| 10 | Module 5.1 — Tuples, lists | Lab 9 | Assignment 5 |
| 11 | Module 5.2 — Dictionary, searching & sorting | Lab 10 | — |
| 12 | Module 6 — OOP | Lab 11 | Assignment 6 |
| 13 | Module 6 — OOP | Lab 12 | — |
| 14 | Module 7 — Intro to Java | Lab 13 | Assignment 7 |
| — | **FINAL EXAM week** — all sections, in their regular lab time | — | — |

**What §3 actually lists.** Walking `semester-workload-plan.md:221–239` row by row, the CSE
1321L items named are: Lab 1 (wk 1) · Labs 2–3 + Assignment 1 (wk 2) · Lab 4 (wk 4) ·
Assignment 4 (wk 7) · Lab 9 (wk 9) · Lab 10 + Assignment 5 (wk 10) · Labs 11–12 +
Assignment 6 (wk 12) · Lab 13 + Assignment 7 (wk 14).

**Absent entirely: Labs 5, 6, 7 and 8, and Assignments 2 and 3.** Nine of thirteen labs and
five of seven assignments are on the page; the other six items are on no row.

**Why it matters more than a missing line.** In the source sequence those six items sit in
slots 5, 6, 7 and 9 — which map to **weeks 5, 6, 7 and 9** of the Fall term. Weeks 5 and 6
are already rated 🔴 in §3 (PHYS Unit Exam 1 + ECON Quiz Ch 4-5; ECON Exam 1 + CSE Quiz 3),
and week 7 carries CSE Test 1. The plan's estimated hours for those weeks — 22 h, 22 h,
19 h — are built on a table that omits two labs and two assignments due inside them.

**It is also an internal inconsistency, not just an omission.** §2's standing baseline
(line 180) states the lab floor as *"One lab most weeks → Gradescope; assignment in 6 of 15
weeks."* If §2 absorbs the labs, no lab should appear in §3. If §3 names them, all thirteen
should be there. As written, weeks 5–8 read lighter than weeks 9–14 for no reason that
exists in the source. Sunday-morning reading of §3 is the page's stated purpose (§7 line
349), so this is the one that will actually cost something.

**Also worth correcting while in there:** §2 line 180 says *"assignment in 6 of 15 weeks."*
There are **seven** assignments.

**Recommended fix.** Put every lab and every assignment in §3, and delete the lab/assignment
clause from §2's floor so there is one home for them. Re-estimate weeks 5, 6, 7 and 9.

---

### 2. `SEMESTER_MAP.md` carries a correction that was claimed but never made

**Evidence.** `03-WIKIS\EDUCATION\wiki\current-position.md:84–91` states:

> ~~**Weeks 6–15 are not yet extracted**~~ — **CORRECTED 2026-08-18. This claim was wrong.**
> … **The same wrong claim sat in `04-SCHOOL\SEMESTER_MAP.md` and was corrected there
> 2026-08-18.**

**It was not corrected there.** `04-SCHOOL\SEMESTER_MAP.md:138` still reads:

> `| 6–15 | Sep 29 → Dec 7 | | 🔴 **Not yet extracted — the technical report (35%) lands in this range** |`

The TCOM hub map has carried weeks 6–14 since 2026-07-21.

**And the correcting file contradicts itself.** `current-position.md:30` — the at-a-glance
status table at the top of the same page — still lists TCOM's blocking gap as
**"Weeks 6–15 not extracted."** Line 84 corrects the claim in prose; line 30 restates it as
current status. Same file, same date, opposite claims. A reader who stops at the status
table gets the wrong answer.

**Why this is the worst of the seven.** A stale claim is a known cost. A *claimed
correction* is worse: the vault now asserts that a fix exists, so no future session will
re-check `SEMESTER_MAP.md:138`. This is the same failure shape as flag #100 — a guard
written, believed, and not actually wired in.

**Recommended fix.** Correct `SEMESTER_MAP.md:138` to reflect weeks 6–14 as extracted
(pointing at the hub map) with week 15 marked as absent from the source. Correct
`current-position.md:30`. Then re-read both to confirm, rather than recording the intent.

---

### 3. TCOM's AI policy is recorded vaguer than its source states it

**Evidence — the syllabus is explicit**, and says it twice
(`TCOM 2010 04 (85633) Fall 2026 Syllabus.md:217` and again at `:419`):

> *"Using AI to write your assignments is considered PLAGIARISM. You may only use AI for
> editing or proofreading, if you cite the usage."*

The following sentence at `:219` removes the usual escape hatch:

> *"Re-writes are not permitted under any circumstances in this class for work that has been
> plagiarized. … Misunderstandings, miscommunication, oversights or lack of comprehension as
> to what constitutes plagiarized materials are not accepted in this course."*

**What the vault says.** `03-WIKIS\EDUCATION\wiki\course-briefs\fall-2026-course-briefs.md:25`
has it correct: *"AI-written assignments = PLAGIARISM. AI only for editing/proofreading, and
only with cited usage."*

But three files a session is far more likely to load say something weaker:

| File | Line | Text |
|---|---|---|
| `04-SCHOOL\SEMESTER_MAP.md` | 318 | "TCOM — verify per assignment." |
| `04-SCHOOL\SYLLABUS_STATUS.md` | 161 | "Verify per assignment" |
| `NOW.md` | 181 | (TCOM omitted from the AI-boundary list entirely) |

**Why this is the highest-consequence item in the report.** "Verify per assignment" reads as
*unknown* when the policy is in fact *known and restrictive*. `SEMESTER_MAP.md` and
`SYLLABUS_STATUS.md` are the cross-course authorities; `NOW.md` § Boundaries is the line a
session reads before touching coursework. TCOM is also the course with the **most writing
Chris will produce**, the one with graded work in Week 1, and the one where an AI's natural
instinct — *"let me draft this for you"* — is exactly the prohibited act. The other four
courses have unambiguous entries in all three files. TCOM, the one that needs the entry
most, has the softest.

`NORTH_STAR.md` §3 names the academic-integrity boundary as consequential and
`AGENT.md` § Academic Integrity makes it a hard stop. A hard stop recorded as an open
question is not a hard stop.

**Recommended fix.** Replace "verify per assignment" in both `04-SCHOOL` files with the
syllabus's actual sentence, quoted. Add a TCOM clause to `NOW.md` § Boundaries. The correct
operating rule is: **AI may proofread or edit Chris's own finished text, and the usage must
be cited in the submission. AI may not draft, generate, restructure from scratch, or produce
prose that enters a TCOM submission.**

---

## 🟠 MEDIUM — for the Aug 23 pre-semester review

### 4. Business Email FINAL is placed a week early in two files

**Evidence.** The syllabus places it at **Week 3 Tuesday** (`:41`):

> `| **Week 3: Tuesday** | | ***Business Email FINAL*** *due: file naming convention: …* |`

The Week 2 Thursday row (`:40`) also mentions it, dated *"Tuesday, January 27th"* — which,
in the recycled Spring calendar the document is built from (term start Jan 12, MLK Jan 19),
**is Week 3's Tuesday.** The two rows agree; the printed date is the giveaway, not the
contradiction.

| File | Placement | Verdict |
|---|---|---|
| `04-SCHOOL\SEMESTER_MAP.md:135` | Week 3, Sep 8 | ✅ correct |
| `semester-workload-plan.md:224` | **Week 2** (Aug 31–Sep 6) | ❌ one week early |
| `tcom-2010\semester-map.md:29` | "1–2" range row | ❌ one week early |

Two independent files made the same one-week error, which suggests both read the Week 2
Thursday row and stopped. Working a week early costs nothing; the risk is that §3's week-2
hour estimate carries an item that isn't due, and week 3's does not carry one that is.

---

### 5. A TCOM group oral presentation in Week 7 appears in no vault page

**Evidence** — `TCOM 2010 04 (85633) Fall 2026 Syllabus.md:50`:

> `| **Week 7: Thursday** | **Group Oral Presentations: Technical Report PPT** | Work on Technical Report projects … |`

This appears in **none** of: `tcom-2010\semester-map.md` (its `6–12` range row names only
draft sections), `04-SCHOOL\SEMESTER_MAP.md`, or `semester-workload-plan.md` §3 (whose week
7 row reads only *"TCOM Technical Report work begins"*).

**Why it matters.** The TCOM grading table
(`fall-2026-course-briefs.md:113–116`) gives **Technical Report Oral Presentation 15%** as a
category distinct from the written report's 20%. Week 12 already carries "Technical Report
Group Presentations." So either there are two presentation events — an early one in week 7
and the graded one in week 12 — or the week 7 row is a Spring artifact. Either answer
changes week 7, which already holds **CSE Test 1 (Mon Oct 5)** and the start of the PHYS
Exam 2 sweep.

**This is a genuine unknown, not a defect.** It goes on the D2L list.

---

### 6. Font Style Quiz is placed a week late

**Evidence** — syllabus `:49`: `| **Week 7: Tuesday** | … | Font Style for MS Word Docs QUIZ …`
Unambiguous, Tuesday of week 7.

`semester-workload-plan.md:230` places it in **week 8**, annotated *"(wk 7–8)"*.
`tcom-2010\semester-map.md:43` files it under a "recurring (e.g. Wk 7 Font Style Quiz)" row,
which is closer but not a placement.

TCOM quizzes score **zero if late** with no exception (`fall-2026-course-briefs.md:118`), so
a one-week-late placement on a no-late-credit item is worth correcting even though it is
small.

---

### 7. The `course-briefs` ENGR section is stale in three separate ways

**Evidence.** `fall-2026-course-briefs.md` frontmatter `source:` (line 4) and its entire
ENGR section (lines 134–153) are built on:

> `03-WIKIS\EDUCATION\raw\Syllabi\ENGR 1000 W01 (51735) Summer 2026 Syllabus - Reference Only.md`

**That file does not exist.** `04-SCHOOL\SYLLABUS_STATUS.md:83–86` already established this
on 2026-08-17:

> *"**That file does not exist anywhere in the live tree** — a broken reference the index
> carried since the July 27 recapture note recorded archiving it as a duplicate."*

Directory listing of `03-WIKIS\EDUCATION\raw\Syllabi\` confirms four files, none of them
W01:

```
ECON 1000 BAC (80643) Fall 2026 Syllabus.md
ENGR 1000 Section 05 (81217) Introduction to Engineering.md
ENGR 1000 Section BD (81208) Introduction to Engineering.md
TCOM 2010 04 (85633) Fall 2026 Syllabus.md
```

Three defects follow from the one dead path:

1. **Wrong source.** Cites a non-existent Summer 2026 W01 file; the live captures are
   §05 (Fall 2025) and §BD (Fall 2025).
2. **Wrong instructor context.** Names **Matt Marshall** as the reference instructor. The
   live captures are Katherine Nawar (§05) and Lori Lowder (§BD), and **Chris's BWD
   instructor is Kamyar Raoufi** (`kraoufi@kennesaw.edu`), corrected 2026-08-17.
3. **Missing the measured finding.** `SYLLABUS_STATUS.md:50–53` records that the two live
   ENGR captures are **body-identical** — `Compare-Object` returns 8 differing lines, all
   frontmatter plus the section name. That is real evidence about how ENGR standardizes its
   syllabus, and `course-briefs` — the page a session actually reads for ENGR — does not
   carry it.

**The same dead path appears in two more live files:**

- `03-WIKIS\EDUCATION\wiki\source-map.md:28`
- `03-WIKIS\EDUCATION\wiki\pre-semester-coverage-plan.md:233`

**Not a defect, and should be left alone:** ENGR has **no `courses\engr-1000\` folder**, and
that is deliberate and documented. `EDUCATION\wiki\current-position.md:120–122`:

> *"There is deliberately no `courses/engr-1000/` folder. `OPERATIONS.md` says to create a
> course folder only after real material or a real study need exists; ENGR has neither.
> Building scaffolding around nothing is the failure this hub's contract is written to
> prevent."*

That reasoning is correct and consistent with `CASTLE\OPERATIONS.md` Standing Rule 5 (*depth
before sprawl*). The problem is the stale **pointers**, not the missing folder.

---

## The recycled-date pattern, pushed one step further

The carried-over rule — **sequence is reliable everywhere, printed dates are not** — held on
every page checked. It is confirmed in four independent places, as recorded in
`semester-workload-plan.md` §6:

| Source | Evidence |
|---|---|
| TCOM 2010 §04 | Prints "Friday, January 16th", "Tuesday, January 20th", "Tuesday, January 27th" |
| CSE 1321 BF | Week 15 reads "May 4th, 2026, Last Day of Classes"; week 1 quizzes print Dec 07 |
| CSE 1321L 04 | Whole calendar runs Jan 12 – May 3, with MLK Day and Spring Break |
| CSE lab/assignment files | Every file versioned `sp26` / `spr26` |

**But the naive form of the rule breaks on CSE 1321L, and that is the most useful thing this
review found.**

### The two terms have different shapes

Reading the actual dates in the lab calendar (`CSE 1321L … Syllabus.md:142`):

| | Spring source | Fall 2026 |
|---|---|---|
| Term span | Jan 12 – May 3 | Aug 24 – Dec 14 |
| Total weekly slots | **16** | **17** |
| Holiday inside term | **MLK Day, week 2** | **Labor Day, week 3 (Mon Sep 7)** |
| Mid-term break | **Spring Break at slot 9** — immediately after the midterm | **Fall Break at slot 14** (Nov 23–29) |
| Break position relative to midterm | directly after | nine weeks after |

**Transposing by week number is only valid when the term shapes match. They do not.** Three
consequences:

**(a) The Oct 13 lab midterm is better supported than §3 claims.** The source puts the
midterm after seven lab weeks, and Fall has no holiday inside that stretch, so slot-alignment
and content-week-count give the **same** answer: Fall week 8, Tuesday **Oct 13**.
`semester-workload-plan.md:230` marks it "~Tue Oct 13 — confirm in D2L," which is properly
cautious, but the estimate is stronger than the page's own hedge implies. It stays a D2L
check because it is 20% of the lab grade — not because the reasoning is weak.

**(b) The back half has one spare week that no vault page accounts for.** Spring ran six
content weeks between the midterm and finals; Fall has **seven** (weeks 9, 10, 11, 12, 13,
then break, then 14, 15). Six labs (8–13) spread across seven weeks. **At least one back-half
lab row in §3 is a week early**, and the plan has no note saying where the slack lands.

**(c) "Labs 2–3 in week 2" is a Spring holiday artifact.** The source doubles Lab 1 and Lab 2
into slot 2 **because MLK Day killed that week's Monday**. Fall week 2 has no holiday — and
the lab meets **Tuesday**, so Labor Day (Mon Sep 7) does not cancel a lab at all. The source
sequence is: *no lab week 1 · Labs 1+2 week 2 · Lab 3 + Assignment 1 week 3*.
`semester-workload-plan.md:223–224` has *Lab 1 in week 1, Labs 2–3 in week 2* — a compression
that exists in neither term.

### Sharpened rule, worth adopting

> **Sequence transposes by position only when the two terms have the same number of weeks and
> their holidays in the same positions.** Before transposing any recycled calendar, count the
> weeks in both terms and locate every break in both. Where the counts differ, the extra week
> has to be assigned deliberately and the assumption written down.

---

## Supporting evidence for §8 item 1 — the CSE 1321 grading conflict

§8 item 1 flags that the CSE 1321 lecture syllabus carries two conflicting weight tables.
Both were read directly (`CSE 1321 BF (81262) Fall 2026 Syllabus.md`, adjacent and unlabeled):

```
| Assessment  | Percentage |        | Assessment  | Percentage |
| Quiz Average| 25%        |        | Quiz Average| 40%        |
| Test 1      | 25%        |        | Midterm     | 20%        |
| Test 2      | 25%        |        | Final Exam  | 40%        |
| Final Exam  | 25%        |
```

**New evidence that resolves it, short of D2L:** the 40/20/40 table names a **"Midterm."**
CSE 1321 lecture has **no midterm.** Its published calendar
(`SEMESTER_MAP.md:99, 104`) has **Test 1 (Mon Oct 5)** and **Test 2 (Mon Nov 9)** — two
tests, no midterm, plus ten quizzes and a final. The 40/20/40 table describes an assessment
structure that does not exist in this course; the 25×4 table matches the calendar exactly.

**Conclusion:** the 40/20/40 block is near-certainly boilerplate carried from another course.
The 25×4 reading that `semester-workload-plan.md` and
`03-WIKIS\PYTHON\wiki\syllabus-alignment.md:84–88` already use is **calendar-consistent**, not
merely the chosen default. Keep the D2L check — it is free and it is a grade weighting — but
plan on 25×4 with more confidence than §8 currently grants.

---

## Verified clean — checked and found correct

Recorded so a later session does not re-spend the time.

| Check | Result |
|---|---|
| **Credit hours, all six enrolments** | Registrar record matches every live page. ECON 2.0 · ENGR 1.0 · CSE 1321 3.0 · **PHYS 2211 §54 3.0** · TCOM 3.0 · CSE 1321L 1.0 = **13**. The only surviving "14 credits / PHYS 4 credits" text in the live tree is `SEMESTER_MAP.md:27` (see below) and the correction callout in the workload plan itself |
| **PHYS `semester-pathway.md` vs. the §54 syllabus** | All five exam dates, both scope boundaries (Ch 1–12, 15, 16.1–16.3), the five grading weights, the drop rules, the AI policy, and the four recorded syllabus defects all reconcile. This page is the strongest in the set |
| **ECON `semester-map.md` vs. the ECON syllabus** | Every dated row checks out. Week 1 (8/25, 8/27) through Week 14 (12/1, 12/3 Final). Quiz groupings, both exam dates, the top-two-of-four rule, and the "no class on Exam 1 day" note all correct. Fall Break correctly absent from the week numbering |
| **ECON room** | Syllabus says *"Engineering Technology Center Q-202"*; registrar says *"Engineering Technology Center, 202."* Same room. No conflict |
| **PYTHON `syllabus-alignment.md` module map** | The 2026-08-18 filename-derived module map (M0–M7) matches the lab syllabus's own module column exactly. Its academic-integrity boundary note (lines 153–157) is correctly scoped and should not be relaxed |
| **TCOM weeks 10–14** | Hub map rows match the syllabus row for row: Progress Report (10), Exec Summary/Transmittal/Slides/References + Rough Draft post (11), Report + Reflective Memo + Presentations (12), Instructions Steps + LAB DAY (13), Instructions Group Project (14) |
| **ENGR having no course folder** | Deliberate, documented, and correct. Leave it |

---

## 🟢 LOW — noted, no action needed before Aug 24

- **`SEMESTER_MAP.md:27` is stale on two numbers.** Its pointer box to the workload plan
  still says *"14 credits implies ~28 hours a week outside class against ~11.75 hours of
  campus blocks."* Both figures were superseded the same day: **13 credits**, and **16.33 h**
  of realistic campus time (`semester-workload-plan.md:81`). Fold into fix #2, same file.
- **`semester-workload-plan.md:218` uses the retired campus figure.** §3's risk key reads
  *"Risk is rated against the ~11.75 campus hours"* — §1 of the same page replaced that with
  16.33 h. The risk ratings themselves still look right; the stated basis does not.
- **`semester-workload-plan.md:166` points at a question already answered.** *"If the 21.75 h
  of mid-day campus gaps are worked… This is the 🔴 open question above"* — it was answered
  🟢 by Chris on the same day (line 68) and revised to 16.33 h.
- **TCOM room is not really disputed.** `SEMESTER_MAP.md:57` presents three values (Academic
  202 registrar · Atrium 2216 calendar · Atrium 2236 walk event) as an open conflict. By this
  report's own authority stack the **registrar wins** — Academic Building 202 — pending
  day-one confirmation. It is a confirmation, not a contest.
- **ECON meeting time, 5-minute discrepancy.** Registrar says 08:00–08:55; the ECON syllabus
  says 8:00–8:50 twice (`:31`, `:48`). Not worth resolving.
- **TCOM Week 9 Thursday carries "Midterm grades due, discuss Withdrawal options"**
  (syllabus `:54`). Not in any vault page. It aligns usefully with the **Fri Nov 6**
  withdraw-without-penalty deadline already tracked in `PHYSICS\wiki\semester-pathway.md:318`.
- **TCOM Week 14 Tuesday has an extra-credit deadline** (syllabus `:63`). §3's week 14 row
  names the Instructions Group Project but not the extra credit. TCOM extra credit is
  never accepted late.

---

## Recommended additions to `semester-workload-plan.md` §8

The existing seven are all still open and correctly ordered. Three additions, plus one
sharpening:

| # | Check | Why it matters |
|---:|---|---|
| **8** | **TCOM Week 7 Thursday — "Group Oral Presentations: Technical Report PPT."** Real Fall event, or Spring artifact? | Ties to the 15% oral-presentation grade category, and lands in the same week as CSE Test 1. Absent from every vault page |
| **9** | **Lab 8, and where the extra Fall week lands in the back half** | Fall has one more week than the Spring source calendar; six labs across seven weeks. At least one back-half lab row in §3 is a week early |
| **10** | **Does TCOM have a Week 15?** | The syllabus says 15 weeks and its table stops at 14. The gap is in the source, not the map |

**Sharpen item 2.** As written it asks *when the CSE 1321L midterm and final are.* The
sequence answers the midterm fairly firmly — **Tue Oct 13**, seven lab weeks with no
intervening holiday. The live question is narrower and better: **does the extra Fall week
land before or after the midterm, and where do Labs 8–13 sit in the seven weeks that
follow it?**

---

## Fix ledger — what to change, and who owns each file

Nothing was edited this session. Each row names its owner per
`NORTH_STAR.md` §6 and `CASTLE\OPERATIONS.md` § Operating Authority.

| # | File | Edit | Owner realm | Judgment call? |
|---:|---|---|---|---|
| 1 | `04-SCHOOL\semester-workload-plan.md` §3 + §2 | Add Labs 5–8, Assignments 2–3; remove the lab clause from §2's floor; re-estimate wks 5, 6, 7, 9; fix "6 of 15" → 7 assignments | `04-SCHOOL` | No — reconciliation against the lab syllabus |
| 2 | `04-SCHOOL\SEMESTER_MAP.md:138`; `EDUCATION\wiki\current-position.md:30` | TCOM weeks 6–14 are extracted; week 15 absent from source | `04-SCHOOL` + EDUCATION | No |
| 3 | `SEMESTER_MAP.md:318`, `SYLLABUS_STATUS.md:161`, `NOW.md:181` | Replace "verify per assignment" with the syllabus's quoted sentence; add TCOM to `NOW.md` Boundaries | `04-SCHOOL` + CASTLE (`NOW.md`) | No — quoting the source |
| 4 | `semester-workload-plan.md:224`; `tcom-2010\semester-map.md:29` | Business Email FINAL → week 3 | `04-SCHOOL` + EDUCATION | No |
| 5 | — | D2L check only. No edit until answered | — | n/a |
| 6 | `semester-workload-plan.md:230` | Font Style Quiz → week 7 Tuesday | `04-SCHOOL` | No |
| 7 | `course-briefs\fall-2026-course-briefs.md` (frontmatter + ENGR section); `source-map.md:28`; `pre-semester-coverage-plan.md:233` | Repoint to the two live Fall 2025 captures; correct instructor to Raoufi; carry the body-identical finding across | EDUCATION | No |
| 🟢 | `SEMESTER_MAP.md:27`; `semester-workload-plan.md:166, 218` | 13 credits, 16.33 h; retire the answered 🔴 | `04-SCHOOL` | No |

**Items 1–4, 6, 7 and the 🟢 batch are pure reconciliation against verified primary sources
and carry no judgment call.** They need Chris's go-ahead only because they cross realm
boundaries, not because any of them is a decision.

---

## The error class

Four of the seven defects — #2, #4 (both instances), #6, and #7 — share one cause, and it is
already named in the vault. `EDUCATION\wiki\current-position.md:90` puts it best, about
itself:

> *"This is the 'absence in the file consulted read as absence in the vault' error class …
> it recurred here because this page was written from memory of the map rather than from the
> map."*

The general form is wider than absence: **a claim written from a summary rather than from the
source.** Every instance found today came from reading a derived page instead of the primary
document — or, in #2's case, from recording an intended correction as a completed one.

It has now been caught on **2026-08-13 (ECON, in `SEMESTER_MAP.md`)**, **2026-08-18 (TCOM,
in `current-position.md`)**, and **twice more today** (#2's uncorrected twin, #7's dead
path). `AGENT.md` § System Evolution Authority sets the bar as *repeated evidence*; four
independent instances in six days clears it.

**Two candidate mitigations, offered as proposals, not as adopted rules:**

1. **A correction is not written until the target file is re-read.** #2 exists precisely
   because a session recorded a fix in file A that it never made in file B. This is the same
   shape as flag #100 and as `NOW.md` Open Risk 1 (writing from a pre-pull copy) — the
   generalized version is *never record an outcome you have not observed.*
2. **Date and deadline claims cite the primary source, not a derived page.** TCOM's week
   numbers should be sourced from the syllabus row, PHYS's from the §54 PDF, the lab's from
   the lab syllabus table — the way `PHYSICS\wiki\semester-pathway.md` already does it, which
   is why it is the only page in this review with nothing to fix.

Both are `SYSTEM_FLAGS.md` candidates rather than same-session changes; neither is urgent
before Aug 24. Chris's call.

---

## Session boundary

- **Read-only.** No wiki page, index, plan, `raw\` file, or governance file was modified.
- **No `raw\` write, move, rename, or delete** — `NORTH_STAR.md` §3 and prohibition 1.
- **No academic content produced.** Syllabi were read for dates, structure, and policy only,
  per `AGENT.md` § Academic Integrity and the Wiki Shared Layer's rule. No CSE lab or
  assignment prompt was opened; the boundary note at
  `PYTHON\wiki\syllabus-alignment.md:153` was respected.
- **Independent review:** none. Single-surface findings, per `AGENT.md` § One AI Team's
  disclosure requirement. Every claim is line-cited so a second surface — or Chris — can
  check each one against the named file without re-deriving the review.

---

*Owner of the plan under review: `04-SCHOOL\semester-workload-plan.md`. Cross-course dates:
`04-SCHOOL\SEMESTER_MAP.md`. Source status: `04-SCHOOL\SYLLABUS_STATUS.md`. Registrar record:
`04-SCHOOL\fall_KSU_schedule.md`. Related open flag: #57 (ENGR half, check moment Fri Aug 21).
Next natural checkpoint: the **Aug 23 pre-semester review**, then the D2L reconciliation pass
on **Aug 24**.*
