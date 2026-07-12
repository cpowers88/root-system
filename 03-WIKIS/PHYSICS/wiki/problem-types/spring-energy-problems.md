---
type: problem-type
status: draft
---

# Problem Type: Spring Energy Problems

## How to recognize it

The problem involves a spring (compressed, stretched, or releasing), possibly with a mass attached. Asks for force, energy stored, or speed of released object.

Key triggers: "spring constant k =...", "compressed/stretched by...", "released from rest", spring attached to a mass on a surface.

## Given information (typical)

- Spring constant k (N/m)
- Displacement from equilibrium x (m or cm — convert to m)
- Mass of attached object (if speed is asked)
- Whether surface is frictionless (if not, friction work must be included)

## Unknown requested

- Spring force at a given compression/extension
- Elastic PE stored in spring
- Speed of object when spring returns to equilibrium
- Compression needed to achieve a target speed

## Diagram to draw

```
 Wall          Spring           Object
  |                                
  |——[spring]——| ○mass
               ← x = compression →
               x = 0 at natural length
```

Mark equilibrium position (x = 0) and label displacement x clearly.

## Equations

```text
Hooke's Law:     F_s = −kx    (force on object, N)
Spring PE:       U_s = ½kx²  (energy stored, J)
Speed at x = 0: ½mv² = ½kx²  (frictionless, object released from rest)
```

## Solving pattern

1. Identify k and x (convert units if needed — cm → m).
2. For force: |F| = kx, direction = toward equilibrium.
3. For PE: U_s = ½kx².
4. For final speed: use energy conservation — U_s(initial) = K(final) on frictionless surface → ½kx² = ½mv² → v = x√(k/m).
5. If friction is present: U_s = K_f + W_friction loss.

## Unit check

F = kx: [N/m][m] = N ✓
U_s = ½kx²: [N/m][m²] = N·m = J ✓

## Common traps

- **Forgetting the ½ in U_s = ½kx²** — the most common arithmetic error.
- **Using total spring length as x** — x is measured from the equilibrium (natural) position, not from the wall.
- **Confusing force and energy equations** — F = kx for force, U = ½kx² for energy. They are different equations for different quantities.
- **Using x in centimeters** — k is in N/m, so x must be in meters. Always convert first.

## Drills

[[../drills/spring-energy-drill]]

## Example

See [[../worked-examples/spring-compression-example]].
