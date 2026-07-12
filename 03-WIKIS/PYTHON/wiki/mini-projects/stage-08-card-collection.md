---
type: mini-project
stage: 08
status: draft
concepts: ["class", "object-instance", "attribute", "method", "sorting", "searching", "big-o"]
solution_included: false
---

# Mini-Project: Card Collection — Class Plus Sort/Search

## User Story

As a learner, I want to build a small `Card` class and then sort and search a list of card instances using algorithms I write myself, so that I can prove I understand both basic OOP and how sorting/searching actually work under the hood.

## Required Concepts

- [[glossary/class]]
- [[glossary/object-instance]]
- [[glossary/attribute]]
- [[glossary/method]]
- [[glossary/sorting]]
- [[glossary/searching]]
- [[glossary/big-o]]

## Build Phases

### Phase 1 — Build the `Card` Class

Write a `Card` class with `__init__(self, rank, suit)` (e.g., rank as a number 2-14, suit as a string) and a method `describe(self)` that returns something like `"Queen of Hearts"` (you can map rank numbers to names like Jack/Queen/King/Ace inside the method, or keep it simple with just numbers — your choice). Create a list of 8-10 `Card` instances with varied ranks.

### Phase 2 — Sort From Scratch

Write your own `selection_sort_cards(cards)` function (no built-in `sorted()` allowed for this phase) that sorts the list of `Card` instances by rank, lowest to highest. You'll need to compare `card.rank` values, not the `Card` objects directly.

### Phase 3 — Search From Scratch

Write your own `linear_search_cards(cards, target_rank)` function that returns the first `Card` instance matching `target_rank`, or `None` if not found. Test it against both a rank that exists and one that doesn't.

## Acceptance Checklist

- [ ] `Card` class has at least two attributes (rank, suit) and one working method.
- [ ] `selection_sort_cards()` correctly sorts the list by rank without using `sorted()` or `.sort()`.
- [ ] `linear_search_cards()` correctly finds an existing rank and correctly returns `None` for a missing one.
- [ ] Chris can state, out loud, the Big O of both the sort and the search written here.
- [ ] Chris can explain what would change (in code and in Big O) if Python's built-in `sorted()` were used instead of the hand-written version.

## Stretch Goals — Parked

- A full `Deck` class that manages the whole list of cards as one object (a direct preview of Think Python Ch.18's case study) — parked, since deep inheritance/multi-class design is beyond Stage 8's scope.
- Binary search instead of linear search (requires the list to already be sorted, and a recursive or iterative halving approach) — a good Stage 8 stretch if Chris wants to push further, but not required.

## Reflection Questions

1. Why did `selection_sort_cards()` need to compare `card.rank` instead of comparing `Card` objects directly?
2. What's the Big O of `selection_sort_cards()`, and what's the Big O of `linear_search_cards()`? Are they the same?
3. If this collection grew to 10,000 cards instead of 10, which function would you be most worried about, and why?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
