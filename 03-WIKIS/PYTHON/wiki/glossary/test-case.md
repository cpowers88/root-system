---
type: glossary-entry
stage: 07
status: draft
aliases: []
related_terms: ["incremental-development"]
timeline: reference
---

# Test Case

## Plain-English Definition

A specific input, paired with the output you expect, used to check that a piece of code actually works correctly.

## What Problem It Helps Solve

"It looked right when I ran it" isn't the same as actually verifying correctness — a test case forces a specific, checkable claim: "for this input, the answer should be exactly this."

## When Chris Will See It

Whenever checking a function or program — especially worth having a few test cases ready *before* writing the code, not just after.

## Code Example

```python
def square(n):
    return n * n

# Test cases:
print(square(2) == 4)     # True — expected
print(square(-3) == 9)    # True — expected, checks a negative number too
print(square(0) == 0)     # True — expected, checks the edge case of zero
```

## Common Confusion

A single test case passing doesn't prove the code is correct in general — it's worth checking a few different kinds of input, including edge cases (zero, empty, negative) not just the "obvious" one.

## Physical-World Anchor

A taste test with a known recipe — you know what the dish *should* taste like, so you can tell precisely if something's off, rather than just guessing "this seems fine."

## Related Terms

- [[glossary/incremental-development]]

## Flashcard Q/A

**Front:** Why isn't "it looked right when I ran it" the same as testing?

**Back:** Because that's not a specific, checkable claim — a real test case pairs a specific input with a specific expected output.
