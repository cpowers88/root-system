---
type: map
timeline: reference
reference_priority: core
tags: [physics, math]
---

# Equation Map

## Purpose

Track equations by meaning, variables, units, assumptions, and problem types.

## Stage 1 — Physics and Measurement (Ch 1)

| Equation | Plain-English meaning | Variables | Units | Assumptions | Use when | Do not use when | Problem type | Page |
|---|---|---|---|---|---|---|---|---|
| ρ = m/V | Density is mass packed into a volume | ρ = density, m = mass, V = volume | kg/m³ | Material is uniform (no air pockets, mixed materials, etc.) | Comparing materials, finding mass/volume of a uniform object | Object is hollow or non-uniform without adjustment | Density/mass/volume problems | [[equations/density]] |

## Stage 2 — Motion in One Dimension (Ch 2)

| Equation family | Meaning | Assumption | Route |
|---|---|---|---|
| `v = dx/dt`, `a = dv/dt`, `Delta x = integral(v dt)`, constant-acceleration equations | motion moves between position, velocity, and acceleration through slopes/areas | the five algebraic kinematic equations require constant acceleration | [[equations/kinematic-equations]], [[calculus-links/kinematics-derivatives]] |

Chapter 1 is mostly conceptual rather than equation-heavy — units, conversions, and significant figures are *methods*, not equations. Dimensional analysis is covered as a method/tool, with its own page since Chris will reuse it every chapter.

## Stage 3 — Vectors (Ch 3)

| Equation | Plain-English meaning | Variables | Units | Assumptions | Use when | Do not use when | Problem type | Page |
|---|---|---|---|---|---|---|---|---|
| x = r cos θ, y = r sin θ, r = √(x²+y²), tan θ = y/x | Converts between distance/angle and horizontal/vertical description of the same point | x, y = Cartesian; r = radial distance; θ = angle from +x axis | m (x, y, r); degrees or radians (θ) | θ measured counterclockwise from +x axis; r always positive | Given one coordinate form, need the other | Adding two vectors directly (convert to Cartesian, add, convert back) | Polar/Cartesian conversion | [[equations/polar-cartesian-conversion]] |
| Ax = A cos θ, Ay = A sin θ; A = √(Ax²+Ay²) | Breaks a vector into perpendicular pieces, or rebuilds magnitude/direction from pieces | A = magnitude; Ax, Ay = components; θ = angle from +x axis | same unit as A | θ measured from +x axis | Any vector given as magnitude+angle, or as components | — | Vector decomposition | [[equations/vector-decomposition]] |
| Rx = Ax+Bx, Ry = Ay+By | Add vectors by adding components separately | A, B = vectors being added; R = resultant | same unit as inputs | Vectors already in component form | Adding two or more vectors | Trying to add magnitudes directly | Vector addition | [[equations/vector-addition-by-components]] |
| A⃗·B⃗ = AB cos θ = AxBx+AyBy (preview — see note) | Collapses two vectors into one scalar number (how much they align) | A, B = magnitudes; θ = angle between them | product of the two vectors' units | — | Not required until Stage 7 (work) | — | — | [[equations/dot-product]] |

**Note on the dot product row above:** kept in Stage 3 for reference since the page already exists, but the textbook (and this map) treat it as **Stage 7 material** — see the Parked for Later section of [[stages/stage-3-vectors]].

## Stage 4 — Motion in Two Dimensions (Ch 4)

| Equation | Plain-English meaning | Variables | Units | Assumptions | Use when | Do not use when | Problem type | Page |
|---|---|---|---|---|---|---|---|---|
| x(t), y(t), vₓ(t), vᵧ(t) projectile equations | 1D kinematics applied independently to x and y | v₀, θ₀, g, t | m, m/s, m/s² | No air resistance; g constant and downward | Any projectile launch | Air resistance is significant | Projectile motion | [[equations/projectile-motion-equations]] |
| a_c = v²/r = ω²r | Inward acceleration from changing direction at constant speed | v, r, ω | m/s² | Speed constant, circular path | Uniform circular motion | Speed is also changing (use tangential+radial instead) | Circular motion | [[equations/centripetal-acceleration]] |
| a_t = dv/dt, a_r = v²/r, a = √(a_r²+a_t²) | Splits acceleration on a curved path into speed-change and direction-change pieces | v, r, a_r, a_t | m/s² | Path has a well-defined radius of curvature | Speed changing along a curved path (non-uniform circular motion) | Speed is constant (reduces to plain a_c) | Non-uniform circular motion | [[equations/tangential-and-radial-acceleration]] |

