---
type: report
timeline: now
status: complete
tags: [update, hats, teaching, learning, codex-review, rehearsal-readiness]
created: 2026-08-13
session_date: 2026-08-13
---

# Teaching-layer rebuild — Codex's review implemented, and where this went past it

**Lead:** Claude Code (Windows). **Independent challenger:** Codex, whose launch-readiness
review of the rewritten hats arrived this afternoon. **Acceptance owner:** Chris. Per
`AGENT.md` § Execution Discipline 6, this is the single reconciled record: what Codex found,
what was implemented, where this report deliberately went further than Codex recommended, and
what the evidence is.

**Codex's verdict, adopted:** *structurally ready for rehearsal, not yet ready for
unsupervised trust.* Nothing below changes that verdict — it changes how much of the wording
risk survives into rehearsal. Answer: none of the five named items.

---

## 1. The state of the layer, measured

| File | Start of day | End of day | Change |
|---|---|---|---|
| `HAT_EDUCATOR.md` | 1,254 | **1,519** | rewritten twice — content added, then **integrated** (peaked at 2,205 mid-day; −31% on the final pass with zero content loss) |
| `HAT_PHYSICS_MATH.md` | — | **1,339** | **new** — the calculus/trig mechanics hat Chris requested |
| `HAT_PYTHON.md` | 680 | 1,094 | rewritten; LockDown Browser + dated exams added |
| `HAT_TCOM.md` | 576 | 920 | rewritten; week-1 graded work + 35% report homed |
| `HAT_ECON.md` | 631 | 858 | rewritten; AI-allowed-if-credited added (was absent) |
| `HAT_PHYSICS.md` | 547 | 682 | rewritten on the integration standard; math-hat routing |
| `HAT_ENGR1000.md` | 358 | 597 | rewritten; false calendar-block claim corrected |
| Layer total | 8,320 | **11,283** | all conditional-load; **always-load unchanged at 5,803** |

**Gates after every write:** `validate_boot_chain.py` PASS (32 files, 1,368 pages) ·
`root_health.py` PASS WITH DEBT exit 0, debt still the pre-existing 4 · Markdown integrity
1,542 files, 0 findings.

---

## 2. Codex's five wording findings — disposition

| # | Codex finding | Disposition | How |
|---|---|---|---|
| 1 | *"Used in every session" is too literal* — cold checks and anchors only fire when applicable | ✅ **Implemented, structurally** | The seven are now "**standing methods** — always loaded, each firing when its trigger occurs," and **every method carries its trigger inline**: *"trigger: any term that must stick," "trigger: every continuing session."* The distinction is expressed as form, not as a caveat paragraph an agent can skip |
| 2 | *The two-technique quota invites teaching theater* — grade the learning, not visible technique use | ✅ **Implemented, then made structural** | First the rule was rewritten to "grade the learning, not the technique count," naming theater as the failure. Then the final integration pass **dissolved the technique menu entirely** — interleaving folded into the depth pass, spacing into Cold Checks, dual coding into Physical Anchors, worked→faded into Skeleton First, elaboration into the encoding questions. There is no checklist left to perform from. A rule against theater can be gamed; a structure with no stage cannot |
| 3 | *Breadth/depth wording is unconfirmed — test live first* | ✅ **Kept as Codex recommends** | The unconfirmed marker stays in the file, reworded to point at rehearsal: *"test it live in rehearsal; if it misreads him, it changes."* This is deliberately **not** resolved on paper — it is the first thing Friday's PHYS session should exercise |
| 4 | *TCOM/ECON/ENGR routing weaker than PHYS/Python* — but tighten only after observing a lost session | ⚠️ **Implemented now, against Codex's sequencing** | All three load-order headers now name the exact state path (`EDUCATION\wiki\current-position.md` → the course folder) instead of "→ 03-WIKIS\EDUCATION". **Why not wait:** the fix costs one line per file and its failure mode is already predicted by both reviews. Spending Friday's limited fresh-session budget rediscovering a defect both models already agree on is evidence spent on nothing — rehearsal time should surface the *unknown* failures |
| 5 | *Volatile course facts in hats — test whether the AI defers when facts conflict* | ⚠️ **Implemented as standing rule, not just a test** | `HAT_EDUCATOR` § *When facts conflict, defer* states the authority order once — **D2L/instructor → `SEMESTER_MAP.md` → exact-section capture → any hat — never averaged** — and every subject hat's footer points at it. Codex asked for a practice-gate check; the check is still worth running Friday, but a deference rule that exists only as a test criterion is not a rule. Now the rehearsal verifies a written contract instead of probing for an unwritten instinct |

