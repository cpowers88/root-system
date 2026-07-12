---
type: reference
tags: [reference, physics, math]
---

# Calculus Reference — Series, Derivatives, and Integrals

**Source:** Appendix B, Sections B.5, B.6, B.7 (pages A-13 to A-19)

Calculus enters PHYS 2211 starting in Stage 2 (kinematics) and is used through the final stage. This page collects every calculus tool from the textbook appendix, organized for quick lookup.

---

## B.5 Series Expansions and Small-Angle Approximations

When a quantity is small, complicated expressions can be simplified dramatically.

### Small-Angle Approximations

When θ is small (θ in **radians**, and |θ| << 1):

```
sin θ ≈ θ
cos θ ≈ 1
tan θ ≈ θ
```

**How small is "small"?** Less than about 15° (0.26 rad) gives < 1% error for sin θ ≈ θ.

**Physics use:** pendulum period formula (Stage 15) is derived using sin θ ≈ θ. Without this approximation, there's no simple equation.

### Binomial Approximation

When |x| << 1:
```
(1 + x)ⁿ ≈ 1 + nx
```

**Physics use:** relativistic factor γ = 1/√(1−v²/c²) → at low speeds, γ ≈ 1 + v²/(2c²). Stage 18.

### Taylor/Power Series (for reference)

| Function | Series expansion | Notes |
|---|---|---|
| eˣ | 1 + x + x²/2! + x³/3! + … | exact for all x |
| sin x | x − x³/3! + x⁵/5! − … | ≈ x for small x |
| cos x | 1 − x²/2! + x⁴/4! − … | ≈ 1 for small x |
| ln(1 + x) | x − x²/2 + x³/3 − … | valid for |x| < 1 |
| (1 + x)ⁿ | 1 + nx + n(n−1)x²/2! + … | ≈ 1+nx for small x |

---

## B.6 Differential Calculus

### Physics Meaning

The derivative is the instantaneous rate of change.

```
v = dx/dt    (velocity = rate of change of position)
a = dv/dt    (acceleration = rate of change of velocity)
a = d²x/dt²  (acceleration = second derivative of position)
```

**The slope of a graph** = derivative. A steep position-time graph → large velocity.

### Derivative Table (Table B.4)

Let a and n be constants; u and v are functions of x.

| Function f(x) | Derivative f'(x) |
|---|---|
| a (constant) | 0 |
| xⁿ | nxⁿ⁻¹ |
| axⁿ | naxⁿ⁻¹ |
| eˣ | eˣ |
| eᵃˣ | aeᵃˣ |
| sin(ax) | a cos(ax) |
| cos(ax) | −a sin(ax) |
| tan(ax) | a sec²(ax) |
| cot(ax) | −a csc²(ax) |
| sec(x) | sec(x) tan(x) |
| csc(x) | −csc(x) cot(x) |
| ln(x) | 1/x |
| ln(ax) | 1/x |
| sin⁻¹(ax) | a / √(1 − a²x²) |
| cos⁻¹(ax) | −a / √(1 − a²x²) |
| tan⁻¹(ax) | a / (1 + a²x²) |

### Derivative Rules

**Sum rule:**
```
d/dx [f + g] = f' + g'
```

**Product rule:**
```
d/dx [fg] = f'g + fg'
```

**Quotient rule:**
```
d/dx [f/g] = (f'g − fg') / g²
```

**Chain rule** (most important for physics):
```
d/dx [f(g(x))] = f'(g(x)) · g'(x)
```

**Chain rule example in physics:** if x = A sin(ωt), then
```
v = dx/dt = A cos(ωt) · d(ωt)/dt = Aω cos(ωt)
```

### Physics Applications of Derivatives

| Physics situation | Derivative used |
|---|---|
| Velocity from position | v = dx/dt |
| Acceleration from velocity | a = dv/dt |
| Power from energy | P = dW/dt = dE/dt |
| Force from potential energy | F = −dU/dx |
| Torque from angular momentum | τ = dL/dt |
| Rate of change of momentum | F = dp/dt |

---

## B.7 Integral Calculus

### Physics Meaning

The definite integral is the area under a curve.

```
∫ₐᵇ f(x) dx = area under f(x) from x = a to x = b
```

**In kinematics:**
- Area under a v-t graph = displacement
- Area under an a-t graph = change in velocity

**In force and energy:**
```
W = ∫ F · dx    (work = area under F-x graph)
```

### Fundamental Theorem of Calculus

```
∫ₐᵇ f(x) dx = F(b) − F(a)    where F'(x) = f(x)
```

The integral and derivative are inverse operations.

### Basic Integration Rules

**Power rule** (n ≠ −1):
```
∫ xⁿ dx = xⁿ⁺¹/(n+1) + C
```

**1/x:**
```
∫ (1/x) dx = ln|x| + C
```

**Exponential:**
```
∫ eˣ dx = eˣ + C
∫ eᵃˣ dx = (1/a)eᵃˣ + C
```

**Trig:**
```
∫ sin(ax) dx = −(1/a) cos(ax) + C
∫ cos(ax) dx =  (1/a) sin(ax) + C
```

**Constant factor:**
```
∫ cf(x) dx = c ∫ f(x) dx
```

**Sum:**
```
∫ [f(x) + g(x)] dx = ∫ f(x) dx + ∫ g(x) dx
```

---

### Integration by Parts

When the integrand is a product of two functions:
```
∫ u dv = uv − ∫ v du
```

**Choose u** to be the function that gets simpler when differentiated.
**Choose dv** to be the function that's easy to integrate.

