---
type: problem-type
timeline: reference
status: draft
---

# Problem Type — Static Equilibrium (Beams and Ladders)

## How to Recognize It

An object (beam, plank, ladder, bridge, crane arm) is at rest under multiple forces applied at different points. Signal words: "at rest," "in equilibrium," "uniform beam," "hinge," "cable," "support."

## Typical Given Information

- Length of beam/ladder, weight (or mass) of the beam, weight of any loads placed on it
- Location and angle of each force (cable, hinge, normal from wall/floor)

## Unknown Requested

- One or more force magnitudes or angles (cable tension, hinge force components, normal force from wall)

## Diagram

Always draw an **extended** free body diagram — unlike the particle FBD from Stage 5, you must show WHERE each force acts along the object.

Label:
- Object's weight W at its center (for a uniform object)
- Applied loads at their positions
- Normal forces and tension at their points of application
- The chosen pivot point P (usually at a hinge or contact point)

## Equations

```
ΣFx = 0    ← usually gives hinge x-component
ΣFy = 0    ← usually gives hinge y-component
Στ = 0     ← about the chosen pivot — the KEY equation
```

## Solving Pattern

1. Draw extended FBD. Identify all forces and their points of application.
2. Choose pivot at the location of the most unknown forces (often the hinge).
3. Write Στ = 0: for each force, compute τᵢ = rᵢ × Fᵢ × sin φᵢ (r = distance from pivot, φ = angle between r and F).
4. Assign signs: counterclockwise torques = positive, clockwise = negative.
5. Solve for the first unknown from the torque equation.
6. Use ΣFx = 0 and ΣFy = 0 to find remaining unknowns (often hinge force components).

## Unit Check

All forces in N, all distances in m, all torques in N·m.

## Common Traps

- Using the wrong moment arm (use perpendicular distance from pivot to the LINE of action, not just the distance to the point of application).
- Forgetting that a hinge/pin can exert force in any direction — its force has BOTH an x and a y component.
- Not including the weight of the beam itself (uniform beam: weight acts at the center).

## Drill

[[../drills/equilibrium-drill]]
