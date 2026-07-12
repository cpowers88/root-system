---
type: flashcards
tags: [later, programming]
---

# Flashcard Batch: Stage 6 — Files, Errors, and Debugging

## Card: Relative vs absolute path

**Front:** What's the difference between a relative and an absolute file path?

**Back:** A relative path depends on where the program is run from; an absolute path is the full address and works from anywhere.

**Tags:** python, stage-06, file-paths

---

## Card: "w" mode danger

**Front:** What happens to a file's existing contents when you open it in `"w"` mode?

**Back:** They're erased immediately, even before you write anything new.

**Tags:** python, stage-06, decision-rule

---

## Card: Exception

**Front:** What is an exception in Python?

**Back:** A signal that something went wrong while the program was running, named by category (ValueError, TypeError, etc.).

**Tags:** python, stage-06, exceptions

---

## Card: Reading a traceback

**Front:** Which line of a traceback should you read first?

**Back:** The last line — it names the actual error type and message.

**Tags:** python, stage-06, debugging

---

## Card: Bare except risk

**Front:** Why is a bare `except:` (with no error type) considered risky?

**Back:** It catches every exception, including unexpected bugs, which can hide real problems instead of surfacing them.

**Tags:** python, stage-06, decision-rule

---

## Card: Three error types

**Front:** Which of the three error types produces no error message at all?

**Back:** A semantic error — the code runs fine, but produces the wrong result.

**Tags:** python, stage-06, error-types

---

## Card: try/except decision rule

**Front:** When should you use `try`/`except` versus just fixing the code?

**Back:** Use `try`/`except` for failures you expect could happen normally (bad user input, a missing file). Don't use it to paper over a bug you haven't actually understood yet.

**Tags:** python, stage-06, decision-rule

---

## Card: Context manager benefit

**Front:** What does `with open(...) as f:` do for you automatically?

**Back:** It closes the file automatically once the block finishes, even if an error occurs inside it.

**Tags:** python, stage-06, files
