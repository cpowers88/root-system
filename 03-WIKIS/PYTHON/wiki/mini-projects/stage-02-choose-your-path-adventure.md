---
type: mini-project
stage: 02
status: draft
concepts: ["condition", "if-elif-else", "boolean-operators", "branch"]
solution_included: false
---

# Mini-Project: Choose-Your-Path Adventure

## User Story

As a learner, I want to build a short branching text adventure (inspired by Invent Your Own Computer Games' "Dragon Realm") so that I can prove I understand conditions, comparisons, and `if`/`elif`/`else` branching.

## Required Concepts

- [[glossary/condition]]
- [[glossary/comparison-operator]]
- [[glossary/boolean-operators]]
- [[glossary/if-elif-else]]
- [[glossary/branch]]

## Build Phases

### Phase 1 — Set the Scene

Print an opening description (2-3 sentences) of a situation with exactly two choices (e.g., "You find two doors: LEFT and RIGHT."). Use `input()` to collect the player's choice.

### Phase 2 — First Branch

Use `if`/`elif`/`else` to handle the player's choice. Each branch should print a different short outcome description, and then present a **second** decision (another `input()` with two or three options).

### Phase 3 — Second Branch and Ending

Handle the second choice with another `if`/`elif`/`else` chain, leading to one of at least three distinct endings (some good, some bad). No looping back — this is a single straight-through story, since loops are Stage 3.

## Acceptance Checklist

- [ ] At least two separate decision points (two rounds of `input()` + branching).
- [ ] At least three distinct possible endings reachable depending on the choices made.
- [ ] Every branch uses `elif`, not stacked separate `if` statements, where the choices are mutually exclusive.
- [ ] At least one condition combines two checks with `and` or `or`.
- [ ] Includes an `else` somewhere to handle unexpected input (e.g., the player types something other than the expected options).
- [ ] Chris can explain, out loud, why a particular sequence of inputs leads to a particular ending.

## Stretch Goals — Parked

- Looping back to let the player try again after reaching an ending (needs Stage 3 — loops).
- Tracking a score or inventory across choices (needs Stage 4-5 — functions, data structures).

## Reflection Questions

1. Which branch in your story was hardest to get the indentation/colons right for, and why?
2. If you added a third choice at the first decision point, what would you need to change — `elif` count, or something else?
3. What's one rule from this story that would have been awkward to write with separate `if` statements instead of `elif`?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
