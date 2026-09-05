---
type: concept
stage: 03
status: draft
source_refs: ["Think Python Ch.7 (Updating Variables)", "Python Workout Ch.2"]
prerequisites: ["for-loops", "while-loops", "variables-and-assignment"]
tags: [counters, accumulators]
timeline: reference
---

# Concept: Counters and Accumulators

## Plain-English Meaning

A **counter** is a variable that keeps track of how many times something has happened, going up by a fixed amount (usually 1) each time. An **accumulator** is a variable that builds up a total (or other combined result) across each pass of a loop.

## What Problem This Solves

A loop's job often isn't just "repeat" — it's "repeat *and remember something across repetitions*," like a running total, a count of matches, or the longest word seen so far. Counters and accumulators are the pattern for that.

## When To Use It

Use a counter when you need to know *how many* times something happened. Use an accumulator when you need to *combine* values across iterations (sum, product, concatenated string, running maximum).

## When Not To Use It

If you don't need to remember anything between iterations — each pass is independent — you don't need a counter or accumulator, just a plain loop.

## Code Shape

```python
counter = 0
for item in some_sequence:
    if some_condition(item):
        counter = counter + 1   # or counter += 1

total = 0
for number in some_numbers:
    total = total + number      # or total += number
```

## Tiny Working Example

```python
numbers = [4, 8, 15, 16, 23, 42]
total = 0
count = 0
for n in numbers:
    total = total + n
    count = count + 1
print(f"Average: {total / count}")
```

## Beginner Mistakes

- Forgetting to initialize the counter/accumulator **before** the loop starts (it must exist with a starting value, usually `0`, before the loop runs).
- Putting the initialization *inside* the loop, which resets it every single pass instead of building up.
- Using `=` instead of `+=` and forgetting to add the old value back in (`total = number` instead of `total = total + number`).

## Physical-World Anchor

A tally counter (the clicker bouncers use at a club) — it starts at zero, and every time something happens, you click it once. It never resets itself; it just keeps building.

## Required Vocabulary

- [[glossary/counter]]
- [[glossary/accumulator]]

## Related Code Patterns

- [[code-patterns/for-loop-over-range]]
- [[code-patterns/while-loop-until-condition]]

## Drill

- [[drills/stage-03-loop-tracing]]

## Explain-Back Questions

1. Why does a counter or accumulator need to be created *before* the loop starts, not inside it?
2. What's the difference in purpose between a counter and an accumulator?
3. What would go wrong if you wrote `total = number` instead of `total = total + number` inside the loop?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.7, "Updating Variables")
- (source: Python Workout, 2nd Ed., Ch.2, "Summing numbers" exercise)
