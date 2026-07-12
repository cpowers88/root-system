---
type: equation
status: draft
---

# Pendulum Period Equations

## Equations

**Simple pendulum (small angle):**
```text
T = 2π√(L/g)
ω = √(g/L)
```

**Physical pendulum (rigid body):**
```text
T = 2π√(I / mgd)
```

## Meaning in Plain English

**Simple pendulum:** A heavier bob does not swing faster — period depends only on length L and local gravity g. A longer pendulum swings more slowly. This is why all grandfather clocks with the same pendulum length tick at the same rate.

**Physical pendulum:** Any rigid object pivoting about a point that is not its center of mass. The formula uses rotational inertia I and the distance d from pivot to center of mass. A simple pendulum is the special case where all mass is at distance L (so I = mL² and d = L → T = 2π√(L/g)).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| T | period | s |
| ω | angular frequency | rad/s |
| L | pendulum length (pivot to bob center) | m |
| g | gravitational field strength | m/s² |
| I | moment of inertia about pivot | kg·m² |
| m | total mass of pendulum | kg |
| d | distance from pivot to center of mass | m |

## Units Check

**Simple:** [2π√(L/g)] = √[m / (m/s²)] = √[s²] = s ✓

**Physical:** [2π√(I/mgd)] = √[kg·m² / (kg·m/s²·m)] = √[s²] = s ✓

## When to Use These Equations

- **Simple pendulum formula:** when the "pendulum" is a small dense bob on a light string, and the swing angle stays below about 15°.
- **Physical pendulum formula:** when the oscillating body is a rigid object (a meter stick, a disk, a door) pivoting about any fixed axis.

## When Not to Use These Equations

- Do not use T = 2π√(L/g) for angles larger than ~15° (≈ 0.26 rad). At large angles the period is longer — the formula underestimates T.
- Do not use the simple pendulum formula for a physical pendulum: the moment of inertia of a rigid body is not simply mL².

## Required Assumptions

- Small-angle approximation: sin θ ≈ θ (in radians). Valid for θ_max ≲ 15°.
- Pivot is frictionless; string/rod is massless (simple case).
- No air resistance (undamped).

## Calculus Origin

For a simple pendulum, torque about the pivot is τ = −mgL sin θ. With the small-angle approximation sin θ ≈ θ: τ = −mgLθ. Using Newton's 2nd law for rotation: τ = Iα = mL²(d²θ/dt²), giving d²θ/dt² = −(g/L)θ. This has the same form as d²x/dt² = −ω²x, so ω = √(g/L).

## Common Mistake

- Applying T = 2π√(L/g) for a large-angle swing (sin θ is NOT ≈ θ for big angles).
- Forgetting that period does NOT depend on mass in the simple pendulum case.
- Using L = distance to the pivot rather than L = distance from pivot to the center of mass of the bob.

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 15.5, Equations 15.26 and 15.28.
