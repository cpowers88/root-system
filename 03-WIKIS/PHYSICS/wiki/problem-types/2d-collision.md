---
type: problem-type
timeline: reference
stage: 9
chapter: 9
---

# Problem Type: 2D Collision

## How to Recognize

A collision where objects move in more than one direction before or after the impact. Often described as a "glancing blow" or involves intersecting paths.

Keywords: "2D collision," "glancing," "at an angle," "two-dimensional," "intersection" (car crash at an intersection).

## Given Information

- Masses m₁, m₂
- Initial speeds and directions (angles from a reference axis)
- Often: one object is at rest before the collision
- Sometimes: one final speed and angle are given; other final velocity is the unknown

## Unknown Requested

- Final speed and/or direction of one or both objects

## Diagram to Draw

Draw x-y axes. Show both objects before with velocity arrows labeled with speed and angle. Show both objects after.

```
     y
     ↑
     |   → [m₁ at v₁ᵢ along +x]    [m₂ at rest]
     |
     +-------→ x

After collision:
     [m₁ at v₁f, angle +37° above x-axis]
     [m₂ at v₂f, angle −θ₂ below x-axis]
```

## Equations

Apply momentum conservation separately in x and y:

```
x: m₁v₁ᵢ·cos θ₁ᵢ + m₂v₂ᵢ·cos θ₂ᵢ = m₁v₁f·cos θ₁f + m₂v₂f·cos θ₂f

y: m₁v₁ᵢ·sin θ₁ᵢ + m₂v₂ᵢ·sin θ₂ᵢ = m₁v₁f·sin θ₁f + m₂v₂f·sin θ₂f
```

This gives two equations. If the collision is elastic, add kinetic energy conservation for a third equation (needed if two unknowns remain).

## Solving Pattern

1. Draw diagram with x-y axes and label all angles from +x axis.
2. Write x-momentum equation. Substitute known values.
3. Write y-momentum equation. Substitute known values.
4. From the two equations, extract the x and y components of the unknown velocity.
5. Combine: speed = √(vx² + vy²), angle = arctan(|vy/vx|) from +x axis.
6. If elastic: verify KE is conserved as a check.

## Unit Check

All momentum terms in kg·m/s; speed in m/s. ✓

## Traps

- **Missing the y-equation:** Students write only the x momentum equation. You need both x and y for 2D.
- **Sign error in y-direction:** If m₁ moves upward and m₂ must move downward (by symmetry or by calculation), the y-component of m₂'s momentum is negative. Forgetting this sign will give wrong answers.
- **Angle measurement:** All angles should be measured from the +x axis consistently. Mixing "from the vertical" and "from the horizontal" causes errors.
- **Forgetting to recombine components:** After finding vx and vy of the unknown, you must use Pythagorean theorem and arctan to get the final speed and angle.

## Worked Example

[[../worked-examples/2d-collision-example]]

## Drill

[[../drills/collision-drill]] — Part D
