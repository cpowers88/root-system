---
type: drill
stage: 05
status: draft
concepts: ["list", "dictionary", "tuple", "set", "index", "slice", "aliasing"]
difficulty: beginner
solution_included: false
---

# Drill: Data Structure Practice

## Objective

Practice indexing/slicing, mutating lists, looking up dictionary values, and choosing the right structure for a given problem — without notes.

## Concepts Practiced

- list indexing, slicing, and mutation
- dictionary lookup (`[]` and `.get()`)
- tuples (light)
- choosing between list and dictionary

## Starter Prompt

**Part A — Lists:**

```python
fruits = ["apple", "banana", "cherry", "date"]
```

1. Print the second item.
2. Print the last item using a negative index.
3. Print a slice containing the middle two items.
4. Append `"elderberry"` to the list, then change `"banana"` to `"blueberry"` in place.

**Part B — Dictionaries:**

```python
inventory = {"apples": 10, "bananas": 5}
```

1. Print the count of `"apples"`.
2. Safely look up `"cherries"` with a default of `0`, without crashing if it's missing.
3. Add a new key `"cherries"` with a count of `3`.
4. Loop over the dictionary and print each item in the form `"X apples: 10"`.

**Part C — Structure Choice (no code, just answer in a comment):**

For each scenario, write a one-line comment saying which structure (list, dictionary, or tuple) fits best and why:

1. Storing a student's name, age, and grade.
2. Storing the order of moves in a tic-tac-toe game.
3. Storing a fixed (latitude, longitude) coordinate.

## Requirements

- Part A and B must run without errors and print correctly.
- Part C only needs a comment — no code required, but the reasoning must be stated, not just the answer.

## Constraints

- No functions required (though fine if you want to wrap things in one for practice).
- Sets are optional extra practice — not required for this drill.

## Expected Behavior

Part A and B should print the requested values/changes correctly. Part C should show correct structure choices with one-sentence justifications.

## Self-Check Questions

1. In Part A, why does appending and then modifying the list work, when the same operations would fail on a string?
2. In Part B, what would have happened if you used `inventory["cherries"]` directly instead of `.get()` before adding that key?
3. In Part C, which scenario was the hardest to decide, and why?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
