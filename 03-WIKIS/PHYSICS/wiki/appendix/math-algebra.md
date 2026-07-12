---
type: reference
tags: [reference, physics, math]
---

# Algebra Reference

**Source:** Appendix B, Sections B.1 and B.2 (pages A-4 to A-10)

This covers the algebra you need to solve physics equations. Every section here gets used at least once across the 18 stages.

---

## B.1 Scientific Notation

Writing numbers as a × 10ⁿ where 1 ≤ a < 10.

**Why:** Physics numbers range from 10⁻³⁵ m (Planck length) to 10²⁶ m (observable universe). Standard notation is unusable for this range.

### Multiplication and Division

When multiplying: add the exponents.
```
(6.0 × 10³)(4.0 × 10⁵) = 24.0 × 10⁸ = 2.40 × 10⁹
```

When dividing: subtract the exponents.
```
(8.0 × 10⁷) / (4.0 × 10²) = 2.0 × 10⁵
```

### Addition and Subtraction

First make the exponents match, then add/subtract coefficients.
```
3.0 × 10³ + 2.0 × 10² = 3.0 × 10³ + 0.2 × 10³ = 3.2 × 10³
```

### Common Powers of 10

| Value | Scientific notation | SI prefix |
|---|---|---|
| 1 000 000 000 | 10⁹ | giga (G) |
| 1 000 000 | 10⁶ | mega (M) |
| 1 000 | 10³ | kilo (k) |
| 0.001 | 10⁻³ | milli (m) |
| 0.000 001 | 10⁻⁶ | micro (μ) |
| 0.000 000 001 | 10⁻⁹ | nano (n) |

---

## B.2 Algebra

### Solving Equations

The one rule: **whatever you do to one side, do to the other.**

```
x/5 = 9   →   (x/5)(5) = 9(5)   →   x = 45
```

### Fraction Rules

| Operation | Rule | Example |
|---|---|---|
| Multiply | (a/b)(c/d) = ac/bd | (2/3)(4/5) = 8/15 |
| Divide | (a/b)/(c/d) = ad/bc | (2/3)/(4/5) = 10/12 |
| Add/Subtract | a/b ± c/d = (ad ± bc)/bd | 2/3 − 4/5 = −2/15 |

---

### Powers and Exponents (Table B.1)

| Rule | Equation | Example |
|---|---|---|
| Zero power | x⁰ = 1 | 5⁰ = 1 |
| First power | x¹ = x | 7¹ = 7 |
| Multiply, same base | xⁿ · xᵐ = xⁿ⁺ᵐ | x² · x⁴ = x⁶ |
| Divide, same base | xⁿ / xᵐ = xⁿ⁻ᵐ | x⁸ / x² = x⁶ |
| Fractional power = root | x^(1/n) = ⁿ√x | x^(1/2) = √x |
| Power of a power | (xⁿ)ᵐ = xⁿᵐ | (x²)³ = x⁶ |
| Negative exponent | x⁻ⁿ = 1/xⁿ | x⁻³ = 1/x³ |

---

### Factoring

| Pattern | Factored Form | Name |
|---|---|---|
| ax + ay + az | a(x + y + z) | common factor |
| a² + 2ab + b² | (a + b)² | perfect square |
| a² − b² | (a + b)(a − b) | difference of squares |

---

### Quadratic Equations

General form:
```
ax² + bx + c = 0
```

Quadratic formula (always works):
```
x = (−b ± √(b² − 4ac)) / (2a)
```

The ± gives two roots: x₊ (with +) and x₋ (with −).

**In physics:** often one root is negative or physically meaningless — pick the one that makes sense.

**Condition for real roots:** b² ≥ 4ac

**Example:** x² + 5x + 4 = 0 → a = 1, b = 5, c = 4
```
x = (−5 ± √(25 − 16)) / 2 = (−5 ± 3) / 2
x₊ = −1    x₋ = −4
```

---

### Linear Equations

General form: y = mx + b

- m = slope = Δy/Δx = (y₂ − y₁)/(x₂ − x₁)
- b = y-intercept (value of y when x = 0)

**Physics use:** position-time graphs, velocity-time graphs, force-extension graphs all use y = mx + b.

---

### Simultaneous Linear Equations

Two unknowns, two equations: solve one for one unknown, substitute into the other.

**Example:**
```
(1) 5x + y = −8
(2) 2x − 2y = 4
```
From (2): x = y + 2. Substitute into (1): 5(y+2) + y = −8 → 6y = −18 → y = −3, x = −1.

**Alternative (elimination):** multiply (1) by 2, then add (2):
```
10x + 2y = −16
 2x − 2y =   4
-----------
12x = −12 → x = −1
```

---

### Logarithms

Two common bases: base 10 (log₁₀) and base e = 2.718 28 (natural log, ln).

**Definition:** if x = aʸ, then y = logₐ x.

| Expression | Meaning |
|---|---|
| y = log₁₀ x | 10ʸ = x |
| y = ln x | eʸ = x |

**Converting between bases:**
```
ln x = (2.302 585) log₁₀ x
```

**Log Properties (any base):**
```
log(ab)  = log a + log b
log(a/b) = log a − log b
log(aⁿ)  = n log a
```

**Natural log special values:**
```
ln e  = 1
ln eᵃ = a
ln(1/a) = −ln a
```

**Physics use:** appears in exponential decay (radioactivity, RC circuits), loudness (decibels), entropy. Especially relevant in Stage 8 (energy), Stage 16 (wave intensity).
