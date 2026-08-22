---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [school, education, governance]
created: 2026-07-24
updated: 2026-08-13
---

# EDUCATION_WIKI — OPERATIONS

> **Split declared 2026-08-13 (Chris-directed; drafted by Codex as W4/J-2, amended and applied
> by Claude).** This hub was doing two unrelated jobs under one contract, which is why its shape
> felt arbitrary. **The split is a contract split, not a folder move.** Nothing was relocated.
> Course folders stay exactly where they are.

## Function — two declared halves, one hub

| Half | Owns | Has a frontier? |
|---|---|---|
| **A — Meta-learning** | Reusable learning and retrieval methods, education research, how Chris learns | **No.** Reference material. No staged progression, no daily position |
| **B — Course support** | Study support for KSU courses that have **no dedicated wiki**: ECON 1000, TCOM 2010, ENGR 1000 | **No.** Tracks *course* reality — syllabus, dates, coverage — never learner mastery |

**Neither half owns a learner frontier.** That is the distinction that was missing and that made
this hub confusing. PYTHON and PHYSICS own staged learner truth because their knowledge outlives
the course. ECON, TCOM, and ENGR end in December.

**Why they stay one hub:** each top-level hub permanently adds an `OPERATIONS.md`, a state
tracker, index/log/source-map, session minimums, lint scope, and health-gate scope. **Three new
hubs for courses that end in December is permanent overhead bought for temporary work.**

**Shared layer:** load `00-BRAIN\WIKI_SHARED_LAYER.md` for every EDUCATION session. This file
adds education and academic-integrity rules on top of it.

## Promotion rule — when a course earns its own hub

> **A subject earns a top-level hub when its knowledge outlives the course.**

Derived from `NORTH_STAR.md` §2's permanent capability base, not invented here.

| Subject | Outlives the course? | Ruling |
|---|---|---|
| PHYSICS, PYTHON (CSE) | Yes — both named in §2 | Own hubs, correct as-is |
| ECON 1000, ENGR 1000 | No — one-semester requirements | **Stay here** |
| TCOM 2010 | The *course* doesn't; the *content* does — "communication" is in §2 | **Stays here, built out.** Promote only when the 35% technical report is delivered **and** it has produced reusable writing assets a client project would reuse |

**Structure follows evidence. Do not build a hub speculatively.**

## Ownership

| Truth | Owner |
|---|---|
| Mission, AI limits, academic-integrity boundary | `NORTH_STAR.md` and `AGENT.md` |
| Semester outcomes and priorities | `01-NORTH_STAR\Goals & Milestones\fall_2026_semester.md` |
| **Cross-course dates, deadlines, and grading** | **`04-SCHOOL\SEMESTER_MAP.md`** |
| Exact-section source status | `04-SCHOOL\SYLLABUS_STATUS.md` |
| Official syllabus captures (ECON, TCOM, ENGR) | `03-WIKIS\EDUCATION\raw\Syllabi\` |
| Course materials, notes, D2L pulls, **graded output** | `04-SCHOOL\<course>\` and `<course>\work\` |
| Reusable learning methods and education research | **this hub, half A** |
| Course study aids for hub-less courses | **this hub, half B** |
| Python learner truth | `03-WIKIS\PYTHON\wiki\current-position.md` |
| Physics learner truth | `03-WIKIS\PHYSICS\wiki\current-position.md` |
| Cross-system sequencing | CASTLE and `NOW.md` |

**An official course source overrides every derivative page here.** Course readiness is not
meta-learning truth, and meta-learning research is not a course schedule.

## State

`wiki\current-position.md` is a **course-support status board — not a learner frontier.** It
records what is verified, what is provisional, and what is still waiting on an official source.
It must never claim mastery, and it must never become a second dashboard for sequencing, which
CASTLE owns.

**If a future EDUCATION project develops a real staged frontier, create a narrowly named state
owner for that project after Chris's approval. Do not recreate a mixed dashboard.**

## Structure

```text
raw/                      immutable supporting sources
wiki/
  index.md                canonical catalog
  current-position.md     course-support status (half B) — NOT a learner frontier
  log.md                  append-only operational history
  ── half A ──────────────────────────────────────────
  methods/                reusable learning and retrieval methods
  references/             education-system research
  ── half B ──────────────────────────────────────────
  course-briefs/          semester-wide policy and requirement comparisons
  courses/<course>/       per-course study aids
  pre-semester-coverage-plan.md
```

**Course folder rule:** create one only after real course material or a real study need exists.
**As of 2026-08-13 there is deliberately no `courses/engr-1000/`** — ENGR 1000 BWD has no
exact-section syllabus, no published meeting time, and no confirmed delivery format. Creating a
folder for it now would be scaffolding around nothing. Create it when the syllabus lands.

**Per-course page pattern** (established by TCOM, T8): `concepts/`, `common-errors/`, `drills/`,
`flashcards/`, `glossary/`, `semester-map.md`. ECON additionally has `reading-guides/`. **Do not
invent a third pattern.**

## Operations

### INGEST

1. Identify the course and the exact learning question.
2. Verify the authoritative course file, its date, and its section.
3. **Check the course AI policy before assisting.**
4. Read supporting sources completely, in bounded chunks per the shared layer.
5. Update the existing page before creating another.
6. Separate confirmed requirements, provisional mappings, guidance, and unknowns — and **say
   which is which on the page itself.**
7. Update the catalog, status board, and log **in the same session** their state changes.

### QUERY

1. Read `wiki\current-position.md` for course-support work; skip it for half-A method questions.
2. Load only the relevant course folder or method page.
3. Answer at the level the course policy allows.
4. End with a concrete study action or a named verification need — **page creation is not proof.**

### LINT

Check official-source precedence, course-policy visibility, ownership, duplicated PYTHON or
PHYSICS content, stale course facts, premature study aids, unresolved links, index drift, and
missing evidence of learning.

## Academic integrity

**Per-course, verified — not assumed:**

| Course | Policy |
|---|---|
| **ECON 1000** | **AI allowed if credited** — the only one of the five where this is true |
| **TCOM 2010** | **AI may edit/proofread Chris's existing writing only, with cited usage; it may not draft assignments** |
| **ENGR 1000** | **Treat as prohibited on submitted work.** Exact BWD is missing; three neighboring Fall 2026 web sections carry the same prohibition |

AI MAY explain concepts, generate fresh private practice, review Chris's reasoning, and help
plan independent work. AI MUST NOT produce prohibited graded submissions or bypass a
course-specific restriction. **When policy is unclear, use the most restrictive verified
interpretation until Chris resolves it.**

## Raw boundary

`raw\` is immutable. AI MUST NOT create, edit, move, rename, archive, or delete anything under
it without Chris explicitly authorizing a named exception.

## Proof and close

Proof is successful explain-back, retrieval, problem solving, or later course performance —
**not page creation.** Close by recording changed status, evidence, the next study action, and
any fact still requiring official verification.

**The hub is healthy when** a fresh session can find the relevant method or course aid without
mistaking EDUCATION for the owner of course schedules, learner frontiers, or graded artifacts.

---
*Split applied 2026-08-13. Prior contract archived in git history. Codex's draft:
`Session_Logs\System Update Log\2026-08-12_ROOT_UPDATE\PROPOSED_EDUCATION_OPERATIONS_REPLACEMENT.md`.*
