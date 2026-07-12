---
type: problem-type
status: draft
---

# Problem Type — FBD: Single Object

## How to Recognize It

One object, multiple forces. The problem asks for acceleration, an unknown force (tension, normal force, friction), or whether the object moves. You're not dealing with connected objects or pulleys.

**Keywords:** "A block is pushed," "a crate slides," "a hanging mass," "find the acceleration," "is the object in equilibrium," "find the tension."

## Given Information

- Mass of the object
- One or more forces (applied, friction coefficient + normal, weight via mass × g, tension)
- Direction of acceleration (or "at rest" / "constant velocity" which means a = 0)

## Unknown Requested

- Acceleration (magnitude and direction)
- A specific force (normal force, tension, friction)
- Whether the object moves (compare applied force to maximum static friction)

## Diagram

Draw a FBD:
1. Object as a dot.
2. Every force as an arrow from the dot: weight (down), normal (perp to surface), tension (along rope), friction (opposing motion), applied force.
3. Label forces. Choose +x and +y.

## Equations

$$\sum F_x = ma_x \qquad \sum F_y = ma_y$$

For equilibrium (at rest or constant velocity): a = 0, so ΣF_x = 0 and ΣF_y = 0.

## Solving Pattern

1. Draw and label the FBD.
2. Choose a coordinate system (+x along acceleration direction, +y perpendicular).
3. Write ΣF_x = ma_x and ΣF_y = ma_y.
4. Substitute each force with its sign.
5. Use ΣF_y = 0 to find n first (if needed for friction).
6. Solve the remaining equation(s) for the unknown.
7. Check: do the sign/direction of your answer make physical sense?

## Unit Check

Force (N) = mass (kg) × acceleration (m/s²). If your answer for a force comes out in kg·m/s², that's the same as N — correct. If you get m/s² for a force, you forgot to multiply by mass.

## Traps

- Forgetting to find the normal force separately before computing friction.
- Using mass (kg) where force (N) is needed.
- Getting the sign of friction wrong (always opposes motion or tendency of motion).
- Assuming n = mg on every surface (only true on flat horizontal surface with no other vertical forces).

## Drills

[[../drills/fbd-drawing-drill]], [[../drills/newtons-second-law-drill]]
