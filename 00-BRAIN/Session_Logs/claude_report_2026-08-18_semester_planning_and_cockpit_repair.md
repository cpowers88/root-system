---
type: report
timeline: now
status: active
tags: [school, fall-2026, planning, governance, cockpit, laptop]
created: 2026-08-18
session_date: 2026-08-18
---

# Session report — semester planning, source intake, and cockpit repair

### Claude Code, Tuesday 2026-08-18, afternoon through evening (~13:30–19:00). Twelve commits, all pushed. `root_health.py` **PASS WITH DEBT, 0 blockers** at close; `wiki_lint --strict` blockers 0. Companion to `claude_report_2026-08-18_laptop_config_and_syllabus_verification.md`, written mid-session and written to be read on the laptop.

**Scope note.** This session ran *after* the 15:00 "have to run" handoff and continued past it;
`HANDOFF_0818_CLAUDE_CODE.md` carries an addendum covering the whole day. The DAILY holds the
task blocks. **This report exists for the findings**, which outnumber and outlast the tasks.

---

## 1. The finding that connects most of the day

**Four of Chris's Fall 2026 course documents are recycled Spring documents, and the carryover
reaches real due dates.** Each was found independently, in a different file, while doing
something else:

| Document | Evidence | Consequence |
|---|---|---|
| **TCOM 2010 §04 syllabus** | Prints *"due on Friday, January 16th," "due Tuesday, January 20th," "Business Email FINAL due Tuesday, January 27th"* | Every TCOM date in the semester plan is placed **by week number, not printed date** |
| **CSE 1321 BF syllabus** | Week 15 topic reads *"May 4th, 2026, Last Day of Classes"* in a Fall document; week 1 quizzes print a Dec 07 due date | Confirmed carryover; the Dec 07 item remains genuinely **ambiguous, not proven wrong** |
| **CSE 1321L syllabus** | Whole calendar runs **Jan 12 – May 3**, with MLK Day and spring break | Lab midterm/final positions usable; dates not |
| **CSE lab + assignment files** | Every file versioned `sp26` / `spr26` | Lab 1's body prints `# Term: ...` as a blank — term-agnostic by construction |

**The rule this produces, now written into four vault files:** *sequence and week number are
reliable; printed dates are not.* Dates used anywhere in the plan come only from the sources
that are genuinely Fall-dated — the **registrar record**, the **PHYS §54 syllabus**, the CSE
1321 lecture calendar, and the ECON dated schedule.

---

## 2. The failure class that produced most of the corrections

Six separate defects this session were the same shape: **a document asserting a state that
nobody had checked against the authority.** `.claude\CONTROL_INVENTORY.md` names this failure
class for controls; it is not confined to controls.

| Defect | Authority that disproved it |
|---|---|
| `CAMPUS_LAPTOP_BUILD.md` §10 framed the LockDown quiz as an open gate **without saying it was impossible** | `SEMESTER_MAP.md` had already ruled D2L opens Aug 24 — on 2026-08-13 |
| §2.1 read LockDown as covering **all 10 quizzes**; syllabus line 84 scopes it to **exams** | The syllabus itself |
| My own workload plan said **14 credits, PHYS at 4** | `fall_KSU_schedule.md` — registrar: **13 credits, PHYS 2211 is 3.0** |
| §7 check 10 asked the battery to survive **2h15**; the real gap is **~6 hours** | Registrar meeting times |
| `EDUCATION\wiki\current-position.md` claimed *"Weeks 6–15 are not yet extracted"* | `courses/tcom-2010/semester-map.md` — rows run through **week 14** |
| `NOW.md` said *"PHYS row 3 — PASSED"* while its own durability note said row 3 was the only rep still owed | `NOW.md`, fifteen lines lower |
| **A seventh, caught while writing this report:** the pointer I added to `SEMESTER_MAP.md` still said *"14 credits … ~11.75 hours of campus blocks"* hours after the plan it points at was corrected | `semester-workload-plan.md` §1 |

**The seventh is the most instructive**, because it is this failure class reproduced by the
session that was documenting it: **a pointer describing another file's contents, not updated
when that file changed.** Corrected in the same pass. A cross-file summary is a claim about a
sibling page and carries the same obligation as any other.