## Stage 5 — The Laws of Motion (Ch 5) — verified against source 2026-07-07, no changes needed

| Equation | Plain-English meaning | Variables | Units | Assumptions | Use when | Do not use when | Problem type | Page |
|---|---|---|---|---|---|---|---|---|
| ΣF = ma | Net force causes acceleration | F, m, a | N, kg, m/s² | Constant mass, inertial reference frame | Any dynamics problem | Force is varying and calculus is required (Stage 7+) | FBD problems | [[equations/newtons-second-law]] |
| w = mg | Weight from mass and local gravity | w, m, g | N, kg, m/s² | Near Earth's surface | Finding weight from mass or vice versa | — | Mass-vs-weight problems | [[equations/weight]] |
| f_k = μ_k n, f_s ≤ μ_s n | Friction force from normal force and a material coefficient | f, μ, n | N, dimensionless, N | Surfaces already in relative motion (kinetic) or not yet moving (static) | Any friction problem | — | Friction problems | [[equations/kinetic-friction]], [[equations/static-friction]] |

## Stages 6-18 Equation Route

| Stage | Equation family | Route |
|---|---|---|
| 6 | `a_c = v^2/r`, radial net force, linear/quadratic drag, terminal speed | [[equations/centripetal-force]], [[equations/terminal-velocity]] |
| 7 | `W = Fd cos(theta)`, `W = integral(F dx)`, `K = 1/2 mv^2`, `W_net = Delta K`, potential energy | [[equations/work-constant-force]], [[equations/kinetic-energy]], [[equations/work-energy-theorem]], [[equations/gravitational-pe]], [[equations/spring-pe]] |
| 8 | mechanical-energy conservation and `P = dE/dt` | [[equations/conservation-of-mechanical-energy]], [[equations/power]] |
| 9 | `p = mv`, impulse-momentum, collision conservation | [[equations/momentum]], [[equations/impulse-momentum-theorem]], [[equations/collision-equations]] |
| 10 | angular kinematics, torque, `sum(tau) = I alpha`, rotational energy, rolling | [[equations/angular-kinematics-equations]], [[equations/torque]], [[equations/moment-of-inertia]], [[equations/rotational-newtons-second-law]], [[stages/stage-10-rotation]] |
| 11 | angular momentum, `sum(tau_ext) = dL/dt`, conservation | [[equations/angular-momentum]], [[equations/conservation-angular-momentum]] |
| 12 | `sum(F) = 0`, `sum(tau) = 0`, elastic modulus | [[equations/equilibrium-conditions]], [[equations/youngs-modulus]] |
| 13 | universal gravitation, general gravitational energy, orbit relations | [[equations/newtons-law-of-gravitation]], [[equations/gravitational-pe-general]], [[equations/orbital-mechanics]] |
| 14 | pressure, depth, buoyancy, continuity, Bernoulli | [[stages/stage-14-fluid-mechanics]] |
| 15 | sinusoidal SHM, spring/pendulum periods, oscillator energy | [[equations/shm-equations]], [[equations/spring-mass-period]], [[equations/pendulum-period]], [[equations/shm-energy]] |
| 16 | wave function/speed, intensity, sound, Doppler | [[stages/stage-16-wave-motion]] |
| 17 | standing-wave and resonance conditions, beat frequency | [[equations/standing-wave-equations]], [[stages/stage-17-superposition]] |
| 18 | Lorentz factor, time dilation, length contraction, transformations, relativistic momentum/energy | [[equations/relativity-equations]] |
