---
type: worked-example
stage: 12
---

# Worked Example: Hinged Beam with Cable Support

## Physical Situation

A uniform 3.0 m horizontal beam of mass M = 12 kg is pinned to a wall at its left end (hinge). A cable attached at the right end makes an angle of 55° above the horizontal. A sign of mass m = 28 kg hangs from the right end. Find (a) the tension T in the cable, and (b) the magnitude and direction of the hinge reaction force.

## Diagram

```
  Wall
  |
  |============================→ beam (3.0 m)
  |hinge               |         |
  (Rx, Ry)         Mg at 1.5m   mg + T at 3.0 m
                              ↗ T (55°)
```

Forces acting on the beam:
- Hinge reaction (Rx to the right/left, Ry up) at x = 0
- Beam weight Mg = (12)(9.8) = 117.6 N downward at x = 1.5 m (midpoint)
- Sign weight mg = (28)(9.8) = 274.4 N downward at x = 3.0 m
- Cable tension T at angle 55° above horizontal at x = 3.0 m

## Step 1: Choose the Pivot

Choose the hinge (left end) as the pivot. This eliminates the unknown hinge forces Rx and Ry from the torque equation entirely.

## Step 2: Apply Στ = 0 About the Hinge

Sign convention: CCW torques are positive.

- Torque from cable tension (T): The perpendicular component to the beam is T sin 55°, acting upward at x = 3.0 m → CCW → positive
  τ_T = T · sin(55°) · 3.0 m = T(0.819)(3.0) = 2.457T N·m

- Torque from beam weight (Mg): downward at x = 1.5 m → CW → negative
  τ_Mg = −(117.6)(1.5) = −176.4 N·m

- Torque from sign weight (mg): downward at x = 3.0 m → CW → negative
  τ_mg = −(274.4)(3.0) = −823.2 N·m

Setting Στ = 0:

```
2.457T − 176.4 − 823.2 = 0
2.457T = 999.6
T = 999.6 / 2.457 = 406.8 N ≈ 407 N
```

## Step 3: Apply ΣFx = 0 and ΣFy = 0

x-direction (horizontal):

```
ΣFx = 0:   Rx − T cos(55°) = 0
Rx = T cos(55°) = (407)(0.574) = 233.6 N (pointing right)
```

y-direction (vertical):

```
ΣFy = 0:   Ry + T sin(55°) − Mg − mg = 0
Ry = Mg + mg − T sin(55°)
Ry = 117.6 + 274.4 − (407)(0.819)
Ry = 392 − 333.3 = 58.7 N (pointing up)
```

## Step 4: Find the Hinge Reaction Magnitude and Direction

```
R = √(Rx² + Ry²) = √(233.6² + 58.7²) = √(54,569 + 3,446) = √58,015 ≈ 241 N

θ = arctan(Ry/Rx) = arctan(58.7/233.6) = arctan(0.251) ≈ 14.1° above horizontal
```

## Summary

- Cable tension: T ≈ 407 N at 55° above horizontal
- Hinge reaction: R ≈ 241 N at 14.1° above horizontal

## Key Lessons

1. **Always pick the pivot at an unknown force** — it removes that force from the torque equation.
2. **Perpendicular component matters:** Use τ = r F sin φ. The cable's perpendicular component to the beam is T sin 55°.
3. **The hinge reaction is NOT straight up or horizontal** — it has both components, determined by the force equations.
4. **Order of steps:** Torque equation first (solves for T), then force equations (solve for Rx, Ry).
