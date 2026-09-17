---
type: worked-example
timeline: reference
status: draft
---

# Is He Speeding? (Unit Conversion Worked Example)

## Problem Statement

On a highway in Wyoming, a car travels at 38.0 m/s. Is the driver exceeding a 75.0 mi/h speed limit?

## Problem Type

[[../problem-types/unit-conversion]]

## Given

Speed = 38.0 m/s. Speed limit = 75.0 mi/h.

## Unknown

The car's speed in mi/h, compared to the limit.

## Diagram

None needed — this is a unit-conversion problem, not a motion diagram.

## Model / Equation Choice

No physics model — pure unit conversion using two conversion factors (length and time) since speed is a compound unit.

## Solution Steps

```text
(38.0 m/s) × (1 mi / 1609 m) × (60 s / 1 min) × (60 min / 1 h)
= (38.0 m/s) × (1 mi / 1609 m) × (3600 s / 1 h)
= 85.0 mi/h
```

## Units Check

m/s × (mi/m) × (s/h) → the meters cancel, the seconds cancel, leaving mi/h. ✓

## Final Answer

85.0 mi/h — yes, the driver is exceeding the 75.0 mi/h limit.

## Explain-Back Prompt

Explain out loud: why do we multiply by 1 mi/1609 m instead of 1609 m/1 mi? What would happen to the units if we used the upside-down version by mistake?

## Common Trap

Forgetting to convert *both* parts of the compound unit (length and time) — converting only meters to miles but leaving seconds unconverted gives a meaningless mixed unit.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 1.4, Example 1.4, p. 12.
