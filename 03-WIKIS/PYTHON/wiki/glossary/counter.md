---
type: glossary-entry
stage: 03
status: draft
aliases: []
related_terms: ["accumulator", "loop"]
---

# Counter

## Plain-English Definition

A variable that tracks how many times something has happened, usually increasing by 1 each time.

## What Problem It Helps Solve

Lets a program answer "how many?" — how many guesses were made, how many matches were found.

## When Chris Will See It

Inside loops where you need a running count of something.

## Code Example

```python
matches = 0
for word in words:
    if word == target:
        matches = matches + 1
```

## Common Confusion

A counter must be created with a starting value (usually `0`) **before** the loop begins — creating it inside the loop resets it every pass.

## Physical-World Anchor

A turnstile clicker that counts how many people walked through — it starts at zero and only goes up.

## Related Terms

- [[glossary/accumulator]]

## Flashcard Q/A

**Front:** Where must a counter be initialized — inside or before the loop?

**Back:** Before the loop. Initializing it inside the loop resets it every pass.
