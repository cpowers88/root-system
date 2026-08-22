---
type: concept
stage: 04
status: ready
source_refs: ["CSE 1321/1321L official syllabi: Python Libraries module", "Python docs tutorial/modules.txt: 6. Modules"]
prerequisites: ["defining-and-calling-functions"]
tags: [modules, standard-library]
timeline: reference
---

# Concept: Standard Library Basics

## Plain-English Meaning

Python ships with reusable modules called the **standard library**. An `import`
statement makes a module available, and dot notation calls something inside it:
`random.randint(...)` or `math.sqrt(...)`.

## What Problem This Solves

It prevents rewriting reliable tools Python already includes. It also teaches the
same function-call shape Chris already knows: `module.function(arguments)`.

## When To Use It

Use a standard-library module when the problem needs a common capability such as
random numbers, math functions, dates, paths, CSV files, or JSON.

## When Not To Use It

Do not install a third-party package when the standard library already solves the
problem. Packages and `pip` remain Stage 9 because dependency management is a
separate skill.

## Code Shape

```python
import module_name

result = module_name.function_name(argument)
```

## Tiny Working Example

```python
import random

roll = random.randint(1, 6)
print(f"You rolled {roll}.")
```

## Beginner Mistakes

- Forgetting the module prefix: `randint(...)` instead of `random.randint(...)`.
- Naming the script `random.py` or `math.py`, which can hide the real library
  module.
- Assuming `import` installs software. It only loads code already available;
  installing third-party packages is a later step.
- Using `from module import *`, which hides where names came from.

## Physical-World Anchor

The standard library is the toolbox supplied with Python. `import random` opens a
labeled drawer; `random.randint()` selects one tool from it.

## Required Vocabulary

- [[glossary/module]]
- [[glossary/import-statement]]
- [[glossary/standard-library]]

## Related Code Patterns

- [[code-patterns/import-and-call-standard-library]]

## Drill

- [[drills/stage-04-library-basics]]

## Explain-Back Questions

1. What does `import random` make available?
2. Why is the function called `random.randint()` instead of only `randint()`?
3. What is the difference between importing a standard-library module and
   installing a third-party package?

## Source Notes

- (sources: active CSE 1321 and CSE 1321L Fall 2026 Markdown syllabi, course schedule sections — Python Libraries follows functions and precedes tuples/lists)
- (source: `raw/DOCS/tutorial/modules.txt`, section 6, "Modules")
