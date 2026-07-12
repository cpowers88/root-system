---
type: error-log
stage: 05
status: draft
tags: [stage-05, errors, debugging-preview]
---

# Stage 5 Common Errors

## 1. `IndexError` from going past the end of a list

```python
fruits = ["apple", "banana"]
print(fruits[2])
```

```text
IndexError: list index out of range
```

**Why it happens:** the list only has indices 0 and 1 — there's no index 2.

**Fix:** check the list's length with `len()` before indexing, or use a loop instead of a hardcoded index.

## 2. `KeyError` from a missing dictionary key

```python
student = {"name": "Chris"}
print(student["age"])
```

```text
KeyError: 'age'
```

**Why it happens:** `"age"` was never added as a key to this dictionary.

**Fix:** use `student.get("age", "unknown")` if the key might not exist, or check `if "age" in student:` first.

## 3. `TypeError` from modifying an immutable value

```python
name = "Chris"
name[0] = "J"
```

```text
TypeError: 'str' object does not support item assignment
```

**Why it happens:** strings (and tuples) are immutable — they can't be changed in place, only lists can.

**Fix:** build a new string instead: `name = "J" + name[1:]`.

## 4. Aliasing surprise — a list "changes on its own"

```python
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)   # [1, 2, 3, 4] — probably not what was expected
```

**No error message** — but unexpected behavior.

**Why it happens:** `copy = original` doesn't make a new list — both names point to the same one.

**Fix:** use `copy = original.copy()` or `copy = original[:]` to make an actual independent copy.

## How to Read Any of These

1. `IndexError` → check you're not indexing past the last valid position (remember, indices start at 0).
2. `KeyError` → check the key actually exists, or use `.get()` with a default.
3. `TypeError: ... does not support item assignment` → you're trying to modify something immutable (a string or tuple).
4. Unexpected shared changes with no error → suspect aliasing; check if you meant to copy a list instead of just assigning it.

## Related

- [[concepts/strings-as-sequences]]
- [[concepts/lists]]
- [[concepts/dictionaries]]
