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

## Pre-Semester Calculus Transfer Sprint (added 2026-07-28; promoted to the
primary evening focus 2026-07-30)

Chris's own framing: spend the runway before Fall classes start (Aug 24)
building fluency at transforming a real physics problem into the calculus
already learned once, using the built [[calculus-map#Calculus-Link Pages
Built So Far|calculus-link pages]] as the spine and the newly screened local
calculus library (`source-map.md` § Local Calculus Library) as backup depth
only when a specific rep doesn't click — not a cover-to-cover math course.

**Scope change, 2026-07-30:** originally scoped as an ahead-check preview
that ran alongside the normal syllabus-paced weekly plan without advancing
the Stage 4 gate early. Chris explicitly paused the syllabus-paced physics
block today: a live session (Problems 1-2, plus a cold derivative/integral
drill) surfaced the real gap as calculus *mechanics* recall — the power
rule and, especially, the constant of integration / boundary-condition step
— not physics concepts, which he already has from prior Physics 1/2 and
Calc 1/2 coursework. This sprint is now the primary evening-reading focus
through Aug 23; see `EVENING_READING_INSTRUCTIONS.md`'s dated override.
Daytime live problem-solving (like today's projectile-motion pair) continues
alongside it — this schedule is the evening layer only.

**Sequence — work these in order, using the Learning Method loop above
(physical situation -> skeleton -> sketch -> guided rep -> transfer ->
explain aloud). Each calculus-link rep gets a same-week cold redo two nights
later to build durability, not just first-pass recognition:**

1. [[calculus-links/kinematics-derivatives]] (Stage 2) — durability check, already passed once.
2. [[calculus-links/2d-kinematics-components]] (Stage 4) — active now; the July 28 session review (`worked-examples/2026-07-28-angled-launch-session-review.md`) already primes this.
3. [[calculus-links/tangential-radial-acceleration-derivative]] (Stage 4/6) — feeds directly into this week's still-open circular-motion drill.
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

### Dated Evening Schedule, 2026-07-30 through 2026-08-23

Opens with a raw calculus-mechanics refresher (not in the original 9-page
sprint) because today's live drill showed that's the actual missing piece —
the power rule itself came back fast, but "why is C = 3 here" did not.
Every calculus-link rep gets a cold-redo night two days later. Last four
nights are formula-recall consolidation, not new material; the final night
is light review only, matching the never-prime-a-cold-gate rule.

| # | Date | Focus |
|---|---|---|
| 1 | Thu Jul 30 | Derivative mechanics refresher — power rule, position→velocity→acceleration chain, x/y independence (today's live session) |
| 2 | Fri Jul 31 | Integral mechanics refresher — power rule reversed, the constant of integration, boundary/initial conditions (today's session, part 2) |
| 3 | Sat Aug 1 | Cold rebuild: derive all three 1D kinematics equations from a = const, no formula sheet. Flag v² = v₀² + 2aΔx explicitly — it's algebraic elimination of t between the other two, not a third integration |
| 4 | Sun Aug 2 | [[calculus-links/kinematics-derivatives]] (Stage 2) |
| 5 | Mon Aug 3 | [[calculus-links/2d-kinematics-components]] (Stage 4) |
| 6 | Tue Aug 4 | Cold redo — 2D kinematics components, from scratch |
| 7 | Wed Aug 5 | [[calculus-links/tangential-radial-acceleration-derivative]] (Stage 4/6) |
| 8 | Thu Aug 6 | Cold redo — tangential/radial acceleration |
| 9 | Fri Aug 7 | [[calculus-links/stage-7-work-integral]] (Stage 7) |
| 10 | Sat Aug 8 | Cold redo — work integral |
| 11 | Sun Aug 9 | [[calculus-links/power-derivative]] (Stage 8) |
| 12 | Mon Aug 10 | Cold redo — power derivative |
| 13 | Tue Aug 11 | [[calculus-links/impulse-integral]] (Stage 9) |
| 14 | Wed Aug 12 | Cold redo — impulse integral |
| 15 | Thu Aug 13 | [[calculus-links/rotational-kinematics-derivatives]] (Stage 10) |
| 16 | Fri Aug 14 | Cold redo — rotational kinematics |
| 17 | Sat Aug 15 | [[calculus-links/angular-momentum-derivative]] (Stage 11) |
| 18 | Sun Aug 16 | Cold redo — angular momentum |
| 19 | Mon Aug 17 | [[calculus-links/shm-differential-equation]] (Stage 15) — also flag #57's D2L/syllabus recheck trigger date |
| 20 | Tue Aug 18 | Cold redo — SHM differential equation |
| 21 | Wed Aug 19 | Retest whichever of reps 1-20 landed roughest — pick from the actual session record, not in advance |
| 22 | Thu Aug 20 | Full formula sweep #1 — every kinematics/dynamics/energy/momentum formula from memory, mark every miss |
| 23 | Fri Aug 21 | Targeted repair of only the Aug 20 misses — not a full redo |
| 24 | Sat Aug 22 | Full formula sweep #2 — cold, timed, no notes — dress rehearsal |
| 25 | Sun Aug 23 | Light review only: reread the running miss-log from the past 3 weeks. No new material the night before class starts |

Each night's actual result (pass/miss, what broke) gets logged in `wiki/log.md`
same as any other rep — this schedule is a plan, not a substitute for the
proof trail.

**Method note, 2026-07-30:** each new-rep night follows `OPERATIONS.md` §
Calculus-Reconstruction Lens's streamlined loop (state the rule -> derive
the formula -> 2-3 problems -> quiz cold). The cold-redo nights already
built into this schedule *are* that method's escalation rule in practice —
depth only adds when a quiz actually misses, not by default.

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
