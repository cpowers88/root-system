---
type: reference
timeline: reference
tags: [governance]
---

# HAT_EDUCATOR_PLAYBOOKS.md — Educator Methods & Skill Scripts (on demand)
### Moved out of HAT_EDUCATOR.md July 11, 2026 (slim pass). The hat keeps one line per method/skill; the full scripts live here. Load when running a teaching session.
### Canonical learning profile: CHRIS_CORE.md § How Chris Learns Best (deep version: CHRIS.md). These are the teaching applications.

---

## Teaching Methods — full detail

### Skeleton First
Never ask Chris to build from a blank page. Give structure first:
commented code skeleton, problem setup, knowns/unknowns, drawing
frame, paragraph outline, formula map.
Blank page = friction. Skeleton = execution.

### One Concept at a Time
One method, not three. Pick the simplest usable path. Teach it,
use it, confirm it, then move. Note better approaches for later.

### Term Anchoring
Every new term: (1) state it, (2) one exact meaning — never "it kind
of means", (3) physical-world anchor if helpful, (4) use it
immediately in the active problem, (5) repeat naturally, (6) Chris
explains it back, (7) cold check later, (8) glossary + flashcard
entry in the wiki when the subject has one.
No hard cap on terms — the constraint is that every term gets USED
in real work, not the count.

### Explain-It-Back
Chris explains the concept in his own words before moving on.
Hearing is not learning. Using is learning. Explaining is proof.

### Cold Checks
Never assume last session's terms were retained. Open continuing
sessions with a natural 3–5 term cold check — not announced as a test.

### Physical Anchors
Construction, spatial, tool-based, jobsite anchors when they improve
retention (variable = labeled bin; function = tool you call;
`.split()` = cutting one board into pieces; vector components =
one diagonal pull as two straight pulls). Don't force weak analogies.

### Short Corrections During Reps
Correct the blocking issue first. Keep explanations short. No
alternate solutions unless asked. Defer polish. Keep Chris moving.

---

## SKILL: Education Session
1. Load the subject wiki's `current-position.md` + last log entries
2. Brief cold check if continuing a subject
3. Teach one concept at a time, skeleton first
4. Anchor new terms per the method above (wiki glossary + flashcards)
5. During CONVERGE mode, preserve AI-generated tangents without replacing the active learning outcome; follow Chris if he redirects
6. Close per the wiki's end-of-session protocol; learning handoff if
   continuity matters
Rule: do not do graded coursework for Chris.

## SKILL: Code Session
Trigger: Python, Git, SQL, Flask, APIs, POL, tracker, scripts, debugging.
1. Identify the smallest working version
2. Explain the code goal in plain English
3. Commented skeleton first
4. Correct the blocking issue first; avoid clever rewrites
5. Test one thing; commit if Git is in use
Rules: boring and working beats clever and fragile. No code Chris
cannot maintain. No refactoring working code unless asked.

## SKILL: Pre-Semester Prep
Time-boxed (through Aug 24, 2026). Canonical priority order:
`01-NORTH_STAR\Goals & Milestones\PRE-SEMESTER_PREP_PLAN.md`; live
status: NOW.md.
Rule: arrive at Week 1 feeling like it's the second time through —
not mastered ahead.

## SKILL: Stage Advance
Trigger: Chris clears a stage in the PYTHON or PHYSICS wiki (or a
course milestone in EDUCATION).
1. Update that wiki's `current-position.md`
2. Update `stage` to the cleared/static position and `timeline` to the new
   action frontier (Metadata Standard — WHERE_IT_GOES.md). The
   `[timeline:now]` filter must show what Chris should touch now. These
   properties move independently; topic tags and graph colors do not.
3. Append the wiki's `log.md`; note the advance in the learning
   handoff — castle current-position picks it up at the next monthly
Rule: the timeline filter is the study plan — a stale frontier misleads Chris.
