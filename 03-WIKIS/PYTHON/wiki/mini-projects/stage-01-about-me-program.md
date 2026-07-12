---
type: mini-project
stage: 01
status: draft
concepts: ["variable", "input", "type-conversion", "string", "print"]
solution_included: false
---

# Mini-Project: "About Me" Program

## User Story

As a learner, I want to build a short program that asks me questions about myself and prints a personalized summary, so that I can prove I understand variables, input, type conversion, strings, and print formatting.

## Required Concepts

- [[glossary/variable]]
- [[glossary/input]]
- [[glossary/type-conversion]]
- [[glossary/string]]
- [[glossary/concatenation]]
- [[glossary/print]]

## Build Phases

### Phase 1 — Collect Information

Use `input()` to collect at least four pieces of information: name, age, a favorite number, and one more of Chris's choosing (favorite food, hobby, etc.). Store each answer in its own clearly-named variable.

### Phase 2 — Convert Types

Identify which answers need to be numbers (age, favorite number) and convert them with `int()` or `float()` as appropriate. Leave text answers as strings.

### Phase 3 — Print a Summary

Use f-strings to print a short paragraph (3-5 sentences) that combines all the collected information, including at least one calculation using a converted number (e.g., "In 10 years you'll be ___ years old.").

## Acceptance Checklist

- [ ] Program runs without errors from start to finish.
- [ ] At least four `input()` calls, each stored in a clearly-named variable.
- [ ] At least one value is correctly converted with `int()` or `float()`.
- [ ] At least one calculation is performed on a converted number.
- [ ] Final output uses f-strings, not `+` concatenation, for at least one line.
- [ ] Chris can explain, out loud, why each conversion was necessary.

## Stretch Goals — Parked

- Add a comment above each `input()` call explaining what it collects and why (good habit, doesn't require new concepts).
- (Do not attempt: conditionals, loops, or functions — those are later stages.)

## Reflection Questions

1. Which line of your program would break first if you removed a type conversion? Why?
2. If you ran this program twice with different answers, what would change and what would stay the same?
3. What's one thing about `input()` or type conversion that surprised you while building this?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