**Two of these were mine**, made this session and corrected the same session. The TCOM
`current-position` one is the sharpest instance: it is *"absence in the file consulted read as
absence in the vault"* — the exact error corrected for ECON on 2026-08-13 — **recurring inside
the page that recorded the first correction**, because the status board was written from memory
of the map rather than from the map.

**Standing fix added to that hub:** a status claim about a sibling page must be checked against
that page in the same edit.

---

## 3. Google Drive — the link is intact, verified four ways

Chris disconnected the mirror by accident, reading the wrong machine's screen, and asked whether
he had broken it. **He had not.**

1. **Config row unchanged.** `root_preference_sqlite.db`, `roots` table — the authority
   `LOCAL_MACHINE_MAP.md` names over the UI: `sync_type 1 (mirror)` · `destination 1` ·
   `state 2 (active)` · `C:\Users\chris\.ROOT`. Identical to the Aug 17 baseline.
2. **Today's edits are in the cloud, matching to the millisecond** — `CAMPUS_LAPTOP_BUILD.md`
   local `14:44:28.756` ↔ Drive `18:44:28.756Z`; the new report at `14:56:45.957` ↔
   `18:56:45.957Z`, 13,493 bytes, so the mirror **creates** as well as updates.
3. **Live round trip after the disconnect.** GoogleDriveFS restarted **15:04** — the fingerprint
   of the accident. A probe written **15:27:08** reached Drive at `19:27:09.520Z`: **a
   one-second upload, 23 minutes post-reconnect.** This is the decisive test.
4. **No duplicate device root.** The only `.ROOT` folders in Drive were created Aug 11–12.

**Not verified:** that the Drive UI lists it under Computers → [device]. A display question; the
config row and a one-second upload settle the substantive one.

**Still unfixed and dangerous:** `LOCAL_MACHINE_MAP.md:110` reads *"neither it nor Drive sync is
a working tree or AI boot target going forward"* — July-17 language contradicting lines 39–45 of
its own file. **It is the single sentence most likely to authorise deleting the live mirror**,
which is the exact question Chris opened the session with. Now `NOW.md` open risk 4.

---

## 4. Semester planning — what was built

**`04-SCHOOL\semester-workload-plan.md`** (new). The per-course semester maps already existed in
PHYSICS, PYTHON and EDUCATION; **none quantified weekly effort or scheduled it against real
available time.** That was the gap.

**Numbers that did not exist anywhere before:**

- **13 credit hours**, ~**26–39 h/week** outside class at the standard ratio.
- **All-A total: ~430 hours**, range 372–495, ~28 h/week. Three methods, and the spread is
  itself the answer — the week-by-week table sums to ~304 h, which is a **deliverable-completion
  floor**; the gap to the credit-hour range is precisely *the difference between finishing the
  work and earning an A*.
- **PHYS is ~37% of the outside-class load** despite being 3 credits, because 75% of its grade
  is four closed-book exams plus a comprehensive final.
- **Campus mid-day gaps: 21.75 h raw → 16.33 h** on Chris's own realistic estimate (2 h less
  Mon/Wed, Friday's short gap to the gym). Leaves **~11.7 h/week** for evenings and weekends —
  about **1.7 h/day**, not the four hours the uncommitted reading implied.
- **Week 12 (Nov 9–15) is the worst week of the semester**: CSE Test 2 Monday, TCOM Technical
  Report due, group presentations, reflective memo, ECON quiz, two labs, an assignment — ~26 h.
  **The report is the movable piece** and has draft checkpoints from week 6.

**The laptop is load-bearing.** It carries ~58% of outside-class study time. That reframing is
what exposed the battery defect in §2 above.

---

## 5. Codex's semester strategy — reviewed, not adopted

Codex produced a full strategy; per `CLAUDE.md` § Doctrine, it was checked against the live
syllabi rather than taken on trust. **Every grade mechanism it stated verified correct**, all
ECON and PHYS dates verified, and its hour allocations matched mine independently. Four changes:

1. **It under-sold the best free points in the semester.** It said *"confirm whether tutoring
   visits add points."* Already confirmed on disk, in **both** syllabi: **0.5% per CCSE Tutoring
   Center visit on the final exam score, max 5% for 10 visits, applied to the lecture *and* lab
   final exam scores** (CSE 1321:94; CSE 1321L:120–122). CSE 1321's final is 25% of that grade,
   the lab's is 30%. **Deterministic gain, no performance risk** — the only points in the plan
   with that property. Promoted to a standing action from week 1; deadline Dec 7.
