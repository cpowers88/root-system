---
type: problem-type
timeline: reference
status: draft
---

# Problem Type — Friction Problems

## How to Recognize It

A problem involving static or kinetic friction — either finding the friction force, determining whether an object will move, finding the acceleration given friction, or finding a coefficient of friction from experimental data.

**Keywords:** "coefficient of friction," "rough surface," "μ_s," "μ_k," "does it slide?", "minimum force to move," "slides at constant velocity," "friction force."

## Given Information

- Mass of object m
- Coefficient(s) of friction: μ_s (static) and/or μ_k (kinetic)
- Applied force (magnitude and direction)
- Surface orientation (horizontal, inclined)

## Unknown Requested

- Does the object move? (Compare applied force to maximum static friction)
- What is the friction force? (Depends on whether static or kinetic applies)
- What is the acceleration? (Use kinetic friction in ΣF = ma)
- What is μ_k? (From constant-velocity experiment: ΣF = 0, so F_applied = f_k)
- At what angle does it slide? (tan θ = μ_s for inclined surfaces)

## Diagram

FBD with friction arrow opposite to motion (kinetic) or opposite to tendency of motion (static). On a horizontal surface:

```
  f_friction <--[object]--> F_applied   (kinetic, moving right)
  f_static <-- [object] ... F_applied   (static, tendency to move right)
```

## Decision Tree for Friction Problems

```
Is the object moving?
  YES → kinetic friction applies: f_k = μ_k × n (fixed value, exact)
  NO  → static friction applies: f_s ≤ μ_s × n
         Is an external force applied?
           YES → Compare F_applied to f_s,max = μ_s × n
                 F_applied ≤ f_s,max → object stays still; f_s = F_applied exactly
                 F_applied > f_s,max → object starts moving; switch to kinetic friction
           NO  → f_s = 0 (nothing trying to slide it)
```

## Equations

$$f_k = \mu_k n \qquad \text{(kinetic — exact)}$$
$$f_s \leq \mu_s n \qquad \text{(static — up to maximum)}$$

Always find n first from ΣF_perp = 0.

## Solving Pattern

1. Identify whether kinetic or static friction applies (is the object moving?).
2. Find the normal force from ΣF_perp = 0 (remember: n = mg cosθ on an incline).
3. Compute the maximum static friction (if checking whether it moves) or the kinetic friction force.
4. Apply ΣF_parallel = ma to find acceleration (kinetic case) or confirm equilibrium (static case).
5. Check: friction force should not exceed μ_s × n (static case) or equal exactly μ_k × n (kinetic case).

## Finding μ from Experiment

If an object slides at **constant velocity** with applied force F:
ΣF = 0 → F = f_k = μ_k × n → μ_k = F / n

If an object is on a slope at the **angle of impending motion** (just barely about to slide):
ΣF_along = 0 → mg sinθ = μ_s × mg cosθ → μ_s = tanθ

## Unit Check

Friction force in N (same units as force). Coefficient μ is dimensionless (no units). n in N.

## Traps

- Confusing static and kinetic: static friction adjusts; kinetic does not.
- Using mg instead of mg cosθ for normal force on an incline.
- Setting f_s = μ_s n when the object is merely at rest (not at impending motion).
- Forgetting that friction can act up a slope (when object tends to slide down) or down a slope (when object is pulled up and friction opposes upward motion).

## Drills

[[../drills/friction-problems-drill]], [[../drills/inclined-plane-drill]]
