---
type: concept
stage: 09
status: draft
source_refs: ["Automate the Boring Stuff Appendix A (Installing Third-Party Packages)", "Python Workout Ch.9 (Modules and Packages)"]
prerequisites: ["defining-and-calling-functions"]
tags: [stage-09, modules, packages, pip]
---

# Concept: Modules and Packages

## Plain-English Meaning

A **module** is a single `.py` file full of reusable code (functions, classes) that you can `import` into another program. A **package** is a published bundle of one or more modules that other people wrote, installed with `pip`.

## What Problem This Solves

Not everything needs to be written from scratch — Python's standard library and the wider package ecosystem already solve huge numbers of common problems (reading CSV files, working with dates, talking to spreadsheets). Modules and packages let you reuse that work instead of reinventing it.

## When To Use It

Anytime a problem matches something a standard library module or well-known third-party package already does well — date handling, file paths, CSV parsing, spreadsheet manipulation.

## When Not To Use It

Don't install a whole package for something trivially easy to write yourself in a couple of lines — that adds an unnecessary dependency. Check the standard library first; it ships with Python and needs no installation.

## Code Shape

```python
import module_name                 # standard library, built into Python
from module_name import thing       # import just one thing from a module

# third-party packages need installing first, from a terminal:
# pip install package_name
import package_name
```

## Tiny Working Example

```python
import csv   # standard library — no installation needed

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## Beginner Mistakes

- Trying to `import` a third-party package without installing it first (`pip install ...`) — raises `ModuleNotFoundError`.
- Confusing the package's *install* name with its *import* name — they're sometimes different (a common real-world example outside this vault's current sources, but worth knowing exists).
- Reinventing something the standard library already provides well — check `raw/docs/library/` or search before writing it from scratch.

## Physical-World Anchor

A module is like a toolbox someone else already built and labeled — instead of forging your own hammer, you open the box and use the one that's already there.

## Required Vocabulary

- [[glossary/module]]
- [[glossary/package]]
- [[glossary/pip]]

## Related Code Patterns

- (none new — `import` appears inside the patterns below, not as its own syntax pattern)

## Drill

- [[drills/stage-09-automation-practice]]

## Explain-Back Questions

1. What's the difference between a module and a package?
2. Why does importing a third-party package sometimes fail with `ModuleNotFoundError` even though the code looks correct?
3. Where should you check before writing a solution to a common problem from scratch?

## Source Notes

- (source: Automate the Boring Stuff, 3rd Ed., Appendix A, "Installing Third-Party Packages")
- (source: Python Workout, 2nd Ed., Ch.9, "Modules and Packages")
