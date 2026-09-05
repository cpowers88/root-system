---
type: glossary-entry
stage: 08
status: draft
aliases: []
related_terms: ["class", "object-instance"]
timeline: reference
---

# Attribute

## Plain-English Definition

A piece of data stored on an object, accessed with dot notation (`object.attribute_name`).

## What Problem It Helps Solve

Lets each instance of a class hold its own data — the actual values that make one `Dog` different from another.

## When Chris Will See It

Set inside `__init__` with `self.attribute_name = value`, and read elsewhere with `instance.attribute_name`.

## Code Example

```python
class Dog:
    def __init__(self, name):
        self.name = name   # "name" is an attribute

fido = Dog("Fido")
print(fido.name)   # "Fido"
```

## Common Confusion

Inside a method, you must write `self.name`, not just `name`, to access the attribute — writing `name` alone creates an unrelated local variable instead.

## Physical-World Anchor

A specific cookie's decoration — the cutter (class) is the same for every cookie, but each cookie's decoration (attribute values) can differ.

## Related Terms

- [[glossary/class]]
- [[glossary/object-instance]]

## Flashcard Q/A

**Front:** How do you access an attribute on an object?

**Back:** With dot notation: `object.attribute_name`.
