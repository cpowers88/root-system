---
type: concept
stage: 08
status: draft
source_refs: ["Think Python Ch.21 (Order of Growth)", "Data Structures & Algorithms Ch.1-3 (Big O Notation, code language unconfirmed)", "Grokking Algorithms Ch.1"]
prerequisites: ["for-loops", "lists"]
tags: [big-o, efficiency]
timeline: reference
---

# Concept: Big O Notation (Intuition Level)

## Plain-English Meaning

**Big O** describes, roughly, how much *more* work an algorithm needs as the input gets bigger — not exact timing, just the shape of the growth. The most common ones at this level: **O(1)** (constant — same work regardless of size), **O(n)** (linear — work grows directly with size), **O(n²)** (quadratic — work grows much faster, often from nested loops over the same data).

## What Problem This Solves

Two different approaches to the same problem can have wildly different performance as the data grows. Big O gives a common language for comparing "will this still be fast with 10,000 items, or will it crawl?" without needing to actually run both and time them.

## When To Use It

When choosing between two approaches to a problem, especially anything involving a loop over a loop (nested loops are a common O(n²) red flag), or comparing list search methods.

## When Not To Use It

Don't over-optimize tiny, one-time scripts where performance genuinely doesn't matter — Big O thinking matters most when data could grow large or code runs repeatedly.

## Code Shape

```python
# O(1) — constant time, regardless of list size
first_item = my_list[0]

# O(n) — linear time, one pass through the list
for item in my_list:
    print(item)

# O(n^2) — quadratic time, a loop inside a loop over the same data
for item in my_list:
    for other_item in my_list:
        compare(item, other_item)
```

## Tiny Working Example

```python
def has_duplicate_slow(items):       # O(n^2) — nested loop
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                return True
    return False

def has_duplicate_fast(items):       # O(n) — single pass using a set
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False
```

## Beginner Mistakes

- Assuming "fewer lines of code" means "faster" — a short nested loop can be much slower than a longer single-pass solution as data grows.
- Confusing "it works fine on my small test list" with "it'll scale" — Big O is specifically about what happens as the input gets *big*, which a small test won't reveal.
- Trying to memorize exact definitions instead of building the intuition: "does this have a loop inside a loop over the same data? That's a red flag for O(n²)."

## Physical-World Anchor

Looking up one specific page in a book by its page number (O(1), instant) versus reading every page to find a specific word (O(n), scales with book length) versus comparing every page to every other page (O(n²), gets painfully slow fast).

## Required Vocabulary

- [[glossary/big-o]]

## Related Code Patterns

- (none — this is an analysis skill applied to code already written, not a new syntax pattern)

## Drill

- [[drills/stage-08-algorithms-and-classes-practice]]

## Explain-Back Questions

1. What's the difference, intuitively, between O(1), O(n), and O(n²)?
2. What's a common code shape that's a red flag for O(n²)?
3. Why might a "shorter" piece of code actually be slower than a "longer" one as data grows?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.21, "Order of Growth")
- (source: A Common-Sense Guide to Data Structures and Algorithms, 2nd Ed., Ch.1-3, "Why Algorithms Matter," "O Yes! Big O Notation" — code language unconfirmed, used here for conceptual explanation only)
- (source: Grokking Algorithms, 2nd Ed., Ch.1, "Introduction to Algorithms")
