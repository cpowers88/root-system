---
type: flashcards
tags: [next, programming]
---

# Flashcard Batch: Stage 3 — Repetition

## Card: Loop

**Front:** What is a loop?

**Back:** A block of code that repeats, either a fixed number of times or until a condition changes.

**Tags:** python, stage-03, loops

---

## Card: Iterable

**Front:** What is an "iterable"?

**Back:** Anything you can loop over item-by-item, like a string or a range() — the thing a for loop steps through.

**Tags:** python, stage-03, iteration

---

## Card: for vs while decision rule

**Front:** When should you choose a `for` loop over a `while` loop?

**Back:** When you know in advance what you're looping over — a fixed count or a known sequence — rather than waiting for a condition to change.

**Tags:** python, stage-03, decision-rule

---

## Card: range() off-by-one

**Front:** What numbers does `range(5)` actually produce?

**Back:** 0, 1, 2, 3, 4 — five numbers total, stopping before 5.

**Tags:** python, stage-03, range

---

## Card: while loop stopping condition

**Front:** What must be true for a `while` loop to eventually stop?

**Back:** Something inside the loop body must change the condition so it eventually becomes False.

**Tags:** python, stage-03, decision-rule

---

## Card: break vs continue

**Front:** What's the difference between `break` and `continue`?

**Back:** `break` exits the loop entirely. `continue` skips the rest of the current pass but keeps looping.

**Tags:** python, stage-03, break-continue

---

## Card: Counter vs accumulator

**Front:** What's the difference between a counter and an accumulator?

**Back:** A counter tracks how many times something happened. An accumulator builds up a combined value (like a sum) across iterations.

**Tags:** python, stage-03, decision-rule

---

## Card: Where to initialize a counter/accumulator

**Front:** Where must a counter or accumulator be initialized — inside or before the loop?

**Back:** Before the loop. Initializing it inside the loop resets it every pass.

**Tags:** python, stage-03, decision-rule

---

## Card: Most common infinite loop cause

**Front:** What's the most common cause of an accidental infinite loop?

**Back:** Forgetting to update, inside the loop body, whatever the while condition depends on.

**Tags:** python, stage-03, infinite-loop
