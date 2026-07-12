---
type: glossary-entry
stage: 03
status: draft
aliases: ["iterable"]
related_terms: ["loop", "for-loop"]
---

# Iteration / Iterable

## Plain-English Definition

**Iteration** is one single pass through a loop's body. An **iterable** is anything you can loop over item-by-item — a string, a `range()`, and later, a list or dictionary.

## What Problem It Helps Solve

Gives a precise word for "one repetition" (iteration) and for "things you're allowed to loop over" (iterable), so the rules of `for` loops can be described exactly.

## When Chris Will See It

"Iteration" comes up when discussing how many times a loop ran. "Iterable" comes up whenever explaining what a `for` loop can sit in front of (`for x in <iterable>:`).

## Code Example

```python
for letter in "Py":   # "Py" is the iterable; this loop runs 2 iterations
    print(letter)
```

## Common Confusion

Not everything is iterable — a plain integer (`for x in 5:`) raises a `TypeError`, because a single number isn't a sequence of items to step through.

## Physical-World Anchor

An iterable is like a deck of cards; iterating is dealing one card at a time until the deck is empty.

## Related Terms

- [[glossary/loop]]
- [[glossary/for-loop]]

## Flashcard Q/A

**Front:** What is an "iterable"?

**Back:** Anything you can loop over item-by-item, like a string or a range() — the thing a for loop steps through.
