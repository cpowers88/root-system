---
type: concept
stage: 07
status: draft
source_refs: ["Think Python Ch.4 (A Development Plan)", "Think Python Ch.9, Ch.13 (Case Studies)"]
prerequisites: ["decomposition-and-pseudocode", "debugging-process"]
tags: [stage-07, incremental-development, testing, algorithm]
---

# Concept: Incremental Development and Testing

## Plain-English Meaning

**Incremental development** means building a program one small, working piece at a time — testing each piece before adding the next — instead of writing the whole thing at once and only then trying to run it. An **algorithm** (in this stage's sense) is just a precise, step-by-step procedure for solving a problem; a **test case** is a specific input you run through the program to check the output is correct.

## What Problem This Solves

Writing an entire multi-step program before running any of it means that when something breaks, you have no idea which of the many new lines caused it. Building and testing incrementally means any bug is almost always in the one small piece you just added.

## When To Use It

Every time you build something with more than 1-2 logical steps — which, after Stage 7, is most things.

## When Not To Use It

For genuinely trivial one-line scripts, there's no meaningful "incremental" path — just write and run it.

## Code Shape

```text
1. Write step 1's code only. Run it. Confirm it works (with print() if needed).
2. Add step 2's code. Run it. Confirm steps 1+2 work together.
3. Add step 3's code. Run it. Confirm.
... repeat until the full decomposed plan is built.
```

## Tiny Working Example

```python
# Step 1: just get a random word and print it (confirm this works first)
import random
secret_word = random.choice(["python", "hangman", "stage"])
print(secret_word)   # temporary — to confirm step 1 works

# Only after confirming step 1, add step 2:
guessed_letters = []
print(guessed_letters)   # temporary — confirm step 2's starting state
```

## Beginner Mistakes

- Writing five new steps in one go "to save time," then having to debug all five at once when something breaks.
- Removing temporary `print()` checks too early, before confirming the next piece also works correctly.
- Not having a specific test case in mind — running a program once and eyeballing the output instead of checking it against a known correct answer.

## Physical-World Anchor

Building with LEGO instructions one step at a time, checking each step matches the picture before moving to the next — rather than dumping out all the pieces and guessing at the final shape.

## Required Vocabulary

- [[glossary/incremental-development]]
- [[glossary/algorithm]]
- [[glossary/test-case]]

## Related Code Patterns

- (none — this is a process skill applied across all previously-learned patterns)

## Drill

- [[drills/stage-07-decompose-a-problem]]

## Explain-Back Questions

1. Why is it easier to debug a program built incrementally than one written all at once?
2. What is a test case, and why is "it looked right when I glanced at it" not the same as testing?
3. What's the difference between "pseudocode" (Stage 7's planning step) and an "algorithm" (the actual step-by-step procedure once it's working)?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.4, "A Development Plan")
- (source: Think Python, 2nd Ed., Ch.9 and Ch.13 — the Case Study chapters model this process directly, used here as a worked example rather than for their specific content)
