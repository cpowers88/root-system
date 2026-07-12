---
type: concept
stage: 08
status: draft
source_refs: ["Think Python Ch.15-17 (Programmer-Defined Types, Attributes, The init Method)", "Python Crash Course Ch.9", "Python Workout Ch.10"]
prerequisites: ["dictionaries", "defining-and-calling-functions"]
tags: [stage-08, classes, objects, oop]
---

# Concept: Classes and Objects

## Plain-English Meaning

A **class** is a blueprint for creating your own data type — it defines what **attributes** (data) and **methods** (functions that belong to it) every **instance** (a specific **object** built from that blueprint) will have. `__init__` is the special method that sets up a new instance's starting attributes.

## What Problem This Solves

A dictionary can group related data, but it can't bundle *behavior* (functions) together with that data. Classes let you package data and the actions that make sense for that data into one reusable blueprint.

## When To Use It

When you have a "thing" with both characteristics (data) and behaviors (actions) that naturally belong together — and you'll likely need more than one of that thing (multiple dogs, multiple cards, multiple players).

## When Not To Use It

If you just need to group a few related values with no associated behavior, a dictionary is simpler and sufficient (see [[concepts/choosing-a-data-structure]]). Don't reach for a class just because it feels more "advanced."

## Code Shape

```python
class ClassName:
    def __init__(self, parameter):
        self.attribute = parameter   # store data on this instance

    def method_name(self):
        # self gives access to this instance's own attributes
        return self.attribute

instance = ClassName(some_value)   # creates a new object
instance.method_name()               # call a method on it
```

## Tiny Working Example

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

fido = Dog("Fido")
print(fido.bark())   # "Fido says Woof!"
```

## Beginner Mistakes

- Forgetting `self` as the first parameter of every method — without it, Python has no way to know *which* instance's attributes the method should use, and calling the method raises a `TypeError`.
- Confusing a class itself with an instance of it — `Dog` is the blueprint; `fido` is one specific dog built from it. Two different `Dog` instances have completely separate attribute values.
- Forgetting `self.` when reading or setting an attribute inside a method (`name` instead of `self.name`) — this creates a regular local variable instead of accessing the instance's data.

## Physical-World Anchor

A class is a cookie cutter; each object is one cookie made from it. Every cookie shares the same shape (the methods), but each one can have its own decoration (its own attribute values).

## Required Vocabulary

- [[glossary/class]]
- [[glossary/object-instance]]
- [[glossary/attribute]]
- [[glossary/method]]

## Related Code Patterns

- [[code-patterns/class-with-init-and-method]]

## Drill

- [[drills/stage-08-algorithms-and-classes-practice]]

## Explain-Back Questions

1. What's the difference between a class and an instance (object)?
2. Why does every method need `self` as its first parameter?
3. If you create two `Dog` instances with different names, do they share the same `name` attribute value, or does each have its own?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.15, "Programmer-Defined Types," "Attributes"; Ch.17, "The init Method")
- (source: Python Crash Course, 3rd Ed., Ch.9, "Creating and Using a Class")
- (source: Python Workout, 2nd Ed., Ch.10, "Objects")
