---
type: concept
status: draft
---

# Relative Velocity

## What is the physical idea?

Velocity is always measured relative to some reference frame — the choice of what is "standing still." Two observers in different frames measure different velocities for the same object. The relative velocity equation lets you convert between frames.

## What real-world situation does it describe?

A swimmer crossing a river (swimming relative to water, but water moves relative to the bank). A plane flying in wind (plane moves relative to air, air moves relative to ground). A car passing another car on a highway — each driver measures the other's speed differently than someone standing on the roadside.

## Objects / System Involved

Three entities: an object P (the thing being tracked), reference frame A (e.g., the riverbank), and reference frame B (e.g., the water). You know two of the three velocities and want the third.

## Quantities That Change

Velocity vectors — direction and magnitude both depend on which frame is doing the measuring.

## Model or Equation

**Vector addition rule for relative velocity:**
```
v⃗_PA = v⃗_PB + v⃗_BA
```

Read as: "velocity of P relative to A equals velocity of P relative to B plus velocity of B relative to A."

**Subscript cancellation trick:** the inner subscripts (the repeated letter) cancel, leaving the outer subscripts.
```
v⃗_PA = v⃗_P[B] + v⃗_[B]A    →    inner B cancels
```

**Example (boat crossing river):**
- v⃗_boat/bank = v⃗_boat/water + v⃗_water/bank
- Boat points directly across; river current pushes downstream
- Use Pythagorean theorem for the resultant speed; use tan for the angle
- Time to cross depends only on the component perpendicular to current: t = width / v_boat/water
- Downstream drift = v_water/bank × t

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| v⃗_PA | velocity of P relative to A | m/s |
| v⃗_PB | velocity of P relative to B | m/s |
| v⃗_BA | velocity of B relative to A | m/s |

Note: v⃗_AB = -v⃗_BA (reversing the subscripts reverses the sign/direction).

## Calculus Connection

None new — this is vector addition, not calculus.

## Diagram / Visual Model

**Boat crossing river (boat aims straight across, current pushes right):**
```
       |   boat heading
       | ↑ (v_boat/water, perpendicular to bank)
       |/
       +——→ current (v_water/bank)
       |
 bank  |  bank
       
Resultant v_boat/bank = diagonal (hypotenuse of the triangle)
```

Draw the vector triangle: place v⃗_PB, then add v⃗_BA tip-to-tail; the resultant is v⃗_PA.

## Problem Types That Use This

Relative velocity problems appear whenever you see: boats, planes, swimmers, or cars described from two different reference points. Recognize the two frames and the object, then write the subscript equation.

## Common Beginner Mistake

Getting the subscript order wrong. Write out the full subscript equation first, check that inner subscripts cancel, then plug in magnitudes and directions. Do not skip the subscript step.

Also: forgetting that the time to cross a river depends only on the perpendicular component (aimed direction), not the total speed.

## Practice Next

After understanding the concept, do one boat-crossing and one plane-in-wind calculation before Stage 5 begins.

## Sources

- Serway & Jewett, 10th ed., Ch. 4.6, pp. 101–104.
