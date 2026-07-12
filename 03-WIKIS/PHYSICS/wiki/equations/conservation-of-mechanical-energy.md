---
type: equation
status: draft
---

# Conservation of Mechanical Energy

## Equation

**No friction (isolated system, conservative forces only):**
```
Ki + Ui = Kf + Uf
```

**With kinetic friction (friction force f_k over distance d):**
```
Ki + Ui - f_k d = Kf + Uf
```

**Expanded with gravitational PE and spring PE:**
```
½mv_i² + mgy_i + ½kx_i² - f_k d = ½mv_f² + mgy_f + ½kx_f²
```

## Meaning in Plain English

The total mechanical energy at the start equals the total mechanical energy at the end — minus whatever was lost to friction along the way. Energy doesn't disappear; it either stays as mechanical energy or becomes thermal energy (heat) from friction.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| K = ½mv² | kinetic energy | J |
| U_g = mgy | gravitational potential energy | J |
| U_s = ½kx² | spring potential energy | J |
| f_k | kinetic friction force | N |
| d | distance friction acts | m |
| m | mass | kg |
| v | speed | m/s |
| g | 9.80 m/s² | m/s² |
| y | height above reference | m |
| k | spring constant | N/m |
| x | spring stretch or compression | m |
| subscript i | initial state | — |
| subscript f | final state | — |

## Units Check

Every term must have units of joules (J = kg·m²/s²).
- K = ½mv²: kg × (m/s)² = kg·m²/s² = J ✓
- U_g = mgy: kg × (m/s²) × m = kg·m²/s² = J ✓
- U_s = ½kx²: (N/m) × m² = N·m = J ✓
- f_k d: N × m = N·m = J ✓

## When to Use It

- An object moves between two states and you need speed, height, or spring compression at one state given the other.
- No need to track every intermediate force or position — only initial and final states.
- Works for: roller coasters, pendulums, balls thrown vertically, blocks on ramps, spring-launched projectiles.

## When Not to Use It

- When the question asks for a force at a specific point (use Newton's 2nd law instead).
- When energy is added externally by a motor or engine — the full energy equation becomes Ki + Ui + W_engine - f_k d = Kf + Uf.
- When the collision or interaction is inelastic (use momentum conservation, Stage 9).

## Required Assumptions

1. All potential energy types present are accounted for on both sides.
2. The same reference height (y = 0) is used throughout the problem.
3. If friction is present, the friction force f_k and the distance d are both known or can be found.

## Calculus Origin

Each PE term comes from integrating the corresponding conservative force:
- U_g = mgy comes from integrating F_gravity = mg over height.
- U_s = ½kx² comes from integrating F_spring = kx over displacement.
These integrations were done in Stage 7. The conservation equation itself requires only algebra.

## Example Problem Type

A ball of mass 0.5 kg is released from rest at height 3.0 m above the floor. Find its speed just before it hits the floor. (Answer: v = √(2gh) = √(2 × 9.80 × 3.0) = 7.67 m/s)

## Common Mistake

**Using different reference heights on the left and right sides.** Choose y = 0 once, mark it on the diagram, and never change it. A good default: y = 0 at the lowest point the object reaches in the problem.

**Forgetting spring PE when a spring is involved.** If a compressed spring launches the object, U_s must appear in the initial state even if U_g = 0 there.
