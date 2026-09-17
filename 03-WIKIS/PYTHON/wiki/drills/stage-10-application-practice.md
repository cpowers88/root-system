---
type: drill
stage: 10
status: draft
concepts: ["cli", "argument-parsing", "unit-test", "database"]
difficulty: beginner
solution_included: false
timeline: reference
---

# Drill: CLI, Testing, and Database Basics

## Objective

Practice the three core Stage 10 tools in isolation, before combining them in the mini-project.

## Concepts Practiced

- `argparse` for CLI arguments
- `pytest` test functions with `assert`
- basic SQLite reads/writes

## Starter Prompt

**Part A — CLI:**

Write a script `greet.py` that takes a required `name` argument and an optional `--shout` flag. Running `python greet.py Chris --shout` should print `"HELLO, CHRIS!"`; without `--shout`, it should print `"Hello, Chris!"`.

**Part B — Testing:**

Write a function `is_palindrome(text)` that returns `True` if a string reads the same backward as forward (ignore this drill's scope creep — case-sensitivity and spaces don't need special handling). Then write at least 3 `pytest` test cases for it, including one that should return `False`.

**Part C — SQLite:**

Write a script that creates a small `notes.db` SQLite database with one table (`notes`, with a `text` column), inserts 2-3 sample notes, and then queries and prints all of them back.

## Requirements

- Part A must use `argparse`, not manual `sys.argv` parsing.
- Part B's tests must use `assert` and follow the `test_` naming convention so `pytest` can discover them.
- Part C must call `conn.commit()` after inserting, and confirm the data persisted by querying it back in the same script.

## Constraints

- No web requests/API calls needed for this drill — Stage 10's API content stays conceptual only.
- Keep the SQLite table to one column for this drill; more complex schemas aren't required here.

## Expected Behavior

Part A should behave correctly with and without `--shout`. Part B's tests should all pass when run with `pytest`. Part C should print back the exact notes that were inserted.

## Self-Check Questions

1. In Part A, what happens if you run `greet.py` with no arguments at all?
2. In Part B, what's one edge case for `is_palindrome` that's worth testing beyond the obvious "racecar" example?
3. In Part C, what would happen to your printed results if you forgot `conn.commit()`?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
