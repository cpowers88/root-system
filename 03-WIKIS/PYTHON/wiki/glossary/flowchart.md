---
type: glossary-entry
stage: 07
status: draft
aliases: []
related_terms: ["pseudocode", "branch"]
timeline: reference
---

# Flowchart

## Plain-English Definition

A diagram of a program's logic using shapes — rectangles for actions, diamonds for decisions/branches — connected by arrows showing the order of execution.

## What Problem It Helps Solve

Makes branching logic easier to see and check than a list of plain-English steps, especially when there are several decision points.

## When Chris Will See It

Planning anything with multiple decision points — a game, a multi-step form, anything that branches more than once or twice.

## Code Example

```text
[Start] -> <Is it raining?>
              /        \
            Yes          No
             |            |
       (Take umbrella) (Leave it)
             \           /
              [Go outside]
```

## Common Confusion

Each diamond in a flowchart corresponds directly to an `if`/`elif`/`else` in real code — if you can draw the diamonds clearly, you already know the conditional structure you'll need.

## Physical-World Anchor

A "choose your own adventure" map — each diamond is a fork, and arrows show exactly where each choice leads.

## Related Terms

- [[glossary/pseudocode]]
- [[glossary/branch]]

## Flashcard Q/A

**Front:** What shape represents a decision point in a flowchart?

**Back:** A diamond.