2. **It left 50% of the lab grade unscheduled.** Midterm 20% + final 30%, no dates. The lab
   syllabus places the midterm after Module 3 / Lab 7 / Assignment 4, during the regular Tuesday
   lab → **week 8, ~Tue Oct 13, the day after PHYS Unit Exam 2.** A third collision week its own
   list did not name.
3. **Two of its four PHYS exam sweeps land inside collision weeks** — the Oct 5–11 sweep starts
   the day CSE Test 1 is written; the Nov 9–17 sweep sits on top of week 12. Both moved forward.
4. **Tuesday is over-assigned** — three courses inside a day running 08:00–19:35, ending in a
   two-hour lab, and it is the one block still counted at full value.

---

## 6. Source intake — 8 clippings routed, 6 books classified, 20 prompts refused

**`77-INBOX` emptied under a named raw exception.** Eight w3resource clippings moved to
`03-WIKIS\PYTHON\raw\`, beside the Aug 11 sibling from the same series. All eight verified
**byte-identical by SHA-256** before and after. Two earlier move attempts were denied at the
permission prompt and **were not worked around** — the move ran only after Chris confirmed.

**Three of six new books must not be used**, found by reading each file's own title page rather
than its filename: `dive_into_python` is **Python 2** (covers Mac OS 9), `python_quick_tour` is
**Python 2 era, dated May 2 2002**, and `python_game_programming` is an **older 2nd edition** of
a book already mapped at 4th. `pro_git` is not Python and not a CSE requirement — routing
question raised rather than filed into the pathway. A 50% reject rate on one batch is the reason
the source map is read before a source is used.

**Twenty live assignment prompts were deliberately not ingested.** `OPERATIONS.md` forbids
transforming a live prompt into practice, and graded status was unambiguous — Lab 1's own text
describes Gradescope autograding. **Topic order was extracted from filenames only**, which
§ INGEST permits, and it surfaced that **M2 flow control is the course's heaviest block (3 labs,
2 assignments) landing on vault Stages 2–3 — the frontier stuck since July.**

---

## 7. Cockpit repair — four defects Chris flagged

| Item | Root cause | Fix |
|---|---|---|
| **Morning brief stale** | **Structural, not neglect.** Evening reading has had a generator *and* a scheduled task since July; the morning brief had instructions and **neither** | `run_morning_brief.ps1` + scheduled task **"ROOT Morning Brief," daily 06:00**. Verified by running it |
| **Evening reading not semester-aware** | Source Priority named only PYTHON and PHYSICS, so **TCOM, ECON and ENGR nights had no stated source** | Per-course owner-page table for all five, the `2e_Word` trap, and a rule that from Aug 24 the current week of the workload plan governs |
| **Education tracking gaps** | EDUCATION's log stopped **Aug 13** while TCOM work ran Aug 17–18 and PHYSICS/PYTHON logged theirs | Backfilled; `current-position.md` corrected and re-dated |
| **NOW.md stale** | **A contradiction, not a date** — "row 3 PASSED" against its own "row 3 is the only rep still owed" | Corrected to `passed (immediate)`, durability owed Wed Aug 19; Aug 24 mode-change note and a freshness rule added |

**The evening-reading fix earlier in the day was the same shape:** the brief was assigning
circular-motion physics because a **dated override (Aug 3–23)** restricted the School line to a
15-minute physics primer. Ended five days early at Chris's direction and marked
do-not-reinstate. The rotation was also **backwards** — Python 3 / Physics 2 / TCOM 1, set in
July before the buffer was measured, while PHYS and CSE sit +2 weeks ahead and TCOM is at 0 with
graded work in week 1. Now **TCOM 2 / ECON 2 / Python 1 / Physics 1**, rebalanced on the deficit
rather than a fixed date.

---

## 8. Controls behaved correctly, twice, against this session

Recorded because a control that only ever fires on someone else is untested.

- **The bulk-work gate denied a read-only `for` loop** over eight filenames, with the wrapper
  redirect — flag #101's known shape. Worked around with a single `ls`; **`ALLOWED_SCRIPTS` was
  not widened.**
- **The deny list blocked deletion of this session's own Drive sync probe.** `Bash(rm *)` and
  `PowerShell(Remove-Item *)` both denied. **The probe is still on disk and is Chris's to
  remove** — `00-BRAIN\Session_Logs\.drive_sync_probe.txt`, untracked, 27 bytes.
- **Claude Code reported that four `Write(...)` deny rules are inert** — "only `Edit(path)`
  rules are matched by file permission checks." **Coverage is intact**: `Edit(...)` rules already
  cover the same paths, so the `Write(...)` lines are redundant rather than a hole. Worth
  tidying, not urgent.
- **A health-gate BLOCKER was diagnosed rather than silenced.** `0x1F` in a `77-INBOX` Python
  clipping — and the byte is *correct content*: the file is a Caesar-cipher exercise where
  space − 1 = `0x1F`. Stripping it to green the gate would have corrupted capture evidence.
  Resolved by routing the file to its correct home, since `raw` is already excluded from the
  text scan. **No script changed, no source edited.**

---

## 9. Open items

**Chris's, blocking nothing:**

1. **Delete the sync probe** — `Remove-Item C:\Users\chris\.ROOT\00-BRAIN\Session_Logs\.drive_sync_probe.txt`
2. **Identify the second `.ROOT` on the laptop before deleting it** — sweep and verdict table in
   the laptop report. **This is the one item with an irreversible downside.**
3. **Is an AI assistant going on the laptop?** The user-scope config deploy waits on it, and
   §5 made the AI/no-AI split structural for three AI-prohibited courses.
4. **`pro_git.pdf` routing** — TECHNOLOGY or `02-LIBRARY`, not the PYTHON pathway.
5. Carried from the 15:00 handoff: the TCOM technical-report topic, the path-audit cluster's
   home, Week D's two approval gates, Day One Access opt-out (**hard deadline Fri Aug 28**).

**System, unfixed and named:**

- `LOCAL_MACHINE_MAP.md:110` — the sentence that could authorise deleting the live Drive mirror.
- `SEMESTER_MAP.md:261` still says "confirm the week-1 quiz date anomaly" — **singular**; it is
  four items.
- **`run_evening_reading.ps1` still strips only a trailing code fence.** The morning script's
  sanitizer fixes this; porting it is a small, obvious win.
- **The laptop is still absent from `LOCAL_MACHINE_MAP.md`** — the build checklist's own step 7.
- ENGR 1000 BWD: no Fall syllabus. **Check moment Fri Aug 21.** Absent from every row of the
  workload plan **by design**, not oversight.

**Aug 24, when D2L opens:** the seven-item reconciliation list, `semester-workload-plan.md` §8.

---

## 10. Honest limits of this session's output

- **Every hour figure in the workload plan is derived, not measured.** Credit ratios and
  deliverable counts, no logged weeks. §7 of that page asks for correction after the first three
  real weeks; until then they are estimates wearing a table.
- **Tuesday's 6.83 h block is the one assumption not stress-tested.** It received no realism
  haircut while Monday and Wednesday did.
- **The Google Calendar was never read.** It cannot be — no Calendar tool exists in this session
  and WebFetch refuses authenticated URLs. The campus-hours figures came from Chris directly and
  from the registrar record. **An `.ics` export dropped into `77-INBOX` would end this
  dependency**, which the vault has carried since `CAMPUS_LAPTOP_BUILD.md` opened with *"the
  calendar answers this precisely"* and then paraphrased it from memory. **PHYS being logged as
  4 credits when the registrar says 3 survived exactly because the authoritative source was
  never opened.**

---

## Commits

`dae70e7` laptop config report + D2L timing · `ae2453a` session close + BLOCKER logged ·
`bc0e885` raw intake under named exception · `1091c0f` semester-prep ingest ·
`c7bd42c` evening reading rebalanced · `b37eecc` semester workload plan ·
`f49fffe` registrar correction, 13 credits · `7dda12c` campus gaps confirmed, battery 3× off ·
`98e5e2e` campus hours revised to 16.33 · `c53e3a4` Codex review folded in ·
`6d630a5` four cockpit defects · `00ac16d` Codex's handoff brought under version control.

*All pushed to `origin/main`. Working tree clean at close.*
