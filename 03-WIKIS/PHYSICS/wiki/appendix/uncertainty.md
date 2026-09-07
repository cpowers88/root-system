---
type: reference
tags: [physics]
timeline: reference
---

# Propagation of Uncertainty

**Source:** Appendix B, Section B.8 (pages A-20 to A-21)

This section is used in labs throughout PHYS 2211. Every measured value has uncertainty — these rules tell you how uncertainty grows (or doesn't) when you combine measurements mathematically.

---

## What Is Uncertainty?

Every physical measurement has two parts: the measured value and the uncertainty.

```
ℓ = (5.5 ± 0.1) cm
```

- **Absolute uncertainty:** 0.1 cm — stated in the same units as the measurement
- **Fractional uncertainty:** 0.1/5.5 = 0.018 (dimensionless ratio)
- **Percent uncertainty:** 1.8%

Uncertainty is a combination of:
- Instrument precision (how fine is the smallest division?)
- System variability (does the thing being measured change?)

---

## Three Rules for Combining Uncertainties

### Rule 1: Multiplication or Division → Add Percent Uncertainties

When measurements are multiplied or divided to get a result, add the **percent uncertainties** of each measurement.

```
Result = A × B    →    %uncertainty(Result) = %uncertainty(A) + %uncertainty(B)
Result = A / B    →    same rule
```

**Example:** Area = length × width = (5.5 ± 1.8%) cm × (6.4 ± 1.6%) cm
```
Area = 35 cm²  ±  (1.8% + 1.6%)  =  35 cm² ± 3.4%  ≈  (35 ± 1) cm²
```

### Rule 2: Addition or Subtraction → Add Absolute Uncertainties

When measurements are added or subtracted, add the **absolute uncertainties**.

```
Result = A + B    →    δResult = δA + δB
Result = A − B    →    δResult = δA + δB  (both add — subtraction is the risky case)
```

**Example:** ΔT = T₂ − T₁ = (99.2 ± 1.5)°C − (27.6 ± 1.5)°C
```
ΔT = 71.6°C  ±  (1.5 + 1.5)°C  =  71.6 ± 3.0°C  ≈  1.6°C ± 4.2%
```

**Warning:** subtraction of two close values amplifies fractional uncertainty dangerously. Avoid experimental designs that subtract nearly equal numbers.

### Rule 3: Powers → Multiply Percent Uncertainty by the Power

When a measurement is raised to a power n, multiply its percent uncertainty by |n|.

```
Result = Aⁿ    →    %uncertainty(Result) = |n| × %uncertainty(A)
```

**Example:** Volume of sphere = (4/3)πr³, radius r = 6.20 cm ± 2.0%
```
V = 998 cm³  ±  (3 × 2.0%)  =  998 cm³ ± 6.0%  ≈  (998 ± 60) cm³
```

---

## Why This Matters

- Uncertainties always add. They never cancel. Complex calculations accumulate larger and larger uncertainty.
- If you subtract two similar numbers (Rule 2 scenario), the result can have an uncertainty **larger than the result itself**.
- Experiments should be designed so the quantity of interest is not a small difference between large numbers.

---

## Summary Table

| Operation | How to combine uncertainties |
|---|---|
| Multiply: A × B | Add percent uncertainties |
| Divide: A / B | Add percent uncertainties |
| Add: A + B | Add absolute uncertainties |
| Subtract: A − B | Add absolute uncertainties |
| Power: Aⁿ | Multiply percent uncertainty by n |
