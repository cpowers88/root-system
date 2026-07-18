---
type: flashcards
tags: [later, programming]
---

# Flashcard Batch: Stage 5 — Data Shapes

## Card: Array terminology bridge

**Front:** In this beginner Python path, what should I usually use when course material says "array"?

**Back:** A Python list, unless the material explicitly introduces a specialized array library such as NumPy.

**Tags:** python, stage-05, arrays, decision-rule

---

## Card: Index

**Front:** What index does the first item in a sequence have?

**Back:** 0 — indexing always starts at zero, not one.

**Tags:** python, stage-05, index

---

## Card: Slice boundary rule

**Front:** Does a slice `[start:stop]` include the item at the `stop` index?

**Back:** No — it includes everything from `start` up to, but not including, `stop`.

**Tags:** python, stage-05, slicing

---

## Card: Mutable vs Immutable

**Front:** What's the difference between mutable and immutable?

**Back:** Mutable values can be changed in place after creation (lists). Immutable values cannot — any change creates a new value (strings, tuples, numbers).

**Tags:** python, stage-05, decision-rule

---

## Card: List

**Front:** What is a list?

**Back:** An ordered, mutable collection of items, written in square brackets.

**Tags:** python, stage-05, lists

---

## Card: Aliasing

**Front:** Does `list_b = list_a` create a copy of the list?

**Back:** No — it makes `list_b` another name pointing to the exact same list. Changing one changes both.

**Tags:** python, stage-05, aliasing

---

## Card: Dictionary lookup

**Front:** How do you look something up in a dictionary?

**Back:** By its key, not by numeric position.

**Tags:** python, stage-05, dictionaries

---

## Card: Duplicate keys

**Front:** What happens if you assign a value to a key that already exists in a dictionary?

**Back:** It overwrites the old value under that key — dictionary keys are unique.

**Tags:** python, stage-05, dictionaries

---

## Card: Tuple vs list decision rule

**Front:** What's the key difference between a tuple and a list?

**Back:** A tuple is immutable (can't be changed after creation); a list is mutable.

**Tags:** python, stage-05, decision-rule

---

## Card: Empty set vs empty dict

**Front:** What does `{}` create — an empty set or an empty dictionary?

**Back:** An empty dictionary. Use `set()` to create an empty set.

**Tags:** python, stage-05, sets

---

## Card: List vs dictionary decision rule

**Front:** When should you use a dictionary instead of a list?

**Back:** When each item needs a meaningful label (key) instead of just a position — when you'd describe the data as "the X of Y."

**Tags:** python, stage-05, decision-rule
