---
type: concept
stage: 05
status: draft
source_refs: ["Think Python Ch.10 (A List Is a Sequence, Lists Are Mutable, Traversing a List, List Slices, List Methods, Aliasing)", "Python Crash Course Ch.3-4", "Automate the Boring Stuff Ch.6"]
prerequisites: ["strings-as-sequences", "for-loops"]
tags: [lists, mutability, aliasing]
timeline: reference
---

# Concept: Lists

## Plain-English Meaning

A **list** is an ordered collection of items, written in square brackets, that you can change after creating it — add to it, remove from it, or modify items in place. Unlike strings, lists are **mutable**.

## What Problem This Solves

Lets a program store and work with a whole group of related values — names, scores, items — as one thing, instead of needing a separate variable for each one.

## When To Use It

Whenever you have an ordered collection of similar items and need to add/remove/change them, or loop over all of them.

## When Not To Use It

If each piece of data needs a meaningful label rather than a position (a person's name vs. their age), a dictionary is usually the better fit (see [[concepts/dictionaries]]). If the collection should never change after creation, a tuple may be more appropriate (see [[concepts/tuples-and-sets]]).

## Code Shape

```python
my_list = [item1, item2, item3]
my_list[0]            # access by index
my_list.append(item)  # add to the end
my_list[0] = new_item # modify in place — lists allow this, strings don't
for item in my_list:
    # loop over every item
```

## Tiny Working Example

```python
scores = [85, 92, 78]
scores.append(100)
scores[0] = 90
for s in scores:
    print(s)
```

## Beginner Mistakes

- Indexing past the end of the list — `IndexError: list index out of range`.
- Assuming `new_list = old_list` makes a copy — it doesn't; both names point to the *same* list (this is called **aliasing**), so changing one changes the other.
- Forgetting that lists are mutable while strings aren't, and trying to apply string habits to lists or vice versa.

## Physical-World Anchor

A list is like a numbered shelf of bins — you can look in bin 0, swap out what's in bin 2, or add a new bin at the end. The shelf itself can be rearranged, unlike a string's fixed row of mailboxes.

## Required Vocabulary

- [[glossary/list]]
- [[glossary/mutable-immutable]]
- [[glossary/aliasing]]

## Related Code Patterns

- [[code-patterns/list-loop-and-index]]

## Drill

- [[drills/stage-05-data-structure-practice]]

## Explain-Back Questions

1. What's the difference between a list and a string in terms of whether you can change them in place?
2. What happens if you write `list_b = list_a` and then change `list_b` — does `list_a` change too? Why?
3. What error do you get from indexing past the end of a list, and how would you avoid it?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.10, "A List Is a Sequence," "Lists Are Mutable," "Traversing a List," "List Slices," "List Methods," "Aliasing")
- (source: Python Crash Course, 3rd Ed., Ch.3-4)
- (source: Automate the Boring Stuff, 3rd Ed., Ch.6)
