---
type: common-errors
stage: 11
chapter: 11
---

# Common Errors — Stage 11: Angular Momentum

## Error 1: Confusing angular momentum L with torque τ

**Mistake:** Treating L = Iω and τ = Iα as if they describe the same thing, or using one when the other is needed.

**Why it's wrong:** L is a state quantity — how much angular momentum an object has at a moment. τ (torque) is a rate — how fast angular momentum is changing: τ = dL/dt. They are related the same way p and F are related: F = dp/dt.

**Correct approach:** Ask: "Does the problem give torque or ask about a change in L?" → use τ = dL/dt = Iα. "Does the problem involve a system with no external torque?" → use conservation of L: Lᵢ = Lf.

---

## Error 2: Applying conservation of angular momentum when external torques exist

**Mistake:** Using Iᵢωᵢ = Ifωf even when friction, an applied torque, or gravity creates a net external torque on the system.

**Why it's wrong:** Angular momentum is conserved only when the net external torque on the system is zero (Στ_ext = 0). Friction at a pivot or gravity acting with a moment arm creates nonzero torque.

**Correct approach:** Identify all forces and their moment arms (lever arms). Only if the net torque is zero can you write Lᵢ = Lf.

---

## Error 3: Forgetting that L = Iω requires ω in radians/second

**Mistake:** Substituting ω in rpm or degrees/second into L = Iω.

**Why it's wrong:** All rotational equations (α = dω/dt, L = Iω, KE = ½Iω²) require ω in rad/s. Using rpm or deg/s gives wrong units and wrong magnitude.

**Correct approach:** Convert angular velocity first: ω (rad/s) = rpm × (2π/60). Always carry the rad/s unit.

---

## Error 4: The spinning skater — confusing what changes and what doesn't

**Mistake:** Thinking that when a skater pulls in their arms, their kinetic energy is conserved (since "nothing external acts").

**Why it's wrong:** Angular momentum L = Iω is conserved. But kinetic energy KE = ½Iω² = L²/(2I) changes because I changes. With smaller I, ω increases proportionally, and KE = ½Iω² increases — the extra energy comes from the skater's muscles doing internal work as they pull their arms in.

**Correct approach:** Use Lᵢ = Lf to find the new ω. Then separately compute KE_i and KE_f — expect KE to increase. The "extra" energy is from the skater's biological work.

---

## Error 5: Applying L = Iω when the object is not rotating about a fixed axis

**Mistake:** Using L = Iω for a particle moving in a straight line.

**Why it's wrong:** A particle moving in a straight line also has angular momentum about any off-axis point: L = mvr_⊥ (where r_⊥ is the perpendicular distance from the point to the line of motion). This is a different formula.

**Correct approach:** L = Iω is for rigid bodies rotating about an axis. L = mvr_⊥ (or L⃗ = r⃗ × p⃗) is for particles or the general case. In this course, most problems use L = Iω for rotating rigid bodies.

---

## Error 6: Wrong sign or direction for angular momentum

**Mistake:** Ignoring the vector nature of L when the rotation axis direction matters.

**Why it's wrong:** L⃗ is a vector (using the right-hand rule: curl fingers in the direction of rotation, thumb points in the direction of L⃗). For a 2D problem (rotation in a plane), clockwise is typically negative and counterclockwise positive.

**Correct approach:** Define your positive rotation direction at the start. Assign consistent signs to all angular quantities. If torque and L are in opposite directions, the object decelerates.
