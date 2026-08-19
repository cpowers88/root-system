---
type: stage
timeline: reference
status: draft
---

# Stage 12 — Static Equilibrium and Elasticity

**Serway & Jewett Chapter 12 | KSU PHYS 2211 §54 Fall 2026 | Farhan Islam**

> **Fall §54 course core: §§12.1 and 12.3 only.** The equilibrium material on
> this page is assessed on Unit Exam 4. Sections 12.2 and 12.4—center-of-gravity
> extensions and elasticity/stress/strain—remain useful reference but are not
> required by the exact syllabus and must not displace equilibrium or SHM work.

---

## Stage Goal

By the end of this stage, Chris can:

- Apply both conditions of static equilibrium (ΣF = 0 and Στ = 0) to any rigid body problem.
- Choose a smart pivot point to eliminate unknowns and simplify torque equations.
- Solve beam, ladder, strut, and hanging sign equilibrium problems from scratch.

Enrichment only after the course-core gate: locate multi-object centers of
gravity and calculate stress, strain, and elastic moduli.

---

## Syllabus Alignment

| Item | Detail |
|---|---|
| Course | PHYS 2211 — Calculus-Based Mechanics |
| Instructor | Farhan Islam, KSU Fall 2026, §54 |
| Chapter | Serway & Jewett 10th Ed., §§12.1 and 12.3 active |
| Exam relevance | Unit Exam 4: §§12.1 and 12.3 |
| Lab relevance | Likely torque/balance lab; possible materials lab |

---

## Textbook Alignment

| Section | Topic |
|---|---|
| 12.1 | Analysis Model: Rigid Object in Equilibrium |
| 12.2 | More on the Center of Gravity *(reference, off active scope)* |
| 12.3 | Examples of Rigid Objects in Static Equilibrium |
| 12.4 | Elastic Properties of Solids *(reference, off active scope)* |

---

## Prerequisite Physics

- Newton's First and Second Laws (Stages 1–2): ΣF = ma; equilibrium means a = 0.
- Free body diagrams, force resolution into x/y components (Stages 3–5).
- Normal force, friction force, tension force (Stages 3–5).
- Torque concept introduced in rotation context (Stages 10–11). Torque is re-introduced here from the static perspective — study this stage fully even if rotation stages are fresh.

---

## Prerequisite Math

- Decomposing vectors into x and y components using sin and cos.
- Setting up and solving two simultaneous equations (two unknowns).
- Cross product magnitude: |A × B| = AB sinφ.
- Basic algebra and unit tracking throughout calculations.

---

## Core Concepts

### 1. What Does Static Equilibrium Mean?

A rigid body is in static equilibrium when:

- It is not translating — velocity is constant (usually zero).
- It is not rotating — angular velocity is constant (usually zero).

Both conditions must hold at the same time. Satisfying only one is not enough.

This matches Serway's "Analysis Model: Rigid Object in Equilibrium" from Section 12.1.

---

### 2. The Two Conditions of Static Equilibrium

**Condition 1 — No net force (translational equilibrium):**

```
ΣFx = 0
ΣFy = 0
```

Every force has an x-component and a y-component. Both sums must independently equal zero.

**Condition 2 — No net torque (rotational equilibrium):**

```
Στ = 0   (about any chosen pivot point)
```

The sum of all torques about any point you choose equals zero. The choice of pivot point does not affect the physics — choose wisely to simplify the algebra.

---

### 3. Torque

Torque is the rotational effect of a force applied at a distance from a pivot point.

```
τ = r × F
|τ| = rF sinφ
```

Where:
- r = distance from the pivot to the point where force is applied
- F = magnitude of the force
- φ = angle between the position vector r and the force vector F

**Sign convention:** Counterclockwise (CCW) = positive. Clockwise (CW) = negative. Commit to this at the start of every problem.

**Key insight:** Only the perpendicular component of the force causes rotation. If a force points directly toward or away from the pivot (φ = 0° or 180°), its torque is zero.

---

### 4. Choosing the Pivot Point

You can choose ANY point as the pivot for the torque equation. The physics does not change.

**Smart choice:** Put the pivot where an unknown force acts. That force then has r = 0, so its torque = 0, and it disappears from your torque equation.

This eliminates one unknown immediately and is the most powerful technique in equilibrium problems.

---

### 5. Center of Gravity

The center of gravity (CG) is the single point where you can treat the entire weight of an object as acting.

For a uniform gravitational field (used in all PHYS 2211 problems):

```
CG = Center of Mass (CM)
```

For a collection of masses:

```
x_cg = Σ(mi xi) / Σmi
y_cg = Σ(mi yi) / Σmi
```

For a uniform object (uniform density, symmetric shape): the CG is at the geometric center.

A beam's weight always acts downward at the midpoint of a uniform beam. The weight of any object acts downward through its CG.

---

### 6. Elasticity — When Materials Deform

Real materials stretch, compress, bend, or twist under applied forces. For small deformations, the material returns to its original shape when the force is removed. This is the elastic regime.

Three types of elastic deformation, each with its own modulus:

