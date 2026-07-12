---
type: map
tags: [reference, physics]
---

# Concept Map

## Purpose

Map physics concepts in dependency order.

```text
measurement → units → dimensional analysis → vectors → position → displacement → velocity → acceleration
force → net force → Newton laws → free-body diagrams
energy → work → kinetic energy → potential energy → conservation
momentum → impulse → collisions
gravitation → orbital motion
oscillation → waves → superposition
classical mechanics assumptions → relativity
```

## Course-wide dependency chain (all 18 stages)

```text
units & dimensions (Ch1)
   -> position/velocity/acceleration in 1D (Ch2)
        -> vectors (Ch3)
             -> position/velocity/acceleration in 2D, projectile motion (Ch4)
                  -> force, Newton's laws, free body diagrams (Ch5)
                       -> circular motion and Newton's law applications (Ch6)
                       -> work & energy (Ch7)
                            -> conservation of energy (Ch8)
                                 -> linear momentum and collisions (Ch9)
                                      -> rotation of rigid objects (Ch10)
                                           -> angular momentum (Ch11)
                                                -> static equilibrium and elasticity (Ch12)
                                      -> universal gravitation (Ch13) [needs Ch6 + Ch7–8]
                                      -> fluid mechanics (Ch14)       [needs Ch5 + Ch7–8]
                                      -> oscillatory motion / SHM (Ch15) [needs Ch5 + Ch7–8]
                                           -> wave motion (Ch16)
                                                -> superposition & standing waves (Ch17)
                       -> relativity (Ch38) [challenges Newtonian assumptions from Ch2–9]
```

## Stage 1 Concepts (Ch 1 — Physics and Measurement)

| Concept | Depends on | Unlocks | Unit introduced | Unit mastered | Common confusion | Page |
|---|---|---|---|---|---|---|
| SI base units (length, mass, time) | none | everything | Stage 1 | Pending | Confusing mass (kg) with weight (N) | [[../concepts/si-base-units]] |
| The particle model | none | all motion analysis | Stage 1 | Pending | Thinking the model is "wrong" because real objects have size | [[../concepts/particle-model]] |
| Dimensional analysis | SI base units | every equation-check in the course | Stage 1 | Pending | Thinking dimensional analysis can find numerical constants (it can't) | [[../concepts/dimensional-analysis]] |
| Unit conversion | SI base units | every numeric problem | Stage 1 | Pending | Multiplying by a conversion factor upside down | [[../concepts/unit-conversion]] |
| Order-of-magnitude estimation | SI base units | quick sanity checks | Stage 1 | Pending | Treating an estimate as if it needs to be exact | [[../concepts/order-of-magnitude-estimation]] |
| Significant figures | none | every reported answer | Stage 1 | Pending | Confusing sig-fig rule for multiplication with the rule for addition | [[../concepts/significant-figures]] |

## Stage 3 Concepts (Ch 3 — Vectors)

| Concept | Depends on | Unlocks | Unit introduced | Unit mastered | Common confusion | Page |
|---|---|---|---|---|---|---|
| Coordinate systems (Cartesian vs. polar) | Trigonometry (Appendix B.4) | Vector components (same triangle, applied to an arrow instead of a point); every later position/vector problem | Stage 3 | Pending | Forgetting to check the quadrant on tan⁻¹(y/x) | [[../concepts/coordinate-systems]] |
| Scalar vs. vector | none | All of mechanics — every quantity is one or the other | Stage 3 | Pending | Treating a vector's magnitude as the whole answer, ignoring direction | [[../concepts/scalar-vs-vector]] |
| Vector components | Coordinate systems | Vector addition, all 2D/3D motion (Stage 4+) | Stage 3 | Pending | Using sin where cos belongs (θ measured from the wrong axis) | [[../concepts/vector-components]] |
| Dot product (preview — textbook formally introduces in Ch 7) | Vector components, scalar vs. vector | Work W = F⃗·d⃗ (Stage 7) | Stage 3 (preview only) | Deferred to Stage 7 | Confusing dot product (scalar result) with cross product (vector result) | [[../concepts/dot-product]] |

## Stage 4 Concepts (Ch 4 — Motion in Two Dimensions)

| Concept | Depends on | Unlocks | Unit introduced | Unit mastered | Common confusion | Page |
|---|---|---|---|---|---|---|
| Projectile motion | Vector components (Stage 3), 1D kinematics (Stage 2) | Every 2D-launch problem | Stage 4 | Pending | Thinking horizontal velocity changes during flight | [[../concepts/projectile-motion]] |
| Uniform circular motion | Vector components | Centripetal force (Stage 6), rotation (Stage 10) | Stage 4 | Pending | Thinking constant speed means zero acceleration | [[../concepts/uniform-circular-motion]] |
| Tangential and radial acceleration | Uniform circular motion, 1D acceleration (Stage 2) | Non-uniform circular motion problems; previews rotational kinematics (Stage 10) | Stage 4 | Pending | Reporting only the centripetal piece when speed is also changing | [[../concepts/tangential-and-radial-acceleration]] |
| Relative velocity | Vector addition (Stage 3) | Any multi-frame velocity problem | Stage 4 | Pending | Getting the subscript order/cancellation wrong | [[../concepts/relative-velocity]] |

## Stage 5 Concepts (Ch 5 — The Laws of Motion) — verified against source 2026-07-07, no changes needed

| Concept | Depends on | Unlocks | Unit introduced | Unit mastered | Common confusion | Page |
|---|---|---|---|---|---|---|
| Force, Newton's 1st/2nd/3rd laws | Vectors (Stage 3), acceleration (Stage 2/4) | All of dynamics, every later chapter | Stage 5 | Pending | Mixing up action-reaction pairs (they act on different objects) | [[../concepts/newtons-first-law]], [[../concepts/newtons-second-law]], [[../concepts/newtons-third-law]] |
| Mass vs. weight, normal force, friction | Newton's 2nd law | Inclined-plane and connected-object problems | Stage 5 | Pending | Confusing kg (mass) with N (weight) | [[../concepts/mass-vs-weight]], [[../concepts/normal-force]], [[../concepts/friction]] |
| Free body diagrams | Force concept | Every dynamics problem for the rest of the course | Stage 5 | Pending | Drawing forces the object exerts on others instead of forces on it | [[../concepts/free-body-diagram]] |

## Later Stages

⚠ **Known gap (flagged 2026-07-07, narrowed after Stage 4/5 review same day):** Stage packets 2 and 6–18 already exist in `wiki/stages/` with their own concept pages, but their concepts were never backfilled into this map after the cruise-prep build session. This map now documents Stages 1, 3, 4, and 5. Backfilling Stage 2 and Stages 6–18 is real but separate work — see `wiki/log.md` 2026-07-07 entries and [[parking-lot]].
