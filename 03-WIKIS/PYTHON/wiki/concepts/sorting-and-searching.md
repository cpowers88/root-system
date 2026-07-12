---
type: concept
stage: 08
status: draft
source_refs: ["Grokking Algorithms Ch.2, Ch.4, Ch.5 (Selection Sort, Quicksort, Hash Tables)", "Think Python Ch.21"]
prerequisites: ["big-o-and-algorithm-efficiency", "lists", "dictionaries", "recursion"]
tags: [stage-08, sorting, searching, hash-tables]
---

# Concept: Sorting, Searching, and Hash Tables

## Plain-English Meaning

**Sorting** puts items in order. **Searching** finds whether (and where) a specific item exists. A **hash table** (Python's dictionary, under the hood) makes searching extremely fast by storing items at computed positions based on their key, instead of checking one by one.

## What Problem This Solves

Working with real data almost always involves finding something or putting things in a meaningful order — and *how* you do it has a huge effect on performance as data grows (this is exactly where Big O intuition pays off).

## When To Use It

Sort when order matters for display or further processing. Use linear search (`in`, or a loop) for small or unsorted data. Use a dictionary/set (hash table) when you need fast repeated lookups by key.

## When Not To Use It

Don't write your own sort or search algorithm for everyday code — Python's built-in `sorted()` and `in` are well-tested and fast. Writing them from scratch here is for understanding *how* they work, not for replacing the built-ins in real projects.

## Code Shape

```python
# Linear search — O(n), checks one at a time
def linear_search(items, target):
    for item in items:
        if item == target:
            return True
    return False

# Selection sort — O(n^2), repeatedly finds the smallest remaining item
def selection_sort(items):
    result = []
    remaining = items.copy()
    while remaining:
        smallest = min(remaining)
        result.append(smallest)
        remaining.remove(smallest)
    return result

# Hash table lookup — O(1) on average, using a dictionary
lookup = {"apple": 10, "banana": 5}
"apple" in lookup   # near-instant, regardless of how many items
```

## Tiny Working Example

```python
numbers = [5, 2, 8, 1]
print(selection_sort(numbers))     # [1, 2, 5, 8]
print(linear_search(numbers, 8))    # True
print(8 in {5: None, 2: None, 8: None})   # True — dictionary/set lookup, much faster at scale
```

## Beginner Mistakes

- Writing a linear search when the data is already in a dictionary or set — missing the much faster O(1) lookup that's already available.
- Implementing selection sort (or any sort) and forgetting to handle an already-sorted or empty list correctly.
- Confusing "sorted" with "searchable quickly" — a sorted list still needs `in` (linear) unless you use binary search specifically; a dictionary is fast for lookup regardless of order.

## Physical-World Anchor

Searching a messy pile of papers one by one (linear search) versus looking a name up in an alphabetized filing cabinet (closer to faster search) versus looking it up by a barcode scanner that jumps straight to the right shelf (hash table).

## Required Vocabulary

- [[glossary/sorting]]
- [[glossary/searching]]
- [[glossary/hash-table]]

## Related Code Patterns

- (none new — this concept applies loops, conditionals, and lists/dictionaries already learned)

## Drill

- [[drills/stage-08-algorithms-and-classes-practice]]

## Explain-Back Questions

1. Why is a dictionary lookup typically faster than searching through a list?
2. What does selection sort actually do, step by step, to put a list in order?
3. When would writing your own search or sort function make sense, versus using Python's built-ins?

## Source Notes

- (source: Grokking Algorithms, 2nd Ed., Ch.2 "Selection Sort," Ch.4 "Quicksort," Ch.5 "Hash Tables")
- (source: Think Python, 2nd Ed., Ch.21, "Analysis of Search Algorithms," "Hashtables")
