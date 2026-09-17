---
type: concept
stage: 03
status: draft
source_refs: ["Think Python Ch.8 (Traversal with a for Loop, pulled forward)", "Automate the Boring Stuff Ch.3", "Python Crash Course Ch.4"]
prerequisites: ["if-elif-else", "comparisons-and-boolean-logic"]
tags: [for-loop, range, iteration]
timeline: reference
---

# Concept: `for` Loops and `range()`

## Plain-English Meaning

A **`for` loop** repeats a block of code once for each item in a sequence — each character in a string, each number in a `range()`, or (later) each item in a list. **`range()`** generates a sequence of numbers to loop over, without you having to write them all out.

## What Problem This Solves

Without loops, repeating an action N times means writing the same line N times by hand. A `for` loop lets you say "do this for every item" once, and Python handles the repetition.

## When To Use It

Whenever you know (or can generate) the exact sequence to repeat over: "do this 10 times," "do this for every letter in this word."

## When Not To Use It

If you don't know in advance how many times you need to repeat — you're waiting for some condition to become true or false — use a `while` loop instead (see [[concepts/while-loops]]).

## Code Shape

```python
for variable in range(n):
    # runs n times, with variable taking values 0, 1, ..., n-1

for character in some_string:
    # runs once per character
```

## Tiny Working Example

```python
for i in range(5):
    print(f"Count: {i}")

for letter in "Py":
    print(letter)
```

## Beginner Mistakes

- Forgetting that `range(5)` produces `0, 1, 2, 3, 4` — five numbers, not including 5. This causes off-by-one errors.
- Forgetting the colon `:` and indentation, same as `if` statements.
- Trying to modify the loop variable inside the loop expecting it to change how many times the loop runs — it won't; `range()` already decided that before the loop started.

## Physical-World Anchor

Like going down a checklist line by line — you do the same action (check the item, move to the next) for every line on the list, until there are no more lines.

## Required Vocabulary

- [[glossary/for-loop]]
- [[glossary/range]]
- [[glossary/iteration]]

## Related Code Patterns

- [[code-patterns/for-loop-over-range]]

## Drill

- [[drills/stage-03-loop-tracing]]

## Explain-Back Questions

1. How many times does `for i in range(5):` run its body, and what values does `i` take?
2. When would you choose a `for` loop over a `while` loop?
3. What happens if you change the loop variable inside the loop body — does it affect how many times the loop runs?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.8, "Traversal with a for Loop" — pulled forward into Stage 3 per `wiki/source-map.md`)
- (source: Automate the Boring Stuff, 3rd Ed., Ch.3)
- (source: Python Crash Course, 3rd Ed., Ch.4, "Using the range() Function")
