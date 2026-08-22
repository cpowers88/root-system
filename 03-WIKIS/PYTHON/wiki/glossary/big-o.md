---
type: glossary-entry
stage: 08
status: draft
aliases: ["Big O notation", "order of growth"]
related_terms: ["sorting", "searching"]
timeline: reference
---

# Big O

## Plain-English Definition

A way of describing how much more work an algorithm needs as its input gets bigger — the shape of the growth, not exact timing. Common levels: O(1) constant, O(n) linear, O(n²) quadratic.

## What Problem It Helps Solve

Lets you compare two approaches to the same problem and predict which will hold up better as the data grows, without needing to actually run and time both.

## When Chris Will See It

Comparing search/sort approaches, or spotting a nested loop over the same data as a possible performance red flag.

## Code Example

```python
my_list[0]                       # O(1) — same work regardless of size
for item in my_list: ...           # O(n) — work grows with size
for a in my_list:                  # O(n^2) — nested loop over the same data
    for b in my_list: ...
```

## Common Confusion

Big O describes how work *scales*, not the actual speed for any one specific input — a "slower" O(n²) algorithm might still beat a "faster" O(n) one on a very small list, but loses badly as the list grows large.

## Physical-World Anchor

Looking up a page by number (instant, O(1)) versus reading a whole book to find a word (O(n)) versus comparing every page to every other page (O(n²), painfully slow on a long book).

## Related Terms

- [[glossary/sorting]]
- [[glossary/searching]]

## Flashcard Q/A

**Front:** What's a common code shape that's a red flag for O(n²)?

**Back:** A loop nested inside another loop, both iterating over the same data.
