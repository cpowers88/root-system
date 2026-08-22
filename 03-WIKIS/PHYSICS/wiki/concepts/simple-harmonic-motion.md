---
type: concept
timeline: reference
status: draft
---

# Simple Harmonic Motion

## What is the physical idea?

Simple harmonic motion (SHM) is the back-and-forth oscillation of an object when the net force on it is always directed toward a fixed equilibrium point and is proportional to how far the object is from that point.

The restoring force law: **F = −kx**

The negative sign means the force always opposes the displacement — if you pull the object to the right (+x), the force pushes left (−). This is what creates the oscillation.

## What real-world situation does it describe?

- A mass bobbing on a spring (vertical or horizontal)
- A pendulum swinging through small angles
- A tuning fork vibrating
- An atom vibrating around its equilibrium position in a crystal
- The needle on a scale oscillating after you step on it

Anywhere a restoring force exists that grows with displacement, you have SHM or something close to it.

## Objects / System Involved

Any object that:
1. Has a stable equilibrium position.
2. Experiences a restoring force when displaced from that position.
3. Experiences no friction or only very small friction (so the oscillation is sustained).

## Quantities That Change

- Position x(t) — oscillates between +A and −A
- Velocity v(t) — oscillates between +Aω and −Aω; zero at turning points, maximum at equilibrium
- Acceleration a(t) — oscillates between +Aω² and −Aω²; maximum magnitude at turning points, zero at equilibrium
- Kinetic energy — maximum at equilibrium, zero at turning points
- Potential energy — maximum at turning points, zero at equilibrium

## Model and Equations

The defining condition for SHM:

```text
a = −ω²x
```

Position, velocity, and acceleration:

```text
x(t) = A cos(ωt + φ)
v(t) = −Aω sin(ωt + φ)
a(t) = −Aω² cos(ωt + φ)
```

See [[../equations/shm-equations]].

For a spring-mass system: ω = √(k/m), T = 2π√(m/k). See [[../equations/spring-mass-period]].

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| x | displacement from equilibrium | m |
| A | amplitude | m |
| ω | angular frequency | rad/s |
| T | period | s |
| f | frequency | Hz |
| φ | phase constant | rad |

## Calculus Connection

SHM arises from the differential equation:

```text
d²x/dt² = −ω²x
```

This says: "the second derivative of position equals a negative constant times position." Any function whose second derivative gives back the negative of itself (scaled) must be sinusoidal. The solution x(t) = A cos(ωt + φ) is exactly that function. See [[../calculus-links/shm-differential-equation]].

Velocity v = dx/dt and acceleration a = dv/dt follow by differentiation.

## Diagram / Visual Model

**Graph of position, velocity, and acceleration vs. time:**

```
x(t)        |      ****
         A -|   *       *
            |*               *---> t
        −A -|           ****
             |<----- T ----->|

v(t)        max speed at x=0
            zero speed at x=±A

a(t)        max magnitude at x=±A (opposite direction to x)
            zero at x=0
```

**Energy bar chart at three positions:**

```
At x = +A:   [PE ████████████] [KE          ]
At x = 0:    [PE          ] [KE ████████████]
At any x:    [PE ████    ] [KE ████        ]   → total always same
```

## Problem Types That Use This

- [[../problem-types/shm-spring-mass-problems]]
- [[../problem-types/pendulum-problems]]

## Common Beginner Mistake

Thinking bigger amplitude means faster oscillation. The period T = 2π√(m/k) does not depend on A. A large-amplitude oscillation takes exactly as long as a small one — the faster maximum speed at a larger amplitude is exactly compensated by the longer distance traveled.

## Practice Next

Work through [[../worked-examples/spring-mass-shm]], then attempt [[../drills/shm-spring-drill]].

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 15.1–15.2.
