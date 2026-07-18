---
type: glossary-entry
timeline: reference
stage: 04
status: ready
aliases: [import]
related_terms: [module, standard-library]
---

# Import Statement

## Plain-English Definition

A Python statement that makes a module or a named part of a module available to the
current program.

## What Problem It Helps Solve

It lets a program reuse capabilities defined elsewhere instead of copying or
rewriting them.

## When Chris Will See It

Near the top of scripts that use modules: `import random`, `import math`, or later
`import csv`.

## Code Example

```python
import random

roll = random.randint(1, 6)
```

## Common Confusion

`import` does not install a third-party package. It makes code already available in
the current Python environment usable by the script.

## Physical-World Anchor

Opening a labeled drawer in an existing toolbox.

## Related Terms

- [[glossary/module]]
- [[glossary/standard-library]]

## Flashcard Q/A

**Front:** What does an import statement do?

**Back:** It makes a module or named part of a module available to the current program.
