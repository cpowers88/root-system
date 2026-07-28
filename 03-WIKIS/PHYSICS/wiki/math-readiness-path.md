---
type: map
timeline: now
status: active
reference_priority: core
tags: [physics, math, school, meta-learning]
---

# Physics Math Readiness Path

## Purpose

This is the just-in-time algebra, trigonometry, and calculus route for PHYS 2211.
It is not a separate math course and it does not delay physics until every math
skill feels perfect. The active physics situation determines the next math rep.

Use the textbook appendix for lookup:

- [[appendix/math-algebra]]
- [[appendix/math-geometry-trig]]
- [[appendix/math-calculus]]

Use [[calculus-map]] to see where each calculus idea enters the course.
Use [[physics-math-crash-course]] for the complete explanations, worked bridges,
transfer checks, and the relevance screen of Chris's external math archive.

## Learning Profile Inputs

The learning loop below reflects a visual and text review of all three supplied
YouScience documents on 2026-07-15:

- `Christopher_Aptitude_Results.pdf`
- `Christopher_Aptitude_Discussion.pdf`
- `Christopher_One_Page_Summary.pdf`

They are design inputs, not limits. The combined implications are to use spatial
models and tangible outcomes, look for numerical patterns, think and explain aloud,
allow more than one approach during exploration, then converge on a stable written
procedure. Keep the future target visible, always name the next action, and avoid
opening several competing math topics at once.

## Learning Method

The aptitude evidence and Chris's 2026-07-28 calibration support a
math-forward, physical, spatial, conversational loop. Mathematical structure is
the fastest entry point; physical translation prevents symbol manipulation from
becoming detached from the actual system:

```text
physical situation -> mathematical skeleton -> symbol/unit map -> sketch
-> physical translation -> guided rep -> changed-parameter transfer
-> explain aloud -> cold check next session
```

Rules:

1. Name the physical system, then show the governing relationship early so Chris
   can orient through its structure.
2. Give every symbol, sign, unit, derivative, integral, and vector operation one
   exact physical meaning and use it immediately.
3. Draw the objects, axes, triangle, graph, or rotation before substituting
   numbers; the diagram verifies that the chosen mathematics matches reality.
4. Learn formulas through derivation, dependency, and physical relationship, not
   as isolated text.
5. Use one worked example, then change the numbers or physical setting for the
   independent rep.
6. Start the next session with one cold retrieval check before adding new material.
7. After solving, compare the result with a nearby case and state the numerical
   pattern you notice.
8. Explain one alternate approach aloud, then record the most dependable process
   as the reusable method.

The control question is always:

> What does the mathematics predict, and what would that prediction look like in
> the physical world?

## Stage-Gated Math Route

| Physics stages | Math gate | Physical anchor | Proof before moving on |
|---|---|---|---|
| 1 | scientific notation, units, proportional reasoning, algebra | estimating material, converting tool dimensions, checking whether a result can physically fit | convert units and reject a dimensionally impossible equation |
| 2 | slope, polynomial derivatives, area under a graph, basic antiderivatives | a vehicle's position, speedometer reading, braking acceleration, accumulated distance | move both directions through `x(t) -> v(t) -> a(t)` and explain a `v-t` area |
| 3 (closed; durability checks continue) | degrees/radians, right-triangle trig, inverse trig, quadrants, Pythagorean theorem | navigation, roof pitch, cable tension, two crews pulling an object | solve a two-vector non-axis addition problem and check the quadrant without notes |
| 4 (active) | component functions, quadratics, derivatives applied separately to x and y | a thrown tool, water from a hose, a vehicle changing direction | build x/y equations from a sketch and explain why horizontal and vertical motion share time |
| 5-6 | simultaneous equations, incline trig, radians, circular geometry | ramp forces, connected loads, a car on a curve, a rotating ride | draw the free-body diagram, resolve forces, and solve without inventing a “centripetal force” |
| 7-8 | dot product, definite-integral area, derivative of potential energy | pushing a cart at an angle, compressing a spring, braking with friction | identify the force component that does work and interpret an `F-x` area |
| 9 | signed/vector components, simultaneous equations, force-time area | vehicle collisions, recoil, catching or stopping an object | choose a system and conserve momentum independently in 1D and 2D |
| 10-12 | radian kinematics, trig torque, cross product/right-hand rule, `I = integral(r^2 dm)`, equilibrium systems | wrench and breaker bar, flywheel, beam, ladder, distributed load | use the right-hand rule physically, choose a pivot, and solve both force and torque balance |
| 13-14 | inverse-square scaling, ratios, density, areas/volumes, multi-term algebra | satellite altitude, water pressure, hydraulic lift, pipe restriction | predict direction and scale before calculating, then verify units |
| 15-17 | sine/cosine graphs, phase, derivatives of trig functions, small-angle approximation, logarithms for decibels, one trig sum identity | suspension spring, pendulum, guitar string, pipe resonance, sound level | connect graph shape to motion/wave behavior and explain what phase changes physically |
| 18 | ratios, square roots, limiting behavior, small-parameter approximations | GPS timing, particle lifetime, why everyday speeds look Newtonian | estimate whether relativity matters before using the Lorentz factor |

