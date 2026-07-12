---
type: glossary-entry
stage: 08
status: draft
aliases: []
related_terms: ["object-instance", "attribute", "method"]
---

# Class

## Plain-English Definition

A blueprint for creating your own data type — it defines what attributes and methods every object built from it will have.

## What Problem It Helps Solve

Lets you bundle related data and behavior (functions that act on that data) into one reusable definition, instead of keeping them separate.

## When Chris Will See It

Anywhere a "thing" needs both data and behavior, and there will likely be more than one of it: `Dog`, `Card`, `Player`.

## Code Example

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
```

## Common Confusion

The class itself (`Dog`) is the blueprint — it's not a dog you can use directly. You need to create an instance (`fido = Dog("Fido")`) before you have something you can actually call `.bark()` on.

## Physical-World Anchor

A cookie cutter — the shape that every cookie (object) made from it will share.

## Related Terms

- [[glossary/object-instance]]
- [[glossary/attribute]]
- [[glossary/method]]

## Flashcard Q/A

**Front:** What is a class?

**Back:** A blueprint for creating your own data type, defining what attributes and methods its objects will have.
