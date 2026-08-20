---
type: plan
timeline: now
status: active
tags: [school, fall-2026, planning, workload]
created: 2026-08-18
---

# Semester Workload Plan — Fall 2026

### The one page that answers "what is a successful week." Built 2026-08-18 at Chris's request, from the five exact-section syllabi on disk. Per-course detail stays in each hub; this assembles it into weeks and measures it against real available time.

**Authority and boundaries.** Dates come from the exact-section syllabi and the
already-reconciled hub pages — `PHYSICS\wiki\semester-pathway.md`,
`PYTHON\wiki\syllabus-alignment.md`, `EDUCATION\wiki\courses\{econ-1000,tcom-2010}\semester-map.md`.
**Hour figures are estimates, not measured**, and are the first thing to correct once real weeks
run. This page plans effort; it never produces graded work.

---

## 1. The arithmetic nobody has written down

> **⚠ Corrected 2026-08-18 against `04-SCHOOL\fall_KSU_schedule.md`, the registrar record.**
> The first version of this page said 14 credits and PHYS 2211 at 4 credits. **Both were wrong.**
> The registrar record — which carries CRNs, instructors, rooms, and exact meeting times — says
> **PHYS 2211 §54 is 3.0 credits** and the load is **13 credits**, not 14. Every figure below is
> rebuilt from that record rather than from assumption.

Chris is enrolled in **13 credit hours**: CSE 1321 (3) · CSE 1321L (1) · **PHYS 2211 (3)** ·
TCOM 2010 (3) · ECON 1000 (2) · ENGR 1000 (1).

The standard expectation is **2–3 hours of outside work per credit hour per week** → **26–39
hours a week outside class.**

### In-class time — computed from the registrar's actual meeting times

| Course | Meeting | Weekly |
|---|---|---:|
| PHYS 2211 lecture | MWF 09:10–10:05, Academic 200 | 2.75 h |
| PHYS 2211 recitation | Fri 11:30–12:25, Atrium 1116 | 0.92 h |
| CSE 1321 | Mon/Wed 16:10–17:30, Academic 203 | 2.67 h |
| CSE 1321L | Tue 17:45–19:35, Atrium 2120 | 1.83 h |
| TCOM 2010 | Tue/Thu 09:35–10:55, Academic 202 | 2.67 h |
| ECON 1000 | Tue/Thu 08:00–08:55, ETC 202 | 1.83 h |
| ENGR 1000 BWD | ⛔ **no meeting time on the registrar record** | ? |
| | **In-class total** | **12.67 h** |

### The campus day is far emptier than this page first claimed

The earlier figure of ~11.75 campus hours came from `CAMPUS_LAPTOP_BUILD.md`, written Aug 13.
**The registrar's real timetable produces almost double that in mid-day gaps:**

| Gap | Hours |
|---|---:|
| Mon 10:05 → 16:10 (PHYS ends, CSE begins) | **6.08** |
| Tue 10:55 → 17:45 (TCOM ends, lab begins) | **6.83** |
| Wed 10:05 → 16:10 | **6.08** |
| Tue + Thu 08:55 → 09:35 | 1.33 |
| Fri 10:05 → 11:30 | 1.42 |
| **Total mid-day gap** | **21.75 h** |

**Monday, Tuesday and Wednesday each contain a six-hour hole between classes.** If those are
worked, the 26–39 hour requirement is substantially covered on campus and the evening load is
modest. If Chris goes home in them, essentially the whole 26–39 hours lands on evenings and
weekends.

> **🟢 ANSWERED 2026-08-18 by Chris: yes, he works the gaps on campus.** In his words, that is
> *why* the laptop was prepared — it exists to make those hours usable.

**Realistic campus hours — Chris's own correction, same day.** He expects **2 fewer hours on
Monday and Wednesday** than the raw gap, and will **use the campus gym on Friday**. Taking him
at his word rather than using the theoretical maximum:

| Block | Raw gap | Realistic |
|---|---:|---:|
| Mon 10:05–16:10 | 6.08 | **4.08** |
| Tue 10:55–17:45 | 6.83 | 6.83 |
| Wed 10:05–16:10 | 6.08 | **4.08** |
| Tue + Thu 08:55–09:35 | 1.33 | 1.33 |
| Fri 10:05–11:30 | 1.42 | **0.00** — gym |
| **Total** | 21.75 | **16.33 h** |

