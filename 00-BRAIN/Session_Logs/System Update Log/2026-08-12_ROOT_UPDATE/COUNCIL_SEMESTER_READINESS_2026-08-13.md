---
type: report
timeline: now
status: complete
tags: [council, update, semester-readiness, structure, capacity, fall-2026]
created: 2026-08-13
---

# Council — Semester Readiness Review

### Commissioned by Chris, 2026-08-13 afternoon: review the update in process for improvement, check the whole folder system, and protect the business/technology track through a semester that starts in 11 days.

**Freeze discipline held.** A council is a discovery pass and the finding freeze
forbids those. Chris directed this one, so it ran — but every new finding below is
**filed**, not worked. Nothing in this document was implemented as a side effect of
writing it. Four items are recommended for execution and each is named as a
recommendation requiring Chris's go.

| | |
|---|---|
| **Seats** | 1 Convergence · 2 Structure · 3 Semester contact · 4 The compounding engine |
| **Lead / reconciliation** | Claude Code (Windows) |
| **Acceptance owner** | Chris |
| **Method** | Live measurement of the tree, the health gate, and the registrar record — not re-reading yesterday's reports |

---

## The verdict in one paragraph

The update is doing genuinely good work and has been converging for two days — eight
Thursday items landed, verified, with the propagation discipline actually holding. The
danger is not quality; it is that **the release gate is defined by properties that cannot
be finished** ("every file justified", "operational and optimized") while the one thing the
system's own council ranked highest — a single executable artifact — remains untouched
for the third consecutive week. Then the calendar arrived and moved the whole problem:
**Chris has already booked Aug 17–21 as a 37.5-hour week to run real coursework through
`.ROOT`, and labelled Sunday Aug 16 "LAUNCH THE UPDATE into prep week."** The build window is
therefore **~32 hours ending Sunday**, not eleven days — and no system file knows this.
The capacity picture is likewise better and worse than assumed: Chris has already blocked
**~25 h/week of study time**, but every hour of it is named *"Sit down + Study"* with no
subject, against a protected technology floor of 5–10 h/week that the week pays **1.5 shared
hours**. His four rulings this session close the three worst structural gaps. What remains is
to stop expanding the gate, ship one artifact, **name the 25 hours**, and release Sunday.

---

## Chris's rulings, this session — recorded because they are new governance