- **Tensile/Compressive** (along one axis): Young's modulus E.
- **Shear** (parallel forces causing layers to slide): Shear modulus S.
- **Bulk** (uniform pressure from all sides): Bulk modulus B.

---

### 7. Stress and Strain

**Stress** = force per unit area applied to the material:

```
stress = F / A     units: Pa = N/m²
```

**Strain** = fractional deformation; how much the material changed relative to its original size:

```
strain = ΔL / L0   (dimensionless — it is a ratio)
```

**Young's Modulus E:**

```
E = stress / strain = (F/A) / (ΔL/L0)
```

Rearranged to find elongation directly:

```
ΔL = (F L0) / (A E)
```

**Shear Modulus S:**

```
F_shear / A = S × (Δx / h)
```

Where Δx = lateral displacement, h = height of the sheared object.

**Bulk Modulus B:**

```
ΔP = −B (ΔV / V0)
```

The negative sign reflects that increasing pressure decreases volume.

---

## Vocabulary

| Term | Plain-English Definition |
|---|---|
| Static equilibrium | Object is not moving and not rotating; ΣF = 0 AND Στ = 0 |
| Rigid body | Object that does not deform significantly during analysis |
| Torque (τ) | Rotational effect of a force; measured in N·m |
| Moment arm | Perpendicular distance from pivot to line of action of force |
| Pivot point | Reference point chosen for calculating torques |
| Center of gravity | Point through which gravity effectively acts on a body |
| Center of mass | Mass-weighted average position of a system of particles |
| Stress | Force per unit area applied to a material surface (Pa) |
| Strain | Fractional deformation (ΔL/L0); dimensionless |
| Young's modulus (E) | Material's resistance to tensile or compressive deformation (Pa) |
| Shear modulus (S) | Material's resistance to shear (sliding) deformation (Pa) |
| Bulk modulus (B) | Material's resistance to volume change under pressure (Pa) |
| Elastic regime | Range of stress where deformation reverses when force is removed |
| Tensile stress | Stress from a stretching force pulling the material apart |
| Compressive stress | Stress from a compression force pushing the material together |
| Shear stress | Stress from forces acting parallel to a surface |

---

## Equations

| Equation | Name | When to Use |
|---|---|---|
| ΣFx = 0 | x-equilibrium | Always; horizontal force balance |
| ΣFy = 0 | y-equilibrium | Always; vertical force balance |
| Στ = 0 | Rotational equilibrium | Always; no net rotation |
| τ = rF sinφ | Torque magnitude | Finding rotational effect of any force |
| x_cg = Σ(mi xi)/Σmi | Center of gravity | Locating CG of a system |
| E = (F/A)/(ΔL/L0) | Young's modulus | Tensile or compressive stretch |
| ΔL = FL0/(AE) | Elongation formula | Finding how much a rod stretches |
| F/A = S(Δx/h) | Shear deformation | Parallel forces causing sliding |
| ΔP = −B(ΔV/V0) | Bulk compression | Pressure change causing volume change |

---

## Variables and Units Table

| Symbol | Quantity | SI Unit |
|---|---|---|
| F | Force | N |
| τ | Torque | N·m |
| r | Moment arm distance | m |
| φ | Angle between r and F | degrees or rad |
| A | Cross-sectional area | m² |
| L0 | Original length | m |
| ΔL | Change in length | m |
| E | Young's modulus | Pa (N/m²) |
| S | Shear modulus | Pa |
| B | Bulk modulus | Pa |
| ΔP | Change in pressure | Pa |
| V0 | Original volume | m³ |
| ΔV | Change in volume | m³ |
| Δx | Lateral displacement in shear | m |
| h | Height of sheared layer | m |
| m | Mass | kg |
| g | Gravitational acceleration | 9.8 m/s² |
| W | Weight (= mg) | N |

---

## Diagrams and Visual Models

### Extended Free Body Diagram Protocol

Unlike particle problems, forces on a rigid body must be drawn at their actual points of application.

1. Isolate the rigid body (the beam, the ladder, the sign).
2. Draw every external force at its point of application: weight (at CG), normal forces, friction, tension, applied loads.
3. Resolve angled forces into x and y components.
4. Mark the chosen pivot with a circled dot.

### Beam on Two Supports

```
      d1            d2
  |<------>|<---------------->|

  =========●==================
  ^         ^                  ^
  R1        W                  R2
(left    (weight at           (right
support)  CG = L/2)          support)
```

ΣFy = 0: R1 + R2 - W = 0
Στ = 0 about left support: -W·d1 + R2·(d1+d2) = 0

### Ladder Against Smooth Wall

```
           /|
          / |
         /  |<--- n_wall (horizontal)
        /   |
       / W  |
      /  (acts at midpoint)
     /       |
    /         |
   /___________
   ^
   n_floor (up) + f_friction (horizontal, away from wall)
```

Pivot at base (floor contact point):
- Weight W acts downward at horizontal distance (L/2)cosθ from base.
- Wall normal n acts horizontal at height L sinθ from base.
- Floor friction and normal have r = 0 at this pivot → zero torque.

### Stress-Strain Graph (Elastic Region)

