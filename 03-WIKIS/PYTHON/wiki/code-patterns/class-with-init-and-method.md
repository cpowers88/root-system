---
type: code-pattern
stage: 08
status: draft
concepts: ["class", "object-instance", "attribute", "method"]
tags: [classes, oop]
timeline: reference
---

# Code Pattern: Class With `__init__` and a Method

## Purpose

Define a reusable blueprint for a "thing" that has both data (attributes) and behavior (methods), and create instances of it.

## Use This When

You have a concept with both characteristics and actions that belong together, and there will likely be more than one of it.

## Do Not Use This When

A dictionary with no associated behavior would do the job just as well — don't reach for a class purely for its own sake.

## Skeleton

```python
class ClassName:
    def __init__(self, parameter):
        self.attribute_name = parameter

    def method_name(self):
        return self.attribute_name

instance = ClassName(some_value)
instance.method_name()
```

## Filled Example

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old."

fido = Dog("Fido", 3)
print(fido.describe())   # "Fido is 3 years old."
```

## Step-by-Step Trace

1. `class Dog:` defines the blueprint.
2. `Dog("Fido", 3)` calls `__init__` automatically, with `self` bound to the new instance, `name` set to `"Fido"`, and `age` set to `3`.
3. Inside `__init__`, `self.name = name` and `self.age = age` store those values as attributes on this specific instance.
4. `fido.describe()` calls the method with `self` automatically bound to `fido`, so `self.name` and `self.age` refer to Fido's specific values.

## Beginner Mistakes

- Forgetting `self` as the first parameter of `__init__` or any method — causes a `TypeError` about the wrong number of arguments.
- Forgetting `self.` when setting or reading an attribute inside a method, accidentally creating an unrelated local variable instead.
- Defining `__init__` but forgetting to actually store the parameters as attributes (`self.name = name`), leaving the instance with no usable data afterward.

## Related Terms

- [[glossary/class]]
- [[glossary/object-instance]]
- [[glossary/attribute]]
- [[glossary/method]]

## Drill Link

- [[drills/stage-08-algorithms-and-classes-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-08-algorithms-and-classes]].
