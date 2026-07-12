---
type: problem-type
status: draft
---

# Problem Type — Atwood Machine

## How to Recognize It

Two masses connected by a string hanging over a frictionless, massless pulley. One mass goes down, the other goes up. The problem asks for the acceleration of the system or the tension in the string.

**Keywords:** "Atwood machine," "two masses over a pulley," "connected by a rope over a frictionless pulley," "find the acceleration and tension."

## Given Information

- m₁ and m₂ (two masses)
- g = 9.80 m/s²
- Pulley: frictionless and massless (stated in problem or assumed)
- Rope: massless and inextensible (same tension throughout, same speed for both masses)

## Unknown Requested

- Acceleration of the system (magnitude a, direction depends on which mass is heavier)
- Tension T in the rope (same throughout the massless rope)

## Diagram

```
       T          T
       ^          ^
       |          |
      [m₁]      [m₂]   (m₂ > m₁)
       |          |
       v          v
      m₁g        m₂g

m₂ falls, m₁ rises.
Define "positive" as m₂ going down (and m₁ going up).
```

## Equations

Write ΣF = ma for each mass separately:

For m₁ (going up, take "up" as positive for m₁):
$$T - m_1 g = m_1 a$$

For m₂ (going down, take "down" as positive for m₂):
$$m_2 g - T = m_2 a$$

Both have the same |a| because the rope is inextensible.

**Add the two equations** (T cancels):
$$m_2 g - m_1 g = (m_1 + m_2) a$$

$$\boxed{a = \frac{(m_2 - m_1)g}{m_1 + m_2}}$$

**Substitute a back** to find T:
$$T = m_1(g + a) = \frac{2m_1 m_2 g}{m_1 + m_2}$$

## Solving Pattern

1. Draw FBD for each mass separately.
2. Define ONE positive direction consistently: typically "m₂ falls = positive."
3. Write ΣF = ma for each mass.
4. Add the two equations to eliminate T; solve for a.
5. Substitute a into either equation to find T.
6. Check: a should be between 0 (equal masses) and g (one mass much larger than the other). T should be between m₁g and m₂g.

## Unit Check

a in m/s². T in N. If m₁ = m₂, check that a = 0 and T = m₁g (the rope just holds the mass up stationary).

## Traps

- Using inconsistent sign conventions for the two masses (writing "up" as positive for m₁ but "up" also as positive for m₂, when one goes up and the other goes down).
- Forgetting that both masses have the same acceleration magnitude (because the rope is inextensible).
- Thinking the tension equals the weight of the heavier mass — it doesn't. T is always between m₁g and m₂g when the system is accelerating.
- Using the total mass in one equation instead of the individual mass in each FBD equation.

## Drills

[[../drills/newtons-second-law-drill]] (Problem 7)