**The methodological difference, stated once:** Codex treated wording risk as something to
observe during rehearsal. Two of the five (4, 5) were cheap, fully-specified, and
failure-predicted — for those, observation is deferral with extra steps. Implementing them
converts Friday's sessions from *finding known defects* to *finding unknown ones*, which is
what a rehearsal with a three-session budget is for. Findings 3 stays live-test-first
precisely because it is **not** fully specified — it is a reading of Chris's intent, and only
Chris can grade it.

---

## 3. Beyond the review — what Codex did not ask for

1. **The delivery contract.** `HAT_EDUCATOR` § *How to word it for Chris* — eight rules derived
   from the measured YouScience model, not preference: map before detail, skeleton before blank
   page, one exact meaning used immediately, derive don't assert, physical when free, dialogue
   not documentation, one next action, specific progress over cheerleading. This is the
   "optimal wording for my learning style" Chris asked for, grounded in `CHRIS.md`'s aptitude
   table rather than in a styles framework.
2. **The memory toolbox.** `03-WIKIS\EDUCATION\wiki\methods\memory-techniques.md` — distilled
   from the four articles Chris routed through `77-INBOX` today (Art of Memory, Harvard
   cueing, Stanford CTL, ADDA), filtered against the aptitude profile. Kept: cueing, memory
   palace/loci (incl. the exam-room variant for PHYS/ECON — explicitly not CSE, whose exams
   are online), mnemonic imagery, sound-alike keywords, chunking, self-test-to-overlearned
   (100% × 3 at exam difficulty), study-before-sleep (mapped to the real 22:00–23:00 calendar
   hour), movement pairing, location rotation. **Dropped with reasons on the page:** peg/PAO
   systems, audio-primary methods. Wired into Term Anchoring step 2 ("build the cue"), so it
   fires from inside a standing method rather than as a separate menu.
3. **The full Feynman loop.** Explain-It-Back was step 2 of Feynman masquerading as the whole
   technique. It now runs all four steps, with step 3 — find the stumble, return to the
   source — named as where the learning happens.
4. **`HAT_PHYSICS_MATH.md`.** Chris's direct request: calculus review delivered through the
   physics he will actually see. Notation table with physical meanings, the 7-step
   integration procedure with the constant-of-integration step made explicit (the exact gap
   the July 30 drill diagnosed), worked → faded → cold delivery, failure-mode table, and the
   corrected entry point — **row 2 of `math-readiness-path.md`'s queue, not today's date**,
   because only row 1 of 27 ever ran. Routed from both `HAT_EDUCATOR` and `HAT_PHYSICS` so it
   cannot orphan (the flag #94 shape).
5. **Two factual defects found in the old hats and corrected:** `HAT_ENGR1000` claimed two
   recurring calendar check-blocks that **do not exist** on the live calendar (the weekly
   protocol protecting the most-forgettable course rested on nothing — Chris still needs to
   create the blocks); `HAT_ECON` carried **no AI policy** despite ECON being the only course
   of the five that permits credited AI.

---

## 4. What rehearsal still owns — unchanged from Codex's plan

Codex's Friday→Sunday structure is adopted as-is: Friday wording/pathway audit + three clean
fresh-session openings (PHYS, CSE/Python, TCOM) · Saturday long realistic sessions with
interruptions, pace changes, `Richard F`, ambiguous graded work, mid-task stops · Sunday
regression in fresh contexts, evidence-backed edits only, final gates.

The six-point grading rubric is adopted verbatim (correct hat + live owner · fast orientation ·
Chris retains control · real retrieval produced · boundaries respected · correct close and
resume point). Launch bar likewise: all three core subjects pass typical, edge, and recovery
twice in fresh sessions; no HIGH defect; no repeated MEDIUM behavior defect; cosmetic wording
does not delay launch.

**Priority additions to Friday's script, from today's work:** (a) grade the two-pass pace rule
live with Chris — finding 3; (b) present a fact conflict deliberately (e.g. the TCOM room,
which has three values on file) and verify deference to the authority order; (c) one
`HAT_PHYSICS_MATH` block entering at row 2, graded on whether the constant-of-integration step
is said in words before symbols.

## 5. Return packet

- **Outcome:** all five Codex wording findings dispositioned (three implemented as specified,
  two implemented beyond the recommended sequencing, with reasoning recorded); teaching layer
  integrated rather than accreted; memory toolbox and delivery contract added from Chris's
  sources and measured profile.
- **Evidence:** word counts in §1; gates green after every write; two factual defects named
  with their corrections; the four inbox source articles read in full.
- **Capability/status movement:** none claimed. Rehearsal, not this report, moves trust —
  Codex's verdict stands.
- **Reusable-asset candidate:** the integration standard itself — *a governance file is done
  when each rule carries its trigger inline and no content appears twice.* Second use would
  be the always-load pass Chris deferred.
- **System-learning candidate (filed, not promoted):** *when a reviewer defers a fix that is
  cheap, fully specified, and failure-predicted, the deferral costs more than the fix* —
  first instance; watch for a second.
