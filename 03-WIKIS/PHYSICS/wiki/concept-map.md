---
type: map
timeline: reference
reference_priority: core
tags: [physics]
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
| SI base units (length, mass, time) | none | everything | Stage 1 | Pending | Confusing mass (kg) with weight (N) | [[concepts/si-base-units]] |
| The particle model | none | all motion analysis | Stage 1 | Pending | Thinking the model is "wrong" because real objects have size | [[concepts/particle-model]] |
| Dimensional analysis | SI base units | every equation-check in the course | Stage 1 | Pending | Thinking dimensional analysis can find numerical constants (it can't) | [[concepts/dimensional-analysis]] |
| Unit conversion | SI base units | every numeric problem | Stage 1 | Pending | Multiplying by a conversion factor upside down | [[concepts/unit-conversion]] |
| Order-of-magnitude estimation | SI base units | quick sanity checks | Stage 1 | Pending | Treating an estimate as if it needs to be exact | [[concepts/order-of-magnitude-estimation]] |
| Significant figures | none | every reported answer | Stage 1 | Pending | Confusing sig-fig rule for multiplication with the rule for addition | [[concepts/significant-figures]] |

## Stage 2 Concepts (Ch 2 — Motion in One Dimension)

| Concept | Depends on | Unlocks | Unit introduced | Unit mastered | Common confusion | Page |
|---|---|---|---|---|---|---|
| Position and displacement | units, coordinate direction | velocity and all kinematics | Stage 2 | Re-check | Confusing distance with signed displacement | [[concepts/position]], [[concepts/displacement-vs-distance]] |
| Velocity | position and slope | acceleration and motion graphs | Stage 2 | Re-check | Confusing speed with velocity | [[concepts/velocity-1d]] |
| Acceleration and free fall | velocity and slope | force, projectiles, circular motion | Stage 2 | Re-check | Assuming zero velocity means zero acceleration | [[concepts/acceleration-1d]], [[concepts/free-fall]] |

## Stage 3 Concepts (Ch 3 — Vectors)

| Concept | Depends on | Unlocks | Unit introduced | Unit mastered | Common confusion | Page |
|---|---|---|---|---|---|---|
| Coordinate systems (Cartesian vs. polar) | Trigonometry (Appendix B.4) | Vector components (same triangle, applied to an arrow instead of a point); every later position/vector problem | Stage 3 | Pending | Forgetting to check the quadrant on tan⁻¹(y/x) | [[concepts/coordinate-systems]] |
| Scalar vs. vector | none | All of mechanics — every quantity is one or the other | Stage 3 | Pending | Treating a vector's magnitude as the whole answer, ignoring direction | [[concepts/scalar-vs-vector]] |
| Vector components | Coordinate systems | Vector addition, all 2D/3D motion (Stage 4+) | Stage 3 | Pending | Using sin where cos belongs (θ measured from the wrong axis) | [[concepts/vector-components]] |
| Dot product (preview — textbook formally introduces in Ch 7) | Vector components, scalar vs. vector | Work W = F⃗·d⃗ (Stage 7) | Stage 3 (preview only) | Deferred to Stage 7 | Confusing dot product (scalar result) with cross product (vector result) | [[concepts/dot-product]] |

## Stage 4 Concepts (Ch 4 — Motion in Two Dimensions)

| Concept | Depends on | Unlocks | Unit introduced | Unit mastered | Common confusion | Page |
|---|---|---|---|---|---|---|
| Projectile motion | Vector components (Stage 3), 1D kinematics (Stage 2) | Every 2D-launch problem | Stage 4 | Pending | Thinking horizontal velocity changes during flight | [[concepts/projectile-motion]] |
| Uniform circular motion | Vector components | Centripetal force (Stage 6), rotation (Stage 10) | Stage 4 | Pending | Thinking constant speed means zero acceleration | [[concepts/uniform-circular-motion]] |
| Tangential and radial acceleration | Uniform circular motion, 1D acceleration (Stage 2) | Non-uniform circular motion problems; previews rotational kinematics (Stage 10) | Stage 4 | Pending | Reporting only the centripetal piece when speed is also changing | [[concepts/tangential-and-radial-acceleration]] |
| Relative velocity | Vector addition (Stage 3) | Any multi-frame velocity problem | Stage 4 | Pending | Getting the subscript order/cancellation wrong | [[concepts/relative-velocity]] |

## Stage 5 Concepts (Ch 5 — The Laws of Motion) — verified against source 2026-07-07, no changes needed

| Concept | Depends on | Unlocks | Unit introduced | Unit mastered | Common confusion | Page |
|---|---|---|---|---|---|---|
| Force, Newton's 1st/2nd/3rd laws | Vectors (Stage 3), acceleration (Stage 2/4) | All of dynamics, every later chapter | Stage 5 | Pending | Mixing up action-reaction pairs (they act on different objects) | [[concepts/newtons-first-law]], [[concepts/newtons-second-law]], [[concepts/newtons-third-law]] |
| Mass vs. weight, normal force, friction | Newton's 2nd law | Inclined-plane and connected-object problems | Stage 5 | Pending | Confusing kg (mass) with N (weight) | [[concepts/mass-vs-weight]], [[concepts/normal-force]], [[concepts/friction]] |
| Free body diagrams | Force concept | Every dynamics problem for the rest of the course | Stage 5 | Pending | Drawing forces the object exerts on others instead of forces on it | [[concepts/free-body-diagram]] |

## Stages 6-18 Concept Route

Granular pages are linked where they exist. The stage packet is the safe fallback
when a later-stage concept page is still planned.

| Stage | Core concept flow | Physical anchor | Route |
|---|---|---|---|
| 6 | circular-force models -> nonuniform motion -> resistive force/terminal velocity -> accelerated frames | vehicle turn, banked curve, falling object | [[concepts/centripetal-force]], [[concepts/vertical-circular-motion]], [[concepts/terminal-velocity]], [[stages/stage-6-circular-motion]] |
| 7 | system -> work -> kinetic/potential energy -> conservative force -> energy diagram/equilibrium | push, lift, spring | [[concepts/work]], [[concepts/kinetic-energy]], [[concepts/potential-energy]], [[concepts/conservative-vs-nonconservative-forces]], [[stages/stage-7-energy-of-a-system]] |
| 8 | mechanical energy -> isolated/nonisolated bookkeeping -> power | braking, roller coaster | [[concepts/mechanical-energy]], [[concepts/conservation-of-energy]], [[concepts/power]] |
| 9 | momentum -> impulse -> system conservation -> collision type -> center of mass | collision and recoil | [[concepts/linear-momentum]], [[concepts/impulse]], [[concepts/conservation-of-momentum]], [[concepts/collision-types]], [[concepts/center-of-mass]] |
| 10 | angular kinematics -> torque -> moment of inertia -> rotational energy -> rolling | wheel and flywheel | [[concepts/angular-kinematics]], [[concepts/torque]], [[concepts/moment-of-inertia]], [[concepts/rotational-kinetic-energy]], [[concepts/rolling-without-slipping]] |
| 11 | cross product/right-hand rule -> angular momentum -> torque as rate -> conservation | spinning skater and gyroscope | [[concepts/angular-momentum]], [[concepts/conservation-of-angular-momentum]], [[stages/stage-11-angular-momentum]] |
| 12 | force equilibrium + torque equilibrium -> center of gravity -> stress/strain | beam and ladder | [[stages/stage-12-static-equilibrium]] |
| 13 | inverse-square gravity -> field -> orbit -> potential/total energy -> Kepler laws | satellite and planet | [[stages/stage-13-universal-gravitation]] |
| 14 | pressure -> pressure with depth -> buoyancy -> continuity -> Bernoulli -> viscosity | hydraulic system and pipe | [[concepts/pressure]], [[concepts/pressure-vs-depth]], [[concepts/buoyancy]], [[concepts/continuity-equation]], [[concepts/bernoullis-equation]] |
| 15 | restoring force -> SHM -> spring/pendulum -> oscillator energy -> damping/forcing | suspension and pendulum | [[concepts/simple-harmonic-motion]], [[concepts/spring-mass-system]], [[stages/stage-15-oscillatory-motion]] |
| 16 | disturbance -> traveling wave -> wave speed/energy -> sound/intensity -> Doppler | string, sound, moving siren | [[concepts/wave-model]], [[stages/stage-16-wave-motion]] |
| 17 | superposition -> interference -> boundary conditions -> standing waves/resonance -> beats | instrument string and pipe | [[stages/stage-17-superposition]] |
| 18 | Galilean model -> Einstein postulates -> simultaneity -> time/length effects -> relativistic momentum/energy | GPS and muons | [[stages/stage-18-relativity]] |
