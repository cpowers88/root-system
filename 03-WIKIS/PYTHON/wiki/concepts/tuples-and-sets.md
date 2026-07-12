---
type: concept
stage: 05
status: draft
source_refs: ["Think Python Ch.12 (Tuples Are Immutable, Tuple Assignment)", "Think Python Ch.19 (Sets, lighter intro)"]
prerequisites: ["lists"]
tags: [stage-05, tuples, sets]
---

# Concept: Tuples and Sets (Light Introduction)

## Plain-English Meaning

A **tuple** is like a list, but immutable — once created, it can't be changed. Written in parentheses: `(item1, item2)`. A **set** is an unordered collection with no duplicates, written in curly braces without keys: `{item1, item2}`.

## What Problem This Solves

Tuples are useful when a small, fixed group of values belongs together and shouldn't accidentally be modified (coordinates, RGB colors, a record that's "done"). Sets are useful when you only care about *whether* something is present, not its order or how many times it appears.

## When To Use It

Use a tuple for a fixed, small group of values that travel together and shouldn't change. Use a set when you need to check membership quickly or eliminate duplicates.

## When Not To Use It

If the collection needs to grow, shrink, or have items replaced, use a list, not a tuple. If order matters, don't use a set.

## Code Shape

```python
point = (3, 4)          # tuple — immutable
x, y = point              # tuple unpacking
unique_items = {1, 2, 2, 3}   # set — automatically becomes {1, 2, 3}
```

## Tiny Working Example

```python
coordinates = (10, 20)
x, y = coordinates
print(f"x={x}, y={y}")

seen = {"apple", "banana", "apple"}
print(seen)   # {"apple", "banana"} — duplicate removed automatically
```

## Beginner Mistakes

- Trying to modify a tuple like a list (`point[0] = 5`) — raises the same kind of `TypeError` as modifying a string.
- Forgetting that sets have no guaranteed order — printing one might not show items in the order you added them.
- Confusing an empty set (`set()`) with an empty dictionary (`{}`) — `{}` is actually an empty dictionary, not an empty set.

## Physical-World Anchor

A tuple is like a sealed envelope with a few fixed items inside — you can look, but you can't swap what's in it without opening a new envelope. A set is like a guest list where you only care who's on it, not the order they RSVP'd.

## Required Vocabulary

- [[glossary/tuple]]
- [[glossary/set]]

## Related Code Patterns

- (none yet at this depth — tuples/sets get light treatment in Stage 5; deeper use appears as needed in later stages)

## Drill

- [[drills/stage-05-data-structure-practice]]

## Explain-Back Questions

1. What's the key difference between a tuple and a list?
2. Why might you choose a set instead of a list to store a collection of items?
3. What does Python do automatically if you try to add a duplicate item to a set?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.12, "Tuples Are Immutable," "Tuple Assignment")
- (source: Think Python, 2nd Ed., Ch.19, "Sets" — light intro only, full chapter parked for Stage 10 per `wiki/parking-lot.md`)
