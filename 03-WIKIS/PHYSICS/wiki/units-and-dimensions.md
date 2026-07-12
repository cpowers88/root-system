---
type: reference
tags: [reference, physics]
---

# Units and Dimensions

## Purpose

Track units, conversions, dimensional analysis, and equation sanity checks. This page accumulates across the whole course — append, don't rebuild.

## SI Base Units

| Quantity | Unit | Symbol |
|---|---|---|
| length | meter | m |
| mass | kilogram | kg |
| time | second | s |
| electric current | ampere | A |
| temperature | kelvin | K |
| amount of substance | mole | mol |
| luminous intensity | candela | cd |

Length, mass, and time are the **fundamental quantities** for mechanics — everything else in this course is a **derived quantity** built from these three.

## Dimensional Symbols

Brackets `[ ]` mean "the dimensions of." Length → **L**, Mass → **M**, Time → **T**.

## Common Derived Units

| Quantity | Unit | Symbol | Base units | Dimension | Stage introduced |
|---|---|---|---|---|---|
| area | — | — | m² | L² | Stage 1 |
| volume | — | — | m³ | L³ | Stage 1 |
| speed | — | — | m/s | L/T | Stage 1 (defined); used starting Stage 2 |
| acceleration | — | — | m/s² | L/T² | Stage 1 (defined); used starting Stage 2 |
| density | — | ρ | kg/m³ | M/L³ | Stage 1 |
| force | newton | N | kg·m/s² | ML/T² | Stage 5 |
| energy/work | joule | J | kg·m²/s² | ML²/T² | Stage 7 |
| power | watt | W | kg·m²/s³ | ML²/T³ | Stage 7–8 |
| pressure | pascal | Pa | kg/(m·s²) | M/(LT²) | not in scope (Ch14, parked) |

## Dimensional Analysis Rule

An equation is suspicious (and must be wrong) if the dimensions on the left side do not match the dimensions on the right side. Quantities can only be added or subtracted if they have the same dimensions. Dimensional analysis can verify the *form* of an equation (which powers of which variables) but **cannot** determine dimensionless numerical constants (like the ½ in x = ½at²).

## SI Prefixes (Powers of Ten)

| Prefix | Symbol | Power | Prefix | Symbol | Power |
|---|---|---|---|---|---|
| yocto | y | 10⁻²⁴ | kilo | k | 10³ |
| zepto | z | 10⁻²¹ | mega | M | 10⁶ |
| atto | a | 10⁻¹⁸ | giga | G | 10⁹ |
| femto | f | 10⁻¹⁵ | tera | T | 10¹² |
| pico | p | 10⁻¹² | peta | P | 10¹⁵ |
| nano | n | 10⁻⁹ | exa | E | 10¹⁸ |
| micro | μ | 10⁻⁶ | zetta | Z | 10²¹ |
| milli | m | 10⁻³ | yotta | Y | 10²⁴ |
| centi | c | 10⁻² | | | |
| deci | d | 10⁻¹ | | | |

## Significant Figures — Working Rules

- **Multiplication/division:** the result has as many sig figs as the input with the *fewest* sig figs.
- **Addition/subtraction:** the result has as many *decimal places* as the input with the *fewest* decimal places.
- Trailing zeros after a decimal point are significant; trailing zeros with no decimal point are ambiguous — use scientific notation to remove ambiguity (e.g., 1.50 × 10³ g has 3 sig figs).
- Round only at the very end of a multi-step calculation, not after each intermediate step (rounding early causes error accumulation).

## Later Stages

New units (frequency = hertz, momentum = kg·m/s, etc.) get appended here as each stage introduces them — not rebuilt from scratch.
