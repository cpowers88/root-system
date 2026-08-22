---
type: concept
timeline: reference
status: draft
---

# Significant Figures

## What is the physical idea?

Every measurement has limited precision. The number of **significant figures** in a reported value communicates how precisely that value is actually known — reporting more digits than you actually measured is misleading, not "more accurate."

## What real-world situation does it describe?

Reading a length off a meter stick to the nearest tenth of a centimeter; reporting a calculated area or speed without pretending your calculator's 10-digit display is all meaningful.

## Objects / System Involved

N/A — applies to any reported numeric result.

## Quantities That Change

N/A.

## Model or Equation

No equation — two arithmetic rules:

- **Multiplication/division:** the result keeps as many significant figures as the *least precise* input.
- **Addition/subtraction:** the result keeps as many *decimal places* as the input with the fewest decimal places.

Rounding rule: if the dropped digit is >5, round up; if <5, round down; if exactly 5, round to the nearest even digit.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| (none) | | |

## Calculus Connection

None.

## Diagram / Visual Model

No diagram. Mental model: significant figures are like the "weakest link in a chain" — your final answer can only be as precise as your least precise input measurement.

## Problem Types That Use This

- [[../problem-types/sig-fig-arithmetic]]

## Common Beginner Mistake

Using the multiplication/division rule (count sig figs) when the operation is actually addition/subtraction (count decimal places instead) — these are two different rules and the most common error in this chapter. Also: rounding intermediate steps instead of waiting until the final answer, which causes small errors to compound.

## Practice Next

Take a measured rectangle's length and width (different numbers of sig figs each) and calculate its area with the correct number of significant figures, showing why.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 1.6, pp. 13–15.
