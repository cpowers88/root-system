---
type: concept
timeline: reference
status: draft
---

# Unit Conversion

## What is the physical idea?

The same physical quantity can be expressed in different units (meters vs. feet, m/s vs. mi/h). Converting between them means multiplying by a ratio that equals exactly 1 — so the *quantity* doesn't change, only its label.

## What real-world situation does it describe?

Reading a car speedometer in mi/h but needing m/s for a physics equation; comparing a US recipe in cups to a metric one in milliliters; any time data arrives in "the wrong" unit system for the calculation at hand.

## Objects / System Involved

N/A — applies to any measured quantity.

## Quantities That Change

The numerical value and unit label change; the physical quantity itself does not.

## Model or Equation

Multiply by a conversion factor written as a fraction equal to 1, arranged so the unwanted unit cancels:

```text
15.0 in. × (2.54 cm / 1 in.) = 38.1 cm
```

For compound units (like speed), convert each part separately:

```text
(38.0 m/s) × (1 mi / 1609 m) × (3600 s / 1 h) = 85.0 mi/h
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| (none — this is a method, not a formula with fixed symbols) | | depends on the quantity being converted |

## Calculus Connection

None.

## Diagram / Visual Model

Picture the unit you want to cancel sitting in a denominator, lining up against the same unit in the numerator of the previous step, so they cancel diagonally — like crossing out matching factors in a fraction.

## Problem Types That Use This

- [[../problem-types/unit-conversion]]

## Common Beginner Mistake

Writing the conversion ratio upside down (e.g., multiplying by 1 in./2.54 cm instead of 2.54 cm/1 in.), which leaves the wrong unit in place instead of canceling it. Always check: does the unit you don't want actually cancel out algebraically?

## Practice Next

Convert a few everyday quantities (your height, a speed limit, a recipe amount) between metric and US units by hand, writing out the cancellation explicitly — don't skip to the calculator.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 1.4, pp. 12.
