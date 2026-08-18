---
type: instruction
timeline: reference
tags: [governance, learning]
status: live
---

# Evening Reading Instructions
### AKA "Nightly Reading" — same file, same schedule; renamed in conversation only, not on disk (rewritten 2026-07-23 per Chris's direct request for a clearer two-block contract).

At 5:00 p.m. local time, read `MORNING_BRIEF.md`, `NOW.md`, today's DAILY, both active bootcamp evidence files, and the relevant owner's Current Reading Queue, then replace root `EVENING_READING.md` with **two short blocks**: **School** (primary) and **Technology** (brief, business-relevant).

## Course Rotation — which course fills the School block (added 2026-07-25)

The School block stays **one course per night**. Which course is set by weekday, so
every registered course gets evening exposure across a week without the brief
growing. The rotation is weighted to the live 40/30/15/10/5 allocation and each
night **primes the next day's first block** in the current weekly plan.

**Rebalanced 2026-08-18 at Chris's direction.** The previous table ran Python 3 /
Physics 2 / TCOM 1 / ECON-or-ENGR 1. That weighting was set in July, before the
buffer position was measured. **It is now backwards.** Measured 2026-08-18: PHYS is
**+2 weeks ahead**, CSE is **+2 and hard-capped** (Module 2 does not exist until D2L
opens), while **TCOM is at 0 buffer with real graded work in week 1**, and ECON's
first graded item is Sep 8. Evening reading now follows the deficit, not the habit.

| Night | School lane | Primes |
|---|---|---|
| **Sunday** | TCOM | Monday's writing block and the week's deliverable |
| **Monday** | ECON | Tuesday's reading and the chapter's quiz window |
| **Tuesday** | TCOM | Wednesday's drafting or peer-response work |
| **Wednesday** | Python / CSE | Thursday's module work |
| **Thursday** | ECON | Friday's quiz or discussion deadline |
| **Friday** | ENGR when its syllabus exists, otherwise Physics | the weekend |
| **Saturday** | Physics | Monday's lecture |

Weekly totals: TCOM 2, ECON 2, Python 1, Physics 1 (2 while ENGR is blocked).

**Rebalance when the deficit moves, not on a fixed date.** If PHYS or CSE falls to 0
buffer, or TCOM/ECON pull ahead, this table is wrong again — say so in the brief
rather than following it off a cliff.

**Four overrides, in this order:**

1. **The owner's live queue still governs.** If the rotation names a course whose
   queue has nothing unlocked, or whose next material is explicitly gated behind a
   proof Chris hasn't produced, move to the next course in the rotation and say so
   in one clause. Never assign locked material to satisfy the schedule.
2. **A real deadline outranks the rotation.** A graded item due the next day takes
   the block regardless of weekday.
3. **Week-1 catch-up, 2026-08-18 through 2026-08-23 — active now.** Classes begin
   Aug 24 and **week-1 work is already knowable from the syllabi on disk.** Assign
   week-1 reading for the 0-buffer courses ahead of the rotation, in this order:
   **TCOM first** — its week 1 carries a Course Policies Quiz, a File Naming Quiz,
   and an Ethics Analysis due Friday, per
   `03-WIKIS\EDUCATION\wiki\courses\tcom-2010\semester-map.md`; then **ECON**
   (OpenStax *Principles of Economics 2e* Ch. 1, per that course's `semester-map.md`).
   Do **not** assign PHYS or CSE week-1 reading this week — both are ≥2 weeks ahead
   and re-reading covered ground buys nothing. This override expires 2026-08-24.
4. **The Aug 3–23 calculus-physics bridge override is ENDED, five days early**
   (2026-08-18, Chris's call). It restricted the School line to a 15-minute physics
   primer, which is why the brief was assigning circular motion instead of school
   reading. The daytime CASTLE bridge blocks continue; they no longer suppress the
   evening School block. **Do not reinstate this.**

ENGR stays orientation/source-verification only until the real Fall BWD syllabus
exists; never assign invented Fall content from the Summer reference section.

## Source Priority

- **School block:** the owner's live reading queue governs (e.g. `PYTHON/wiki/current-position.md`, `PHYSICS/wiki/current-position.md`) — never assign a stage/chapter that queue hasn't unlocked yet. A raw PDF is **not a last resort** — for KSU spine material (Think Python, the Physics textbook, official syllabi) the raw source is the *preferred, recommended* citation over a wiki-processed page; point straight at it (`.../raw/books/....pdf` or `04-SCHOOL/...`) with the exact chapter/section, and page numbers when the PDF is already page-mapped.
- **No-contamination rule (clarified 2026-08-02, closes flag #86):** priming the next day's first block means assigning the **raw textbook chapter or general topic exposition** on that subject — never the wiki's own stage/drill file, which carries the exact problems, code patterns, or mastery-checklist items the next day's cold gate will use. Reading the textbook chapter on loops the night before a loops cold gate is intended and correct; reading `wiki/stages/stage-03-...md` itself would not be. This is why raw sources are preferred over wiki-processed pages above — it is not only a citation preference, it is what keeps priming from contaminating the next day's measurement.
- **Page numbers are now available and expected for Python.** `03-WIKIS/PYTHON/wiki/source-page-map.md` carries verified **physical** PDF pages for Think Python, Python Crash Course, and Python Workout. Cite the physical page, not just the chapter. PHYSICS page ranges live in its `source-map.md`.
- **Technology block:** the single most immediately useful slice tied to active Bootcamp/business work; prefer continuing the same source across nights over restarting elsewhere.

## Format

Each line is one sentence, ≤35 words. `**FOCUS**` replaces the old `**WHY**` line — it answers where the reading fits into current work or school material, and folds any note-worth detail in as **bolded inline text** rather than a separate notes line, to keep this short:

```
## School
**READ —** source plus exact chapter/section/pages/file.
**FOCUS —** where this fits into current work or school material, with the one detail worth remembering **bolded inline**.
**STOP —** the precise endpoint (a section boundary or a time cap).

## Technology
**READ —** source plus exact section/pages/file.
**FOCUS —** same rule as above.
**STOP —** endpoint.
```

## Rule

The only rule beyond standing `.ROOT` governance: **keep this brief** — two blocks, six lines total, nothing more. Never assign a broad chapter, treat reading as mastery, or copy owner context into the brief.

The next measured session records whether the assignment was completed, useful,
well-timed, and correctly scoped; that result returns to the evidence lane it served
and is cross-reviewed Sunday.
