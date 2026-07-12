---
type: problem-type
status: draft
---

# Problem Type: Work-Energy Theorem Problems

## How to recognize it

The problem asks for a final speed (or initial speed, or stopping distance) and you know the forces acting over a displacement — but not the time of travel. 

Key triggers: "find the speed after...", "how far does it take to stop...", "find the velocity when...", forces given but no time information.

## Given information (typical)

- Mass of the object
- Initial speed (possibly zero = "starts from rest")
- All forces acting and the displacement over which they act
- OR: initial and final speeds, and you need to find work or force

## Unknown requested

- Final speed (most common)
- Stopping distance
- Work done by one specific force (when other forces and speed change are known)

## Diagram to draw

Energy bar chart:

```
BEFORE:               AFTER:
|  K_i  |             |    K_f    |

If W_net > 0:  K_f bar is taller
If W_net < 0:  K_f bar is shorter
```

Also draw a free-body diagram to identify all forces.

## Equations

```text
W_net = ΔK = ½mv_f² − ½mv_i²

W_net = W₁ + W₂ + ... (sum work from each force)
```

## Solving pattern

1. Draw a free-body diagram — list all forces.
2. Compute the work done by each force over the given displacement.
3. Sum all works: W_net = ΣW.
4. Apply W_net = ½mv_f² − ½mv_i².
5. Solve for the unknown (v_f, d, or a specific force's work).
6. Check units: W in J, m in kg, v in m/s.

## Unit check

W_net = ΔK: [J] = [kg][m²/s²] ✓

## Common traps

- **Summing all works, not just one force**: W_net must include friction, gravity (if vertical component), normal force (usually zero), applied force, etc.
- **Starting from rest means K_i = 0**: Many problems give v_i = 0 — simplifies to W_net = ½mv_f².
- **Negative W_net means slowing down, not impossible**: If friction or opposing forces dominate, the object decelerates. ΔK < 0 is physical.
- **Using net force × distance instead of work sum**: This only works if all forces act in the same direction and over the same path. Calculate each force's work separately.

## Drills

[[../drills/work-energy-theorem-drill]]

## Example

See [[../worked-examples/work-energy-speed-example]].
