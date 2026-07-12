---
type: reference
tags: [reference, physics, math]
---

# Geometry and Trigonometry Reference

**Source:** Appendix B, Sections B.3 and B.4 (pages A-10 to A-13)

Geometry and trig are tools you will use constantly from Stage 3 onward. Trig is the language of vectors, angles, forces, and waves.

---

## B.3 Geometry

### Distance Between Two Points

```
d = √((x₂ − x₁)² + (y₂ − y₁)²)
```

This is the Pythagorean theorem applied to coordinates.

### Radian Measure

For a circular arc of radius r and central angle θ (in radians):

```
s = rθ        (arc length)
θ = s/r       (angle from arc and radius)
```

**Why radians matter:** all calculus formulas for derivatives and integrals of sin/cos only work when the angle is in radians. If your calculator is in degree mode, you will get wrong answers.

### Areas and Volumes (Table B.2)

| Shape | Formula |
|---|---|
| Rectangle | A = ℓw |
| Circle | A = πr², circumference C = 2πr |
| Triangle | A = ½bh |
| Sphere | Surface area = 4πr², Volume = (4/3)πr³ |
| Cylinder | Lateral area = 2πrℓ, Volume = πr²ℓ |
| Rectangular box | Surface area = 2(ℓh + ℓw + hw), Volume = ℓwh |

**Physics use:** density problems (Stage 1), pressure/buoyancy (Stage 14), moment of inertia (Stage 10), wave intensity (Stage 16).

### Equations of Curves

These appear in projectile motion, orbital paths, and oscillations.

| Curve | Equation | Notes |
|---|---|---|
| Straight line | y = mx + b | m = slope, b = y-intercept |
| Circle (centered at origin) | x² + y² = R² | radius R |
| Ellipse | x²/a² + y²/b² = 1 | a = semimajor, b = semiminor |
| Parabola | y = ax² + b | vertex at y = b |
| Rectangular hyperbola | xy = constant | Boyle's Law, universal gravity |

**Physics use:**
- Projectile path is a parabola (Stage 4)
- Planetary orbit is an ellipse (Stage 13, Kepler's first law)
- P and V in an ideal gas follow a hyperbola

---

## B.4 Trigonometry

### Right Triangle Definitions

Consider a right triangle with angle θ, opposite side a, adjacent side b, and hypotenuse c.

```
sin θ = opposite / hypotenuse = a/c

cos θ = adjacent / hypotenuse = b/c

tan θ = opposite / adjacent = a/b
```

**Pythagorean theorem:**
```
c² = a² + b²
```

**Derived from definitions:**
```
sin² θ + cos² θ = 1     (fundamental identity)
tan θ = sin θ / cos θ
```

**Reciprocal functions:**
```
csc θ = 1/sin θ
sec θ = 1/cos θ
cot θ = 1/tan θ
```

---

### Common Angle Values

Memorize these — they appear in almost every vector and force problem.

| θ | sin θ | cos θ | tan θ |
|---|---|---|---|
| 0° | 0 | 1 | 0 |
| 30° | 1/2 | √3/2 | 1/√3 ≈ 0.577 |
| 45° | √2/2 ≈ 0.707 | √2/2 ≈ 0.707 | 1 |
| 60° | √3/2 ≈ 0.866 | 1/2 | √3 ≈ 1.732 |
| 90° | 1 | 0 | undefined |
| 180° | 0 | −1 | 0 |
| 270° | −1 | 0 | undefined |

---

### Trigonometric Identities (Table B.3)

**Pythagorean identities:**
```
sin² θ + cos² θ = 1
sec² θ = 1 + tan² θ
csc² θ = 1 + cot² θ
```

**Double-angle formulas:**
```
sin 2θ = 2 sin θ cos θ
cos 2θ = cos² θ − sin² θ
tan 2θ = 2 tan θ / (1 − tan² θ)
```

**Half-angle formulas:**
```
sin²(θ/2) = ½(1 − cos θ)
cos²(θ/2) = ½(1 + cos θ)
1 − cos θ = 2 sin²(θ/2)
tan(θ/2) = √((1 − cos θ)/(1 + cos θ))
```

**Sum and difference formulas:**
```
sin(A ± B) = sin A cos B ± cos A sin B
cos(A ± B) = cos A cos B ∓ sin A sin B
```

**Product-to-sum formulas:**
```
sin A + sin B = 2 sin[½(A+B)] cos[½(A−B)]
cos A + cos B = 2 cos[½(A+B)] cos[½(A−B)]
cos A − cos B = 2 sin[½(A+B)] sin[½(B−A)]
```

**Physics use of double-angle:** projectile range formula uses sin 2θ (Stage 4). Superposition of waves uses sum formulas (Stage 17).

---

### Symmetry Properties

```
sin(−θ) = −sin θ       (odd function)
cos(−θ) =  cos θ       (even function)
tan(−θ) = −tan θ       (odd function)

sin θ = cos(90° − θ)
cos θ = sin(90° − θ)
cot θ = tan(90° − θ)
```

---

### For Any Triangle (not just right triangles)

For a triangle with sides a, b, c and opposite angles α, β, γ:

Angle sum: α + β + γ = 180°

**Law of cosines:**
```
a² = b² + c² − 2bc cos α
b² = a² + c² − 2ac cos β
c² = a² + b² − 2ab cos γ
```

**Law of sines:**
```
a/sin α = b/sin β = c/sin γ
```

**Physics use:** Law of cosines and law of sines appear in 2D vector addition and force equilibrium problems (Stage 3, 5, 12).

---

### Inverse Trig Functions

Used to find angles from ratios:
```
θ = sin⁻¹(a/c)    "what angle has this sine?"
θ = cos⁻¹(b/c)
θ = tan⁻¹(a/b)
```

**Range:** sin⁻¹ and cos⁻¹ return values in [−90°, 90°]. In physics, always check the diagram to confirm you have the right quadrant.

---

### Diagram for Decomposing Vectors

Given a vector of magnitude F at angle θ above the horizontal:

```
F_x = F cos θ    (horizontal component)
F_y = F sin θ    (vertical component)
```

This decomposition is used in nearly every force, velocity, and displacement problem from Stage 3 onward. Draw it every time.

```
          |
      F_y | / F
          |/ θ
          +---------- F_x
```
