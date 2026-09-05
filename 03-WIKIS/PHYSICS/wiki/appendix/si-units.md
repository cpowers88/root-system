---
type: reference
tags: [physics]
timeline: reference
---

# SI Units and Prefixes

**Source:** Appendix D (Table D.1, D.2) + Appendix B.1

---

## 7 SI Base Units (Table D.1)

These are the seven fundamental units from which all others are built. Memorize all seven.

| Base Quantity | Name | Symbol |
|---|---|---|
| Length | meter | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | ampere | A |
| Temperature | kelvin | K |
| Amount of substance | mole | mol |
| Luminous intensity | candela | cd |

**For PHYS 2211 mechanics:** you will use m, kg, s constantly. K enters in thermal physics; A, mol, cd are beyond Stage 17.

---

## Derived SI Units (Table D.2)

These are combinations of base units that get their own names. Every physics equation you solve should produce one of these (or a combination).

| Quantity | Name | Symbol | In Base Units | Also Written As |
|---|---|---|---|---|
| Plane angle | radian | rad | m/m (dimensionless) | — |
| Frequency | hertz | Hz | s⁻¹ | cycles/s |
| Force | newton | N | kg·m/s² | J/m |
| Pressure | pascal | Pa | kg/(m·s²) | N/m² |
| Energy, Work, Heat | joule | J | kg·m²/s² | N·m |
| Power | watt | W | kg·m²/s³ | J/s |
| Electric charge | coulomb | C | A·s | — |
| Electric potential | volt | V | kg·m²/(A·s³) | W/A |
| Capacitance | farad | F | A²·s⁴/(kg·m²) | C/V |
| Electric resistance | ohm | Ω | kg·m²/(A²·s³) | V/A |
| Magnetic flux | weber | Wb | kg·m²/(A·s²) | V·s |
| Magnetic field | tesla | T | kg/(A·s²) | — |
| Inductance | henry | H | kg·m²/(A²·s²) | T·m²/A |

**Mechanics-critical derived units:** N, Pa, J, W are used constantly. Others appear in PHYS 2212.

---

## SI Prefixes

Prefixes attach to any base or derived unit. Example: 1 km = 10³ m, 1 mN = 10⁻³ N.

| Prefix | Symbol | Power of 10 | Example |
|---|---|---|---|
| tera | T | 10¹² | 1 THz = 10¹² Hz |
| giga | G | 10⁹ | 1 GW = 10⁹ W |
| mega | M | 10⁶ | 1 MJ = 10⁶ J |
| kilo | k | 10³ | 1 km = 10³ m |
| hecto | h | 10² | 1 hPa = 100 Pa |
| deca | da | 10¹ | — |
| — | — | 10⁰ | base unit |
| deci | d | 10⁻¹ | 1 dm = 0.1 m |
| centi | c | 10⁻² | 1 cm = 0.01 m |
| milli | m | 10⁻³ | 1 mm = 0.001 m |
| micro | μ | 10⁻⁶ | 1 μm = 10⁻⁶ m |
| nano | n | 10⁻⁹ | 1 nm = 10⁻⁹ m |
| pico | p | 10⁻¹² | 1 ps = 10⁻¹² s |
| femto | f | 10⁻¹⁵ | 1 fm = 10⁻¹⁵ m |
| atto | a | 10⁻¹⁸ | — |

**Most-used in PHYS 2211:** k (kilo), c (centi), m (milli), μ (micro), n (nano).

---

## Mechanics Unit Chain

Every mechanics quantity ultimately reduces to combinations of m, kg, s:

```
Force:    N = kg·m/s²
Energy:   J = kg·m²/s² = N·m
Power:    W = kg·m²/s³ = J/s
Pressure: Pa = kg/(m·s²) = N/m²
Momentum: kg·m/s  (no special name)
Torque:   N·m  (same dimensions as energy — different physical meaning)
```

**Common unit trap:** torque (N·m) and energy (J = N·m) have the same dimensions but are different quantities. Context tells you which one you have.
