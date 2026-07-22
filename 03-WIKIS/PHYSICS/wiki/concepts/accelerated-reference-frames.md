---
type: concept
status: draft
---

# Motion in Accelerated Reference Frames

## What is the physical idea?

Newton's laws — as used everywhere else in this course — only work as written in an
**inertial frame**: one that is not accelerating. Every FBD so far has quietly
assumed you (the observer) are standing on solid, non-accelerating ground.

A **noninertial frame** is a reference frame that is itself accelerating —
a braking car, a spinning carousel, an accelerating elevator. Inside that frame,
objects appear to accelerate even when no real force is causing it. To keep using
ΣF = ma inside a noninertial frame, you must add a **fictitious force** (also
called a pseudo-force): F_fict = −ma_frame, pointing opposite the frame's
acceleration. It is not a real force — no object is exerting it — it is a
bookkeeping term that makes the noninertial observer's equations balance.

Two equally valid ways to solve the same problem:

- **Inertial-frame view** (the ground observer): only real forces exist. Apply
  ΣF = ma directly. This is the method used everywhere else in this stage.
- **Noninertial-frame view** (the accelerating observer, e.g. a rider inside the
  accelerating car): add F_fict = −ma_frame to the real forces, then treat the
  object as if it were in equilibrium in that frame.

Both views predict the same real-world outcome. The fictitious force exists only
to make the *accelerating observer's* math work.

## What real-world situation does it describe?

- A rider in a car that suddenly brakes feels "thrown forward" — there is no real
  forward force; the car (and the rider's seat) is decelerating, and the rider's
  body's inertia keeps it moving forward relative to the car.
- A passenger in an elevator that accelerates upward feels heavier — the floor
  pushes up harder than gravity pulls down, because the passenger must accelerate
  upward too.
- A rider on a spinning carousel feels pushed outward ("centrifugal force") — this
  is the fictitious force that appears in the rotating frame; a ground observer
  sees only the real inward (centripetal) force keeping the rider on the ride.

## Objects / System Involved

Any object viewed from a reference frame that is itself accelerating (linear
acceleration, like a braking car or accelerating elevator; or rotational
acceleration, like a spinning platform).

## Quantities That Change

- The apparent (measured) weight of an object in an accelerating elevator differs
  from its true weight mg.
- The direction and magnitude of the fictitious force depend entirely on the
  frame's acceleration a_frame, not on any property of the object being observed
  (other than its mass).

## Model / Equation

Ground (inertial) observer, for an object of mass m inside an accelerating frame:

```
ΣF_real = ma_object
```

Same object, from inside the accelerating frame (noninertial observer), where
a_frame is the frame's own acceleration relative to the ground:

```
ΣF_real + F_fict = ma_object,relative-to-frame
F_fict = −m·a_frame
```

**Apparent weight in an accelerating elevator** (a_frame = a, positive upward):

```
n = m(g + a)      elevator accelerating upward
n = m(g − a)      elevator accelerating downward
n = 0             free fall (a = g downward) — apparent weightlessness
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| a_frame | acceleration of the noninertial frame relative to the ground | m/s² |
| F_fict | fictitious (pseudo) force | N |
| m | mass of the object being observed | kg |
| n | normal force (apparent weight, elevator problems) | N |
| g | gravitational acceleration | 9.80 m/s² |

## Calculus Connection

None new. This section reuses ΣF = ma from Stage 5; the only new idea is which
frame you are applying it in, and what extra term appears when that frame is
noninertial.

## Diagram / Visual Model

```
GROUND OBSERVER (inertial):          RIDER IN ACCELERATING CAR (noninertial):

  car accelerates -->                  car accelerates -->
  [rider] stays put relative           [rider] appears pushed backward
  to the ground; car seat pushes       relative to the car seat
  rider forward via the seat back

  Real force only: seat pushes         Real force (seat) + fictitious force
  rider forward = ma                   (backward, = −ma) → rider "feels"
                                        pushed back, net apparent force ~0
```

**Elevator apparent-weight diagram:**
```
        ↑ n (normal force / scale reading)
     [person]
        ↓ mg (true weight, always mg)

Accelerating up:   n > mg  (feels heavier)
Accelerating down: n < mg  (feels lighter)
Free fall (a = g): n = 0   (feels weightless)
```

## Problem Types That Use This

- [[../problem-types/horizontal-circular-motion]] — the "centrifugal force" a
  rotating-frame observer reports is this same fictitious-force idea.
- Elevator apparent-weight problems are typically folded into
  [[../problem-types/fbd-single-object]]; use the accelerated-frame model above
  when the object itself is inside an accelerating system.

## Common Beginner Mistake

**Adding the fictitious force in the ground observer's equation.** If you are the
ground observer (the usual choice in this course), do not add F_fict — only real
forces belong in ΣF = ma for an inertial frame. The fictitious force only appears
if you deliberately choose to analyze the problem from inside the accelerating
frame. Most PHYS 2211 problems are solved fastest by staying in the inertial
(ground) frame and skipping the fictitious force entirely — it exists here mainly
so "centrifugal force" and "feeling pushed back in a car" have a correct physical
explanation instead of being treated as a real push.

## Practice Next

- Rework a horizontal circular motion problem from Stage 6 and explain, in words,
  what a rider on the rotating object would report feeling — then explain why the
  ground observer sees no such force.
- Apparent-weight elevator problem: given elevator acceleration, find scale
  reading; then find the acceleration that would make the scale read zero.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 6.3
  (Motion in Accelerated Frames).
