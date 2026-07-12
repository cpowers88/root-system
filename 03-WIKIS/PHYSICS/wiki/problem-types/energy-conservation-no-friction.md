---
type: problem-type
status: draft
---

# Energy Conservation — No Friction

## How to Recognize This Problem Type

The problem describes an object moving between two positions under gravity (and possibly a spring), with no friction or air resistance mentioned. It asks for speed at one position, maximum height, or the position at which the object stops — and gives information about the other position.

**Keywords:** frictionless, ideal, smooth, "ignore air resistance," released from rest, roller coaster, pendulum, free fall, spring launched.

## Given Information Usually Present

- Mass of the object (sometimes cancels out)
- Initial height or speed (or both if one is zero)
- Final height or spring compression (one unknown)

## Unknown Usually Requested

- Speed at a specific position
- Maximum height reached
- Compression or stretch of a spring at one state

## Diagram to Draw

Two snapshots:
```
STATE 1 (initial)         STATE 2 (final)
  y = y_i                   y = y_f
  v = v_i                   v = v_f = ?
  x_spring = x_i            x_spring = x_f

Set y = 0 at the lowest point the object reaches.
Draw a dashed reference line there.
```

## Equations Commonly Used

```
Ki + Ui = Kf + Uf
½mv_i² + mgy_i + ½kx_i² = ½mv_f² + mgy_f + ½kx_f²
```

Simplified forms for common cases:
- Object falls from rest (v_i = 0, y_f = 0):   mgy_i = ½mv_f²   →   v_f = √(2gy_i)
- Object launched upward (v_f = 0 at peak):    ½mv_i² = mgy_f   →   y_f = v_i²/(2g)
- Spring to height (x_f = 0, y_i = 0):          ½kx_i² = mgy_f + ½mv_f²

## Step-by-Step Solving Pattern

1. **Draw** initial and final states. Label all energies in each state.
2. **Set** reference height y = 0 at the lowest point.
3. **Write** Ki + Ui = Kf + Uf.
4. **Expand** each K and U term (which types of PE are present?).
5. **Substitute** known values.
6. **Simplify** (many terms may be zero — v = 0 at rest, y = 0 at reference).
7. **Solve** algebraically for the unknown.
8. **Check units:** should produce m/s for speed, m for height, m for spring length.
9. **Sanity check:** speed should be less than free-fall from the same height if the object started at rest above the reference; height should be less than initial height if speed at top is requested.

## Unit Checks

- Speed from energy: v = √(2gy) → √(m/s² × m) = √(m²/s²) = m/s ✓
- Height from energy: y = v²/(2g) → (m/s)²/(m/s²) = m ✓

## Common Traps

1. **Inconsistent reference height.** Choose y = 0 once and use it everywhere. The same dashed line must be the zero for both Ki and Kf.
2. **Forgetting that mass often cancels.** For gravity-only problems with no spring, m appears in every term and divides out. Don't be surprised if the answer doesn't depend on mass (like free fall).
3. **Ignoring spring PE.** If a spring is compressed at either state, you must include ½kx² there.
4. **Applying this to inelastic collisions.** Kinetic energy is NOT conserved in a collision unless explicitly stated to be elastic.

## Practice Drills

- [[../drills/energy-conservation-drill]] Problems 1–3

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 8.1–8.2.
