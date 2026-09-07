---
type: glossary-entry
stage: 08
status: draft
aliases: ["object", "instance"]
related_terms: ["class"]
timeline: reference
---

# Object / Instance

## Plain-English Definition

A specific thing built from a class's blueprint. "Object" and "instance" mean the same thing — each call to a class creates a new, independent instance.

## What Problem It Helps Solve

Lets a single class definition produce many separate, independently-tracked things, each with its own attribute values.

## When Chris Will See It

Any time a class is actually used: `fido = Dog("Fido")` creates one instance; `rex = Dog("Rex")` creates a completely separate one.

## Code Example

```python
fido = Dog("Fido")
rex = Dog("Rex")
print(fido.name)   # "Fido"
print(rex.name)    # "Rex" — separate, unaffected by fido
```

## Common Confusion

Changing one instance's attribute never affects another instance of the same class — each one has its own independent copy of the attributes defined in `__init__`.

## Physical-World Anchor

One specific cookie cut from the cookie-cutter blueprint — each cookie is separate, even though they share the same shape.

## Related Terms

- [[glossary/class]]

## Flashcard Q/A

**Front:** If you create two instances of the same class, do they share attribute values?

**Back:** No — each instance has its own independent set of attribute values.
