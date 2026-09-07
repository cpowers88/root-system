---
type: mini-project
stage: 03
status: draft
concepts: ["while-loop", "for-loop", "counter", "accumulator", "break-continue", "if-elif-else"]
solution_included: false
timeline: reference
---

# Mini-Project: Number-Guessing Game with Limited Attempts

## User Story

As a learner, I want to build a number-guessing game that gives the player a limited number of attempts and tracks how many guesses they used, so that I can prove I understand `while` loops, counters, and combining loops with conditionals.

## Required Concepts

- [[glossary/while-loop]]
- [[glossary/for-loop]]
- [[glossary/counter]]
- [[glossary/break-continue]]
- [[glossary/if-elif-else]]

## Build Phases

### Phase 1 — Basic Loop

Pick a secret number yourself (hardcoded, e.g. `secret = 7`) and write a `while` loop that keeps asking "Guess the number (1-10):" until the player guesses correctly. Print "Too low" or "Too high" using `if`/`elif`/`else` after each wrong guess.

### Phase 2 — Limit the Attempts

Add a counter that tracks how many guesses have been made. Limit the player to 5 attempts total — if they run out without guessing correctly, print a "Game over" message and end the loop (using either the `while` condition itself, or a `break`).

### Phase 3 — Final Report

After the loop ends (whether by winning or running out of attempts), print how many guesses the player used, and whether they won or lost.

## Acceptance Checklist

- [ ] Uses a `while` loop, not a `for` loop, since the number of guesses isn't fixed in advance.
- [ ] A counter tracks the number of guesses made, initialized before the loop.
- [ ] The game correctly stops both on a correct guess **and** after 5 failed attempts.
- [ ] Uses `if`/`elif`/`else` to give "too low" / "too high" / "correct" feedback.
- [ ] Prints a final summary (guesses used, win/lose) after the loop ends.
- [ ] Chris can explain, out loud, what would happen if the attempt counter were initialized inside the loop instead of before it.

## Stretch Goals — Parked

- Let the computer pick a random secret number instead of a hardcoded one (needs the `random` module — fine to mention, not required).
- Let the player play multiple rounds in a row (needs an outer loop — fine as a stretch, but don't let it block finishing the core project).

## Reflection Questions

1. Why was `while` the right loop choice here instead of `for`?
2. What were the two different conditions that could end your loop, and how did you handle both?
3. If you wanted to also track the player's *fastest* win across multiple games, what would you need to add? (Just describe it — building it is a later stage.)

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
