---
type: concept
timeline: reference
status: draft
---

# Free Body Diagram (FBD)

## What is the physical idea?

A **free body diagram** is a drawing that shows a single object isolated from its environment, with every force acting ON that object drawn as a labeled arrow. It is the essential first step for applying Newton's Second Law — you cannot reliably set up ΣF = ma without one.

"Free" means the object is isolated, separated from everything touching it. "Body" means the object itself (drawn as a dot). "Diagram" means the visual representation.

## What real-world situation does it describe?

Any situation where you need to apply Newton's Laws: a block on a table, a hanging mass, a car on a road, a person in an elevator, an Atwood machine, a block on an incline.

## Objects / System Involved

One object (the "system") is chosen and isolated. All other objects become "environment" — their effect is represented by the forces they exert on the system.

## The Five Rules for FBDs

1. **Draw the object as a dot** (particle model).
2. **Draw one arrow for every force ON the object** — starting at the dot, pointing in the force's direction.
3. **Label each arrow** with the force name and symbol (n, w, f_k, T, F_app, etc.).
4. **Never draw forces the object exerts on other things** — only forces ON the object.
5. **Choose a coordinate system** (+x, +y) and mark it on the diagram.

## Quantities That Change

The FBD itself doesn't compute anything — it organizes the forces so you can write ΣF_x = ma_x and ΣF_y = ma_y correctly.

## Model or Equation

After drawing the FBD:

$$\sum F_x = ma_x \qquad \sum F_y = ma_y$$

Substitute every labeled force into the appropriate equation, with the correct sign based on your coordinate system.

## Calculus Connection

None in Stage 5. When force varies, you'll integrate F(t) = m·dv/dt (Stage 7 and beyond). But the FBD approach is always step 1.

## Diagram / Visual Model

**Example: Block on rough horizontal surface, pulled right by rope tension T**

```
Step 1: Identify forces
- Weight w = mg (Earth on block, downward)
- Normal n (floor on block, upward)
- Tension T (rope on block, rightward)
- Kinetic friction f_k (floor on block, leftward — opposes motion)

Step 2: Draw FBD
            n
            ^
            |
  f_k <--[•]--> T       (• = the block as a dot)
            |
            v
            w = mg

Step 3: Choose axes (+x = right, +y = up)

Step 4: Write equations
ΣF_x = T − f_k = ma_x
ΣF_y = n − mg = 0 → n = mg → f_k = μ_k mg
```

## Problem Types That Use This

- [[../problem-types/fbd-single-object]]
- [[../problem-types/fbd-connected-objects]]
- [[../problem-types/inclined-plane]]
- [[../problem-types/atwood-machine]]
- [[../problem-types/friction-problems]]

## Common Beginner Mistake

Drawing forces that don't exist (like "the force of motion" — there is no such force) or forces the object exerts on other things. Every arrow must correspond to a real physical interaction: gravity, contact (normal), friction, tension, applied push/pull, or a field force.

## Practice Next

[[../drills/fbd-drawing-drill]] — seven progressively complex scenarios to draw FBDs for, from "book on table" to "two-block stacked system."

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 5.7, pp. 133–135.
