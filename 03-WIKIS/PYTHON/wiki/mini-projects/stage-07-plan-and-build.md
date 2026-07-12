---
type: mini-project
stage: 07
status: draft
concepts: ["decomposition", "pseudocode", "flowchart", "incremental-development", "test-case"]
solution_included: false
---

# Mini-Project: Plan-and-Build (Chris's Choice)

## User Story

As a learner, I want to pick my own small program idea, plan it fully before writing any code, and build it incrementally with test cases along the way, so that I can prove I can apply Stage 7's process to a problem nobody handed me pre-decomposed.

## Required Concepts

- [[glossary/decomposition]]
- [[glossary/pseudocode]]
- [[glossary/flowchart]]
- [[glossary/incremental-development]]
- [[glossary/test-case]]

## Build Phases

### Phase 0 — Pick a Problem

Choose a small program idea using only Stage 1-6 tools (values, conditionals, loops, functions, data shapes, files) — something with at least 3-4 real steps and at least one decision point. Ideas: a tip calculator with a discount rule, a simple quiz with a score tracker, a basic to-do list saved to a file. (If stuck, ask for suggestions — but the decomposition itself should be Chris's own work.)

### Phase 1 — Plan First

Write a numbered pseudocode list decomposing the problem into steps. If the problem has more than one or two decision points, also sketch a flowchart for the branching logic. Write down at least 2 test cases — specific inputs and the exact output you expect — before writing any code.

### Phase 2 — Build Incrementally

Code one step from the plan, run it, confirm it works (using a temporary `print()` if needed), then move to the next step. Do not write more than one new step's worth of code before testing again.

### Phase 3 — Verify Against Test Cases

Run the finished program against the test cases written in Phase 1. If any fail, debug using Stage 6's process (read the traceback or check intermediate values) rather than guessing randomly.

## Acceptance Checklist

- [ ] A written plan (pseudocode and, if needed, a flowchart) exists *before* any code was written — not reconstructed afterward.
- [ ] At least 2 test cases were written down before coding, and both are confirmed passing against the finished program.
- [ ] The build log (comments or notes) shows it was built incrementally — at least 3 distinct "add a step, test it" cycles.
- [ ] The finished program actually does what the original plan described.
- [ ] Chris can explain, out loud, one moment where the plan caught a problem before it became a coding mistake (or one moment where reality forced a change to the plan — both are valid lessons).

## Stretch Goals — Parked

- Add a second decision-heavy feature once the first version works (good incremental-development practice, optional).
- Formal flowchart software/diagramming tools — pen and paper (or plain text arrows like in [[concepts/flowcharts]]) is entirely sufficient here.

## Reflection Questions

1. What was the hardest part of the problem to decompose, and why?
2. Did the plan survive contact with actual coding, or did you have to revise it? What changed?
3. If you'd skipped the planning step and just started coding, what do you think would have gone wrong first?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
