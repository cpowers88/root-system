---
type: concept
timeline: reference
status: draft
---

# Mass vs. Weight

## What is the physical idea?

**Mass** (kg) is the amount of matter in an object. It is an intrinsic property — it doesn't change based on location, gravity, or motion.

**Weight** (N) is the gravitational force on that mass. It depends on the local gravitational field: w = mg. Weight changes if you move to the Moon, orbit a planet, or go deep into space.

## What real-world situation does it describe?

- Your mass is the same on Earth, the Moon, and deep space: it's the 70 kg of stuff that makes you up.
- Your weight on Earth: 70 × 9.80 = 686 N downward.
- Your weight on the Moon (g ≈ 1.62 m/s²): 70 × 1.62 = 113 N. Much lighter, same mass.
- In the International Space Station, you are in free fall — you feel weightless (apparent weight = 0) but your mass and true gravitational weight are unchanged.

## Objects / System Involved

Any object. The concept applies universally.

## Quantities

| Quantity | Symbol | Unit | Changes with location? |
|---|---|---|---|
| Mass | m | kg | No |
| Weight | w | N | Yes (depends on g) |
| Gravitational acceleration | g | m/s² | Yes (9.80 near Earth surface, less on Moon, etc.) |

## Model or Equation

$$w = mg$$

Where g = 9.80 m/s² at Earth's surface (directed downward).

See [[../equations/weight]] for full detail.

## Calculus Connection

None. This is a direct proportionality.

## Diagram / Visual Model

```
MASS is fixed:             WEIGHT changes:
m = 70 kg everywhere       w = mg

Earth:  w = 70 × 9.80 = 686 N
Moon:   w = 70 × 1.62 = 113 N
Mars:   w = 70 × 3.72 = 260 N
Space:  apparent weight ≈ 0 (free fall)
```

## Common Beginner Mistake

Saying "the block weighs 5 kilograms." Weight is measured in newtons, not kilograms. Kilograms measure mass. "The block has mass 5 kg and weight 49 N" is correct.

A second mistake: using mass (kg) in a force equation when you need weight (N). If a problem gives you mass and asks about force, always multiply by g first.

## Practice Next

Every problem in Stage 5 requires converting mass (kg) to weight (N) via w = mg. Check [[../drills/newtons-second-law-drill]] Problem 3 (hanging mass) to practice this immediately.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 5.4, pp. 117–120.
