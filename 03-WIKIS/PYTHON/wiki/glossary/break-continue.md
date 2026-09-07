---
type: glossary-entry
stage: 03
status: draft
aliases: ["break", "continue"]
related_terms: ["loop", "while-loop", "for-loop"]
timeline: reference
---

# `break` / `continue`

## Plain-English Definition

`break` immediately exits the loop entirely, skipping any remaining iterations. `continue` skips only the rest of the *current* pass and moves on to the next iteration.

## What Problem It Helps Solve

Lets a loop react to something mid-way through without finishing every planned iteration, or without acting on every single item.

## When Chris Will See It

Searching for something and stopping as soon as it's found (`break`); skipping invalid items but still processing the rest (`continue`).

## Code Example

```python
for n in range(10):
    if n == 5:
        break          # stop the loop entirely
    print(n)            # prints 0, 1, 2, 3, 4

for n in range(5):
    if n == 2:
        continue        # skip just this one pass
    print(n)            # prints 0, 1, 3, 4
```

## Common Confusion

`break` and `continue` are easy to mix up because they both involve "skipping" — `break` skips the *rest of the loop*, `continue` skips only the *rest of this one pass*.

## Physical-World Anchor

`break` is like leaving a line entirely once you've gotten what you came for. `continue` is like skipping your turn but staying in line for the next round.

## Related Terms

- [[glossary/while-loop]]
- [[glossary/for-loop]]

## Flashcard Q/A

**Front:** What's the difference between `break` and `continue`?

**Back:** `break` exits the loop entirely. `continue` skips the rest of the current pass but keeps looping.
