---
type: flashcards
tags: [later, programming]
---

# Flashcard Batch: Stage 8 — Algorithms and Data Structures

## Card: Recursion essentials

**Front:** What are the two essential parts of any correctly-written recursive function?

**Back:** A base case (a simple version answered directly) and a recursive call that moves toward that base case.

**Tags:** python, stage-08, recursion

---

## Card: Base case failure

**Front:** What happens if a recursive function's base case is never actually reached?

**Back:** Infinite recursion — the function keeps calling itself until Python raises a RecursionError.

**Tags:** python, stage-08, decision-rule

---

## Card: Class

**Front:** What is a class?

**Back:** A blueprint for creating your own data type, defining what attributes and methods its objects will have.

**Tags:** python, stage-08, classes

---

## Card: Instances are independent

**Front:** If you create two instances of the same class, do they share attribute values?

**Back:** No — each instance has its own independent set of attribute values.

**Tags:** python, stage-08, objects

---

## Card: self in method definitions vs calls

**Front:** Do you write `self` when calling a method, or only when defining it?

**Back:** Only when defining it. Python passes the instance as `self` automatically at the call site.

**Tags:** python, stage-08, decision-rule

---

## Card: Big O red flag

**Front:** What's a common code shape that's a red flag for O(n²)?

**Back:** A loop nested inside another loop, both iterating over the same data.

**Tags:** python, stage-08, big-o

---

## Card: Writing your own sort

**Front:** Should you write your own sort algorithm for everyday Python code?

**Back:** No — use the built-in `sorted()`. Writing one yourself is for understanding the algorithm, not for production use.

**Tags:** python, stage-08, decision-rule

---

## Card: Dictionary lookup speed

**Front:** Why is searching a dictionary or set usually faster than searching a list?

**Back:** A dictionary/set uses a hash table, which can jump near-directly to where an item would be, instead of checking every item one by one like a list does.

**Tags:** python, stage-08, hash-tables

---

## Card: List vs class decision rule

**Front:** When should you use a class instead of a dictionary to group related data?

**Back:** When the data also needs associated behavior (methods) and you'll likely need multiple independent instances of it.

**Tags:** python, stage-08, decision-rule
