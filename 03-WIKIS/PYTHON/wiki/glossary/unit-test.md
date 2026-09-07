---
type: glossary-entry
stage: 10
status: draft
aliases: ["pytest"]
related_terms: ["test-case"]
timeline: reference
---

# Unit Test

## Plain-English Definition

A small, automated check that a specific piece of code (usually one function) produces the correct result for a given input, written so a tool like `pytest` can run it automatically.

## What Problem It Helps Solve

Re-checking correctness by hand (Stage 7's approach) gets slow and unreliable as a project grows. A unit test automates that check, permanently.

## When Chris Will See It

Functions in a `test_*.py` file, named `test_*`, using `assert` to check expected results.

## Code Example

```python
def square(n):
    return n * n

def test_square():
    assert square(4) == 16
    assert square(0) == 0
```

## Common Confusion

A test function that runs without crashing isn't automatically "passing" — only `assert` statements actually check correctness. A test with no `assert` at all will always appear to pass, even if the code is wrong.

## Physical-World Anchor

A factory's quality-control check — a specific, repeatable test confirms correctness automatically, instead of trusting a quick visual glance.

## Related Terms

- [[glossary/test-case]]

## Flashcard Q/A

**Front:** What does `assert` do inside a test function?

**Back:** It checks that a condition is true; if it's false, the test fails and pytest reports it.