## Current Three-Rep Math Bridge — Stage 4

1. **Now — projectile setup:** work the cold transfer rep in
   [[physics-math-crash-course#Stage 4 Immediate Bridge — Projectile Motion]].
   Draw the trajectory and build separate x/y equation lanes before substituting.
2. **Repair only the first observed gap:** use the matching crash-course module —
   components, quadratics, or derivatives — then return immediately to the same
   projectile rep with changed numbers.
3. **Close the bridge:** explain aloud why x and y share time but not acceleration,
   and use units plus the landing-velocity direction to check the answer.

## Pre-Semester Calculus Transfer Sprint (added 2026-07-28)

Chris's own framing: spend the runway before Fall classes start (Aug 24)
building fluency at transforming a real physics problem into the calculus
already learned once, using the built [[calculus-map#Calculus-Link Pages
Built So Far|calculus-link pages]] as the spine and the newly screened local
calculus library (`source-map.md` § Local Calculus Library) as backup depth
only when a specific rep doesn't click — not a cover-to-cover math course.
This is the same ahead-check pattern already used for Stage 5; it previews
transfer skill, it does not advance the active Stage 4 gate early.

**Sequence — work these in order, one rep each, using the Learning Method
loop above (physical situation -> skeleton -> sketch -> guided rep ->
transfer -> explain aloud):**

1. [[calculus-links/kinematics-derivatives]] (Stage 2) — durability check, already passed once.
2. [[calculus-links/2d-kinematics-components]] (Stage 4) — active now; today's session review (`worked-examples/2026-07-28-angled-launch-session-review.md`) already primes this.
3. [[calculus-links/tangential-radial-acceleration-derivative]] (Stage 4/6) — next scheduled per the weekly plan (Thu Jul 30).
4. [[calculus-links/stage-7-work-integral]] (Stage 7)
5. [[calculus-links/power-derivative]] (Stage 8)
6. [[calculus-links/impulse-integral]] (Stage 9)
7. [[calculus-links/rotational-kinematics-derivatives]] (Stage 10)
8. [[calculus-links/angular-momentum-derivative]] (Stage 11)
9. [[calculus-links/shm-differential-equation]] (Stage 15)

Stage 14 (fluids) and Stage 16 (waves) have no calculus-link page yet —
build those only when Chris actually reaches them, per the one-stage-at-a-
time rule; they are not part of this sprint.

A rep is done when the explain-back and practice problems in that page pass
without notes. If one doesn't click, pull the matching named section from
Strang or the OpenStax volumes (`source-map.md` table), work it there, then
return to the same calculus-link page — never substitute textbook reading
for the physics rep itself.

## Support Sources

- [OpenStax Precalculus 2e](https://openstax.org/books/precalculus-2e/pages/preface) -
  use Chapters 5-8 only when a trig or vector diagnostic shows a real gap.
- [MIT OpenCourseWare 8.01SC: derivatives in mechanics](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-1-kinematics/1-6-derivatives/) -
  use when the slope/rate meaning is unclear.
- [MIT OpenCourseWare 18.01SC](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) -
  use the specific derivative, integral, or series unit needed by the live stage.
- [PhET Vector Addition](https://phet.colorado.edu/en/simulations/vector-addition) -
  use the 2D and equations screens to make components and resultants visible.

These are support sources, not a replacement course spine. Retrieve or intake only
the section that answers a demonstrated learning gap.
