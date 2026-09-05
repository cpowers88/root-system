---
type: concept
timeline: reference
status: draft
---

# Rolling Without Slipping

## What is the physical idea?

Rolling without slipping is a special condition where a rotating object moves along a surface such that the contact point has zero velocity relative to the surface at every instant. This links the rotational and translational motion: knowing one lets you find the other. It's not obvious — it requires static friction to maintain, and it means the bottom of the wheel is momentarily stationary while the top moves at twice the center speed.

## What real-world situation does it describe?

A car tire rolling on dry pavement. A bowling ball after it's stopped skidding and settled into a roll. A ball bearing in a race. Any wheel or ball rolling on a surface where there's enough friction to prevent slip.

## The Rolling Condition

For an object of radius R rolling without slipping:

```
v_cm = Rω        (linear speed of center = radius × angular speed)
a_cm = Rα        (linear acceleration of center = radius × angular acceleration)
```

This is the key constraint. Once you know one, you know the other.

**Physical meaning of v_cm = Rω:**
- The center of mass moves forward at v_cm
- The object rotates at ω
- These two are locked together — you can't have one without the other
- At the contact point: v_contact = v_cm − Rω = 0 (the point touching the ground is instantaneously at rest)
- At the top: v_top = v_cm + Rω = 2v_cm (moves at twice the center speed)

## What Maintains Rolling?

**Static friction** at the contact point. Without friction (on ice), an object slides instead of rolls. Rolling without slipping requires sufficient static friction; if the friction force required exceeds μₛN, the object begins to slip.

## Velocity Profile of a Rolling Object

```
     v_top = 2v_cm ──→
              •
             / \
            /   \
           •     •   ← sides: speed = v_cm, direction angled
            \   /
             \ /
              •  ← contact point: v = 0 (instantaneously at rest)
          
   Center → v_cm
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| v_cm | speed of center of mass | m/s |
| ω | angular speed | rad/s |
| R | radius of object | m |
| a_cm | linear acceleration of center | m/s² |
| α | angular acceleration | rad/s² |

## Using Rolling in Energy Problems

Substitute ω = v_cm/R into K_rot = ½Iω² to eliminate ω:
```
K_rot = ½I(v_cm/R)² = (I/2R²)v_cm²
K_total = ½mv_cm² + (I/2R²)v_cm² = ½v_cm²(m + I/R²)
```

For energy conservation on a ramp (starting from rest at height h):
```
mgh = ½v_cm²(m + I/R²)
v_cm = √(2gh / (1 + I/(mR²)))
```

The denominator (1 + I/(mR²)) is always ≥ 1, so a rolling object always arrives at the bottom slower than a sliding object (which would give v = √(2gh) — no rotational term).

## Calculus Connection

The rolling condition comes from kinematics: if the contact point is stationary, then the velocity of the center equals the tangential velocity at the rim: v_cm = rω. Differentiating: a_cm = rα.

## Diagram / Visual Model

```
  ────────────────────────  surface
        •
       / \  ← R
      /   \
     •  c  •    c = center, v_cm = Rω to the right
      \   /
       \ /
        •    ← contact: v = 0 at this instant
  ────────────────────────  (static friction acts here, to the left for acceleration to the right)
```

## Problem Types That Use This

- [[../problem-types/rolling-problems]]

## Common Beginner Mistake

1. **Forgetting the rolling condition:** treating translation and rotation as independent. They're not — v_cm = Rω locks them together.
2. **Applying rolling to a sliding object:** rolling requires sufficient static friction. On a frictionless surface, there is no rolling without slipping.
3. **Using kinetic friction instead of static friction:** the contact point is instantaneously at rest in rolling without slipping, so static friction applies (even if the object is moving). Kinetic friction applies only when slipping is occurring.
4. **Confusing the speed at the contact point (zero) with the speed of the center (v_cm):** the ball itself is moving; the contact point is just instantaneously stationary.

## Practice Next

[[../worked-examples/rolling-cylinder-incline-example]] and [[../drills/rotational-energy-drill]].

## Sources

Serway & Jewett, 10th ed., Ch. 10.8.
