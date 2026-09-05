---
type: equation
timeline: reference
status: draft
---

# Equation — Gravitational Potential Energy (General Form)

## Equation

```
U = −G × m₁ × m₂ / r
```

This is the general gravitational PE valid at any separation r. Unlike U = mgh (Stage 8), this does not assume constant g.

## Plain-English Meaning

Two masses separated by distance r have a stored gravitational potential energy of −Gm₁m₂/r. The negative sign means the system is bound — you must ADD energy to pull the masses apart to infinity. At r → ∞, U → 0 (defined reference point).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| G | 6.674×10⁻¹¹ N·m²/kg² | N·m²/kg² |
| m₁, m₂ | masses of the two objects | kg |
| r | center-to-center distance | m |
| U | gravitational potential energy | J |

## Key Features

- **Always negative** for finite r. The more negative U is, the more tightly the system is bound.
- **U → 0 as r → ∞**: zero PE is defined at infinite separation (unlike mgh where you choose the zero).
- **Higher orbit → less negative U → more energy needed**: counterintuitively, a satellite in a higher orbit has MORE total mechanical energy (KE + PE), not less.

## Relationship to Near-Surface Form

For small height h above Earth's surface (h << R_E):
U = −GM_E m/(R_E + h) ≈ −GM_E m/R_E + mgh

The constant term −GM_E m/R_E drops out when taking ΔU, leaving ΔU ≈ mgh — the Stage 8 result.

## When to Use

- Orbital energy calculations (satellite, Moon, planets)
- Escape speed derivation
- Comparing PE at two different distances from a planetary body
- Any problem where height is not small compared to the planet's radius

## When NOT to Use

Near Earth's surface (h << R_E) — use U = mgy for simplicity.

## Common Mistake

Forgetting the negative sign. Students sometimes write U = +GMm/r, which gives total energy that increases as r decreases (wrong — bound systems get more negative as objects get closer).
