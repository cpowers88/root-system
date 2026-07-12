---
type: problem-type
status: draft
---

# Problem Type: Work Calculation

## How to recognize it

The problem asks: "How much work does [force] do on [object] as it moves [distance]?" or "Find the work done by each force."

Key triggers: force at an angle, displacement over a distance, multiple forces listed.

## Given information (typical)

- Force magnitude and direction (or angle with the horizontal/motion)
- Displacement magnitude and direction
- Possibly: multiple forces (gravity, friction, applied)

## Unknown requested

Work done (J) by one or more forces.

## Diagram to draw

```
     F (arrow, labeled with angle θ from horizontal or from d)
      \
       \ θ
        \——————→ d (direction of motion)

Label: F cos θ is the component doing work.
```

## Equations

```text
Single force, constant:   W = F d cos θ
Sum of all forces:        W_net = W₁ + W₂ + W₃ + ...
Varying force:            W = ∫ F_x dx
```

## Solving pattern

1. Identify every force acting on the object.
2. For each force, determine the angle θ between that force and the displacement vector.
3. Compute W = F d cos θ for each force.
4. Sum the works to find W_net (needed for the work-energy theorem).
5. Note signs: force along motion = +, force opposing motion = −, force perpendicular = 0.

## Unit check

W = [N][m] = [kg·m/s²][m] = kg·m²/s² = J ✓

## Common traps

- **Angle vs. complement**: If the force makes angle α with the vertical but the displacement is horizontal, the angle for the formula is (90° − α), not α. Always measure θ FROM the displacement direction.
- **Perpendicular forces = zero work**: Normal force and gravity on level ground always do zero work on a horizontally-moving object.
- **Negative work is real work**: Friction doing −60 J is physically meaningful — it's energy removed, not "no work."

## Drills

[[../drills/work-calculation-drill]]
