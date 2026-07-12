---
type: concept
status: draft
---

# Centripetal Force

## What is the physical idea?

Any object moving in a circle is continuously changing direction. Changing direction means changing velocity — and changing velocity means acceleration. That acceleration always points toward the center of the circle (inward). By Newton's second law, an inward acceleration requires an inward net force. That required inward net force is called the **centripetal force**.

Centripetal force is not a new type of force. It is a *role* played by whatever real forces happen to be available: tension, gravity, friction, normal force, or some combination.

## What real-world situation does it describe?

- A car rounding a curve: friction from the road provides the centripetal force.
- A satellite orbiting Earth: gravity provides the centripetal force.
- A ball swung on a string: string tension provides the centripetal force.
- A roller coaster loop: normal force (and gravity) provide the centripetal force.

## Objects / System Involved

Any object constrained to move in a circular path.

## Quantities That Change

- Velocity direction changes continuously (even if speed is constant).
- Centripetal acceleration magnitude stays constant if speed and radius are constant.

## Model / Equation

From Newton's second law (ΣF = ma), applied to the inward (centripetal) direction:

```
ΣF_c = mv²/r
```

where the left side is the **net** force pointing toward the center.

The centripetal acceleration itself:
```
a_c = v²/r     (directed inward, toward center)
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| ΣF_c | net centripetal (inward) force | N |
| m | mass of object | kg |
| v | speed of object | m/s |
| r | radius of circular path | m |
| a_c | centripetal acceleration | m/s² |

## Calculus Connection

None new in this stage. Centripetal acceleration is derived from the definition of acceleration applied to circular motion — it requires calculus to prove rigorously, but the result (a_c = v²/r inward) is used algebraically here.

## Diagram / Visual Model

```
         center
           ·
           ↑
           | a_c (centripetal, inward)
           |
         [object moving in circle]
         → v (tangent to circle, perpendicular to a_c)
```

The velocity vector is always tangent (sideways). The acceleration vector always points inward. They are always perpendicular for uniform circular motion.

## Problem Types That Use This

- [[../problem-types/horizontal-circular-motion]]
- [[../problem-types/vertical-circular-motion]]

## Common Beginner Mistake

**Drawing "centripetal force" as a separate arrow on the FBD.** Do not do this. The centripetal force is the label you give to the *net* of real forces after you have drawn them all. On your FBD, draw tension, gravity, normal force, friction — whichever real forces act. Then add them vectorially. The net inward component is the centripetal force.

A second mistake: **confusing centripetal (inward) and centrifugal (outward)**. In an inertial reference frame (which is what PHYS 2211 uses), there is no outward centrifugal force. The feeling of being "pushed outward" in a turning car is your inertia trying to go straight. The car's seat pushes you inward (centripetally). Centrifugal force is a fictitious force that only appears in rotating reference frames, which is beyond this course.

## Practice Next

- Apply ΣF_c = mv²/r to the horizontal circle (string tension) case → [[../problem-types/horizontal-circular-motion]]
- Then apply it to the vertical circle (tension + gravity) case → [[../concepts/vertical-circular-motion]]

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 6.1–6.2.
