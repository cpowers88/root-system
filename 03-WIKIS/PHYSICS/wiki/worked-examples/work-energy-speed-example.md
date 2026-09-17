---
type: worked-example
timeline: reference
status: draft
---

# Worked Example: Finding Final Speed Using the Work-Energy Theorem

## Physical Situation

A 5.0 kg box starts from rest on a rough horizontal floor. A person pushes it with a constant horizontal force of 30 N over a distance of 4.0 m. Friction applies a constant opposing force of 10 N. What is the box's speed after 4.0 m?

## Step 1 — Draw the diagram

```
     F_push = 30 N (→)        x = 4.0 m traveled (→)
     
     ┌─────┐
     │ box │→ displacement d = 4.0 m
     └─────┘
     ← 10 N (friction)      ↑ N (normal)     ↓ mg (gravity)
```

## Step 2 — Identify the system

System: the box (5.0 kg). We track mechanical energy only.

## Step 3 — List forces and compute work for each

| Force | F (N) | d (m) | θ | W = Fd cos θ |
|---|---|---|---|---|
| Push force | 30 | 4.0 | 0° (parallel to motion) | 30 × 4.0 × 1 = +120 J |
| Friction | 10 | 4.0 | 180° (opposite to motion) | 10 × 4.0 × (−1) = −40 J |
| Normal force | N | 4.0 | 90° (perpendicular) | 0 J |
| Gravity | mg | 4.0 | 90° (perpendicular) | 0 J |

## Step 4 — Compute net work

W_net = 120 + (−40) + 0 + 0 = **+80 J**

## Step 5 — Apply the work-energy theorem

```text
W_net = ΔK = ½mv_f² − ½mv_i²

80 = ½(5.0)v_f² − ½(5.0)(0)²

80 = 2.5 v_f²

v_f² = 80 / 2.5 = 32

v_f = √32 = 5.7 m/s
```

## Answer

**v_f ≈ 5.7 m/s** after 4.0 m of pushing.

## Unit check

W_net in J = kg·m²/s². Then v_f² = (2 × J) / kg = m²/s². So v_f in m/s. ✓

## Why this approach

If we'd used kinematics, we'd need net force (= 30 − 10 = 20 N), then a = F/m = 4.0 m/s², then v² = 2ad = 32. Same answer — but the energy approach didn't require computing acceleration separately and works directly even if the forces vary with position.

## Common mistake to avoid

Only computing the work done by the push force and forgetting friction's negative contribution. Net work = sum of ALL individual works.
