---
type: concept
timeline: reference
status: draft
---

# Terminal Velocity and Resistive Forces

## What is the physical idea?

A falling object does not accelerate forever. As it speeds up, air resistance increases. Eventually the drag force equals the weight. At that point the net force is zero, so the acceleration is zero, and the object falls at constant speed — called **terminal velocity**.

## What real-world situation does it describe?

- A skydiver in free fall (before the parachute opens).
- A raindrop falling through air.
- A car at top speed on a flat road (engine force = drag force).
- A feather settling slowly because its drag force equals its tiny weight at a low speed.

## Objects / System Involved

Any object moving through a fluid (air, water) that exerts a resistive force opposing motion.

## Quantities That Change

- Speed increases from rest → terminal velocity.
- Net force decreases from mg (at rest, no drag) → 0 (at terminal velocity, drag = weight).
- Acceleration decreases from g → 0.

## Model / Equation

There are two drag models depending on speed:

**Low-speed (linear) drag:** applies to very slow motion or very small objects (dust, pollen)
```
R = bv        (b = linear drag coefficient, units kg/s)
```
Terminal velocity when R = mg:
```
bv_t = mg   →   v_t = mg/b
```

**High-speed (quadratic) drag:** applies to everyday objects — falling people, cars, balls
```
R = ½DρAv²
```
| Symbol | Meaning | Unit |
|---|---|---|
| D | drag coefficient (shape-dependent, dimensionless) | — |
| ρ | density of air (≈ 1.2 kg/m³ at sea level) | kg/m³ |
| A | cross-sectional area of object | m² |
| v | speed | m/s |

Terminal velocity when R = mg:
```
½DρAv_t² = mg   →   v_t = √(2mg / DρA)
```

## Calculus Connection

The full equation of motion during the fall (before terminal velocity) requires solving a first-order differential equation. The solution gives an exponential approach to v_t:

```
v(t) = v_t (1 - e^(-bt/m))    [linear drag model]
```

In PHYS 2211, you only need the endpoint (v_t) and the physical reasoning — not the differential equation solution.

## Diagram / Visual Model

**Force diagram during the fall (at some intermediate speed v < v_t):**
```
         ↑ R = ½DρAv²   (drag, upward, opposes motion)
         
       [object]
       
         ↓ mg            (weight, downward)

Net downward = mg - R > 0   →   still accelerating
```

**At terminal velocity:**
```
         ↑ R = mg        (drag = weight)
       [object]
         ↓ mg

Net force = 0   →   constant velocity (no acceleration)
```

**Velocity vs. time graph:**
```
v_t ____________ (asymptote, never quite reached)
    /
   /
  /
 /
/________________ t
```

## Problem Types That Use This

- [[../problem-types/horizontal-circular-motion]] (drag-limited speed on roads)
- See also `wiki/drills/terminal-velocity-drill.md`

## Common Beginner Mistake

**Thinking terminal velocity is a hard upper limit that can never be exceeded.** Terminal velocity is the speed at which drag equals weight for a specific object in a specific orientation. Change the object's shape (tuck into a ball vs. spread-eagle skydiver), change the fluid, or change altitude and v_t changes.

**Forgetting which drag model to use.** High-speed (quadratic) drag is almost always correct for problems about people, vehicles, and sports balls. Low-speed (linear) drag is for tiny/slow objects.

**Thinking acceleration suddenly stops at v_t.** Acceleration gradually decreases toward zero as drag increases toward weight. It approaches zero exponentially — the object asymptotically approaches v_t and technically never quite reaches it.

## Practice Next

Use [[../drills/terminal-velocity-drill]] to calculate v_t for real-world objects.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 6.4, pp. 143–149.
