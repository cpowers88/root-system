---
type: equation
timeline: reference
status: draft
---

# Equation — Static Friction

## Equation

$$f_s \leq \mu_s n$$

At the moment of impending motion (just about to slide):

$$f_{s,\text{max}} = \mu_s n$$

## Plain-English Meaning

Static friction resists the tendency to slide between two surfaces that are not moving relative to each other. It is not a fixed value — it adjusts to whatever is needed to prevent sliding, up to a maximum of μ_s × n. Once the applied force exceeds this maximum, the object starts sliding and kinetic friction takes over.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| f_s | static friction force (adjustable, up to its maximum) | N |
| μ_s | static coefficient of friction | dimensionless |
| n | normal force | N |

## When to Use

- When the object is stationary and you want to know whether it will start moving, or what the friction force currently is.
- μ_s > μ_k always. Static friction is harder to break than kinetic friction is to maintain.

## When NOT to Use

- After the object is already sliding — kinetic friction applies then.
- Do not write f_s = μ_s n as an equation when the object is merely at rest (not on the verge of moving). The static friction force only equals its maximum at the tipping point.

## Assumptions

- The surfaces are in contact and not moving relative to each other (yet).
- μ_s is a property of the specific pair of surfaces (e.g., rubber on concrete ≈ 0.80; steel on steel ≈ 0.74).

## Calculus Origin

None. Static friction is an algebraic constraint: f_s ≤ μ_s n.

## Example

**Is it stationary?** A 5.0 kg block (μ_s = 0.40) sits on a horizontal surface. You push horizontally with 15 N.
Maximum static friction: f_s,max = 0.40 × (5.0 × 9.80) = 19.6 N.
Applied force (15 N) < maximum (19.6 N) → object stays stationary. Actual f_s = 15 N (opposing your push).

## Common Mistake

Writing f_s = μ_s n when the object hasn't started moving. This gives the maximum possible static friction, not the actual friction at that moment. The actual static friction is equal to the net force that would accelerate the object — it takes whatever value keeps the object at rest.
