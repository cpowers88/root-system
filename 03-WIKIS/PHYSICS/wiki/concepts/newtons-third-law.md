---
type: concept
timeline: reference
status: draft
---

# Newton's Third Law (Action-Reaction)

## What is the physical idea?

If object A exerts a force on object B, then object B simultaneously exerts a force on object A that is equal in magnitude and opposite in direction.

Forces always come in pairs. You cannot have a single isolated force — every force has a reaction force somewhere.

**Critical rule:** The two forces in an action-reaction pair ALWAYS act on DIFFERENT objects.

## What real-world situation does it describe?

- Your foot pushes backward on the ground → ground pushes forward on you (walking).
- A gun fires → bullet pushed forward, gun pushed backward (recoil).
- Earth pulls the Moon toward Earth → Moon pulls Earth toward the Moon.
- You push a wall → the wall pushes back on your hand.
- Tires push backward on the road → road pushes forward on the car (friction, that's what moves the car).

## Objects / System Involved

Always two objects: A and B. The action-reaction pair is one force on A from B, and one force on B from A.

## Quantities That Change

The forces in a pair are always equal in magnitude and opposite in direction. But they may produce very different accelerations because the masses may differ (F = ma → a = F/m).

## Model or Equation

$$\vec{F}_{AB} = -\vec{F}_{BA}$$

Force of A on B is equal and opposite to force of B on A. Same magnitude, opposite direction.

## Variables and Units

| Symbol | Meaning | Unit |
|---|---|---|
| F_AB | force exerted on object B by object A | N |
| F_BA | force exerted on object A by object B | N |

## Calculus Connection

None in this stage. Newton's Third Law is a statement about simultaneous force pairs, not a rate-of-change relationship.

## Diagram / Visual Model

```
Newton's Third Law Pair Example: Block on Table

    n (table pushes block UP)           [block FBD]
         ^
         |
       [BLOCK]
         |
         v
    w = mg (Earth pulls block DOWN)

    n' (block pushes table DOWN)        [table FBD]
         ^
         |
       [TABLE]

PAIR 1: n and n' — one on block (up), one on table (down) — equal magnitude
PAIR 2: w and w' — Earth pulls block down, block pulls Earth up — equal magnitude

NOTE: n and w are NOT a Newton's Third Law pair. They are both on the block (same object). They are equal in magnitude only because the block isn't accelerating (ΣF = 0).
```

## Problem Types That Use This

- [[../problem-types/fbd-connected-objects]] (tension in a rope is the Third Law interaction between rope and each block)
- [[../problem-types/fbd-single-object]] (identifying action-reaction pairs correctly)

## Common Beginner Mistake

Thinking that action-reaction pairs cancel out. They don't cancel because they act on DIFFERENT objects. If you're analyzing one object, only the forces ON that object go into its ΣF = ma equation. The reaction force lives on the other object's FBD.

A second mistake: thinking the normal force and weight are a Newton's Third Law pair. They are NOT. Weight (Earth on block, downward) pairs with block pulling Earth upward. Normal force (table on block, upward) pairs with block pushing table downward. Normal and weight happen to be equal in this case only because the block is in equilibrium.

## Practice Next

After understanding the law, work through [[../problem-types/fbd-connected-objects]] to see how Third Law pairs create tension in ropes between objects.

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 5.6, pp. 127–132.
