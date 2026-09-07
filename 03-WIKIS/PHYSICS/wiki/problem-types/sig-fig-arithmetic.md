---
type: problem-type
timeline: reference
status: draft
---

# Significant-Figure Arithmetic

## How to Recognize This Problem Type

A calculation combines two or more measured values (not exact counted numbers), and the problem asks for the result reported with the correct number of significant figures — or directly asks "how many significant figures does this number have?"

## Given Information Usually Present

Two or more measured numeric values, possibly with a stated operation (multiply, divide, add, subtract).

## Unknown Usually Requested

The final answer rounded to the correct number of significant figures (or decimal places, for addition/subtraction).

## Diagram to Draw

None.

## Equations Commonly Used

No physics equation — two arithmetic rules:
- Multiplication/division → match the *fewest sig figs* among inputs.
- Addition/subtraction → match the *fewest decimal places* among inputs.

## Step-by-Step Solving Pattern

1. Identify which operation is being performed (multiplication/division vs. addition/subtraction) — the rule depends entirely on this.
2. Count sig figs (for mult/div) or decimal places (for add/sub) in each input.
3. Perform the full calculation without rounding any intermediate step.
4. Round only the final answer to match the limiting input identified in step 2.

## Unit Checks

N/A — this problem type is about numeric precision, not units. (Still keep units attached to avoid losing track of the physical quantity.)

## Common Traps

- Applying the multiplication rule to an addition/subtraction problem, or vice versa — this is the single most common error.
- Rounding after each intermediate step instead of only at the end, which silently degrades accuracy.
- Treating trailing zeros with no decimal point (like 1500) as automatically significant — they're ambiguous without scientific notation.

## Practice Drills

- [[../drills/sig-fig-drill]]

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 1.6, Example 1.6, pp. 13–15.
