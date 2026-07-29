---
type: concept
timeline: reference
status: draft
---

# Spring-Mass System

## What is the physical idea?

A spring-mass system is the standard physical model for SHM. A mass m is attached to a spring with spring constant k. When displaced from equilibrium by distance x, Hooke's Law provides a linear restoring force F = −kx that drives the mass back and forth.

This system is important because it is the exact mechanical realization of the SHM differential equation. Understanding the spring-mass system gives you the template for understanding all other oscillators (pendulums, LC circuits, vibrating atoms).

## What real-world situation does it describe?

- A mass hanging on a spring bouncing up and down (vertical spring-mass)
- A mass on a frictionless surface connected to a spring (horizontal spring-mass)
- The front suspension of a car (mass of car body, spring of shock absorber)
- Any system with a stiffness and an inertia that oscillates

## Objects / System Involved

- **Mass m** — the inertia that resists changes in velocity.
- **Spring with constant k** — the restoring element that provides force proportional to displacement.
- **Equilibrium position** — the natural rest length of the spring. This is defined as x = 0.

**Vertical spring-mass:** The equilibrium position shifts downward from the natural length by mg/k (where the spring force balances gravity). Oscillations still occur symmetrically about this new equilibrium, and the period formula is unchanged: T = 2π√(m/k).

## Quantities That Change

- x — displacement from equilibrium
- v — velocity
- a — acceleration
- KE and PE — exchange continuously, but total E is conserved

## Model and Equations

Newton's 2nd Law applied to the spring force:

```text
F_net = ma
−kx = m(d²x/dt²)
d²x/dt² = −(k/m)x = −ω²x   where ω = √(k/m)
```

Key equations:
```text
ω = √(k/m)          angular frequency (rad/s)
T = 2π√(m/k)        period (s)
f = (1/2π)√(k/m)    frequency (Hz)
```

Position, velocity, acceleration: see [[../equations/shm-equations]].
Energy: see [[../equations/shm-energy]].

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| k | spring constant | N/m |
| m | mass | kg |
| x | displacement from equilibrium | m |
| ω | angular frequency | rad/s |
| T | period | s |
| A | amplitude | m |
| E | total mechanical energy | J |

## Calculus Connection

The equation F = ma applied to Hooke's Law gives the second-order ODE d²x/dt² = −ω²x. Its general solution is x(t) = A cos(ωt + φ), where A and φ are determined by the initial position x₀ and velocity v₀. See [[../calculus-links/shm-differential-equation]].

## Diagram / Visual Model

**Horizontal spring-mass on frictionless surface:**

```
   ___________
  |     k    |
  |/\/\/\/\/-|====[ m ]
  |__________|
        ←F = −kx when x > 0 (spring pulls left)
        →F = −kx when x < 0 (spring pushes right)

  Equilibrium: x = 0
  Right turning point: x = +A  (v = 0, a = −Aω²)
  Left turning point:  x = −A  (v = 0, a = +Aω²)
  Equilibrium:         x = 0   (v = ±Aω, a = 0)
```

**Vertical spring-mass:**

```
  ceiling
    |
   /\/\/\  ← spring (k)
    |
   [m]      ← at equilibrium (x = 0), spring stretched by mg/k

  Oscillations above: x < 0 (compressed beyond equilibrium)
  Oscillations below: x > 0 (stretched beyond equilibrium)
  Period still T = 2π√(m/k)  ← gravity shifts equilibrium but does not change period
```

## Problem Types That Use This

- [[../problem-types/shm-spring-mass-problems]]

## Common Beginner Mistake

For a vertical spring: thinking you need to add gravity to the equation of motion separately. You do not — when you measure x from the new equilibrium position (where the spring force already balances gravity), the oscillation equation is identical to the horizontal case: d²x/dt² = −ω²x.

Another mistake: computing T = 2π√(m/k) when the problem asks for f or ω. Always identify which quantity is asked for before computing.

## Practice Next

Attempt [[../worked-examples/spring-mass-shm]], then [[../drills/shm-spring-drill]].

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 15.2, pp. 454–461.
