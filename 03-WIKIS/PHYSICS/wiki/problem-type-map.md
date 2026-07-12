---
type: map
tags: [reference, physics]
---

# Problem-Type Map

## Purpose

Classify physics problems by recognition pattern.

## Stage 1 — Physics and Measurement (Ch 1)

| Problem type | How to recognize it | Given usually includes | Unknown usually asks for | Diagram | Equations | Common traps | Page |
|---|---|---|---|---|---|---|---|
| Dimensional consistency check | "Show that this equation is dimensionally correct/incorrect," or you derived a formula and want to sanity-check it | An equation with symbols, told which quantities the symbols represent | Whether dimensions match on both sides | None — substitute L/M/T for each symbol instead | [v]=L/T, [a]=L/T² | Forgetting that addition/subtraction requires matching dimensions; thinking dimensional analysis finds numeric constants | [[../problem-types/dimensional-consistency-check]] |
| Unit conversion | Quantity given in one unit system, asked for it in another | A value with units, a conversion factor (or a need to look one up) | Same quantity, different units | None | Multiply by conversion ratio = 1 | Putting the conversion factor upside down; forgetting to convert every unit in a compound quantity (e.g., m/s to mi/h needs both length and time conversion) | [[../problem-types/unit-conversion]] |
| Order-of-magnitude estimation | "Estimate...", asks for a power-of-ten answer, no precise data given | A real-world scenario, rough/no numbers | An answer "to the nearest power of ten" | Often none, sometimes a simple model | None — uses reasonable assumed values | Trying to be precise instead of reasonable; not stating assumptions | [[../problem-types/order-of-magnitude-estimation]] |
| Significant-figure arithmetic | A calculation combining measured values; asks "how many sig figs" or for a properly rounded final answer | Several measured numbers to combine | A correctly rounded result | None | Multiplication/division rule vs. addition/subtraction rule | Applying the multiplication rule to an addition problem (or vice versa); rounding too early in a multi-step calculation | [[../problem-types/sig-fig-arithmetic]] |

## Stage 3 — Vectors (Ch 3)

| Problem type | How to recognize it | Given usually includes | Unknown usually asks for | Diagram | Equations | Common traps | Page |
|---|---|---|---|---|---|---|---|
| Polar ↔ Cartesian conversion | Point/vector given as (x,y) or (r,θ), asked for the other | One coordinate pair | The other coordinate pair | Right triangle, origin, angle from +x axis | x=r cos θ, y=r sin θ, r=√(x²+y²), tan θ=y/x | Forgetting the quadrant check on tan⁻¹; reporting r as negative | [[../problem-types/polar-cartesian-conversion]] |
| Vector decomposition | A vector given as magnitude + angle; need its x/y pieces | Magnitude A, angle θ | Ax and Ay | Vector on axes with angle labeled | Ax = A cos θ, Ay = A sin θ | Using sin/cos backwards when θ is measured from the wrong axis | [[../problem-types/vector-decomposition]] |
| Vector addition | Two or more vectors given, need the resultant | Multiple vectors as magnitude+angle or components | Resultant magnitude and direction | Tip-to-tail sketch of all vectors | Rx=ΣAx, Ry=ΣAy, then magnitude/direction formulas | Adding magnitudes directly instead of components | [[../problem-types/vector-addition]] |

## Stage 4 — Motion in Two Dimensions (Ch 4)

| Problem type | How to recognize it | Given usually includes | Unknown usually asks for | Diagram | Equations | Common traps | Page |
|---|---|---|---|---|---|---|---|
| Projectile — horizontal launch | Object launched purely horizontally, falls under gravity | v₀, launch height h | Range, time of flight, landing velocity | Parabolic path from a height | x=v₀t, y=h−½gt² | Assuming vₓ changes; forgetting the object starts with vᵧ=0 | [[../problem-types/projectile-horizontal-launch]] |
| Projectile — angled launch | Object launched at an angle above horizontal | v₀, θ₀ | Max height, time of flight, range | Full parabolic arc | v₀ₓ=v₀cosθ₀, v₀ᵧ=v₀sinθ₀, kinematics in each axis | Using the range formula when launch/landing heights differ | [[../problem-types/projectile-angled-launch]] |
| Circular motion (uniform) | Constant speed around a circle/arc | Two of {v, r, a_c, T} | The third quantity, or required force | Object on circle, v tangent, a_c inward | a_c=v²/r, F_c=mv²/r, T=2πr/v | Treating "centripetal force" as a separate force | [[../problem-types/circular-motion]] |
| Non-uniform circular motion | Curved path AND speed is changing | r, v, and dv/dt (or enough to find it) | Total acceleration, or one component | Two perpendicular arrows: a_r inward, a_t along path | a_r=v²/r, a_t=dv/dt, a=√(a_r²+a_t²) | Reporting only a_r; adding components instead of using Pythagorean theorem | [[../problem-types/nonuniform-circular-motion]] |
| Relative velocity | Multiple reference frames (boat/river, plane/wind) | Velocities in two frames | Velocity in a third frame, or resultant | Vector triangle of the three velocities | v⃗_PA = v⃗_PB + v⃗_BA | Wrong subscript order; sign error on reversed subscripts | (see [[../concepts/relative-velocity]]) |

## Stage 5 — The Laws of Motion (Ch 5) — verified against source 2026-07-07, no changes needed

| Problem type | How to recognize it | Given usually includes | Unknown usually asks for | Diagram | Equations | Common traps | Page |
|---|---|---|---|---|---|---|---|
| FBD — single object | One object, forces acting on it, flat or inclined surface | Masses, angles, applied forces | Acceleration or an unknown force | Free body diagram (dot + force arrows) | ΣF=ma in x and y | Drawing forces the object exerts on others | [[../problem-types/fbd-single-object]] |
| FBD — connected objects | Two or more objects linked by a string/rope | Masses, connection type | Common acceleration, tension | Separate FBD for each object | ΣF=ma per object, shared a and T | Forgetting acceleration and tension are shared/linked | [[../problem-types/fbd-connected-objects]] |
| Inclined plane | Object on a ramp/slope | Angle θ, mass, friction coefficient | Acceleration, forces along/perpendicular to incline | Tilted axes aligned with incline | w_x=mg sinθ, w_y=mg cosθ | Using horizontal/vertical axes instead of incline-aligned axes | [[../problem-types/inclined-plane]] |
| Atwood machine | Two masses connected over a pulley | Two masses | Acceleration, tension | FBD for each hanging mass | ΣF=ma for each mass, shared T and a | Sign convention inconsistent between the two masses | [[../problem-types/atwood-machine]] |
| Friction problems | Object with friction specified (static or kinetic) | μ_s and/or μ_k, normal force info | Whether motion starts, or the friction force magnitude | FBD with friction opposing motion/tendency | f_k=μ_k n, f_s≤μ_s n | Using μ_s when object is already moving (should be μ_k) | [[../problem-types/friction-problems]] |

## Later Stages

⚠ **Known gap (flagged 2026-07-07, narrowed after Stage 4/5 review same day):** Stage 2 and Stages 6–18 already have built problem-type pages, but were never backfilled into this map. Stages 1, 3, 4, and 5 are current here. Problem types accumulate as the course progresses — e.g., Stage 2's "constant acceleration" recognizer assumes Chris is already fluent with the unit/dimension checks above.