**What that leaves for evenings and weekends:**

| Requirement | Evenings + weekends | Per day, spread over 7 |
|---|---:|---:|
| 24 h/wk (low) | 7.67 h | **1.1 h** |
| **28 h/wk (working)** | **11.67 h** | **1.7 h** |
| 32 h/wk (high) | 15.67 h | 2.2 h |

**This still works comfortably.** Roughly **1.7 hours a day** outside campus at the working
figure — an evening block, not an evening consumed. The earlier uncommitted reading implied
four hours a day; the real number is well under half that.

**One scheduling note worth taking.** Friday's 1.42 h gap sits *between* the PHYS lecture
(ends 10:05) and the recitation (11:30–12:25). **After recitation ends at 12:25 the academic
day is over** — so a gym session placed *after* 12:25 rather than in that mid-morning gap costs
zero study time and keeps 1.42 h/week. Small, free, and worth doing deliberately.

> **⚠ The remaining optimistic assumption is Tuesday.** Its 6.83 h gap is now the single largest
> study block of the week and is still counted in full. If Tuesday behaves like Monday and
> Wednesday and loses ~2 h, campus time drops to **14.33 h** and the evening requirement rises
> to **~13.7 h/week (≈2 h/day)** — still workable, but it is the next number to check against
> reality in week 1.

**The load-bearing dependency this creates:** the campus laptop carries **~58% of all
outside-class study time** at the realistic figure. It is not a convenience machine — **if it
is unavailable during a campus block, that block is lost**, and the plan has no slack for that
happening repeatedly. See the battery finding immediately below.

> ### 🔴 The battery requirement was specified at a third of the real need
>
> `CAMPUS_LAPTOP_BUILD.md` §7 check 10 asks the laptop to survive *"a 2h15 Monday block at
> 09:10–12:30."* **Both halves are wrong against the registrar record.** PHYS ends at
> **10:05**, CSE begins at **16:10**, so the real Monday requirement is **~6 hours**, and
> Tuesday's is **~6.8 hours**. A battery test was reported passed — but against a 2h15 target
> that does not correspond to any actual gap in the timetable.
>
> The machine holds **48,948 mWh** at ~93% health. Six hours unplugged on a Victus with a
> discrete GPU present is optimistic even on integrated graphics. **Treat outlet access in the
> Mon/Tue/Wed gap locations as a requirement to verify on day one, not an assumption**, and
> re-run the endurance check against 6 hours rather than 2h15.

**Where the buffer actually is:** PHYS and CSE both sit **+2 weeks ahead** as of 2026-08-18
(measured, not assumed). TCOM is at **0** and has graded work in week 1. That asymmetry is
what makes the early weeks survivable, and it is why the evening-reading rotation was
reweighted to TCOM/ECON the same day.

### Total outside-class hours for all A grades

Asked directly 2026-08-18. Three methods, and the distance between them is itself the answer.

| Method | Semester total |
|---|---:|
| Sum of §3's week-by-week estimates | **~304 h** (~19.6 h/wk) |
| 13 credits × 2–3 h/credit × ~15.5 wks | **403–605 h** (26–39 h/wk) |
| **Per-course, A-level (table below)** | **372–495 h** |

**They disagree because they measure different things.** §3's 304 hours is a
**deliverable-completion floor** — built from actual work products, enough to finish everything
on time and pass comfortably. The credit-hour range assumes continuous study: reading ahead,
reworking missed problems, retrieval practice. **That gap is the difference between finishing
the work and earning an A.** In PHYS especially, no amount of on-time homework reaches an A if
exam classification is not automatic.

| Course | Cr | h/week | Semester |
|---|---:|---|---:|
| **PHYS 2211** | **3** | 9–11 | **140–170** |
| CSE 1321 + 1321L | 4 | 7–9 | 108–140 |
| TCOM 2010 | 3 | 5–7 | 78–108 |
| ECON 1000 | 2 | 2–3 | 31–46 |
| ENGR 1000 | 1 | 1–2? | 15–31 |
| **Total** | **13** | **24–32** | **372–495** |

**Working figure: ~430 hours outside class, ~28 h/week.**

