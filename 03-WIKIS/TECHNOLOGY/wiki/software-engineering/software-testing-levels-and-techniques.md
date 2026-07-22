---
domain: technology
type: concept
tags: [subject/testing, subject/software-engineering]
timeline: later
status: wiki-only
source_role: primary
use_cases: [tech-stack]
---

# Software Testing: Unit, Feature, System/Release, and Risk-Based Testing

**Summary**: The four levels of testing a product actually needs, and how
to decide what to prioritize testing for when there's no time to test
everything. A genuinely uncovered topic in this wiki — the `devops/`
folder covers deployment pipelines and continuous delivery conceptually,
but not testing technique itself.

**Sources**: EngineeringSoftwareProducts.pdf (Ian Sommerville, *Engineering
Software Products*, Pearson, 2020), Chapter 9

**Last updated**: 2026-07-13

---

## The Four Levels

- **Unit testing** — the smallest scope: a single function, method, or
  class, tested in isolation. Fast, cheap, and the foundation everything
  else builds on — this is what "test automation" in the Scrum sprint
  cycle ([[agile-software-engineering-and-scrum]]) primarily refers to.
- **Feature testing** — does a complete feature (e.g., the "New Group"
  example from [[personas-scenarios-and-user-stories]]) work end-to-end
  as a user would actually use it, not just as isolated units.
- **System and release testing** — the whole product, integrated,
  checked before it goes out the door. This is where cross-feature
  interaction problems surface that unit and feature tests, by design,
  can't catch.

## Risk-Based Testing

When there isn't time or budget to exhaustively test everything (the
normal case), prioritize testing effort by risk: what's the cost if this
specific thing breaks in production, and how likely is it to break?
High-risk, high-likelihood areas (e.g., payment handling, data loss paths)
get disproportionate testing attention over low-risk, rarely-touched
code. This is a direct application of the same risk-prioritization logic
`AGENT.md`'s own Agent Evaluation Gate already uses for AI-workflow
testing (scale test cases to what a workflow actually introduces) —
independent confirmation that risk-scaled testing effort is a general
principle, not an AI-specific one.

## Connects to

[[reliable-programming-techniques]] — refactoring safely depends on the
unit-test layer described here. [[agile-software-engineering-and-scrum]]
— Scrum's "test automation" sprint rule is this page's unit-testing level
in practice.

## North Star Connection

For any client-facing tool build (`TECHNOLOGY_LIBRARY_STRATEGY.md`
Category 9/12): risk-based testing is the practical answer to "how much
testing is enough" for a small retainer-maintained tool — don't aim for
exhaustive coverage, aim coverage at whatever would actually hurt a
client if it broke (data loss, wrong numbers on an invoice) over
cosmetic edge cases.
