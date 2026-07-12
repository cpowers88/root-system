---
type: common-errors
stage: 8
chapter: 8
---

# Common Errors — Stage 8: Conservation of Energy

## Error 1: Applying energy conservation when the system is nonisolated

**Mistake:** Writing Ki + Ui = Kf + Uf even when friction or an applied external force acts on the system.

**Why it's wrong:** Mechanical energy is only conserved in an isolated system with no nonconservative forces. Friction converts mechanical energy into thermal energy — it doesn't disappear, but it's no longer "mechanical."

**Correct approach:** Use the generalized energy equation: Kf + Uf = Ki + Ui − f_k · d (subtract friction loss) or Kf + Uf = Ki + Ui + W_ext (add work done by external force).

---

## Error 2: Using the wrong reference height for gravitational PE

**Mistake:** Choosing different reference heights (y = 0) at different points in the problem, or choosing a reference that makes the initial PE negative when it could be zero.

**Why it's wrong:** The reference height is arbitrary, but you must use the same reference throughout the entire problem. If you set y = 0 at the bottom of a ramp, all heights measured upward are positive.

**Correct approach:** Set y = 0 at the lowest point in the problem at the start. Then all heights are positive and the calculation is cleaner. State your choice explicitly.

---

## Error 3: Forgetting to include all forms of mechanical energy

**Mistake:** Writing ½mv² = mgh and forgetting that a rolling object has both translational and rotational kinetic energy.

**Why it's wrong:** KE_total = ½mv² + ½Iω². If the object rolls without slipping, both terms matter. Ignoring rotational KE leads to an overestimate of the final speed.

**Correct approach:** In Stage 8, if the problem involves only sliding (no rolling), then KE = ½mv² only. But when Ch 10 arrives, always check: is the object rolling? If yes, include ½Iω².

---

## Error 4: Confusing power with energy

**Mistake:** Using P = W/t (power) when the question asks for total energy, or forgetting to multiply power by time to get energy.

**Why it's wrong:** Power (W or J/s) is the rate of energy transfer. Energy (J) is the total amount transferred. They are related by W = P · t.

**Correct approach:** Read carefully. "How much energy does the motor deliver in 5 minutes?" → W = P · t. "How fast does the motor do work?" → P = W/t.

---

## Error 5: Not accounting for both endpoints correctly

**Mistake:** Taking "before" as the initial condition but using an intermediate position as "after," or vice versa.

**Why it's wrong:** Energy conservation applies between any two well-defined states, but both endpoints must be fully specified (position, speed) for the equation to work.

**Correct approach:** Clearly label State 1 (before) and State 2 (after). Write all quantities for each state before writing the conservation equation.

---

## Error 6: Forgetting that spring PE is ½kx², not kx

**Mistake:** Writing the spring's potential energy as U_s = kx instead of U_s = ½kx².

**Why it's wrong:** The ½ comes from the integration of Hooke's law (F = kx) over displacement. It is not optional.

**Correct approach:** Memorize: U_spring = ½kx². The ½ is always there. Check with dimensional analysis: [k][x²] = (N/m)(m²) = N·m = J ✓.
