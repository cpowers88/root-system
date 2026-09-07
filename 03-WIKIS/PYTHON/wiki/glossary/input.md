---
type: glossary-entry
stage: 01
status: draft
aliases: ["input()"]
related_terms: ["print", "type-conversion"]
timeline: reference
---

# `input()`

## Plain-English Definition

A built-in function that pauses the program, optionally shows a prompt, and waits for the user to type something. It always hands back what they typed as a **string**.

## What Problem It Helps Solve

Lets a program collect information from the person running it instead of having everything hardcoded.

## When Chris Will See It

Any time the program needs to ask the user something before continuing.

## Code Example

```python
name = input("What's your name? ")
age = int(input("How old are you? "))   # converted immediately, since math is needed
```

## Common Confusion

`input()` **always** returns a string — even if the user types `42`. If you need to do math with the answer, you must convert it first (see [[glossary/type-conversion]]).

## Physical-World Anchor

Like asking a question out loud and waiting silently for the answer before doing anything else.

## Related Terms

- [[glossary/print]]
- [[glossary/type-conversion]]

## Flashcard Q/A

**Front:** What type of value does `input()` always return?

**Back:** A string — always, even if the user types something that looks like a number.
