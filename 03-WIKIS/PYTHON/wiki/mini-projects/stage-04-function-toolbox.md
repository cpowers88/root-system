---
type: mini-project
stage: 04
status: draft
concepts: ["function", "def", "call", "parameter", "argument", "return-value", "scope"]
solution_included: false
timeline: reference
---

# Mini-Project: Function Toolbox

## User Story

As a learner, I want to build a small program made of 3-4 functions that call each other, so that I can prove I understand how to define, call, and combine functions — including passing one function's return value into another.

## Required Concepts

- [[glossary/function]]
- [[glossary/parameter]]
- [[glossary/argument]]
- [[glossary/return-value]]
- [[glossary/scope]]

## Build Phases

### Phase 1 — Two Independent Functions

Write two simple fruitful functions that don't depend on each other — for example, one that converts a price with tax (`add_tax(price, tax_rate)`) and one that calculates a percentage (`percent_of(amount, percent)`).

### Phase 2 — A Function That Uses Another Function's Result

Write a third function that calls one of the Phase 1 functions internally and builds on its result — for example, `total_with_tip(price, tax_rate, tip_percent)` that calls `add_tax()` first, then adds a tip on top.

### Phase 3 — Tie It Together

Write a small driver section (not itself a function, just regular top-level code) that calls your functions with a few different inputs and prints a readable summary using f-strings.

## Acceptance Checklist

- [ ] At least 3 functions, each with at least one parameter.
- [ ] At least 2 of the functions use `return`, not `print()`, internally.
- [ ] At least one function calls another function and uses its return value (Phase 2's requirement).
- [ ] The driver code at the bottom calls every function at least once and prints results clearly.
- [ ] Chris can explain, out loud, the order in which the functions actually execute when the driver code runs.

## Stretch Goals — Parked

- Default parameter values (e.g., `tip_percent=15`) — a small preview of something fuller in later stages; fine to try, not required.
- Validating that inputs are positive numbers — needs more conditionals/error-handling depth than Stage 4 requires.

## Reflection Questions

1. Which function in your toolbox would be hardest to test on its own, separate from the others, and why?
2. What would happen if `add_tax()` used `print()` instead of `return`, and `total_with_tip()` tried to use its result in a calculation?
3. If two of your functions both used a local variable with the same name, would that cause a conflict? Why or why not?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
