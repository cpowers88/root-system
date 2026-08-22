---
type: common-errors
tags: [physics]
timeline: later
---

# Common Errors — Stage 12: Static Equilibrium and Elasticity (Ch 12)

1. **Not drawing an extended free body diagram.** In Stage 5, forces were placed at the center of a particle. In equilibrium problems, forces act at specific points on an extended object — their location determines the torque they produce. Placing all forces at the center loses all torque information.

2. **Choosing a poor pivot point.** You can choose ANY point as the pivot for torque calculations, but a bad choice adds unknown forces into the torque equation. Smart choice: pick the point where an unknown force acts — that unknown's torque = 0 and drops out of the equation.

3. **Using the wrong moment arm.** τ = r × F — the moment arm is the perpendicular distance from the pivot to the LINE of action of the force. Not the distance to the point of application if those differ. For a force at angle φ to the position vector: τ = rF sin φ.

4. **Getting torque signs wrong.** Set a clear sign convention (counterclockwise = positive, clockwise = negative) at the start and apply it consistently to EVERY torque in the problem. One sign error causes the entire system of equations to give a wrong answer.

5. **Forgetting the reaction force at a pivot/hinge.** A hinge or pin joint can exert force in ANY direction. Its force has an x-component AND a y-component — both unknown. These must appear in your ΣFx = 0 and ΣFy = 0 equations, even if you cleverly chose the pivot to eliminate them from the torque equation.

6. **Applying only one of the two equilibrium conditions.** Statics requires BOTH ΣF⃗ = 0 (no translation) AND Στ = 0 (no rotation). Satisfying only one condition is insufficient — an object can be translationally still but spinning, or rotationally still but accelerating.

7. **Confusing Young's, shear, and bulk moduli.** Young's modulus governs tensile/compressive deformation (change in length). Shear modulus governs angular deformation under a shear stress. Bulk modulus governs volume change under uniform pressure. Match the type of deformation to the correct modulus.