**PHYS carries the most hours despite being 3 credits, not 4** — 75% of that grade is four
closed-book unit exams plus a comprehensive final, so its hours are driven by assessment
structure rather than credit count. It is roughly **37% of the total outside-class load**.

**Two things that move the real number down:**

1. **The +2 week buffer is already banked.** These figures describe a student starting cold on
   Aug 24. Stages 1–4 and CSE Modules 0–1 are done — plausibly 30–50 hours already spent.
2. **If the 21.75 h of mid-day campus gaps are worked**, ~28 h/week is nearly covered before any
   evening work at all. If they are not, ~28 h/week means about **4 hours every evening and
   weekend**. This is the 🔴 open question above, and it is worth more than any other estimate
   on this page.

---

## 2. Standing weekly baseline — every ordinary week

Before any dated item, each week carries this floor:

| Course | Recurring weekly work | Est. |
|---|---|---:|
| **PHYS 2211** | WebAssign homework (10%, weekly, **late = zero**) + recitation worksheet (10%) + reading for MWF 9:10 lecture | 5–7 h |
| **CSE 1321** | Module reading/practice for Mon+Wed lecture; a quiz most weeks | 3–4 h |
| **CSE 1321L** | One lab most weeks → Gradescope; assignment in 6 of 15 weeks | 2–3 h |
| **TCOM 2010** | TTh in person; reading + the week's deliverable; **6 weeks of report work happen in class** | 3–5 h |
| **ECON 1000** | Chapter reading; graded items are sparse but heavy | 1–2 h |
| **ENGR 1000** | ⛔ **Unknown — see §5** | 1–2 h? |
| | **Ordinary-week floor** | **15–23 h** |

**Two rules that come straight from the syllabi and are worth internalising now:**

- **PHYS homework late = zero.** Extensions exist but must be requested *through WebAssign
  before* the deadline. This is the most unforgiving recurring rule in the five courses.
- **TCOM has no late credit at all on quizzes, discussion posts, and extra credit.** Major work
  takes −10%/day; the small items simply score zero.

### 🟢 Standing action — the cheapest grade points in the semester

> **CCSE Tutoring Center visits are worth 0.5% each on the final exam score, up to 5% for 10
> visits — and the credit applies to BOTH CSE courses.**
>
> *"Students can earn 0.5% extra credit on their final exam score for each visit to the CCSE
> Tutoring center… up to a maximum of 5% (10 visits). These extra credit points will be added
> to the **lecture and lab final exam score**. The last day credit can be earned is the last day
> of classes."*
> — `CSE 1321 BF … Syllabus.md:94`, and `CSE 1321L 04 … Syllabus.md:120–122`
>
> **Verified on disk 2026-08-18, not assumed.** CSE 1321's final is **25%** of that grade and
> CSE 1321L's is **30%** of that one, so this is a deterministic gain against the two largest
> single line items in the CSE pair — with **no performance risk**, unlike every other point in
> this plan.
>
> **Ten visits across fifteen weeks is roughly two visits every three weeks.** Start in week 1 rather
> than discovering the allowance in November; the deadline is the last day of classes,
> **Dec 7**. Tutoring is also an authorised human resource under both AI policies — going there
> when stuck on a lab is explicitly permitted where AI assistance is not.

### Week 1 reading — the run-in and the first week (added 2026-08-19)

§3's week-1 row lists what is **graded**. It never said what to **read**, and that is the
question a fast start actually turns on. Assembled from the five owner pages; each cell
cites its owner rather than restating it.

**Run-in, Aug 19–23 — three readings, and none of them is a textbook chapter for a class
you are behind in.** PHYS and CSE are +2 weeks ahead; re-reading covered ground buys
nothing (evening-reading override 3).