**Example:**
```
∫ x eˣ dx   →   u = x, dv = eˣ dx
                du = dx, v = eˣ
∫ x eˣ dx = x eˣ − ∫ eˣ dx = x eˣ − eˣ + C = eˣ(x − 1) + C
```

---

### Table B.5 — Indefinite Integrals

(An arbitrary constant C should be added to each result.)

**Algebraic:**

| Integral | Result |
|---|---|
| ∫ xⁿ dx | xⁿ⁺¹/(n+1), n ≠ −1 |
| ∫ dx/x | ln\|x\| |
| ∫ dx/(a + bx) | (1/b) ln\|a + bx\| |
| ∫ x dx/(a + bx) | x/b − (a/b²) ln\|a + bx\| |
| ∫ dx/(x(x+a)) | −(1/a) ln\|(x+a)/x\| |
| ∫ dx/(a + bx)² | −1/(b(a + bx)) |
| ∫ dx/(a² + x²) | (1/a) tan⁻¹(x/a) |
| ∫ dx/(a² − x²) | (1/2a) ln\|(a+x)/(a−x)\| (a²>x²) |
| ∫ dx/(x² − a²) | (1/2a) ln\|(x−a)/(x+a)\| (x²>a²) |

**Radical:**

| Integral | Result |
|---|---|
| ∫ dx/√(a²−x²) | sin⁻¹(x/a) = −cos⁻¹(x/a), a²>x²>0 |
| ∫ dx/√(x²±a²) | ln(x + √(x²±a²)) |
| ∫ x dx/√(a²−x²) | −√(a²−x²) |
| ∫ x dx/√(x²±a²) | √(x²±a²) |
| ∫ √(a²−x²) dx | ½(x√(a²−x²) + a² sin⁻¹(x/\|a\|)) |
| ∫ x√(a²−x²) dx | −⅓(a²−x²)^(3/2) |
| ∫ √(x²±a²) dx | ½x√(x²±a²) ± ½a² ln(x + √(x²±a²)) |
| ∫ x(√(x²±a²)) dx | ⅓(x²±a²)^(3/2) |
| ∫ dx/(x²+a²)^(3/2) | x/(a²√(x²+a²)) |
| ∫ x dx/(x²+a²)^(3/2) | −1/√(x²+a²) |

**Exponential and logarithm:**

| Integral | Result |
|---|---|
| ∫ eᵃˣ dx | (1/a)eᵃˣ |
| ∫ ln(ax) dx | x ln(ax) − x |
| ∫ xeᵃˣ dx | (eᵃˣ/a²)(ax − 1) |
| ∫ x dx/(a + beˣ) | x/a − (1/ae) ln(a + beˣ) |

**Trigonometric:**

| Integral | Result |
|---|---|
| ∫ sin(ax) dx | −(1/a) cos(ax) |
| ∫ cos(ax) dx | (1/a) sin(ax) |
| ∫ tan(ax) dx | (1/a) ln\|sec(ax)\| |
| ∫ cot(ax) dx | (1/a) ln\|sin(ax)\| |
| ∫ sec(ax) dx | (1/a) ln\|sec(ax) + tan(ax)\| |
| ∫ csc(ax) dx | (1/a) ln\|csc(ax) − cot(ax)\| |
| ∫ sin²(ax) dx | x/2 − sin(2ax)/(4a) |
| ∫ cos²(ax) dx | x/2 + sin(2ax)/(4a) |
| ∫ dx/sin²(ax) | −(1/a) cot(ax) |
| ∫ dx/cos²(ax) | (1/a) tan(ax) |
| ∫ tan²(ax) dx | (1/a) tan(ax) − x |
| ∫ cot²(ax) dx | −(1/a) cot(ax) − x |
| ∫ x dx/(a²±x²) | ±½ ln(a²±x²) |
| ∫ sin⁻¹(ax) dx | x sin⁻¹(ax) + √(1−a²x²)/a |
| ∫ cos⁻¹(ax) dx | x cos⁻¹(ax) − √(1−a²x²)/a |

---

### Table B.6 — Gauss's Probability Integral and Definite Integrals

These appear in thermal physics (beyond Stage 17 for PHYS 2211, but listed for completeness).

```
∫₀^∞ xⁿ e^(−ax) dx = n! / a^(n+1)

I₀ = ∫₀^∞ e^(−ax²) dx = ½ √(π/a)     (Gauss's probability integral)
I₁ = ∫₀^∞ x e^(−ax²) dx = 1/(2a)
I₂ = ∫₀^∞ x² e^(−ax²) dx = ¼ √(π/a³)
I₃ = ∫₀^∞ x³ e^(−ax²) dx = 1/(2a²)
I₄ = ∫₀^∞ x⁴ e^(−ax²) dx = (3/8) √(π/a⁵)
I₅ = ∫₀^∞ x⁵ e^(−ax²) dx = 1/a³

Pattern:  I₂ₙ = (−1)ⁿ (dⁿI₀/daⁿ)
          I₂ₙ₊₁ = (−1)ⁿ (dⁿI₁/daⁿ)
```

---

### Calculus-Physics Quick Reference

| Physics equation | Calculus relationship |
|---|---|
| v = dx/dt | velocity is derivative of position |
| a = dv/dt = d²x/dt² | acceleration is second derivative of position |
| x = x₀ + ∫v dt | position is integral of velocity |
| v = v₀ + ∫a dt | velocity is integral of acceleration |
| W = ∫F dx | work is integral of force over displacement |
| F = −dU/dx | force is negative derivative of potential energy |
| P = dW/dt | power is derivative of work (energy) |
| τ = dL/dt | torque is derivative of angular momentum |
| F = dp/dt | force is derivative of linear momentum |
