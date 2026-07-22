---
type: glossary-entry
stage: 06
status: draft
aliases: []
related_terms: ["exception"]
timeline: reference
---

# Traceback

## Plain-English Definition

The report Python prints when an unhandled exception occurs, showing the sequence of calls that led to the failure, ending with the specific error type and message at the bottom.

## What Problem It Helps Solve

Tells you exactly where and why a program crashed, instead of leaving you to guess.

## When Chris Will See It

Any time a program crashes without being caught by `try`/`except`.

## Code Example

```text
Traceback (most recent call last):
  File "script.py", line 4, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero
```

## Common Confusion

Read a traceback **bottom-up**: the last line names the actual error and message; the lines above show the path that led there. Beginners often start reading from the top and get lost in the call chain before reaching the useful part.

## Physical-World Anchor

A flight recorder's final readout — the most important fact (what actually went wrong) is the last line, with the sequence of events leading up to it shown above.

## Related Terms

- [[glossary/exception]]

## Flashcard Q/A

**Front:** Which line of a traceback should you read first?

**Back:** The last line — it names the actual error type and message.
