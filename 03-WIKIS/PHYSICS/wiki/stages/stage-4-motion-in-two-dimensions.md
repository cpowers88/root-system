---
type: stage
timeline: now
stage: 4
status: active
tags: [physics, math]
---

# Unit/Stage 4 — Motion in Two Dimensions / Projectile Motion

## Goal

Apply 1D kinematic equations independently to the x and y directions to analyze projectile motion, uniform circular motion, and relative velocity.

## Syllabus Alignment

Ch 04. Neighbor-section pacing estimate: F Sep 4 and W Sep 9, 2026; Section
54's exact dates remain unconfirmed.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 4,
book pp. 68–94, sections 4.1–4.6 (Position/Velocity/Acceleration Vectors;
2D Motion with Constant Acceleration; Projectile Motion; Uniform Circular
Motion; Tangential and Radial Acceleration; Relative Velocity). Verified
against `raw/textbook/Physics book-0001-0100.pdf` and
`Physics book-0101-0200.pdf` 2026-07-25. Section 4.5 (tangential/radial
acceleration for *non-uniform* circular motion) was previously missing from
this stage and miscited as Stage 10 material; corrected below.

## Prerequisite Physics

Stages 2 and 3 — must be fluent with 1D kinematic equations (Stage 2) and vector components (Stage 3) before starting this stage. The core idea is that 2D motion is just two independent 1D problems sharing the same clock.

## Prerequisite Math

Vector components (sin/cos decomposition), quadratic equations, trig identities — especially sin 2θ = 2 sin θ cos θ.

## Math-to-Physical-World Bridge

The mathematical skeleton for projectile motion is two functions using the same
input, time:

```text
x(t) = x0 + (v0 cos theta)t
y(t) = y0 + (v0 sin theta)t - (1/2)gt^2
```

- `x(t)` is linear because the model contains no horizontal acceleration. Its
  graph has constant slope `v0 cos theta`; physically, equal time intervals add
  equal horizontal distances.
- `y(t)` is quadratic because gravity changes vertical velocity at a constant
  rate. Its graph curves downward; physically, each successive time interval
  removes another `g` worth of upward velocity.
- The same `t` appears in both equations because there is one projectile and one
  clock, even though the two component motions follow different rules.
- `cos theta` projects the launch vector onto the horizontal axis; `sin theta`
  projects it onto the vertical axis. These are not decorative trig operations:
  they measure the two shadows cast by one velocity vector.

Before calculating, predict the effect of changing one parameter:

- Increasing `v0` increases both component magnitudes and generally increases
  height and range.
- Increasing `theta` transfers more of the fixed launch speed into vertical
  motion and less into horizontal motion.
- Increasing `g` bends the vertical graph downward faster, shortening flight and
  reducing height and range.

Then check the prediction against the equations, units, graph, and final physical
result. This `predict -> calculate -> interpret` loop applies to every Stage 4
problem type.

## Core Concepts

- [[../concepts/projectile-motion]]
- [[../concepts/uniform-circular-motion]]
- [[../concepts/tangential-and-radial-acceleration]] — the non-constant-speed generalization of circular motion (Sec 4.5)
- [[../concepts/relative-velocity]]

## Required Vocabulary

Projectile, trajectory, range, maximum height, centripetal acceleration, centripetal force, tangential acceleration, radial acceleration, period (circular), relative velocity, reference frame. See `wiki/glossary/` and [[../flashcards/stage-4-motion-in-two-dimensions]].

## Equations

- [[../equations/projectile-motion-equations]]
- [[../equations/centripetal-acceleration]]
- [[../equations/tangential-and-radial-acceleration]]

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| x, y | horizontal and vertical position | m |
| v₀ | initial speed of projectile | m/s |
| θ₀ | launch angle above horizontal | degrees or rad |
| v₀ₓ = v₀ cos θ₀ | horizontal component of initial velocity | m/s |
| v₀ᵧ = v₀ sin θ₀ | vertical component of initial velocity | m/s |
| vₓ | horizontal velocity (constant throughout) | m/s |
| vᵧ | vertical velocity (changes due to gravity) | m/s |
| g | magnitude of free-fall acceleration | 9.80 m/s² |
| R | horizontal range (landing at same height) | m |
| h | maximum height | m |
| t | time of flight | s |
| r | radius of circular path | m |
| v | speed in circular motion (constant, or instantaneous if changing) | m/s |
| a_c | centripetal acceleration | m/s² |
| T | period of circular motion | s |
| a_r | radial (centripetal) acceleration component | m/s² |
| a_t | tangential acceleration component (dv/dt) | m/s² |
| a | magnitude of total acceleration = √(a_r²+a_t²) | m/s² |

## Diagrams / Visual Models

