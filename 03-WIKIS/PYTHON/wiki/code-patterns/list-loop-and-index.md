---
type: code-pattern
stage: 05
status: draft
concepts: ["list", "index", "for-loop"]
tags: [stage-05, lists, loops]
---

# Code Pattern: Looping Over a List by Index or by Item

## Purpose

Visit every item in a list, either just to use the item's value, or when you also need to know its position.

## Use This When

You need to process every item in a list. Use the index version specifically when you need the position itself (to compare neighboring items, or to modify the list in place at that position).

## Do Not Use This When

You need to look something up by a meaningful label rather than position — that's a dictionary lookup instead (see [[code-patterns/dictionary-lookup]]).

## Skeleton

```python
# by item — when you just need the value
for item in my_list:
    # use item

# by index — when you need the position too
for i in range(len(my_list)):
    # use my_list[i] and i
```

## Filled Example

```python
scores = [85, 92, 78]

# by item
for score in scores:
    print(score)

# by index — needed here because we're modifying in place
for i in range(len(scores)):
    scores[i] = scores[i] + 5   # curve every score by 5
```

## Step-by-Step Trace

1. `for score in scores:` — each pass, `score` takes the next value from the list directly. Simple, but you don't know the position.
2. `for i in range(len(scores)):` — `i` takes each valid index (0, 1, 2 for a 3-item list).
3. `scores[i]` uses that index to read or write the item at that exact position.

## Beginner Mistakes

- Using `for item in my_list:` when you actually need to modify the list in place — `item` is just a copy of the value for that pass; reassigning `item` doesn't change the list.
- Using `range(len(my_list))` when a plain `for item in my_list:` would be simpler and the position isn't actually needed.
- Off-by-one from forgetting `range(len(my_list))` already produces valid indices (0 through `len-1`), matching the list exactly.

## Related Terms

- [[glossary/list]]
- [[glossary/index]]
- [[glossary/for-loop]]

## Drill Link

- [[drills/stage-05-data-structure-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-05-data-shapes]].
