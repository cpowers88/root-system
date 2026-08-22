---
type: common-errors
timeline: reference
stage: 9
chapter: 9
---

# Common Errors — Stage 9: Linear Momentum and Collisions

## Error 1: Applying momentum conservation when external forces exist

**Mistake:** Using m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f even when a significant external force acts during the collision (like gravity pulling down on a pendulum during a long collision).

**Why it's wrong:** Conservation of momentum requires ΣF_ext = 0. Gravity is always there, but for a very brief collision, the impulse due to gravity (F·Δt) is negligible compared to the impulsive collision force. For slow or prolonged collisions, this assumption breaks down.

**Correct approach:** Check whether the collision is brief enough that external impulses can be ignored. For the ballistic pendulum, the collision is instantaneous — apply momentum conservation for the collision, then energy conservation afterward for the swing.

---

## Error 2: Treating "inelastic" as "both objects stop"

**Mistake:** Thinking that because kinetic energy is lost, both objects must come to rest.

**Why it's wrong:** Kinetic energy is not conserved, but momentum still is. Objects continue moving — just with different speeds and/or directions. Only in a perfectly inelastic head-on collision where the center of mass is at rest do both objects stop after colliding.

**Correct approach:** Apply momentum conservation to find the final velocity. If both objects end up with vf = 0, that means p_total was zero before the collision — a special case, not the norm.

---

## Error 3: Forgetting that momentum is a vector

**Mistake:** Adding speeds (magnitudes) instead of velocities (signed quantities) when setting up momentum conservation.

**Why it's wrong:** An object moving left with speed 5 m/s has p = −5m, not +5m. If two equal-mass objects approach each other head-on at 5 m/s and collide perfectly inelastically, the final speed is 0, not 5.

**Correct approach:** Always define a positive direction at the start. Assign signs to every velocity before plugging in. The equation must have signed velocities, not speeds.

---

## Error 4: Using the elastic collision formulas without checking both conditions

**Mistake:** Applying v₁f = [(m₁ − m₂)/(m₁ + m₂)]v₁ᵢ even when the problem is not elastic.

**Why it's wrong:** Those formulas were derived assuming both momentum AND kinetic energy are conserved. If the problem says "collision" without specifying elastic, it may be inelastic.

**Correct approach:** Read the problem carefully. "Elastic" or "kinetic energy conserved" → use both conservation equations. "Stick together" → perfectly inelastic. "Collision" with energy loss stated → inelastic, use only momentum conservation plus the energy loss equation.

---

## Error 5: Applying energy conservation during the collision phase

**Mistake:** Using ½m₁v₁ᵢ² = ½m₁v₁f² + ½m₂v₂f² for a perfectly inelastic collision, then getting an unsolvable equation.

**Why it's wrong:** Mechanical energy is not conserved during an inelastic collision (it converts to heat, sound, deformation). You only have one conservation equation — momentum — and one unknown (vf), so the system is solvable without energy conservation.

**Correct approach:** For perfectly inelastic: use momentum only → find vf. For elastic: use both momentum and kinetic energy → solve the system of two equations for two unknowns.

---

## Error 6: Forgetting to work in components for 2D collisions

**Mistake:** Trying to apply momentum conservation as a single scalar equation in 2D.

**Why it's wrong:** Momentum is a vector. In 2D there are two independent equations — one for x and one for y.

**Correct approach:** Draw the before-and-after diagram with explicit angles. Decompose each momentum vector: px = mv·cos θ, py = mv·sin θ. Write two separate equations. Solve each independently.
