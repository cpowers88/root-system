---
type: stage
status: draft
---

# Unit/Stage 3 — Vectors (Ch 3)

## At a Glance
- **Core claim:** vectors/components/unit vectors are the mathematical toolkit every later chapter depends on — this stage is prerequisite math, not a standalone topic.
- **When to use it:** this is Chris's current active study stage (per `NOW.md` and `current-position.md`), lecture-aligned to Ch 3, Sep 2, 2026.
- **Decision/action it supports:** whether to move to Stage 4 — gated by "Do Not Move On Until" below, not by reading the page once.
- **Key risk:** the dot product previews here but isn't required until Stage 7, and the cross product until Stage 11 — don't chase either ahead of schedule (see Parked for Later).

## Goal

Handle 2D and 3D physical quantities correctly using coordinate systems, vector components, and unit vectors — the mathematical toolkit every later chapter depends on. (The dot product previews here but isn't required until Stage 7 — see Parked for Later.)

## Syllabus Alignment

Ch 03, lecture W Sep 2, 2026.

## Textbook Alignment

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Chapter 3, sections 3.1–3.4 (Coordinate Systems; Vector and Scalar Quantities; Basic Vector Arithmetic; Components of a Vector and Unit Vectors). Verified against `raw/textbook/Physics book-0001-0100.pdf` 2026-07-07 — this chapter has only four sections, not six. The textbook itself defers the dot product to Chapter 7 (Energy of a System) and the cross product to Chapter 11 (Angular Momentum) — see "Parked for Later" below.

## Prerequisite Physics

Stage 1 (units and dimensions), Stage 2 (1D kinematics — you already used displacement and velocity as signed scalars in 1D; now you extend them to true vectors in 2D/3D).

## Prerequisite Math

Trigonometry: sin, cos, tan definitions and the Pythagorean theorem. Inverse trig: tan⁻¹. Both are in `wiki/appendix/math-geometry-trig.md`.

## Core Concepts

- [[../concepts/coordinate-systems]] — Cartesian vs. polar (Sec 3.1)
- [[../concepts/scalar-vs-vector]]
- [[../concepts/vector-components]]

## Required Vocabulary

Cartesian coordinates, polar coordinates, scalar, vector, component, unit vector, resultant. See [[../flashcards/stage-3-vectors]].

## Equations

- [[../equations/polar-cartesian-conversion]] — x = r cos θ, y = r sin θ; r = √(x²+y²)
- [[../equations/vector-decomposition]] — Ax = A cos θ, Ay = A sin θ; A = √(Ax²+Ay²)
- [[../equations/vector-addition-by-components]] — add component by component

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| x, y | Cartesian coordinates | m |
| r | radial distance from origin (polar) | m |
| A, B | vector magnitudes | same as the physical quantity (m, m/s, N, etc.) |
| Ax, Ay | x and y components of vector A | same as A |
| θ | angle from +x axis (vector direction, or polar angle) | degrees or radians |
| î, ĵ, k̂ | unit vectors along +x, +y, +z | dimensionless (magnitude = 1) |

## Diagrams / Visual Models

**Coordinate systems diagram** — the same right triangle, applied to a point instead of a vector:

```
        ^ y
        |
        |  • (x, y)
        | /|
        |/ | y = r sin θ
   -----+--+--------> x
     O  |  x = r cos θ
```

**Vector decomposition diagram** — always draw this before plugging into trig:

```
        ^ y
        |
        |  / A (magnitude, at angle θ)
        | /
        |/ θ
   -----+----------> x
        |
```

- The horizontal leg = Ax = A cos θ
- The vertical leg = Ay = A sin θ
- θ is always measured from the +x axis going counterclockwise

**Tip-to-tail addition** — place B's tail at A's tip; the resultant R goes from A's tail to B's tip.

## Calculus Connections

None new in this stage. This chapter uses trigonometry, not calculus. Calculus returns in Stage 4 when position, velocity, and acceleration become 2D vector functions of time.

## Problem Types

- [[../problem-types/polar-cartesian-conversion]]
- [[../problem-types/vector-decomposition]]
- [[../problem-types/vector-addition]]

## Worked Examples

- [[../worked-examples/polar-coordinates-conversion-example]]
- [[../worked-examples/vector-force-components-example]]

## Drills

- [[../drills/polar-cartesian-conversion-drill]]
- [[../drills/vector-components-drill]]
- [[../drills/vector-addition-drill]]

## Common Errors

See [[../common-errors/stage-3-vectors]].

## Mastery Checklist

- [ ] Convert a point between Cartesian (x, y) and polar (r, θ) form in both directions, checking the quadrant every time
- [ ] State the difference between a scalar and a vector, and give two examples of each
- [ ] Decompose any vector into x and y components using Ax = A cos θ and Ay = A sin θ (with θ from +x axis)
- [ ] Reconstruct magnitude and direction from components using A = √(Ax²+Ay²) and θ = tan⁻¹(Ay/Ax), checking quadrant on a sketch
- [ ] Add two vectors by adding their components separately, then find the resultant's magnitude and direction
- [ ] Explain what î, ĵ, k̂ mean and why their magnitude is 1

## Do Not Move On Until

Chris can convert between Cartesian and polar coordinates, decompose a vector at any angle, and add two vectors by components — all without looking at notes — and can explain the difference between a scalar result and a vector result.

## Parked for Later

- **The dot product (A⃗·B⃗ = AB cos θ = AxBx + AyBy)** — pages already exist ([[../concepts/dot-product]], [[../equations/dot-product]]) as an early preview of the vector-operations toolkit, but the textbook itself does not formally introduce the dot product until **Chapter 7 (Energy of a System)**, where it's needed for W = F⃗·d⃗. Not required for the Ch3/Sep 2 lecture or exam — Stage 7's packet already lists it as a prerequisite pulled forward from here. Revisit these pages when Stage 7 starts; they don't need to be mastered now.
- The cross product (A⃗×B⃗) is introduced here conceptually but not used until Stage 10 (torque = r⃗×F⃗) and, per the textbook, formally in **Chapter 11** (angular momentum L⃗ = r⃗×p⃗). No problems require the cross product until those stages.
