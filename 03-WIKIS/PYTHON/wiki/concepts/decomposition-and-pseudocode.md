---
type: concept
stage: 07
status: draft
source_refs: ["Think Python Ch.4 (A Development Plan)", "Think Like a Programmer Ch.1 (Strategies for Problem Solving) — strategy discussion only"]
prerequisites: ["defining-and-calling-functions", "lists", "dictionaries"]
tags: [stage-07, decomposition, pseudocode, program-design]
---

# Concept: Decomposition and Pseudocode

## Plain-English Meaning

**Decomposition** is breaking a big, vague problem into smaller, concrete steps that are each simple enough to code directly. **Pseudocode** is writing those steps out in plain English (or a loose code-like shorthand), *before* writing any real Python.

## What Problem This Solves

A problem like "build a hangman game" is too big to write in one sitting without a plan — it's easy to get lost, write yourself into a corner, or forget a piece. Decomposing it first turns one huge problem into several small, manageable ones.

## When To Use It

Before starting any program bigger than a few lines — especially mini-projects and anything with multiple moving parts (input, processing, output, repeated logic).

## When Not To Use It

For a one-line script, formal decomposition is overkill — just write it. The skill is recognizing when a problem is big enough to need a plan first.

## Code Shape

```text
Problem: "Build a hangman game"

Decomposed steps (pseudocode):
1. Pick a random secret word
2. Track which letters have been guessed
3. Show the word with unguessed letters blanked out
4. Ask the player for a letter
5. Check if the letter is in the word
6. Update the display and guess count
7. Repeat until the word is guessed or guesses run out
8. Show win/lose message
```

## Tiny Working Example

```python
# Pseudocode translated into real (partial) code, one step at a time:

# Step 1
import random
secret_word = random.choice(["python", "hangman", "stage"])

# Step 2 (next step, built only after step 1 is confirmed working)
guessed_letters = []
```

## Beginner Mistakes

- Skipping straight to code without writing the steps down first — this is the single biggest cause of getting stuck or lost on a project.
- Writing pseudocode so vague it doesn't actually help ("make the game work") instead of concrete, codeable steps ("pick a random word from a list").
- Trying to decompose *and* code at the same time — write the full list of steps first, then start coding step 1.

## Physical-World Anchor

A recipe's ingredient list and numbered steps, written out *before* anyone starts cooking — not figured out mid-recipe while the stove is already on.

## Required Vocabulary

- [[glossary/decomposition]]
- [[glossary/pseudocode]]

## Related Code Patterns

- (none — this is a planning skill, not a syntax pattern)

## Drill

- [[drills/stage-07-decompose-a-problem]]

## Explain-Back Questions

1. Why decompose a problem before writing any code, instead of just starting?
2. What makes a pseudocode step "concrete enough" versus too vague?
3. Pick a small everyday task (making a sandwich, getting ready for school) and decompose it into 5 steps.

## Source Notes

- (source: Think Python, 2nd Ed., Ch.4, "A Development Plan")
- (source: Think Like a Programmer, V. Anton Spraul, Ch.1, "Strategies for Problem Solving" — strategy/discussion only, the book's code examples are C++ and are not used here, per `wiki/parking-lot.md`)
