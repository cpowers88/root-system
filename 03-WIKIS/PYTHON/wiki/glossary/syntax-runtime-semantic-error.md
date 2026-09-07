---
type: glossary-entry
stage: 06
status: draft
aliases: ["syntax error", "runtime error", "semantic error"]
related_terms: ["exception", "traceback"]
timeline: reference
---

# Syntax / Runtime / Semantic Error

## Plain-English Definition

Three categories of bugs. A **syntax error** means the code isn't valid Python at all — caught before the program even starts running. A **runtime error** means the code is valid but crashes partway through (an exception). A **semantic error** means the code runs fine and produces no error — but gives the wrong result.

## What Problem It Helps Solve

Naming which category a bug falls into points you toward the right debugging technique — semantic errors need `print()`-based investigation since there's no error message to read.

## When Chris Will See It

Every single bug fits into one of these three categories.

## Code Example

```python
# Syntax error — missing colon, won't even run
if x > 5
    print("big")

# Runtime error — valid syntax, crashes when run
print(1 / 0)

# Semantic error — runs fine, wrong answer, no error at all
def add(a, b):
    return a - b   # should be a + b
```

## Common Confusion

Semantic errors are the hardest to notice precisely *because* nothing looks wrong on the surface — the program runs and produces output, just the wrong output.

## Physical-World Anchor

Syntax error: a sentence with broken grammar that doesn't parse. Runtime error: a grammatically correct sentence describing an impossible action. Semantic error: a perfectly correct, parseable sentence that's simply factually wrong.

## Related Terms

- [[glossary/exception]]
- [[glossary/traceback]]

## Flashcard Q/A

**Front:** Which of the three error types produces no error message at all?

**Back:** A semantic error — the code runs fine, but produces the wrong result.
