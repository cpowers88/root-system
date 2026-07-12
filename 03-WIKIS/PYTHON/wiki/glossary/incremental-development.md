---
type: glossary-entry
stage: 07
status: draft
aliases: []
related_terms: ["test-case", "decomposition"]
---

# Incremental Development

## Plain-English Definition

Building a program one small, working piece at a time, testing each piece before adding the next.

## What Problem It Helps Solve

If you write a whole multi-step program before running any of it, a bug could be hiding anywhere in dozens of new lines. Building incrementally means a new bug is almost always in the one small piece you just added.

## When Chris Will See It

Anywhere a decomposed plan (see [[glossary/decomposition]]) is being turned into actual code — build and confirm step 1, then step 2, then step 3.

## Code Example

```python
# Confirm step 1 works before adding step 2:
import random
word = random.choice(["python", "stage"])
print(word)   # check this works first

# Only then add step 2, and re-run to confirm both work together:
guesses = []
print(guesses)
```

## Common Confusion

Incremental development feels slower at first because you're running the program many more times — but it's almost always faster overall, because each bug is isolated to a tiny, recently-added piece instead of buried in a large block.

## Physical-World Anchor

Following LEGO instructions one step at a time, checking each step against the picture, instead of dumping out all the pieces and guessing the final shape.

## Related Terms

- [[glossary/test-case]]
- [[glossary/decomposition]]

## Flashcard Q/A

**Front:** Why does building incrementally make debugging easier?

**Back:** Because any new bug is almost always in the one small piece you just added, instead of hidden somewhere in a large block of untested code.
