---
type: code-pattern
stage: 10
status: draft
concepts: ["unit-test", "function", "return-value"]
tags: [stage-10, testing, pytest]
---

# Code Pattern: `pytest` Test Function

## Purpose

Write an automated, repeatable check that a function produces the correct result, so correctness can be verified instantly at any time, not just by hand once.

## Use This When

A function's correctness matters and will be relied on or changed over time.

## Do Not Use This When

A throwaway, one-off script that will never be touched again doesn't need formal tests — the informal checking from Stage 7 is enough there.

## Skeleton

```python
# in my_module.py
def function_to_test(input_value):
    # ... logic ...
    return result

# in test_my_module.py
from my_module import function_to_test

def test_function_to_test():
    assert function_to_test(known_input) == expected_output
```

## Filled Example

```python
# in calculator.py
def add(a, b):
    return a + b

# in test_calculator.py
from calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

## Step-by-Step Trace

1. `pytest` scans files named `test_*.py` and runs every function inside them named `test_*`.
2. Each `assert` statement checks one specific expected result.
3. If every `assert` in a test function succeeds, that test passes. If any fails, `pytest` reports exactly which assertion failed and what the actual value was.

## Beginner Mistakes

- Forgetting `assert` entirely — a test function with no assertions always "passes," even on completely wrong code.
- Naming the test file or function without the `test_` prefix — `pytest` won't discover it, and it silently never runs.
- Writing only the "obvious" test case and skipping edge cases (zero, negative, empty) that often reveal real bugs.

## Related Terms

- [[glossary/unit-test]]
- [[glossary/test-case]]

## Drill Link

- [[drills/stage-10-application-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-10-application-thinking]].