| # | Read | By | Why this one |
|---:|---|---|---|
| 1 | **TCOM §2.13 *Emails & Memos*** — `03-WIKIS\EDUCATION\raw\Open-TC_Course-Resources\Open-TC-PDF.pdf` | **Aug 23** | The required instructor email is sent **Tue Aug 25**, and the Business Email is 15% of the course |
| 2 | **TCOM Ch 3 *Ethics*** — same PDF, plus one case from `raw\Linked-Resources\` (`3_Harcourt`, `3_Killer`, `3_Mistry`, `3_Reed`, `3_Rouche`) | **Aug 26** | The **Ethics Analysis is graded and due Fri Aug 28** — a week-1 graded item whose format and filename appear nowhere in the syllabus |
| 3 | **ECON — OpenStax *Principles of Economics 2e* Ch. 1** (`04-SCHOOL\04-ECON\`) | Aug 23 | **Substitute, not the real book.** Mathews & Patrono is D2L-locked until Aug 24; read it as a topic primer and re-anchor on the real Ch. 1 that day |

**⛔ Never cite `2e_Word\`** for any TCOM chapter — its Ch 3 is *Library and Internet
Research*, not *Ethics*. This exact defect was live in two `.ROOT` study pages until
2026-08-19 and reproduced in Chris's failed reps.

**The reading that is not a textbook, and decides week 1 more than any chapter does.**
Five courses print five different late policies, five naming conventions and five AI
policies, and week 1 grades three of them:

- **TCOM course policies + file naming** → `03-WIKIS\EDUCATION\wiki\courses\tcom-2010\concepts\course-policies-and-file-naming.md`. **Two graded quizzes in week 1, and TCOM accepts no late credit on quizzes, ever.** Cold diagnostic on 2026-08-19 scored ~3 of 8, and **both confident wrong answers were PHYS rules imported into TCOM.**
- **CSE 1321 + 1321L policy sections** → `03-WIKIS\PYTHON\raw\syllabi\`. **Two graded syllabus/policy quizzes in week 1.** Note the two conflicting grade tables (§8 check 1).
- **PHYS §54 syllabus** → `03-WIKIS\PHYSICS\raw\syllabus\Syllabus.pdf`. Two lines only: the **WebAssign extension rule** (request *before* the deadline or a miss is a flat zero) and the **Day One Access opt-out, Fri Aug 28 11:45 PM**.

**Week 1 proper, Aug 24–30.**

| Course | Read | By | Owner |
|---|---|---|---|
| **PHYS** | **Serway 3.1–3.4** (vectors), **4.1–4.2, 4.4–4.5** (2D motion, projectile, UCM) — this is **week 2's** material. `PHYSICS\raw\textbook\physic(full_book).pdf`; **the PDF runs +30 pages ahead of the printed numbers**, see `wiki\textbook-page-map.md` | across the week | `PHYSICS\wiki\semester-pathway.md` Phase 2. Lecture covers Ch 1–2, which he already holds; the one-week-ahead lead is what converts each pre-exam week into pure retrieval, and **pre-class reading is graded here** |
| **TCOM** | Finish Ch 3 *Ethics*; then §5.2 *Audience Analysis* + §2.12 *Oral Presentations* | Ch 3 by Aug 26; the rest by Sep 2 | `tcom-2010\tcom-2010-17-week-execution-plan.md` |
| **CSE** | *Think Python* (`PYTHON\raw\books\thinkpython.pdf`) Ch 1 and Ch 4 "A Development Plan"; then the Module 1 spine — Ch 1 values/types/operators, Ch 2 assignment/variables/expressions, Ch 5 "Keyboard Input". Cite **physical** pages from `wiki\source-page-map.md` | Ch 1/4 by Aug 24; Module 1 by Aug 30 | `PYTHON\wiki\syllabus-alignment.md` § Semester Reading Queue. **Module 1 opens week 2 and Quiz 1 is Sun Sep 6** |
| **ECON** | **Mathews & Patrono Ch 1**, the moment D2L opens — and check its numbering against the OpenStax mapping | Aug 27 | `econ-1000\semester-map.md`. Quiz Ch 1-2-3 is **Tue Sep 8** |
| **ENGR** | ⛔ **The syllabus itself is the week-1 reading.** It does not exist yet | **Aug 24, D2L** | Flag #57's remaining half; check moment Fri Aug 21 |

**Total run-in reading: roughly 3 hours across five days.** It is small because the
buffer is real — the work is to keep it.

### Keeping pace after week 1 — three mechanisms, already built

Nothing new is needed. These exist and only have to be run:

1. **The evening rotation** (`00-BRAIN\EVENING_READING_INSTRUCTIONS.md`) — rebuilt
   2026-08-19 onto the registrar's timetable: **PHYS 2 · TCOM 2 · CSE 2 · ECON 1** nights
   a week, each priming the next day's actual first class. The **Technology block is
   paused** for the semester unless it ties to a course deliverable due within 7 days.
2. **The PHYS one-week-ahead rule**, broken only for the three reasons its own page
   names. **Move the two red exam sweeps forward** — Exam 2's to Oct 1–2, Exam 4's into
   week 11 — or they land on CSE Test 1 and on week 12.
3. **TCOM's four ungraded report checkpoints** — Oct 13, Oct 20, Oct 27, Nov 3. They are
   the only thing standing between 35% of that grade and the worst week of the semester.
   Being ungraded is exactly why they get skipped.

---

## 3. Week-by-week — load, deadlines, and risk

Risk is rated against the ~11.75 campus hours plus a normal evening load. 🟢 ordinary ·
🟡 heavy, plan ahead · 🔴 collision, work must move earlier.

| Wk | Dates | Graded items due | Est. | Risk |
|---:|---|---|---:|:--:|
| 1 | Aug 24–30 | CSE Syllabus & Policy quizzes · Lab 1 · **TCOM Ethics Analysis (Fri)** · TCOM Policies + File-Naming quizzes · Business Email draft | ~14 h | 🟢 |
| 2 | Aug 31–Sep 6 | **CSE Quiz 1 (Sun Sep 6)** · Labs 2–3 · Assignment 1 · TCOM Audience Analysis + peer response · Business Email **final** · ECON Ch 1–3 reading | ~18 h | 🟡 |
| 3 | Sep 7–13 | **ECON Quiz Ch 1-2-3 (Tue Sep 8)** · TCOM Fairy Tale presentation + Elevator Speech · Labor Day Mon Sep 7 | ~16 h | 🟢 |
| 4 | Sep 14–20 | **CSE Quiz 2 (Sun Sep 20)** · Lab 4 · TCOM Individual Project Proposal work | ~17 h | 🟡 |
| 5 | Sep 21–27 | 🔴 **PHYS UNIT EXAM 1 (Mon Sep 21, Ch 1–5 + 6.1–6.2)** · **ECON Quiz Ch 4-5 (Tue Sep 22)** · TCOM Proposal Presentation | ~22 h | 🔴 |
| 6 | Sep 28–Oct 4 | 🔴 **ECON EXAM 1 (Tue Sep 29, Ch 1–5)** · **CSE Quiz 3 (Sun Oct 4)** · **TCOM Report Group Charter + Task Schedule due Thu Oct 1 midnight** · **TCOM Document Redesign due Thu Oct 1** | ~22 h | 🔴 |
| 7 | Oct 5–11 | **CSE TEST 1 (Mon Oct 5, Modules 1–2)** · Assignment 4 · **TCOM Font Style for MS Word QUIZ (Tue Oct 6)** · TCOM report PPT group orals (Thu Oct 8) · **report build runs weeks 6–12** | ~19 h | 🟡 |
| 8 | Oct 12–18 | 🔴 **PHYS UNIT EXAM 2 (Mon Oct 12)** · 🆕 **CSE 1321L MIDTERM, 20% (~Tue Oct 13 — confirm in D2L)** · **CSE Quiz 4 (Sun Oct 18)** · 🎯 **TCOM report checkpoint 1 — Introduction, Tue Oct 13** | ~24 h | 🔴 |
| 9 | Oct 19–25 | **CSE Quiz 5 (Sun Oct 25)** · **ECON Quiz Ch 7-8-9 (week of Oct 20)** · 🎯 **TCOM report checkpoint 2 — Project Description, Tue Oct 20** · Lab 9 | ~19 h | 🟡 |
| 10 | Oct 26–Nov 1 | 🎯 **TCOM report checkpoint 3 — Recommendation & Conclusion, Tue Oct 27** · **TCOM Progress Report email due Thu Oct 29** · Lab 10 · Assignment 5 | ~16 h | 🟢 |
| 11 | Nov 2–8 | 🔴 **PHYS UNIT EXAM 3 (Wed Nov 4)** · **CSE Quiz 6 (Sun Nov 8)** · 🎯 **TCOM report checkpoint 4 — Exec Summary/Transmittal/Slides/References + Rough Draft post, Tue Nov 3** · **TCOM peer reviews due Thu Nov 5** | ~21 h | 🔴 |
| 12 | Nov 9–15 | 🔴🔴 **CSE TEST 2 (Mon Nov 9)** · **TCOM TECHNICAL REPORT + REFLECTIVE MEMO DUE Thu Nov 12** + Group Presentations Tue & Thu · **ECON Quiz Ch 10-11-12 (week of Nov 10)** · Labs 11–12 · Assignment 6 | **~26 h** | 🔴 |
| 13 | Nov 16–22 | 🔴 **PHYS UNIT EXAM 4 (Wed Nov 18)** · **CSE Quiz 7 + Quiz 8 (Thu Nov 19)** · TCOM Instructions Steps written in class (Tue Nov 17) · **TCOM LAB DAY Thu Nov 19 — bring polished instructions, all equipment, printed worksheet** · ECON Financial Literacy + extra-credit quiz | ~23 h | 🔴 |
| — | Nov 23–29 | **FALL BREAK — no classes.** The only real catch-up window in the back half | — | 🟢 |
| 14 | Nov 30–Dec 6 | 🔴 **ECON FINAL EXAM (Thu Dec 3, Ch 7–12)** · **CSE Quiz 9 (Sun Dec 6)** · **TCOM Instructions Group Project due Thu Dec 3 — last TCOM class** · TCOM Extra Credit due Tue Dec 1 · Lab 13 · Assignment 7 | ~21 h | 🔴 |
| 15 | Dec 7 | **CSE Quiz 10 (Mon Dec 7)** — last day of classes. **No TCOM meeting** (TTh course) | ~8 h | 🟢 |
| F | Dec 8–14 | **PHYS FINAL (Wed Dec 9, 8:00–10:00 AM, comprehensive)** · CSE Final Exam · CSE 1321L final · **ECON and TCOM are already finished** | ~20 h | 🔴 |

---

## 4. The six things this table makes visible

**1. Week 12 (Nov 9–15) is the worst week of the semester — by a wide margin.** CSE Test 2 on
Mon Nov 9, the **TCOM Technical Report and Reflective Memo both due Thu Nov 12**, group
presentations on Tuesday *and* Thursday, an ECON quiz, two labs and an assignment. That is ~26
estimated hours against 16.33 campus hours.

**The report is the movable piece, and the mechanism for moving it is now dated.** The TCOM
extraction (2026-08-18) shows **four professor-review checkpoints — Tue Oct 13, Tue Oct 20,
Tue Oct 27, Tue Nov 3** — covering Introduction, Project Description, Recommendation &
Conclusion, and Exec Summary/Transmittal/Slides/References. **They are ungraded**, which is
exactly why they get skipped under pressure. Hit all four and the report is substantially
written before November; miss them and the whole 35% lands on the worst week of the term.
**Finishing it a week early is the single highest-leverage scheduling decision in the semester.**

**2. Exams cluster on Mondays and Wednesdays, which collides with the lightest campus days.**
PHYS unit exams land Mon/Mon/Wed/Wed; CSE Test 1 and Test 2 both land Monday. Monday offers
2.25 campus hours. **Every exam's real preparation happens the weekend before**, not the morning
of.

**3. Five weeks carry two or more major assessments** (5, 6, 8, 11, 12, 13, 14). In each, at
least one item is knowable a week ahead. None of these should be a surprise.

**4. Fall Break (Nov 23–29) sits between the two worst weeks** — after week 13's double exam and
before week 14's ECON final. It is the only structural catch-up window in the back half. Protect
it for the PHYS final and do not spend it.

**4b. Finals week is a two-course week, not a five-course week** — established by the TCOM
extraction, 2026-08-18. **TCOM has no final exam at all**; its last graded item is the
Instructions Group Project on **Thu Dec 3**. **ECON's final is also Thu Dec 3**, in the regular
class slot. So by the end of week 14, **two of the five courses are completely finished**, and
Dec 8–14 carries only the PHYS final (Wed Dec 9), the CSE final and the CSE 1321L final. That
makes the back end of the semester materially lighter than the front — and it means **the last
push is week 14, not finals week.**

**5. The CSE lab's two exams are 50% of that grade and were unmapped until 2026-08-18.**
Midterm 20% + final 30%, both "in class, closed book, closed notes, no outside resources," both
taken **during the regularly scheduled Tuesday lab**. The lab syllabus places the midterm
immediately after Module 3 / Lab 7 / Assignment 4 — **week 8**, i.e. **~Tue Oct 13**, the day
after PHYS Unit Exam 2. The lab final falls in the final exam week. Both dates are on a
Spring-dated calendar and **must be confirmed in D2L**; the *position in the sequence* is
reliable, the printed date is not.

**6. The dropped-lowest rules are a real, quantifiable buffer — use them deliberately.**
PHYS drops the lowest of four unit exams, the lowest homework, worksheet and quiz. ECON counts
only the **top two of four quizzes**, making quizzes 1 and 2 effectively free diagnostics. CSE
drops the lowest quiz; CSE 1321L drops the lowest assignment and lowest lab. **A single bad week
is already absorbed by the grading structure** — which is exactly why it should be spent on a
collision week rather than wasted early.

### PHYS exam sweeps — start them earlier than the obvious seven days

The sound rule is: **seven days before each unit exam, stop advancing and run timed mixed
retrieval.** Applied naively it produces these windows — and **two of the four land inside
collision weeks**, which defeats the purpose:

| Sweep | For | Conflict |
|---|---|---|
| Sep 14–20 | Exam 1, Mon Sep 21 | 🟢 clean, only CSE Quiz 2 (Sep 20) |
| **Oct 5–11** | Exam 2, Mon Oct 12 | 🔴 **starts the day CSE Test 1 is written** (Mon Oct 5) |
| Oct 26–Nov 3 | Exam 3, Wed Nov 4 | 🟡 overlaps TCOM Progress Report + rough-draft work |
| **Nov 9–17** | Exam 4, Wed Nov 18 | 🔴🔴 **sits on top of week 12** — CSE Test 2 (Nov 9) *and* the TCOM Technical Report due |

**Move the two red sweeps forward by roughly half a week.** Begin the Exam 2 sweep on
**Oct 1–2**, before CSE Test 1 consumes the weekend; begin the Exam 4 sweep in **week 11**, so
that week 12 carries the report and CSE Test 2 without a physics sweep layered on it. The
alternative is discovering in week 12 that three subjects each want the same evenings.

### Tuesday is the day most likely to underperform its plan

Tuesday runs **08:00 ECON → 09:35 TCOM → [6.83 h gap] → 17:45 lab, ending 19:35**. That is
**11.5 hours on campus ending in a two-hour lab.** It is simultaneously the largest single study
block of the week and the one still counted at full value in §1.

**Do not schedule three courses into it by default.** Put the work that needs the most focus in
the first half of the gap, and treat the last 90 minutes before the lab as lab preparation
rather than new material. **Check in week 1 how the back half of that day actually feels** — if
it loses ~2 h like Monday and Wednesday, the whole week's evening requirement rises by that
amount.

---

## 5. What is NOT planned here, and why

**ENGR 1000 BWD is absent from every row above.** There is no Fall BWD syllabus — only the
Summer 2026 W01 reference section and a Section 05 capture, neither of which is Chris's section.
Its meeting format is unpublished. `EDUCATION\wiki\course-briefs\fall-2026-course-briefs.md`
records its AI policy as **prohibited** on the Summer reference, unverified for Fall.

**Deliberately not invented.** A 1-credit course plausibly adds 1–2 hours a week, and the ⛔ rows
say so rather than filling in plausible content. Flag #57's remaining half has a check moment of
**Fri Aug 21**; if nothing arrives, plan as if attendance is graded and verify when D2L opens
Aug 24. **Add ENGR to §2's baseline the day its syllabus lands** — every estimate here rises.

---

## 6. ⚠️ Date warning — this is the third instance of one defect

**Several Fall 2026 syllabi are recycled Spring documents, and the carryover reaches actual
printed due dates.** Confirmed today:

| Where | Evidence |
|---|---|
| **TCOM 2010 §04** | The week-by-week table prints **"due on Friday, January 16th," "due Tuesday, January 20th," "Business Email FINAL due Tuesday, January 27th"** — January dates in a Fall syllabus |
| **CSE 1321 BF** | Week 15 topic reads **"May 4th, 2026, Last Day of Classes"**; week 1 quizzes print a Dec 07 due date |
| **CSE 1321L** | The whole calendar uses January–May dates and a spring break under a Fall 2026 title |
| **CSE lab/assignment files** | Every file versioned `sp26` / `spr26` |

**What this means for this page.** The **weekday and sequence** structure is reliable — Week 1
Tuesday/Thursday, quiz-then-exam order, draft-then-final rhythm. **The printed calendar dates in
TCOM and the CSE lab are not.** The dates used in §3 above come from the sources that *are*
Fall-dated: the PHYS §54 syllabus (all five sittings confirmed), the CSE 1321 lecture calendar,
and the ECON dated schedule.

**Every TCOM row in §3 was placed by week number. Since 2026-08-18 those week numbers carry real
dates**, and the conversion is verified rather than assumed: the syllabus has exactly 14 numbered
weeks and there are exactly 14 Tue/Thu pairs between Tue Aug 25 and the last day of classes once
Fall Break (Nov 23–29) is removed. Two counts, no remainder — so each syllabus week has exactly
one home. **This raises TCOM from "week number only" to 🟡 dated.** Still confirm against D2L
from **Aug 24**; a derived date loses to a posted one.

---

## 7. How to use this, weekly

1. **Sunday:** read the week's row **and the same week's block in
   `04-SCHOOL\semester-reading-plan.md`** — this page says what is *due*, that one says what
   to *open*, with chapter, section and exact page for all five courses. If the row is 🟡 or
   🔴, move one item earlier into the week before.
2. **Check the recurring floor first** (§2) — PHYS WebAssign is due weekly and scores zero if late.
3. **The campus blocks are for the work that needs a desk — including 3–5 hours of reading.**
   *(Corrected 2026-08-19. This line previously read "reading fits the evening brief." It does
   not: reading is **6–8 h/week** across five courses and the evening block carries only
   2.3–3.5 h of it. The arithmetic is in `semester-reading-plan.md` §1. Reading is a planned
   campus activity, not a leftover — roughly a third of the 16.33 h of campus gaps.)*
4. **After the week runs, correct the estimate.** These hours are unmeasured. A week that took
   19 hours against an estimate of 14 is information, and this page should absorb it.

**Update triggers:** the ENGR syllabus arriving · D2L confirming real TCOM dates · any exam date
moving · the first three weeks producing real hour counts.

---

## 8. D2L reconciliation list — Aug 24, in priority order

Everything below is a known unknown, not a discovered problem. Each has a specific question.

| # | Check | Why it matters |
|---:|---|---|
| 1 | **CSE 1321 lecture grade weights** — the syllabus carries **two conflicting tables**: 25/25/25/25 (line 108) and 40/20/40 (line 115) | Changes how much a quiz is worth relative to a test. The 25×4 reading is used throughout this plan |
| 2 | **CSE 1321L midterm and final dates** | 50% of the lab grade. Sequence says week 8 (~Tue Oct 13) and finals week; the printed calendar is Spring |
| 3 | **TCOM real Fall due dates** — the syllabus prints January dates. **Now derived to real dates (2026-08-18) and the week→date conversion is verified** (14 numbered weeks ↔ 14 Tue/Thu pairs, Aug 25 → Dec 3, Fall Break removed), so this is a confirmation, not an extraction. **Also grab the three Group Charter samples** — D2L-only, needed by Thu Oct 1 | Every TCOM row above is now dated 🟡. If D2L disagrees, D2L wins |
| 4 | **ENGR 1000 BWD structure and meeting format** | Absent from every row in §3. Flag #57's remaining half |
| 5 | **PHYS §54 unit-exam room and sitting time** | Printed at the §51/52/53 recitation slot, not Chris's |
| 6 | **CSE final exam date** | Not printed in the lecture syllabus |
| 7 | **ECON textbook mapping** — Mathews & Patrono vs. the OpenStax substitute | The EDUCATION semester-map's chapter mapping is unverified against the real book |

---

*Per-course detail: `03-WIKIS\PHYSICS\wiki\semester-pathway.md` ·
`03-WIKIS\PYTHON\wiki\syllabus-alignment.md` ·
`03-WIKIS\EDUCATION\wiki\courses\econ-1000\semester-map.md` ·
`03-WIKIS\EDUCATION\wiki\courses\tcom-2010\semester-map.md`. Cross-course context:
`04-SCHOOL\SEMESTER_MAP.md`. Course source status: `04-SCHOOL\SYLLABUS_STATUS.md`.*
