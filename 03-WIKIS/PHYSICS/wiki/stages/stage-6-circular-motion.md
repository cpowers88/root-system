---
type: stage
status: draft
---

# Stage 6 — Circular Motion and Other Applications of Newton's Laws (Ch 6)

## Goal

Apply Newton's second law to objects moving in circles and to objects slowed by resistive forces. This stage removes two common illusions: that "centripetal force" is a new type of force, and that falling objects accelerate forever.

## Syllabus Alignment

Ch 06 — confirmed in scope (Chris, 2026-06-25). Lecture dates pending full D2L calendar.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 6, sections 6.1–6.4.
File: `raw/textbook/Physics book-0101-0200.pdf`, textbook pp. 127–149.

## Prerequisite Physics

- Stage 5 — Newton's laws, free body diagrams, friction. This stage is a direct extension of Newton's second law ΣF = ma.
- Stage 4 — centripetal acceleration concept (a_c = v²/r) was introduced; here it gets force applied to it.

## Prerequisite Math

- Algebra (solving for v, r, m, T in centripetal force equation)
- Trigonometry (resolving normal force components on a banked curve)
- Square roots

## Core Concepts

- [[../concepts/centripetal-force]]
- [[../concepts/vertical-circular-motion]]
- [[../concepts/terminal-velocity]]

## Required Vocabulary

Centripetal acceleration, centripetal force, uniform circular motion, nonuniform circular motion, drag force, terminal velocity, banked curve. See `wiki/glossary/` and [[../flashcards/stage-6-circular-motion]].

## Equations

- [[../equations/centripetal-force]] — ΣF_c = mv²/r
- [[../equations/terminal-velocity]] — v_t = √(2mg/DρA) and v_t = mg/b

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| a_c | centripetal acceleration | m/s² |
| v | speed of object | m/s |
| r | radius of circular path | m |
| m | mass of object | kg |
| T | tension | N |
| n | normal force | N |
| f_s | static friction force | N |
| μ_s | coefficient of static friction | dimensionless |
| θ | angle of banked curve | degrees or rad |
| g | gravitational acceleration | 9.80 m/s² |
| R | resistive (drag) force | N |
| b | linear drag coefficient | kg/s |
| D | dimensionless drag coefficient | dimensionless |
| ρ | air density | kg/m³ |
| A | cross-sectional area | m² |
| v_t | terminal velocity | m/s |

## Diagrams / Visual Models

**Horizontal circular motion — FBD at position on circle:**
```
        [string]
object --T-->  center of circle
(moving into/out of page)
Net inward force = T = mv²/r
```

**Vertical circle — FBD at TOP:**
```
     [center of circle above]
          ↓ T (tension, inward)
     [object at top]
          ↓ mg (gravity, also inward at top)
ΣF_inward = T + mg = mv²/r
```

**Vertical circle — FBD at BOTTOM:**
```
     [object at bottom]
          ↑ T (tension, inward = upward here)
          ↓ mg (gravity, outward = downward here)
ΣF_inward = T - mg = mv²/r → T = mv²/r + mg
```

**Banked curve — FBD:**
```
Normal force n at angle θ from vertical
n cos θ = mg (vertical equilibrium)
n sin θ = mv²/r (horizontal = centripetal)
→ tan θ = v²/(rg)
```

**Terminal velocity — velocity vs. time:**
```
v ↑
v_t ------- (asymptote)
     /
    /
   /
  /
 /____________ t
Starts at 0, approaches v_t as drag = weight
```

## Calculus Connections

No new calculus in this stage.

Nonuniform circular motion introduces tangential acceleration a_t = dv/dt, which is a derivative — but computing it is Stage 2 territory. Here you only need to recognize it exists and find total acceleration: a = √(a_c² + a_t²).

## Problem Types

- [[../problem-types/horizontal-circular-motion]]
- [[../problem-types/vertical-circular-motion]]

## Worked Examples

- [[../worked-examples/banked-curve-example]]

## Drills

- [[../drills/circular-motion-forces-drill]]
- [[../drills/terminal-velocity-drill]]

## Common Errors

See [[../common-errors/stage-6-circular-motion]].

## Mastery Checklist

- [ ] State in one sentence what centripetal force IS and what it is NOT
- [ ] Draw a correct FBD for an object on a horizontal circular path (string, flat curve, banked curve)
- [ ] Draw a correct FBD at the TOP and BOTTOM of a vertical circle — correctly identifying which forces point inward vs. outward at each position
- [ ] Apply ΣF_inward = mv²/r to find tension, normal force, friction, or speed
- [ ] Derive the banked curve formula tan θ = v²/(rg) from FBD components
- [ ] Explain physically why terminal velocity is reached and what "net force = 0" means for motion
- [ ] Calculate terminal velocity given mass, drag coefficient, air density, and area
- [ ] Identify whether a problem uses linear drag (low speed, R = bv) or quadratic drag (high speed, R = ½DρAv²)

## Do Not Move On Until

Chris can draw FBDs for both horizontal and vertical circular motion without help, correctly identify which forces are inward vs. outward in each geometry, and solve for unknown speed, radius, or tension using ΣF = mv²/r.

## Parked for Later

Nonuniform circular motion with calculus (finding angular acceleration as a function of time) is fully treated in Stage 10 (Ch 10 — Rotation). The concepts introduced here (a_t, a_c) carry directly into that stage.
