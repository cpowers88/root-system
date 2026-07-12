---
type: worked-example
stage: 9
---

# Worked Example: 2D Glancing Collision

## Physical Situation

Two hockey pucks on a frictionless ice surface. Puck 1 slides in the +x direction and strikes stationary Puck 2 in a glancing (off-center) blow. After the collision, each puck moves at an angle to the original direction. Find Puck 2's speed and direction.

## Given

- m₁ = m₂ = 0.17 kg (identical masses)
- Puck 1 initial speed: v₁ᵢ = 5.0 m/s in the +x direction
- Puck 2 initial speed: v₂ᵢ = 0
- Puck 1 final: v₁f = 3.0 m/s at θ₁ = 37° above the +x axis
- Find: v₂f (magnitude and direction θ₂)

## Diagram

```
Before:                          After:
[Puck 1 → 5.0 m/s]   [Puck 2]      [Puck 1 → 3.0 m/s at +37°]
                                     [Puck 2 → v₂f at −θ₂]
```

## Step 1: Apply Momentum Conservation in the x-Direction

```
m·v₁ᵢ + 0 = m·v₁f·cos(37°) + m·v₂f·cos(θ₂)
```

The mass m cancels (identical masses):

```
5.0 = 3.0·cos(37°) + v₂f·cos(θ₂)
5.0 = 3.0·(0.799) + v₂f·cos(θ₂)
5.0 = 2.40 + v₂f·cos(θ₂)
v₂f·cos(θ₂) = 2.60 m/s        ← equation (x)
```

## Step 2: Apply Momentum Conservation in the y-Direction

Initially, zero momentum in the y-direction.

```
0 = m·v₁f·sin(37°) − m·v₂f·sin(θ₂)
```

(Puck 2 moves below the x-axis if Puck 1 moved above it — hence the minus sign.)

Again m cancels:

```
0 = 3.0·sin(37°) − v₂f·sin(θ₂)
0 = 3.0·(0.602) − v₂f·sin(θ₂)
v₂f·sin(θ₂) = 1.81 m/s        ← equation (y)
```

## Step 3: Solve for v₂f and θ₂

From equations (x) and (y):

```
v₂f = √[(v₂f·cos θ₂)² + (v₂f·sin θ₂)²]
v₂f = √[(2.60)² + (1.81)²]
v₂f = √[6.76 + 3.28]
v₂f = √10.04
v₂f ≈ 3.17 m/s
```

```
tan(θ₂) = (v₂f·sin θ₂)/(v₂f·cos θ₂) = 1.81/2.60 = 0.696
θ₂ = arctan(0.696) ≈ 34.9° ≈ 35°
```

Puck 2 moves at 3.2 m/s at **35° below the +x axis**.

## Step 4: Unit and Sanity Check

Units: velocity in m/s ✓

Sanity check: Was kinetic energy conserved?

```
KE_before = ½(0.17)(5.0)² = 2.125 J

KE_after = ½(0.17)(3.0)² + ½(0.17)(3.17)² = 0.765 + 0.855 = 1.62 J
```

KE is NOT conserved (1.62 ≠ 2.125), so this was an **inelastic collision** — the glancing blow deformed the pucks slightly or produced friction. If the problem had stated "elastic," we'd use the elastic formulas and KE would check out.

## Key Lessons

1. **Always decompose into x and y components.** You get two independent equations for one collision.
2. **Signs matter.** If Puck 1 goes above the x-axis, Puck 2 goes below — assign negative to the y-component of Puck 2.
3. **Use Pythagorean theorem to recombine components** into the final speed.
4. **Sanity-check with KE** — verify the problem type matches the energy outcome.
