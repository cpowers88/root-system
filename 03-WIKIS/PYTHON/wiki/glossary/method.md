---
type: glossary-entry
stage: 08
status: draft
aliases: []
related_terms: ["class", "function"]
---

# Method

## Plain-English Definition

A function that belongs to a class, defined inside it, that operates on a specific instance's data (via `self`).

## What Problem It Helps Solve

Lets the actions associated with a type of object live right alongside that object's data, instead of as separate, disconnected functions.

## When Chris Will See It

Defined inside a `class` block, always with `self` as the first parameter; called with dot notation: `instance.method_name()`.

## Code Example

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):     # this is a method
        return f"{self.name} says Woof!"

fido = Dog("Fido")
print(fido.bark())
```

## Common Confusion

Calling a method without `self` being passed explicitly is normal — Python passes the instance (`fido`) as `self` automatically when you write `fido.bark()`. You never type `self` at the call site, only in the method's definition.

## Physical-World Anchor

An action a cookie "knows how to do" because of its shape (class) — every cookie cut from the same cutter can perform the same actions, each on its own decoration (data).

## Related Terms

- [[glossary/class]]
- [[glossary/function]]

## Flashcard Q/A

**Front:** Do you write `self` when calling a method, or only when defining it?

**Back:** Only when defining it. Python passes the instance as `self` automatically at the call site.
