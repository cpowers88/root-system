---
type: concept
timeline: reference
status: draft
---

# Vertical Circular Motion

## What is the physical idea?

When an object moves in a vertical circle (ball on a string, roller coaster loop), gravity always points downward but the "inward" direction rotates as the object moves around the loop. At the top, "inward" means downward. At the bottom, "inward" means upward. This means the same gravity force helps the centripetal requirement at the top but opposes it at the bottom — so the required tension changes as the object moves around.

## What real-world situation does it describe?

- Ball swung on a string in a vertical plane.
- Roller coaster car going through a loop.
- Aircraft doing a loop.
- Object going over the top of a hill at speed.

## Objects / System Involved

An object of mass m moving in a circle of radius r in a vertical plane, subject to gravity (mg) and a contact force (tension T or normal force n).

## Quantities That Change

- The direction of "inward" rotates as the object moves.
- The required tension or normal force changes around the loop even if speed were constant.
- In reality, speed also changes (object speeds up going down, slows going up) — so both v and the contact force change.

## Model / Equation

Apply ΣF_inward = mv²/r at each position separately.

**At the TOP of the circle:**
Both gravity and tension point downward = inward toward center.
```
T + mg = mv²/r       (at top)
T = mv²/r - mg
```
Minimum speed at the top (string just barely taut, T = 0):
```
0 + mg = mv²_min/r   →   v_min = √(gr)
```
If v < √(gr) at the top, the string goes slack and circular motion fails.

**At the BOTTOM of the circle:**
Tension points upward (inward), gravity points downward (outward = away from center).
```
T - mg = mv²/r       (at bottom)
T = mv²/r + mg
```
The tension at the bottom is always greater than at the top (for same speed), because now tension must both provide centripetal force AND support the weight.

**At the TOP of a HILL (object on road, no string):**
Normal force n points upward (away from center, which is below the hill). Gravity mg points downward (toward center of the hill's arc).
```
mg - n = mv²/r       (top of hill)
n = mg - mv²/r = m(g - v²/r)
```
When v = √(gr), normal force = 0. The object leaves the road.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| T | tension in string | N |
| n | normal force | N |
| m | mass | kg |
| v | speed at that point | m/s |
| r | radius of circle | m |
| g | gravitational acceleration (9.80) | m/s² |

## Calculus Connection

None new. Speed at different points can be related using energy conservation (Stage 8) — that's how you find v at the top from v at the bottom without calculus.

## Diagram / Visual Model

```
        TOP
        [object]
        ↓ T  (tension, toward center = down)
        ↓ mg (gravity, also down)
        Center of circle is below object
        ΣF_down = T + mg = mv²/r


        BOTTOM
        Center of circle is above object
        ↑ T  (tension, toward center = up)
        ↓ mg (gravity, away from center = down)
        ΣF_up = T - mg = mv²/r
```

## Problem Types That Use This

- [[../problem-types/vertical-circular-motion]]

## Common Beginner Mistake

**Forgetting which direction is "inward" at each point.** At the top, inward is downward. At the bottom, inward is upward. Many students write ΣF = mv²/r and put all forces on the same side — you must think about which forces point toward the center and which point away.

**Using the same equation at every position.** Draw the FBD fresh at each position. The equation changes because "inward" changes direction.

**Forgetting that minimum speed occurs at the top**, not the bottom. The bottom has the largest tension (hardest on the string/track). The top has minimum tension and is where the object most risks losing contact.

## Practice Next

Apply these equations to the loop problems in [[../problem-types/vertical-circular-motion]].

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 6.2, pp. 133–137.