| # | Question | Ruling |
|---|---|---|
| **R1** | Release-gate scope | ✅ **Bounded by file class.** Deep review for always-load, current-state, and semester-critical files only. Everything else takes a class-level disposition. **This supersedes the "1,544 files × five fields" wording in `UPDATE_PLAN.md` § Goal correction** |
| **R2** | Is income a survival condition? | ✅ **No — the Aug 11 ruling stands.** Not a condition of continuing past Fall 2026. The protected floor goes to compounding capability; revenue is opportunistic. **Four REVENUE_LAB files now contradict this and must be reconciled** |
| **R3** | Output bay (Phase E) | ✅ **Inside each course folder** — `04-SCHOOL\<course>\work\`. Closes the one structural decision with a hard Aug 24 deadline, four days before its own decision date |
| **R4** | Campus laptop | Windows wipe **already done**; setup in progress and partly ad-hoc. Chris wants a build specification and a Codex review. **Not blocked — in flight** |

---

## Seat 1 — Is the update converging or expanding?

**Converging on execution. Expanding on definition.**

The execution record is real: Aug 12 delivered 9 items, Aug 13 delivered 8, all gate-checked,
with commit SHAs. `root_health.py` is exit 0 and `validate_boot_chain.py` passes 32 files.
Always-load fell 7,138 → 5,803 words in one day. This is the most productive stretch the
update has had.

**S1-A — The gate has moved three times in 36 hours.**

| When | Release criterion |
|---|---|
| Aug 12 | T2 + Friday's technical gates + the three-structure test |
| Aug 13 am | **+ justify 1,544 Markdown files + "operational, optimized `.ROOT`"** |
| Aug 13 (Codex) | **+ state compiler + journey eval suite + truth-propagation check** |

Claude's own reconciled verdict already caught the third expansion and refused it. R1 now
closes the second. **The residue is the word "optimized," which has no test attached.** A
gate whose criterion is an adjective will move again. *Filed: define "optimized" as a
pass/fail list or strike it from the gate.*

**S1-B — The plan has the defect it was written to fix.**

`UPDATE_PLAN.md` is **985 lines / ~11,000 words** and has grown every day. It is required
reading for anyone touching the update — which makes it a de facto load file. Phase D's
entire insight was that `SYSTEM_FLAGS.md` grew without bound because every event appended
forensics to a document everyone must read. **The plan is now doing exactly that, and no one
has applied the lesson to it.** *Filed: at update close, split it the way `SYSTEM_FLAGS.md`
was split — a live phase register plus an execution-history file.*

**S1-C — Worth protecting: propagation is actually working now.** T8 took navigation debt
4 → 16 → 4 inside a single pass. T2 was marked in the plan, `NOW.md`, and the DAILY in the
session it happened. Council finding C1 was this vault's characteristic failure and it is
being actively countered. **Name it and keep it.**

---

## Seat 2 — The folder system, measured today

| Realm | Files | Note |
|---|---|---|
| `03-WIKIS` | **2,318** | PYTHON 882 · PHYSICS 374 · AIAS 302 · EDUCATION 262 · TECHNOLOGY 186 · SYSTEMS 173 · BUSINESS 123 · REVENUE_LAB 16 |
| `02-LIBRARY` | ~4,796 | of which `.PROJECTS` ~4,700 — **see S2-B** |
| `00-BRAIN` | ~335 | `Session_Logs` 210 = 63% |
| `04-SCHOOL` | **128** | `05-ENGR` **0 files** · `03-TCOM` 3 · `04-ECON` 7 · `02-Physics` 17 |
| `05-BUSINESS` | 34 | across 6 folders |
| `99-ARCHIVE` | ~600 | 269 loose, **all correctly `ARCHIVED_` prefixed — not a defect** |
| `77-INBOX` | **1** | the front door, effectively unused |

**S2-A — The three-noun ruling is right and is not yet true on disk.** `04-SCHOOL` is "what
he is graded on," and it holds 128 files with one empty course folder eleven days out from
receiving ~27 h/week. R3 fixes the container; the shape still has to be built.

**S2-B — Correction to an earlier concern, including my own.** `.PROJECTS` looked like the
largest un-inventoried mass in the vault. It is not. It is ~4,700 files of which
`MCP_Bootcamp` is overwhelmingly a **vendored Python environment** — 2,047 `.pyc`, 2,024
`.py`, plus `.pyd`/`.pyi`/`.typed` — and it is **already gitignored at `.gitignore:38`**.
Actual project work is five folders totalling ~44 files. **Decision #6 (`.PROJECTS` vs.
`00-PROJECTS`) drops from structural to cosmetic.** Recorded so no future session spends a
runway day on a phantom.

**S2-C — The capture path is broken and the inbox proves it.** `77-INBOX` holds one file.
The route into it is the Obsidian clipper — **the same clipper that lost five sources**
(flag #97, still open, "fix or retire before pointing it at anything else"). During a
semester, capture is the highest-frequency operation there is. K-3 already identified a
purpose-built capture template as the clipper's *replacement* rather than a convenience.
**This is a semester-readiness gap that appears on no critical-path list.**

**S2-D — The mass ratio is 18:1 against the semester.** 2,318 wiki files support a learner at
PYTHON Stage 4b of 11 and PHYSICS Stage 4 of 18. The Aug 11 council found content readiness
has not been the constraint for months; a month more of evidence agrees. **Recommendation:
a wiki content-generation freeze for the semester** — no new wiki pages except where a live
course deadline requires one. This is the cheapest single protection available for the
technology/business floor, because wiki maintenance is what will eat it.

**S2-E — Two hub loader files survive.** `00-BRAIN\CASTLE\CLAUDE.md` and `AGENTS.md` exist,
while `AGENT.md:142` states hubs no longer carry them (removed 2026-08-10). CASTLE is not in
`03-WIKIS`, so this is technically consistent — but a fresh session reads the claim and then
finds the files. *Filed, LOW.*

---

## Seat 3 — Does the system survive contact on August 24?

**This seat was rewritten after Chris supplied the live `.ROOT` Google Calendar (fetched
2026-08-13, 42 events).** The registrar-only analysis it originally carried was correct about
the class grid and **wrong about the conclusion.** The correction is the most useful thing in
this report and is stated first.

### S3-A — The runway has a hard deadline, and it is Sunday August 16 — not "next week"

Chris's own calendar sets the release moment explicitly. `NOW.md` says *"the completed
`OK TO START` statement comes next week."* **The calendar says next week is already booked for
something that requires the release to have already happened.**

| Date | Block (EDT) | Chris's own label | Hours |
|---|---|---|---|
| **Thu Aug 13** | 12:15–17:00 | *System Work Optimization* | 4h45 |
| **Fri Aug 14** | 09:30–17:00 | *"we can use 90% or so for system opti…"* | 7h30 |
| **Sat Aug 15** | 09:45–20:00 | *"This whole section should also be free time"* | 10h15 |
| **Sun Aug 16** | 10:00–20:00 | **"This needs to be LAUNCH THE UPDATE into prep week"** | 10h00 |
| **Mon–Fri Aug 17–21** | 09:30–17:00 daily | **"Do first week of class work with `.ROOT`"** | **37h30** |
| Sat Aug 22 | 09:45–20:00 | *Syllabi hunt for semester start and last min prep* | 10h15 |
| Sun Aug 23 | 18:00–20:00 | *Weekly Review + Next Week Plan* | 2h00 |

**Two conclusions follow, and both are load-bearing:**

1. **The build window is ~32 hours and closes Sunday Aug 16 at 20:00.** `OK TO START` should
   fire that evening, because Chris literally named that block *"LAUNCH THE UPDATE into prep
   week."*
2. **Aug 17–21 is a 37.5-hour rehearsal week whose purpose is to *use* the system, not build
   it.** Running the first week of real coursework through `.ROOT` before classes start is a
   far stronger readiness test than any gate in `UPDATE_PLAN.md` — and it is already scheduled.

**This supersedes two entries in `NOW.md` § Fixed and Dated.** "August 22 — dress rehearsal
(Week D)" does not match the calendar: **Aug 22 is syllabi hunt and last-minute prep**, and the
real rehearsal is the *preceding week*. The system is planning a rehearsal for after the
rehearsal has finished.

### S3-B — The class grid, and one conflict to resolve before day one

| | Mon | Tue | Wed | Thu | Fri |
|---|---|---|---|---|---|
| 08:00 | | ECON (ETC 202) | | ECON | |
| 09:10 | PHYS (Acad 200) | | PHYS | | PHYS |
| 09:30 | | TCOM | | TCOM | |
| 11:30 | | | | | PHYS breakout (Atrium 1116) |
| 16:10 | CSE (Acad 203) | | CSE | | |
| 17:45 | | **CSE Lab** (Atrium 2120) | | | |

Every class time above matches the registrar record.

**Total scheduled contact — all six components summed, stated explicitly because the figure is
easy to misread as belonging to one course:**

| Component | Meeting | Minutes/week |
|---|---|---|
| PHYS 2211 lecture | MWF 09:10–10:05 | 165 |
| PHYS 2211 breakout | Fri 11:30–12:25 | 55 |
| ECON 1000 | Tu/Th 08:00–08:55 | 110 |
| TCOM 2010 | Tu/Th 09:35–10:55 | 160 |
| CSE 1321 lecture | Mo/We 16:10–17:30 | 160 |
| CSE 1321L lab | Tue 17:45–19:35 | 110 |
| **ENGR 1000 BWD** | **none published** | **0 — unknown** |
| | | **760 min = 12h40** |

**⚠ ENGR 1000 BWD is a genuine hole, not an assumption.** It carries 1 credit and has **no
meeting time on the registrar record and none on the calendar.** Chris's read is that it is
likely online — roughly twelve ~40-minute sessions, or one longer weekly block. Nothing on file
confirms either shape, and its AI policy is known-prohibited, which makes the delivery format
consequential rather than cosmetic. **This is the second half of flag #57 and a second reason
to email today** — the Aug 17–21 rehearsal week cannot rehearse a course whose format is
unknown.

**⚠ TCOM 2010 has three different rooms on file.** The registrar says **Academic Building 202**;
the calendar event says **Atrium 2216**; and the 09:00 walk event says **Atrium 2236**. One of
these is right. **Chris confirms in D2L or on the first-day walk — do not guess.** *Filed.*

### S3-C — The real finding: capacity is not the problem. Naming is.

The original registrar-only reading said gap time was "unplanned." **It is planned.** Chris has
already blocked it. Measured across the semester template:

| Category | Hours/week | State |
|---|---|---|
| **Generic study blocks** — *"Sit down + Study"*, *"Sit + Study"*, *"do what you can in the time"* | **~25 h** | ⚠️ **unnamed — no subject, no proof, no deliverable** |
| `PYTHON ONLY STUDY` (Tue 16:00–17:45) | 1h45 | ✅ the **only** subject-labelled block in the week |
| `Relax and Needed System Maitence` (Sat 15:30–17:00) | 1h30 | the only system/tech block |
| Gym (Mon–Wed, Fri 13:00–15:00) | 8 h | protected, and correctly so |
| Ben / family / Heather | ~25 h | protected, and correctly so |

**Twenty-five hours a week of blocks named "Sit down + Study."** Set that against Chris's own
Round One words, already on file since July 26:

> *"I don't study without being told what to study, I will go tangent and read something else
> completely."*

**The calendar has built, at scale, exactly the condition he says causes him to lose the
session.** This is not a scheduling failure — the discipline is genuinely impressive. It is a
**routing** failure, and it is the single highest-leverage fix available before Aug 24: the
system's job is to put a subject, a proof, and a next action on each of those 25 hours. That is
what `EVENING_READING.md` and CASTLE already exist to do, and it has never been pointed at the
real calendar.

### S3-D — The protected floor is contradicted by the calendar, measurably

`NORTH_STAR.md` §4 and `AGENT.md` guarantee a **5–10 h/week technology/business floor during
semesters**. The calendar allocates **1h30** — a single Saturday block labelled *"Relax and
Needed System Maitence,"* which is shared with relaxing.

**Governing law says 5–10 h. The week provides 1.5 h, shared.** Phase E's note that
"BUILD/PROJECTS time on the semester calendar is zero" is now confirmed by direct measurement
and is worse than recorded, because the one candidate block is also the rest block. Under R2
the floor exists to build compounding capability — and there is nowhere for it to happen.

**Two honest options, and this is Chris's call:** convert ~4 h/week of the 25 unnamed study
hours into a named technology block, or amend the law to match the life. **What must not
continue is a governing document promising 5–10 hours that the week cannot pay.**

### S3-E — Tuesday, and one unmodelled trip

Tuesday runs **06:45 → 20:20**: travel prep, ECON, a walk, TCOM, gym, study, CSE Lab until
19:35, then travel home to dinner. It is the longest day and the only one with three courses.
**Recommendation: Tuesday carries zero optional system work, permanently, and is pre-staged
Monday evening** — which `EVENING_READING.md` already exists to do.

**⚠ One gap in the model:** gym is blocked Tue 13:00–15:00, but Chris is on campus from 08:00
until the lab ends at 19:35, and the only Tuesday travel-home block is *after* the lab. Either
the gym is the KSU recreation centre — in which case the block is fine — or there is an
unmodelled round trip in the middle of the longest day of the week. *Needs Chris's answer.*

### S3-F — Flag #57 should fire today, not Aug 17

PHYS 2211 §54 is 3 credits, MWF plus breakout, and Chris has **no grading weights, no exam
count, and no policy**. The instructor is confirmed twice over — Farhan Islam,
`fislam7@kennesaw.edu`, corroborated independently by the registrar record. **Waiting four more
days gains nothing**, and the rehearsal week starting Aug 17 is materially weaker without the
real syllabus. **Recommendation: send both emails (PHYS §54, ENGR BWD) today.** Chris's action;
it is outbound.

### S3-G — On Aug 24 the suspension lifts onto a rule that has never been enforced

`NOW.md` suspends Execution Discipline 1 for the runway. When it resumes it becomes the most
important rule in the file — and council C2 measured that in the six days to Aug 11, **20+
sessions read that rule and one touched learning.** The rule exists; the instrument does not.
Worth arguing back onto the runway (see the sequence).

---

## Seat 4 — The compounding engine

R2 settles the direction: the floor is for **capability**, not revenue. That makes the next
finding sharper, not softer.

**S4-A — With income deprioritized, the floor has exactly one job, and it is the one job that
has never been done.** Council step 4 — *one ML/data rep on real data* — was ranked
**highest value ÷ effort in the entire vault** on Aug 11, costs 3–4 hours, and is still open.
Measured again today:

- **Zero `.ipynb` files anywhere in `.ROOT`.** Not one.
- Against 3,789 pages of AI/ML material read, 30 named ML design patterns catalogued, and
  `skill-map.md` listing probability/statistics, LLM extraction, and provider APIs as
  *not-started*.
- **And the data is already sitting on disk:** `04-SCHOOL\04-ECON\datasets\` holds real FRED
  macro series — `CPIAUCSL` (CPI), `GDP`, `GDPC1` (real GDP), `UNRATE` (unemployment).

The Aug 11 council set its own ordering rule and then the vault spent two days breaking it:

> *Anything that produces an executable output precedes anything that produces a cleaner document.*

**Two full days of the runway have produced cleaner documents. This is the one item that
produces an artifact.** It is also, conveniently, non-submission personal work against public
macro data — so it sits entirely outside every course's academic-integrity boundary.

**S4-B — Four files now contradict a standing ruling.** Per R2, these say income is "a
condition of continuing past Fall 2026":
`REVENUE_LAB\README.md:12-13` · `REVENUE_LAB\HOW_TO_USE.md:14` · `REVENUE_LAB\wiki\log.md:11` ·
`REVENUE_LAB\wiki\revenue-lane-scan-brief.md:9`. A fifth,
`Goals & Milestones\value_production_goal.md:17`, frames continuity income before Spring 2027
as an outcome. **C1 discipline says these get reconciled in the same session as the ruling.**
Small, bounded, ~20 minutes. Recommended below.

**S4-C — CASTLE's `current-position.md` is 25 days stale.** It reads "July 2026 Monthly
Baseline," reconciled July 19, and states *"Next monthly reconciliation: August 1, 2026."*
That date passed twelve days ago. Codex's W3 independently found EDUCATION and PHYSICS
`current-position` semantically stale. **This is the sequencing layer for the whole system,
and the semester starts in 11 days against a July baseline.** *Filed as the highest-value
staleness item.*

---

## Where the seats converge

1. **The system's failure mode is producing documents instead of artifacts** (S1-B, S4-A,
   and the Aug 11 council's own T2). Three independent reviews across three days.
2. **The semester's real constraint is routing, not content and not capacity** (S2-D, S3-C,
   S4-A). There is enough material — 2,318 wiki files. There are enough hours — ~25/week
   already blocked. **What is missing is the assignment of subject to hour**, which is the one
   thing Chris said in July he cannot supply for himself.
3. **Detection still outruns propagation** (S1-C is the counter-example that proves the rule;
   S4-B and S4-C are two live instances discovered today).

## Where the seats are in tension

**Seat 1 wants the gate closed and the update shipped. Seat 3 wants four more things built
before Aug 24.** Both are right, and the resolution is that they are not competing for the
same hours: the gate is *document* work and the semester items are *build* work. **Resolution:
cap the gate at R1's bounded scope and give every remaining runway hour to build.** The gate
does not get more valuable with more hours; the semester shape does.

---

## Corrections the record needs

| # | Where | Correction |
|---|---|---|
| 1 | `UPDATE_PLAN.md` § Goal correction | "1,544 files × five fields" is **superseded by R1** |
| 2 | 4 REVENUE_LAB files + `value_production_goal.md` | Income as survival condition is **superseded by R2** |
| 3 | `UPDATE_PLAN.md` Phase E / Decision 5 | **Ruled by R3** — `work\` inside each course folder |
| 4 | `UPDATE_PLAN.md` Decision 6 | `.PROJECTS` is a gitignored vendored venv — **cosmetic, not structural** |
| 5 | `CASTLE\wiki\current-position.md` | 25 days stale, past its own stated reconciliation date |
| 6 | `NOW.md` § Fixed and Dated | **"Aug 22 dress rehearsal"** is wrong. The rehearsal is **Aug 17–21**; Aug 22 is syllabi hunt + last-min prep (S3-A) |
| 7 | `NOW.md` § Active Lane | *"the completed `OK TO START` comes next week"* — **next week is the rehearsal.** Release is **Sun Aug 16** |
| 8 | `04-SCHOOL\SYLLABUS_STATUS.md` | ENGR 1000 BWD has **no meeting format**, not just no syllabus — record the gap explicitly (S3-B) |
| 9 | TCOM 2010 room | **Three rooms on file** — Academic 202 (registrar), Atrium 2216 (calendar), Atrium 2236 (walk event). Confirm before day one |

---

## The reconciled sequence — anchored to the calendar, not to Aug 24

**The build window is ~32 hours and closes Sunday Aug 16 at 20:00**, because Chris's calendar
books Aug 17–21 as a 37.5-hour rehearsal week that *uses* the system. Everything below is
sized to fit inside that window. `OK TO START` fires Sunday evening.

### Window A — Today, Thu Aug 13, 12:15–17:00 (4h45)

| # | Action | Cost | Owner |
|---|---|---|---|
| 1 | **Email both instructors** — PHYS §54 and ENGR BWD. The rehearsal week cannot rehearse an unknown course | 10 min | **Chris** (outbound) |
| 2 | **Campus laptop build spec** + execute alongside Chris; Codex reviews | ~2 h | Chris + AI |
| 3 | **Build the output bay** — `work\` in all six course folders per R3, plus the `WHERE_IT_GOES.md` routing line | 30 min | Claude |
| 4 | **Reconcile the 5 income files** to R2 | 20 min | Claude — C1 discipline, same session as the ruling |
| 5 | **Three empty folder shells** — `tmp\`, `outputs\`, `...projectSuccess\` | 2 min | **Chris**, in Explorer |

### Window B — Fri Aug 14, 09:30–17:00 (7h30, Chris says ~90% system)

| # | Action | Cost |
|---|---|---|
| 6 | **The Friday gate** — technical checks + the PHYS/CSE/TCOM structure test | ½ day |
| 7 | **The file-class register** — the deliverable that makes R1 executable and does not yet exist | ~2 h |
| 8 | **Refresh `CASTLE\current-position.md`** to an August baseline | ~1 h |

### Window C — Sat Aug 15, 09:45–20:00 (10h15)

| # | Action | Cost | Why here |
|---|---|---|---|
| 9 | **Deep review: ~60–80 files** — always-load, current-state, semester-critical; class-level disposition for the rest | ~4 h | This *is* the bounded gate under R1 |
| 10 | **Name the 25 unnamed study hours** (S3-C) — a subject, a proof, and a next action per recurring block, wired to `EVENING_READING.md` | ~2 h | **The highest-leverage item in this report** |
| 11 | **One data rep on the FRED data already on disk** — heuristic benchmark first, then k-fold with mean *and* standard deviation, leakage asked variable by variable | 3–4 h | **Highest value ÷ effort in the vault, open since Aug 11. The only item that produces an artifact** |

### Window D — Sun Aug 16, 10:00–20:00 — *"LAUNCH THE UPDATE into prep week"*

| # | Action |
|---|---|
| 12 | **Resolve the floor contradiction** (S3-D) — 4 h/week named technology block, or amend the law. Chris's call |
| 13 | **Wiki content freeze** for the semester (S2-D) — one clause |
| 14 | **Tuesday protection rule** (S3-E) — zero optional system work, pre-staged Monday evening |
| 15 | **A minimal proof instrument** (S3-G) — days-since-last-learner-proof emitted into `NOW.md` |
| 16 | **The `77-INBOX` capture template** (S2-C) — replaces the clipper that lost five sources |
| 17 | **Assemble and fire `OK TO START`** — with named, owned debt rather than a claim of completeness |

### Window E — Mon–Fri Aug 17–21, the rehearsal week (37h30)

**No system building.** Run the first week of real coursework through `.ROOT` and let the
failures name the remaining work. This is a stronger readiness test than any gate in
`UPDATE_PLAN.md`, and it is the only place where "operational and optimized" can actually be
evidenced rather than asserted.

Fixed inside it: **Aug 17 — Drive relink ruling** (scoped link, not a re-sync of the dead Aug 9
copy). Anything the rehearsal breaks is filed and fixed in the **Sat Aug 22** block, which
Chris has already labelled *syllabi hunt and last-minute prep*.

### Tier 4 — Cut or defer, with dates

| Item | Disposition |
|---|---|
| Full 1,544-file justification | **Cut** — superseded by R1 |
| Journey eval suite (Codex) | **Defer to October.** Genuinely good, wrong moment |
| State compiler beyond the two failing facts | **Defer.** Add only when a real failure names one |
| J-3 playbook → skill conversion (2,497 w) | **Defer to the first semester break.** Decided, not urgent |
| K-2 mutual calibration record | **Defer indefinitely** until a real friction instance names it. A new unbounded append-target is the exact defect Phase D just fixed |
| Codex W2/W3 (shared-layer + freshness matrices) | **Defer**, except `CASTLE\current-position.md` which is item 11 |
| Codex W1 (4 health-debt items) | **Fold into Friday** if it is genuinely one index fix; otherwise defer |
| `.PROJECTS` rename | **Cut** — cosmetic (S2-B) |
| Phase F — mine the July 26 interview | **Fold into item 8.** It is one of the files being reviewed |
| `AGENT.md` Execution Discipline pass (517 w) | **Stays deferred** per Chris's ruling |

---

## Decisions still needed from Chris

1. **Confirm the Sunday Aug 16 release date** (S3-A). It is read off Chris's own calendar
   label, but no system file carries it and the whole sequence depends on it.
2. **The floor contradiction** (S3-D) — convert ~4 h/week of unnamed study into a named
   technology block, or amend `NORTH_STAR.md` §4 to match the week. **Do not leave a law
   promising 5–10 hours the calendar cannot pay.**
3. **Does "optimized" get a pass/fail definition, or come out of the gate?** (S1-A) — the last
   moving part in the release criterion.
4. **Wiki content freeze for the semester** — yes/no (item 13).
5. **Two calendar facts to confirm:** the TCOM room (three on file), and whether Tuesday's
   13:00–15:00 gym is on campus or an unmodelled round trip (S3-E).

---

## Return Packet

- **Outcome:** four-seat council delivered; four Chris rulings recorded as new governance;
  five corrections to live documents identified; an 11-day sequence with explicit cuts.
- **Evidence:** live tree measurement, `root_health.py` (PASS WITH DEBT, exit 0, 1,526 files),
  the registrar schedule, **the live `.ROOT` Google Calendar (42 events, fetched 2026-08-13)**,
  `.gitignore`, extension-level inventory of `.PROJECTS`, and a vault-wide `.ipynb` scan
  returning zero.
- **Capability/status movement:** none. This document authorizes nothing; Chris is the
  acceptance owner.
- **Reusable-asset candidate:** the derived weekly time-shape table and the 25-hour unnamed
  study measurement — the input to every semester planning decision, and neither existed
  before today.
- **System-learning candidate:** two, pending second instances. (1) *A release gate defined by
  an adjective will move; gates need tests, not adjectives.* (2) **The strongest finding in
  this review came from a source outside the vault entirely.** Every gate, validator, and
  council seat had been pointed inward at `.ROOT`'s own files; the deadline that reorganised
  the whole sequence was sitting in Chris's calendar, which no instrument had ever read.
  *Filed, not promoted.*

## Correction made during drafting

An earlier draft of Seat 3 read the semester off the registrar record alone and concluded that
~20 h/week of campus gap time was **unplanned**. The calendar showed that conclusion was wrong:
the time is planned, blocked, and disciplined — it is *unnamed*. Recorded here rather than
silently overwritten, because the difference between "Chris has not scheduled his time" and
"Chris has scheduled it and the system has not filled it" points at completely different work,
and only the second one is true.
