---
type: glossary-entry
stage: 01
status: draft
aliases: []
related_terms: []
timeline: reference
---

# Comment

## Plain-English Definition

A note in the code, starting with `#`, that Python completely ignores when running the program. It's there for humans reading the code.

## What Problem It Helps Solve

Lets you (or someone else reading the code later) understand *why* a piece of code exists, especially when it's not obvious from the code itself.

## When Chris Will See It

At the top of files, before tricky lines, or anywhere a non-obvious decision was made.

## Code Example

```python
# convert the input to an integer because input() always returns text
age = int(input("Age? "))
```

## Common Confusion

A good comment explains *why*, not *what* — `x = x + 1  # add one to x` is a useless comment because the code already says that.

## Physical-World Anchor

Like a sticky note left for the next person, explaining a decision that isn't obvious just from looking at the result.

## Related Terms

- (none yet)

## Flashcard Q/A

**Front:** What does a comment do in Python?

**Back:** Nothing to the program — Python ignores anything after `#` on a line. It's a note for humans reading the code.
