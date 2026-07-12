---
type: mini-project
stage: 10
status: draft
concepts: ["cli", "argument-parsing", "unit-test", "decomposition", "incremental-development"]
solution_included: false
---

# Mini-Project: Stage 10 Capstone (Chris's Choice)

## User Story

As a learner, I want to build one small, complete, end-to-end program — choosing the track that interests me most — so that I can prove I can take a project from input through processing to output, with at least one automated test, closing out the original 11-stage path.

## Required Concepts

- [[glossary/cli]] (Track A)
- [[glossary/unit-test]] (all tracks)
- [[glossary/decomposition]]
- [[glossary/incremental-development]]

## Choose One Track

### Track A — CLI Tool

Build a command-line tool using `argparse` that does something genuinely useful — a word-counter for a text file, a simple unit converter, or a file-renaming batch tool. Must accept at least one required argument and one optional flag.

### Track B — Small Pygame Game

Build a minimal game using Pygame (Python Crash Course Part II, Ch.12-14, or Invent Your Own Computer Games Ch.17-21 for ideas) — even something as simple as a single moving shape responding to keypresses counts. This track requires installing a third-party package (Stage 9's `pip` skill).

### Track C — Tested Module

Build a small module of 2-3 related functions (a simple statistics helper, a text-formatting toolkit, a grade calculator) with a full `pytest` test suite covering normal cases and at least one edge case per function.

## Build Phases (apply Stage 7's process regardless of track)

### Phase 1 — Plan First

Decompose the chosen project into steps, write pseudocode, and identify at least 2 test cases before writing code.

### Phase 2 — Build Incrementally

Build one piece at a time, confirming each works before adding the next — same discipline as every prior stage.

### Phase 3 — Test and Finish

Write at least one automated `pytest` test for some piece of the logic (even Track A and B should have at least one pure, testable function pulled out — e.g., the word-counting logic in Track A, or a scoring calculation in Track B).

## Acceptance Checklist

- [ ] A track was chosen and the plan was written before coding (per Stage 7).
- [ ] The program runs end-to-end: input -> processing -> output, with no manual intervention needed mid-run.
- [ ] At least one piece of core logic is pulled out into a function that's tested with `pytest`, independent of the CLI/game/interactive parts.
- [ ] Input validation handles at least one realistic bad-input case without crashing unhelpfully.
- [ ] Chris can explain, out loud, why the tested function was kept separate from the input/output handling (testability, per this stage's "tightly coupled code can't be tested" lesson).

## Stretch Goals — Parked

- Track A: add a third option or subcommand.
- Track B: add a simple win/lose condition or score tracker.
- Track C: extend to a small SQLite-backed version, storing results between runs.

## Reflection Questions

1. Why did you choose this track over the other two?
2. Which part of the project was hardest to make testable, and how did you (or could you) restructure it to fix that?
3. Looking back across all 10 stages, which single concept from earlier stages did this capstone rely on the most?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
