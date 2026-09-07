---
type: flashcards
tags: [programming]
timeline: later
---

# Flashcard Batch: Stage 10 — Application Thinking

## Card: CLI

**Front:** What does CLI stand for, and what does it mean for a program?

**Back:** Command-line interface — a program that takes its input as arguments typed after the command, rather than through interactive prompts.

**Tags:** python, stage-10, cli

---

## Card: Positional vs optional arguments

**Front:** What's the difference between a positional argument and an optional flag in argparse?

**Back:** A positional argument is required by position and usually mandatory. An optional flag (starting with `--`) is named and usually optional.

**Tags:** python, stage-10, decision-rule

---

## Card: assert in tests

**Front:** What does `assert` do inside a test function?

**Back:** It checks that a condition is true; if it's false, the test fails and pytest reports it.

**Tags:** python, stage-10, testing

---

## Card: Tests need assertions

**Front:** Can a test function "pass" even if it has no assert statements at all?

**Back:** Yes — without an assert, the test only checks that the code runs without crashing, not that the result is correct. Always assert the actual expected value.

**Tags:** python, stage-10, decision-rule

---

## Card: conn.commit()

**Front:** What does `conn.commit()` do, and what happens if you forget it?

**Back:** It saves pending changes to the database. Forgetting it means inserts/updates are never actually persisted.

**Tags:** python, stage-10, databases

---

## Card: CSV/JSON vs database decision rule

**Front:** When should you reach for a database instead of a CSV or JSON file?

**Back:** When data needs to be searched, filtered, or updated efficiently, especially as it grows large or needs structured querying.

**Tags:** python, stage-10, decision-rule

---

## Card: API response format

**Front:** What format do most APIs return data in?

**Back:** JSON.

**Tags:** python, stage-10, apis

---

## Card: Checking a web request

**Front:** Why should you check a web request's status code before using its data?

**Back:** Because a failed request can still return a response object — the status code tells you whether it actually succeeded.

**Tags:** python, stage-10, web-requests
