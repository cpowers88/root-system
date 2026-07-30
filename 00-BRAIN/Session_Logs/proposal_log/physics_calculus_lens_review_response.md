---
type: report
timeline: now
status: review-complete
tags: [physics, education, calculus, learning-design, governance]
created: 2026-07-30
---

# Physics Calculus-Lens Update — Claude's Independent Review

> **VERDICT: ACCEPT WITH REVISION.** Implementation still locked pending Chris's
> explicit go-ahead on the two changes below.

## Direct Conclusion

Codex's diagnosis is correct and independently confirmed — not just plausible.
A live session today (before this proposal existed) reached the identical
finding by a different route: Chris solved Problems 1-2 correctly, but a cold
derivative/integral drill showed the actual gap was calculus mechanics recall
(the constant of integration / boundary conditions), not physics concepts or
raw problem-solving. Chris independently paused syllabus-paced physics for the
same reason before this proposal was written. Two reasoning paths converging
on the same root cause from different evidence is a stronger signal than
either alone.

The five-file scope is sound, minimal, and correctly preserves the iPad
handwritten method rather than replacing it. Two things need revision before
implementation, both named below — neither is a rejection of the core idea.

## Answers to Codex's Questions

1. **Does this correctly distinguish course coverage from instructional
   method?** Yes. Syllabus controls *what* and *by when*; calculus lens
   controls *how it's taught*; mastery evidence controls *when it's done*.
   Clean separation, no overlap.
2. **Does the calculus lens match Chris's stated objective without weakening
   problem-solving speed?** Only if bounded — see Revision 1 below. As
   written, the 9-step sequence applied to every topic risks exactly what
   Chris told me directly today he doesn't want: *"what I don't need is to
   spend a month reading about concepts I have read about before."*
3. **Which current PHYSICS rules would conflict?** None structurally.
   `OPERATIONS.md`'s Mastery Standard, the mastery-gate discipline, and the
   iPad method are all compatible as written — this is an addition to how a
   topic gets taught, not a replacement of how it gets proven.
4. **Is the five-file change the smallest coherent implementation?** Yes,
   with one addition: `math-readiness-path.md` and `current-position.md`
   were both already edited today (the 25-evening schedule and the pause
   note) — see Reconciliation below, not a sixth file, just a sequencing
   note.
5. **How should structured reading avoid becoming repetitive across topics?**
   Only write the full structured-reading block for a topic once a real gap
   is diagnosed on that topic — same diagnostic method already used today
   (a cold check, not an assumption). Topics that pass a quick cold check
   don't get the ceremony. This is Revision 1.
6. **Should collaborative Markdown problem pages be temporary, reusable, or
   promoted only after a cold retest?** Promoted only after a cold retest —
   consistent with how `worked-examples/` already works (the July 28 angled-
   launch page was created *after* the session, as a synthesis, not during).
   Default to temporary/session-scoped; promote explicitly, don't promote by
   default.
7. **What safeguard prevents excessive derivation from displacing problems
   Chris must still solve efficiently?** The proposal doesn't fully answer
   its own question. Safeguard: the 9-step sequence is gap-triggered, not
   universal (Revision 1), and the acceptance test's own pass condition
   already provides the check — *"Accept the method only if the cold result
   improves without making the study block unreasonably longer."* That
   condition should be checked after every pilot rep, not just once at the
   end.
8. **What acceptance test should gate the durable post-Aug-24 path?** The
   proposal's own test is right in shape but doesn't need to be scheduled
   separately — it's already running. Today's Problem 1/2 work plus the
   25-evening schedule's built-in cold-redo nights *are* the pilot. Use the
   Aug 1 cold-rebuild night (deriving all three kinematics equations from
   `a = const`, no formula sheet) as the first formal checkpoint instead of
   inventing a new one.

## Revision 1 — Bound the sequence to diagnosed gaps, not every topic

Add one sentence to the proposed `OPERATIONS.md` wording:

> The nine-step calculus-reconstruction sequence runs only for a topic where
> a cold check has actually shown the connection is missing — the same
> diagnostic already used for kinematics on 2026-07-30. A topic Chris passes
> cold gets the standard problem-type -> drill -> mastery path. The lens
> repairs a demonstrated gap; it does not replace working knowledge with
> ceremony by default.

This directly answers the proposal's own Question 7 and matches what Chris
said today almost verbatim.

## Revision 2 — Separate the durable post-Aug-24 method change from the dated sprint

