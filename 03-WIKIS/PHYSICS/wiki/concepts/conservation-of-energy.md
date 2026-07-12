---
type: concept
status: draft
---

# Conservation of Energy

## What Is the Physical Idea?

In an isolated system (no external forces doing work), the total mechanical energy cannot change. Kinetic and potential energy continuously convert into each other, but their sum — E_mech — stays the same at every moment and every position along the path.

When friction or another nonconservative force is present, mechanical energy is not conserved — some is converted to thermal energy (heat). But the *total* energy of the universe is still conserved; we just can't recover the thermal portion as motion again.

## What Real-World Situation Does It Describe?

- A pendulum swinging (ignoring air resistance): fastest at the bottom, momentarily stopped at the top — total E_mech constant throughout.
- A roller coaster on a frictionless track: height converts to speed, speed converts to height.
- A ball thrown vertically: rises until K = 0 (U_g maximum), falls until U_g = 0 (K maximum again).
- With friction: a block sliding down a ramp reaches a lower final speed because f_k d of energy is lost to heat.

## Objects / System Involved

The system must include the object(s) and all sources of potential energy (the Earth for gravity, the spring for elastic PE). The system boundary determines whether forces are internal or external.

## Quantities That Change

K and U change continuously. E_mech = K + U stays constant (no friction) or decreases by f_k d (with friction).

## Model / Equation

**No friction (isolated, conservative forces only):**
```
Ki + Ui = Kf + Uf
```
Equivalently: ΔE_mech = 0

**With kinetic friction (friction force f_k acts over distance d):**
```
Ki + Ui - f_k d = Kf + Uf
```
Equivalently: ΔE_mech = -f_k d

**Written out in full (gravity only):**
```
½mv_i² + mgy_i = ½mv_f² + mgy_f         (no friction)
½mv_i² + mgy_i - f_k d = ½mv_f² + mgy_f  (with friction)
```

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| K | kinetic energy = ½mv² | J |
| U | potential energy (gravity or spring) | J |
| f_k | kinetic friction force = μ_k N | N |
| d | distance over which friction acts | m |
| subscript i | initial state | — |
| subscript f | final state | — |

## Calculus Connection

None for applying conservation. The underlying reason conservative forces conserve energy does involve path-independence of work integrals (W = ∫F·dr), but you don't need that to use the equation.

## Diagram / Visual Model

**Step 1:** Draw the initial state (label height, speed, spring compression).
**Step 2:** Draw the final state (label height, speed, spring compression).
**Step 3:** Write Ki + Ui = Kf + Uf, substitute, solve.

Never draw the path between states — energy conservation doesn't care about the path, only the endpoints.

```
    [A] ball at top, v_A = 0, height h
         |
         | (any path — doesn't matter)
         |
    [B] ball at bottom, v_B = ?, height = 0 (reference)

    Ki + Ui = Kf + Uf
    0 + mgh = ½mv_B² + 0
    v_B = √(2gh)
```

## Problem Types That Use This

- [[../problem-types/energy-conservation-no-friction]]
- [[../problem-types/energy-conservation-with-friction]]

## Common Beginner Mistake

**Picking an inconsistent reference height.** You are free to choose y = 0 anywhere, but you must use the same reference for all height calculations in that problem. Choosing y = 0 at the top for initial state and y = 0 at the bottom for final state in the same problem gives wrong answers.

The fix: pick y = 0 at the lowest point the object reaches, draw it on the diagram, and measure all heights from that line.

## Practice Next

Start with no-friction problems (roller coaster, pendulum). Then add friction (block on ramp). See [[../drills/energy-conservation-drill]].

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 8.1–8.3.
