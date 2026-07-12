---
type: glossary-entry
stage: 04
status: draft
aliases: []
related_terms: ["def", "call", "parameter", "return-value"]
---

# Function

## Plain-English Definition

A named, reusable block of code that can be run (called) as many times as needed.

## What Problem It Helps Solve

Lets you write a piece of logic once and reuse it everywhere it's needed, instead of copy-pasting it.

## When Chris Will See It

Anywhere logic needs to be reused, or anywhere a chunk of code deserves a name for clarity.

## Code Example

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Chris")
```

## Common Confusion

Defining a function (`def ...`) doesn't run it — the body only runs when the function is actually called by name.

## Physical-World Anchor

A recipe card — writing the recipe doesn't make food appear; you have to actually cook from it (call it).

## Related Terms

- [[glossary/def]]
- [[glossary/call]]

## Flashcard Q/A

**Front:** What is a function?

**Back:** A named, reusable block of code that runs when called.