```
Stress
(Pa)  |         . proportional limit
      |       /
      |     /   slope = E (Young's modulus)
      |   /
      | /
      |/______________
              Strain (ΔL/L0, dimensionless)
```

The linear (elastic) region has slope = E. Past the proportional limit, deformation is no longer linear.

---

## Calculus Connections

### 1. Distributed Loads on Beams

If a beam has a non-uniform mass distribution λ(x) in kg/m:

```
Total weight:       W = ∫0^L λ(x) g dx

CG location:        x_cg = ∫0^L x λ(x) dx / ∫0^L λ(x) dx

Torque from load:   τ = ∫0^L x λ(x) g dx   (about one end)
```

For a uniform beam (λ = constant = m/L), these reduce to W = mg and x_cg = L/2.
The integrals are the conceptual foundation even when the result is simple.

### 2. Young's Modulus as a Slope

In the elastic regime, Young's modulus is the derivative of stress with respect to strain:

```
E = d(stress) / d(strain)
```

For linear elastic materials (Hooke's law materials), this is constant — the stress-strain graph is a straight line, and E is its slope.

### 3. Connection to Hooke's Law

Hooke's law F = kx (from springs, Stage 7) is the macro-scale version of E = stress/strain:

```
F = (EA/L0) × ΔL
```

The spring constant of a uniform rod is k = EA/L0. A stiffer material (larger E), a thicker rod (larger A), or a shorter rod (smaller L0) all produce a larger spring constant.

---

## Problem Types

| Problem Type | Recognition Signal | Key Strategy |
|---|---|---|
| Beam on two supports | Horizontal beam, two support forces, loads at positions | ΣFy = 0 and Στ = 0; pivot at one support |
| Ladder against smooth wall | Ladder at angle, floor friction, wall normal | Pivot at base; torque from weight + wall force |
| Strut with cable | Rod attached at wall, cable at angle, load hanging | Resolve cable tension x/y; pivot at wall |
| Hanging sign | Sign from cable + hinge, or two cables | Pivot at hinge; solve for cable tension |
| Center of gravity location | Multiple masses, find balance point | x_cg = Σ(mi xi)/Σmi |
| Young's modulus (tensile) | Wire/rod stretched or compressed by force F | ΔL = FL0/(AE) |
| Shear modulus | Block with parallel forces, lateral displacement | F/A = S(Δx/h) |
| Bulk modulus | Object submerged, pressure increase, volume change | ΔP = −B(ΔV/V0) |

---

## Worked Examples

- [[../worked-examples/beam-with-hanging-mass]] — Uniform beam attached at wall, cable at angle, mass hanging at free end.
- [[../worked-examples/ladder-against-wall]] — Ladder of known mass at known angle; find minimum coefficient of friction.

---

## Drills

- [[equilibrium-drill]] — 6 problems: beam, ladder, strut, hanging sign.
- [[../drills/stress-strain-drill]] — 5 problems: Young's modulus, shear, bulk.

---

## Common Errors

See: [[../common-errors/stage-12-static-equilibrium]]

---

## Mastery Checklist

Before moving to the next assessed unit (Stage 15), Chris must pass the
equilibrium items below. Elasticity items are enrichment, not a semester gate:

- [ ] State both equilibrium conditions from memory with correct symbols.
- [ ] Draw a complete labeled FBD for a beam, ladder, and strut problem.
- [ ] Choose a pivot point and explain in words why that choice simplifies the problem.
- [ ] Write torque equations with correct signs (CCW positive, CW negative).
- [ ] Calculate τ = rF sinφ for a force at any angle.
- [ ] Locate the CG of a two- or three-mass system on a beam.
- [ ] Explain why weight acts through the CG.
- [ ] Apply Young's modulus to find elongation: ΔL = FL0/(AE).
- [ ] Identify which elastic modulus applies to a given scenario without hints.
- [ ] Apply shear modulus to a lateral deformation problem.
- [ ] Apply bulk modulus to a pressure-volume problem.
- [ ] Solve a full beam equilibrium problem: FBD → two conditions → two unknowns.
- [ ] Solve a full ladder problem: pivot at base → torques → minimum friction.
- [ ] Verify answers with unit checks and sanity checks.

---

## Do Not Move On Until

1. You can solve a ladder problem completely without looking at notes.
2. You correctly select the right elastic modulus for each physical scenario without hints.
3. You can explain to someone else why changing the pivot point gives the same answer.
4. You can draw a complete FBD for a strut-and-cable system from a verbal description.

---

## Parked Material

| Topic | Why Parked | Unlock Condition |
|---|---|---|
| Stress-strain curve beyond elastic limit | Plastic deformation, yield point, fracture — material science depth | Advanced mechanics or materials science |
| Thin-shell pressure vessels | Hoop stress, cylinder/sphere walls — requires stress tensor | Mechanics of materials |
| Statically indeterminate structures | More unknowns than equations; needs deformation compatibility | Structural statics |
| Torsion of shafts | Twisting torques, polar moment of inertia | Mechanics of materials |
| 3D equilibrium | 6 equations (3 force + 3 torque) in 3D | After mastering 2D equilibrium fully |
