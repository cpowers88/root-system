---
type: glossary-entry
stage: 03
status: draft
aliases: ["while statement"]
related_terms: ["loop", "infinite-loop", "break-continue"]
---

# `while` Loop

## Plain-English Definition

A loop that keeps running its body as long as a condition stays `True`, checking that condition again before every pass.

## What Problem It Helps Solve

Handles repetition where the number of passes isn't known in advance — the loop should continue "until" something happens.

## When Chris Will See It

Validating input until it's correct, repeating a game round until the player quits or wins, anything driven by "keep going until X."

## Code Example

```python
attempts = 0
while attempts < 3:
    print("Trying...")
    attempts = attempts + 1
```

## Common Confusion

Nothing inside a `while` loop automatically stops it — *you* must make sure something inside the loop eventually makes the condition `False`, or it becomes an infinite loop.

## Physical-World Anchor

Stirring a pot "until it thickens" — you keep checking and stirring, with no fixed number of stirs decided in advance.

## Related Terms

- [[glossary/infinite-loop]]
- [[glossary/break-continue]]

## Flashcard Q/A

**Front:** What must be true for a `while` loop to eventually stop?

**Back:** Something inside the loop body must change the condition so it eventually becomes False.
