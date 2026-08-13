---
type: reference
timeline: reference
tags: [governance]
---

# HAT_EDUCATOR_PLAYBOOKS.md — Educator Skill Scripts (on demand)
### Canonical learning profile: CHRIS_CORE.md § How Chris Learns Best (deep version: CHRIS.md). These are the teaching applications.

---

## The seven teaching methods are NOT here — they are in `HAT_EDUCATOR.md`

**Returned to the hat 2026-08-13, closing flag #94.** The July 11, 2026 slim pass moved them
here behind a judgment-call load ("load when running a teaching session"), and the result was
a hat that behaved as two different teachers depending on whether this file happened to be
opened. Skeleton First, One Concept at a Time, Term Anchoring, Explain-It-Back, Cold Checks,
Physical Anchors and Short Corrections now live in `HAT_EDUCATOR.md` alongside the
encoding/retrieval model and the pace rule.

**The governing rule, so this does not happen again:**

> **Situational procedures may move. Methods used every time may not.**

This file keeps only the four procedure scripts below, which are genuinely situational —
each fires on a named trigger rather than in every session.

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
`01-NORTH_STAR\Goals & Milestones\fall_2026_semester.md`; learner truth:
the owning course wiki current-position; live sequence: NOW.md.
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
