---
type: concept
stage: 01
status: draft
source_refs: ["Think Python Ch.1, Ch.5 (Keyboard Input)", "Python Crash Course Ch.2", "Automate the Boring Stuff Ch.1"]
prerequisites: ["values-and-expressions", "variables-and-assignment", "strings"]
tags: [print, input, comments]
timeline: reference
---

# Concept: `print()`, `input()`, and Comments

## Plain-English Meaning

`print()` displays text or values to the screen. `input()` pauses the program, shows an optional prompt, and waits for the user to type something — then hands back whatever they typed, as a string. A **comment** (starting with `#`) is a note in the code that Python ignores; it's there for humans only.

## What Problem This Solves

A program needs a way to show results (`print()`) and a way to receive information from the person running it (`input()`). Comments let you (or future-you) remember why code does what it does.

## When To Use It

- `print()`: any time you want to see a result or message.
- `input()`: any time the program needs information from the user before it can continue.
- Comments: when the *why* behind a line isn't obvious from the code itself — not to restate what the code already says.

## When Not To Use It

Don't write a comment that just repeats the code (`x = x + 1  # add one to x`). Don't use `input()` when the value should come from inside the program itself (a calculation, not the user).

## Code Shape

```python
print(value_or_expression)
name = input("Prompt text: ")
# this is a comment — Python skips this line entirely
```

## Tiny Working Example

```python
# ask the user for their name and greet them
name = input("What's your name? ")
print(f"Hello, {name}!")
```

## Beginner Mistakes

- Forgetting that `input()`'s return value is always a string, even when it looks like a number (see [[concepts/numbers-and-type-conversion]]).
- Putting code after a comment on the same line without realizing everything after `#` on that line is ignored.
- Calling `print` without parentheses (`print "hello"`) — that's Python 2 syntax and is a `SyntaxError` in Python 3.

## Physical-World Anchor

`print()` is like speaking out loud; `input()` is like asking a question and waiting silently until the other person answers.

## Required Vocabulary

- [[glossary/print]]
- [[glossary/input]]
- [[glossary/comment]]

## Related Code Patterns

- [[code-patterns/input-and-type-conversion]]

## Drill

- [[drills/stage-01-input-and-conversion]]

## Explain-Back Questions

1. What type of value does `input()` always return?
2. Why might `print "hello"` (no parentheses) fail in Python 3?
3. Give an example of a comment that's actually useful, and one that isn't.

## Source Notes

- (source: Think Python, 2nd Ed., Ch.1; Ch.5, "Keyboard Input" — pulled forward into Stage 1)
- (source: Python Crash Course, 3rd Ed., Ch.2)
- (source: Automate the Boring Stuff, 3rd Ed., Ch.1)