**Projectile path:**
```
        peak (vy=0, vx unchanged)
       /  \
      /    \
     /      \   <-- parabolic arc
    /        \
   launch     landing
   (θ₀)
   
   x-axis: constant velocity (no acceleration)
   y-axis: free-fall under gravity
```

**Velocity vectors at each point:** vₓ is always horizontal, vy changes direction (up → zero → down). The total speed |v| = √(vₓ² + vᵧ²) is NOT constant (except horizontal launch where it only increases).

**Centripetal acceleration:**
```
         v (tangent to circle)
         ^
         |
    a_c <--O  (a_c points inward toward center, always perpendicular to v)
```

**Tangential + radial acceleration (speed changing along the path):**
```
              a_t (along v, if speeding up)
              ↗
        v →  /
    ----O------
        |
        ↓ a_r (toward center)
```
When a_t = 0, this reduces to the plain centripetal-acceleration diagram above.

## Calculus Connections

The 1D kinematic equations from Stage 2 (derived by integrating constant acceleration) are applied twice — once for x(t) and once for y(t). The calculus is the same as Stage 2; what is new is the conceptual independence of the two directions.

For circular motion: centripetal acceleration is a derivative result — even though speed is constant, the direction of velocity changes, so dv⃗/dt ≠ 0. When speed also changes, a_t = dv/dt reuses the exact 1D-derivative idea from Stage 2, just applied along the curved path instead of a straight line.

Full worked derivations, multi-problem practice, and a real-world use case for
each: [[../calculus-links/2d-kinematics-components]] (vector differentiation
for projectile motion) and
[[../calculus-links/tangential-radial-acceleration-derivative]] (a_t as a
derivative of speed along a curved path).

## Problem Types

- [[../problem-types/projectile-horizontal-launch]]
- [[../problem-types/projectile-angled-launch]]
- [[../problem-types/circular-motion]]
- [[../problem-types/nonuniform-circular-motion]]

## Worked Examples

- [[../worked-examples/projectile-cliff-example]]

## Drills

- [[../drills/projectile-motion-drill]]
- [[../drills/circular-motion-drill]]
- [[../drills/tangential-radial-acceleration-drill]]
- [[../drills/relative-velocity-drill]]

## Recommended Reading and Rep Order

1. **Build the two-clock model:** chapter overview and §4.1–4.2, pp. 68–74;
   write the component equations before solving numbers.
2. **Projectile core:** §4.3, pp. 74–80; complete horizontal-launch problems
   before angled-launch problems.
3. **Uniform turn:** §4.4, pp. 81–83; name the real force that supplies the
   inward net force.
4. **Changing-speed turn:** §4.5, pp. 84–85; draw radial and tangential
   components before combining them.
5. **Reference frames:** §4.6, pp. 85–88; write the subscript equation before
   inserting values.
6. **Cold gate:** use the chapter summary, pp. 89–90, then run the mastery
   checklist without notes. End-of-chapter problems on pp. 90–94 are reserve
   transfer practice, not the first exposure.

## Common Errors

See [[../common-errors/stage-4-motion-in-two-dimensions]].

## Mastery Checklist

- [ ] State the key independence principle: horizontal and vertical motions are independent; they share only the time variable
- [ ] Decompose any launch velocity into v₀ₓ and v₀ᵧ using sin and cos
- [ ] Write the four projectile equations (x(t), y(t), vₓ(t), vᵧ(t)) from memory
- [ ] Explain why vₓ is constant throughout flight and vᵧ is not
- [ ] Identify the conditions under which the range formula R = v₀² sin 2θ₀ / g applies (same launch and landing height)
- [ ] Find the time to peak height by setting vᵧ = 0 and solving for t
- [ ] Solve a horizontally-launched projectile problem (given cliff height, find range and landing velocity)
- [ ] Solve an angled-launch problem (find max height, time of flight, and range)
- [ ] Explain why centripetal acceleration is not zero even when speed is constant
- [ ] Calculate centripetal acceleration given speed and radius
- [ ] Given a curved-path problem where speed is also changing, identify and compute both a_r and a_t, and combine them with √(a_r²+a_t²)
- [ ] Explain why a_t = 0 exactly when speed is constant (the uniform-circular-motion special case)
- [ ] Set up a relative velocity problem using the subscript-cancellation method

## Do Not Move On Until

Chris can set up the x and y equation systems for a projectile without prompting, correctly identify which equations apply to each direction, and obtain the correct range and time of flight. Must also be able to calculate centripetal acceleration and explain why it points inward, and — when speed is changing — split total acceleration into radial and tangential components.

## Parked for Later

Air resistance and drag forces are parked to Stage 6. **Rotational versions** of these same ideas (angular acceleration α, torque, moment of inertia) come back in Stage 10 — that's a genuinely later topic, distinct from the Section 4.5 tangential/radial split above (which is required for this stage; corrected 2026-07-07, was previously miscited as Stage 10 material).
