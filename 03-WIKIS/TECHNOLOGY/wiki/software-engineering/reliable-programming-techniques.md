---
domain: technology
type: concept
tags: [subject/code-quality, subject/software-engineering]
timeline: later
status: wiki-only
source_role: primary
use_cases: [tech-stack]
---

# Reliable Programming: Complexity, Design Patterns, Refactoring, Defensive Coding

**Summary**: Practical techniques for writing software that fails less
and is easier to change — complementary to, not overlapping with, the
existing `devops/` folder's IT-operations-level reliability content
(deployment pipelines, resilience engineering at the systems level). This
page is code-level, not systems-level.

**Sources**: EngineeringSoftwareProducts.pdf (Ian Sommerville, *Engineering
Software Products*, Pearson, 2020), Chapter 8

**Last updated**: 2026-07-13

---

## Program Complexity

More relationships between entities (functions, classes, variables) means
more places a bug can hide and more cost to change anything safely.
Complexity isn't just "long code" — it's the density of interconnection.
The techniques below are all, in different ways, complexity-reduction
tools.

## Design Patterns

Reusable solutions to recurring design problems, expressed as a relationship
between abstract and concrete classes rather than as literal code to copy.
The value isn't the specific pattern catalog — it's having a shared
vocabulary so a team can say "use a factory here" instead of re-explaining
the whole approach from scratch every time the same shape of problem
recurs.

## Refactoring

Restructuring existing code without changing its external behavior —
done in small, safe, test-verified steps rather than large rewrites. The
existing `devops/` deployment-pipeline pages already establish *why* small
batches matter at the systems level; refactoring is the same principle
applied inside a single codebase.

## Defensive Coding — Input Validation and Number Checking

Concrete, checkable habits: validate input format before trusting it
(regular expressions as the standard tool for structural validation —
e.g., is this string actually shaped like an email or phone number before
you use it as one), and explicitly check numeric inputs for type and
range rather than assuming a value that "looks numeric" is safe to
compute with directly.

## Exception Handling

The mechanism for separating the normal-case logic of a function from its
failure-case handling, rather than interleaving error checks into every
line of normal logic. Treated as a reliability discipline, not just a
language feature: an uncaught or overly-broad exception handler is itself
a reliability bug, since it can silently swallow failures that should have
stopped execution or surfaced to a human.

## Connects to

[[software-testing-levels-and-techniques]] — refactoring specifically
depends on having a test suite to verify behavior didn't change; the two
techniques are meant to be used together, not independently.
`03-WIKIS\TECHNOLOGY\wiki\devops\resilience-engineering-and-chaos-testing.md`
— the systems-level analog of this page's code-level reliability focus.

## North Star Connection

Directly applicable to any client-facing tool build under
`TECHNOLOGY_LIBRARY_STRATEGY.md` Category 9/12 — these are the specific
habits (input validation, exception handling, refactor-with-tests) that
separate a demo script from something maintainable on a retainer, which
is the explicit bar `flask-web-development.md`'s own North Star note
already sets for client tools.