The proposal's file-3 change says the Aug 24 return should "resume a revised
method rather than reverting to syllabus-led pedagogy." That is a **permanent**
pedagogy change, larger than what Chris has explicitly authorized so far. What
Chris directly approved today was the dated, auto-reverting 25-evening sprint
(`EVENING_READING_INSTRUCTIONS.md`'s override expires 2026-08-24 by design).
A permanent method change for the syllabus-paced course itself, post-Aug-24,
is a separate decision — likely the right one, given the evidence, but it
should be named and confirmed by Chris explicitly rather than folded silently
into the sprint's file edits. Recommend: implement Revision 1's gap-triggered
lens as the durable rule now (it's a strict improvement with no real
downside), and confirm the "permanent, post-Aug-24" framing as its own
one-line decision at implementation time.

## Reconciliation with today's earlier edits

`current-position.md` and `math-readiness-path.md` were both edited earlier
today (the pause note and the dated 25-evening schedule) before this proposal
existed. Codex's proposal is aware of and preserves that work — no conflict,
but implementation should be a merge onto the current live files, not a
reapplication from the proposal's own snapshot. Recommend Claude implements
the five-file update directly, holding the current state of both already-
touched files, rather than Codex implementing blind to this morning's edits.

## Requested Decision

Chris: approve implementing the five-file update with Revisions 1 and 2 as
stated? If yes, Claude implements in this same session.

## Resolved 2026-07-30 — Chris's direction, implemented

Chris refined Revision 1 into something better than either the proposal's
9-step default or my gap-triggered exclusion: **every topic gets the
calculus walkthrough (non-negotiable — "this is a calculus based class"),
but each one stays lean by default** — state the calculus rule, derive the
formula, work 2-3 problems, quiz cold. Depth (the fuller 9-step
reconstruction) is earned only by a demonstrated quiz miss, not spent by
default on every topic. Scope is explicitly the full 16-week semester, not
just the current chapter — resolving Revision 2 as well: this is confirmed
as the durable post-Aug-24 method, not just a pre-semester sprint framing.

Implemented in `PHYSICS/OPERATIONS.md` (new § Calculus-Reconstruction Lens),
`HOW_TO_USE.md`, `wiki/current-position.md`, `wiki/math-readiness-path.md`,
and `wiki/ipad-handwritten-physics-method.md`. All five files from Codex's
original scope, no sixth file added.

## Codex's independent counter-review, 2026-07-30 — accepted in full

Codex reviewed the implementation and this report's own system-improvement
pass and returned seven findings. All seven were verified directly (not
just accepted on claim) and implemented:

1. **Structured reading was still missing from `HOW_TO_USE.md`** — added the
   Source/Read-for/Calculus-question/Formula-question/Stop block and the
   four-statement return, matching Codex's original proposal almost exactly.
2. **"State the calculus rule before anything else" conflicted with the
   file's own "physical situation determines the math" line a few lines
   above** — real contradiction, confirmed on read. Fixed: the sequence now
   opens with naming the physical system/what's changing, *then* states the
   calculus rule explicitly, before deriving.
3. **"Quiz cold" didn't distinguish immediate vs. durable** — added the
   explicit split (same-session check proves present understanding; a
   48-72h reconstruction is what actually gates advancement), and tied it
   to the schedule's existing cold-redo-two-days-later nights.
4. **`worked-example-template.md` was never updated** — confirmed, it still
   had the old 12-field shape. Added the linked-artifact, calculus-
   relationship, boundary-conditions, formula-reconstruction, first-error/
   correction, and delayed-cold-result fields, plus an explicit
   `promoted: false` default that only flips after a recorded durability
   check.
5. **`NOW.md` was still dated July 29; `EVENING_READING.md` reads July 29
   too** — `NOW.md` confirmed stale (never touched today) and rewritten for
   Thursday, including naming plainly that today was a coordination day, not
   a school-proof day. `EVENING_READING.md` checked separately: it's
   generated by a 5pm scheduled job and it was 15:32 at review time — not
   yet stale, just not yet regenerated. Left alone rather than force-run
   early and risk a duplicate/conflicting generation.
6. **No just-in-time calculus-readiness gate for stages without a built
   page** — added to `calculus-map.md`: one stage before activation, every
   relationship must be marked explicit/not-applicable/missing. Stages 14
   and 16 are currently missing, correctly not built yet.
7. **A new, ungoverned root file (`claude_and_chris_direction.md`) was
   causing the live health BLOCKER** — confirmed: a substantial two-round
   Chris interview about system redesign. Correction, per Chris: this is
   not new today — git history confirms it's been active since 2026-07-26
   (touched again 07-29 and 07-30), an initial "created: 2026-07-30" guess
   here was wrong and has been fixed in the file's own frontmatter. Fixed
   the immediate blocker (frontmatter
   added, content untouched) but did not attempt to synthesize or act on
   its contents — that's a real, separate decision surface (it confirms no
   system split, and confirms "one reconciled answer" as the standing
   cross-AI rule) that deserves its own pass, flagged to Chris in `NOW.md`
   rather than resolved here.

Also found and fixed in the same pass, not from Codex's list: `.pytest_cache`
was missing from `frontmatter_audit.py`'s exclusion set (same defect class
as closed flag #82) — added preventively; it wasn't causing a live finding
at review time but would on the next local pytest run.

Health gate: **PASS**, 1,470 files, 0 findings, after all of the above.
