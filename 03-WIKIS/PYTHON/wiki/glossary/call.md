---
type: glossary-entry
stage: 04
status: draft
aliases: ["function call"]
related_terms: ["function", "def", "argument"]
timeline: reference
---

# Call

## Plain-English Definition

Actually running a function by writing its name followed by parentheses (and any arguments it needs).

## What Problem It Helps Solve

This is the step that makes a defined function actually do something.

## When Chris Will See It

Anywhere a function is used: `greet("Chris")`, `print(...)`, `len(...)`.

## Code Example

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Chris")   # this line is the call
```

## Common Confusion

A function can be called as many times as needed, from anywhere in the program, after it's been defined — each call runs the body fresh.

## Physical-World Anchor

Cooking from a recipe card — you can cook the same recipe many times; each time is a separate "call."

## Related Terms

- [[glossary/function]]
- [[glossary/def]]

## Flashcard Q/A

**Front:** What is a function call?

**Back:** Actually running a function by writing its name with parentheses (and any needed arguments).
