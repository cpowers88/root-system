---
type: flashcards
tags: [programming]
timeline: next
---

# Flashcard Batch: Stage 2 — Decisions

## Card: Condition

**Front:** What is a condition in Python?

**Back:** An expression that evaluates to True or False, used to decide whether a branch of code runs.

**Tags:** python, stage-02, conditions

---

## Card: Boolean

**Front:** What is a Boolean value?

**Back:** A value that is either True or False — Python's `bool` type.

**Tags:** python, stage-02, boolean

---

## Card: `=` vs `==`

**Front:** What's the difference between `=` and `==`?

**Back:** `=` assigns a value to a variable. `==` compares two values and returns True or False.

**Tags:** python, stage-02, decision-rule

---

## Card: `and` vs `or`

**Front:** What's the difference between `and` and `or`?

**Back:** `and` needs both conditions to be True. `or` only needs one of them to be True.

**Tags:** python, stage-02, decision-rule

---

## Card: How many branches run

**Front:** How many branches of an `if`/`elif`/`else` chain run for a single pass through it?

**Back:** Exactly one — as soon as one condition is True, the rest are skipped.

**Tags:** python, stage-02, conditionals

---

## Card: Branch

**Front:** What is a "branch" in the context of `if`/`elif`/`else`?

**Back:** One possible block of code that runs depending on whether its condition is True.

**Tags:** python, stage-02, conditionals

---

## Card: Truthy vs Falsy

**Front:** Is `0` truthy or falsy? Is `"0"` (the string) truthy or falsy?

**Back:** `0` is falsy. `"0"` is truthy, because it's a non-empty string.

**Tags:** python, stage-02, truthy-falsy

---

## Card: When to use `elif` vs separate `if`

**Front:** When should I use `elif` instead of a separate `if` statement?

**Back:** Use `elif` when the conditions are mutually exclusive (only one should ever run). Separate `if` statements can accidentally let more than one branch execute.

**Tags:** python, stage-02, decision-rule

---

## Card: Why `else` matters

**Front:** Why include an `else` at the end of an `if`/`elif` chain?

**Back:** It's a safety net that catches any case not explicitly handled by the conditions above it — without it, unexpected input might silently do nothing.

**Tags:** python, stage-02, decision-rule
