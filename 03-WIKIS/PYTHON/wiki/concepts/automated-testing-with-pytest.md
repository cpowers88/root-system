---
type: concept
stage: 10
status: draft
source_refs: ["Python Crash Course Ch.11 (Testing Your Code)"]
prerequisites: ["defining-and-calling-functions", "return-values", "test-case"]
tags: [testing, pytest]
timeline: reference
---

# Concept: Automated Testing with `pytest`

## Plain-English Meaning

A **unit test** is a small, automated check that a specific piece of code (usually one function) produces the correct result for a given input. `pytest` is a tool that finds and runs all your test functions automatically, reporting which passed and which failed.

## What Problem This Solves

Stage 7 introduced test cases as something you check by hand. As programs grow, re-checking everything by hand every time you change something becomes slow and unreliable. `pytest` automates that checking — run one command, see instantly whether anything broke.

## When To Use It

For any function whose correctness matters and that you'll be changing or relying on over time — especially as a project grows beyond a single script.

## When Not To Use It

For a tiny one-off script you'll run once and never touch again, formal automated tests are usually overkill — the informal Stage 7 approach (checking by hand) is fine.

## Code Shape

```python
# in my_module.py
def square(n):
    return n * n

# in test_my_module.py — pytest finds functions starting with "test_"
from my_module import square

def test_square():
    assert square(4) == 16
    assert square(0) == 0
    assert square(-3) == 9
```

## Tiny Working Example

```bash
pip install pytest
pytest test_my_module.py
```
```text
1 passed in 0.01s
```

## Beginner Mistakes

- Forgetting `assert` — without it, a test function that runs without crashing looks like it "passed," even if the actual values are wrong.
- Naming test files or functions without the `test_` prefix `pytest` looks for — they simply won't be discovered and run.
- Writing only one test case per function ("the obvious one") and missing edge cases like zero, negative numbers, or empty input.

## Physical-World Anchor

A quality-control checklist at a factory — instead of trusting that each product is fine by eye, a specific, repeatable check confirms it every time, automatically.

## Required Vocabulary

- [[glossary/unit-test]]

## Related Code Patterns

- [[code-patterns/pytest-test-function]]

## Drill

- [[drills/stage-10-application-practice]]

## Explain-Back Questions

1. What does `assert` actually do inside a test function?
2. Why might re-checking test cases by hand (Stage 7's approach) become unreliable as a project grows?
3. What naming convention does `pytest` rely on to find test functions automatically?

## Source Notes

- (source: Python Crash Course, 3rd Ed., Ch.11, "Testing Your Code")
