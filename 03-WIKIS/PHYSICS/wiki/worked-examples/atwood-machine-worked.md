---
type: worked-example
timeline: reference
status: draft
---

# Worked Example — Atwood Machine

## Problem

In an Atwood machine, mass m₁ = 4.0 kg and mass m₂ = 6.0 kg are connected by a massless string over a frictionless, massless pulley. Find: (a) the acceleration of the system and (b) the tension in the string. (g = 9.80 m/s²)

## Physical Situation

Two hanging masses over a pulley. m₂ is heavier, so it falls and pulls m₁ upward. Both move at the same speed (inextensible rope), so both have the same magnitude of acceleration.

## Step 1: Define Positive Direction

"Positive" = m₂ falling (and m₁ rising). Both accelerate at the same magnitude a.

## Step 2: Free Body Diagrams

```
     T                     T
     ^                     ^
     |                     |
    [m₁]                 [m₂]
     |                     |
     v                     v
   m₁g = 39.2 N          m₂g = 58.8 N
   
FBD of m₁ (going up = positive direction for this mass):
  T − m₁g = m₁a   ... (1)

FBD of m₂ (going down = positive direction for this mass):
  m₂g − T = m₂a   ... (2)
```

## Step 3: Solve for Acceleration

Add equations (1) and (2) to eliminate T:

$$T - m_1 g + m_2 g - T = m_1 a + m_2 a$$
$$(m_2 - m_1)g = (m_1 + m_2)a$$
$$a = \frac{(m_2 - m_1)g}{m_1 + m_2} = \frac{(6.0 - 4.0)(9.80)}{4.0 + 6.0} = \frac{2 \times 9.80}{10} = 1.96 \text{ m/s}^2$$

**m₂ accelerates downward at 1.96 m/s²; m₁ accelerates upward at 1.96 m/s².**

## Step 4: Solve for Tension

Substitute a into equation (1):

$$T = m_1(g + a) = 4.0(9.80 + 1.96) = 4.0 \times 11.76 = 47.0 \text{ N}$$

## Step 5: Verify with Equation (2)

$$m_2 g - T = m_2 a$$
$$58.8 - 47.0 = 6.0 \times 1.96$$
$$11.8 = 11.8 \checkmark$$

## Step 6: Sanity Checks

- Is a between 0 and g? 0 < 1.96 < 9.80 ✓ (If a > g, something is wrong.)
- Is T between m₁g and m₂g? 39.2 < 47.0 < 58.8 ✓ (Tension always between the two weights for an accelerating Atwood.)
- If m₁ = m₂: a should be 0, T should equal mg. Check: (0)g/(2m) = 0 ✓.

## Key Insight

The trick to Atwood machines: write separate equations for each mass, then ADD them to eliminate tension and solve for a. Substituting back gives T. Never try to use one equation for both masses — that's how sign errors creep in.

## Stage Reference

[[../stages/stage-5-laws-of-motion]] — [[../problem-types/atwood-machine]] — [[../equations/newtons-second-law]]
