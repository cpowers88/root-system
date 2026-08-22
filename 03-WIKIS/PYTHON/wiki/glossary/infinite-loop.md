---
type: glossary-entry
stage: 03
status: draft
aliases: []
related_terms: ["while-loop", "break-continue"]
timeline: reference
---

# Infinite Loop

## Plain-English Definition

A loop whose condition never becomes `False`, so it never stops on its own — the program appears to "freeze" running the same block forever.

## What Problem It Helps Solve

It doesn't solve a problem — it's almost always a bug. Recognizing the shape of one is the goal here, not creating them on purpose.

## When Chris Will See It

Most often by accident in a `while` loop, when whatever the condition depends on never gets updated inside the loop body.

## Code Example

```python
# BUG: count never changes, so this never stops
count = 0
while count < 5:
    print("stuck")
```

## Common Confusion

A `for` loop over a `range()` can't easily become infinite (it has a fixed number of steps already decided) — infinite loops are almost always a `while` loop problem.

## Physical-World Anchor

A car stuck in a roundabout that never takes the exit — it keeps going around because nothing tells it to leave.

## Related Terms

- [[glossary/while-loop]]

## Flashcard Q/A

**Front:** What's the most common cause of an accidental infinite loop?

**Back:** Forgetting to update, inside the loop body, whatever the while condition depends on.
