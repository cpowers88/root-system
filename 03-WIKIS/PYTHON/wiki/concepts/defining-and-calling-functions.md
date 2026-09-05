---
type: concept
stage: 04
status: draft
source_refs: ["Think Python Ch.3 (Function Calls, Composition, Adding New Functions, Definitions and Uses, Flow of Execution)", "Automate the Boring Stuff Ch.4", "Python Crash Course Ch.8"]
prerequisites: ["for-loops", "while-loops", "if-elif-else"]
tags: [functions, def, call]
timeline: reference
---

# Concept: Defining and Calling Functions

## Plain-English Meaning

A **function** is a named, reusable block of code. You **define** it once with `def`, then **call** it (run it) by name as many times as you want, anywhere in the program.

## What Problem This Solves

Without functions, any logic used more than once has to be copy-pasted everywhere it's needed. Functions let you write the logic once, name it, and reuse it — and if you need to fix or change it, you only fix it in one place.

## When To Use It

Whenever a piece of logic is used more than once, or whenever a chunk of code is complex enough that giving it a name makes the program easier to read.

## When Not To Use It

Don't wrap a single line that's only ever used once into a function just for the sake of it — that adds indirection without benefit. Wait until there's an actual reuse or clarity reason.

## Code Shape

```python
def function_name():
    # body — runs only when the function is called
    pass

function_name()   # this is what actually runs the body
```

## Tiny Working Example

```python
def greet():
    print("Hello!")
    print("Welcome to Stage 4.")

greet()   # prints both lines
greet()   # prints both lines again
```

## Beginner Mistakes

- Defining a function but forgetting to *call* it — nothing happens, because `def` only describes the function, it doesn't run it.
- Expecting the function body to run top-to-bottom as soon as Python reads the `def` line — it doesn't; it only runs when called.
- Misspelling the function name when calling it, causing a `NameError`.

## Physical-World Anchor

A recipe card is the function **definition** — writing it down doesn't make food appear. Actually cooking from the card is the function **call**.

## Required Vocabulary

- [[glossary/function]]
- [[glossary/def]]
- [[glossary/call]]

## Related Code Patterns

- [[code-patterns/function-with-parameter]]

## Drill

- [[drills/stage-04-function-writing]]

## Explain-Back Questions

1. What's the difference between defining a function and calling it?
2. What happens if you define a function but never call it?
3. Why might you choose to turn a piece of code into a function even if you only use it once right now?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.3, "Function Calls," "Composition," "Adding New Functions," "Definitions and Uses," "Flow of Execution")
- (source: Automate the Boring Stuff, 3rd Ed., Ch.4)
- (source: Python Crash Course, 3rd Ed., Ch.8, "Defining a Function")
