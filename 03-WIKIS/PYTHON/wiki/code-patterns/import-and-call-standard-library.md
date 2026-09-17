---
type: code-pattern
stage: 04
status: ready
concepts: [module, import-statement, standard-library, function-call]
tags: [standard-library, import]
timeline: reference
---

# Code Pattern: Import and Call a Standard-Library Function

## Purpose

Use a capability that ships with Python without rewriting it.

## Use This When

The standard library already provides the needed operation and the module is known.

## Do Not Use This When

The operation is a tiny expression Chris can already write clearly, or the proposed
tool is a third-party package that would need installation and dependency checks.

## Skeleton

```python
import module_name

result = module_name.function_name(argument)
```

## Filled Example

```python
import math

distance = 81
root = math.sqrt(distance)
print(root)
```

## Step-by-Step Trace

1. `import math` makes the module name available.
2. `math.sqrt` selects the `sqrt` function inside that module.
3. The argument `distance` is passed into the function.
4. The returned value is stored in `root` and then printed.

## Beginner Mistakes

- Omitting `math.` from the function call.
- Writing `math = 5` and overwriting the module name.
- Naming the current file `math.py`.
- Confusing `import` with `pip install`.

## Related Terms

- [[glossary/module]]
- [[glossary/import-statement]]
- [[glossary/standard-library]]

## Drill Link

- [[drills/stage-04-library-basics]]

## Flashcards

- [[flashcards/stage-04-library-basics]]
