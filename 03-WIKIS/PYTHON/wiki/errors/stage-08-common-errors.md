---
type: error-log
stage: 08
status: draft
tags: [errors, debugging-preview]
timeline: reference
---

# Stage 8 Common Errors

## 1. `RecursionError` from a missing or unreachable base case

```python
def countdown(n):
    print(n)
    countdown(n - 1)   # no base case at all!
```

```text
RecursionError: maximum recursion depth exceeded
```

**Why it happens:** there's no base case to stop the recursion, so it keeps calling itself until Python's recursion limit is hit.

**Fix:** add a base case that's actually reachable, and confirm each recursive call moves the input toward it.

## 2. `TypeError` from forgetting `self`

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark():            # missing self!
        return "Woof!"

fido = Dog("Fido")
fido.bark()
```

```text
TypeError: bark() takes 0 positional arguments but 1 was given
```

**Why it happens:** Python automatically passes the instance as the first argument when you call `fido.bark()` — the method definition must have a parameter (conventionally named `self`) to receive it.

**Fix:** add `self` as the first parameter of every method, including `__init__`.

## 3. `AttributeError` from a typo or missing attribute

```python
class Dog:
    def __init__(self, name):
        self.name = name

fido = Dog("Fido")
print(fido.naem)   # typo
```

```text
AttributeError: 'Dog' object has no attribute 'naem'
```

**Why it happens:** the attribute name doesn't match exactly what was set in `__init__` — often a typo.

**Fix:** double-check the spelling matches exactly what was assigned with `self.attribute_name = ...`.

## 4. Forgetting `self.` inside a method

```python
class Dog:
    def __init__(self, name):
        name = name   # BUG: should be self.name = name
```

**No error** — but `fido.name` later raises an `AttributeError`, because the attribute was never actually stored on the instance.

**Why it happens:** `name = name` just creates a local variable inside `__init__` that disappears when the method ends — it never touches `self`.

**Fix:** always use `self.attribute_name = value` to actually store data on the instance.

## How to Read Any of These

1. `RecursionError` → check the base case exists and is reachable.
2. `TypeError` mentioning argument counts on a method call → check `self` is present in the method's definition.
3. `AttributeError` → check spelling, and check the attribute was actually set with `self.` inside `__init__`.

## Related

- [[concepts/recursion]]
- [[concepts/classes-and-objects]]
