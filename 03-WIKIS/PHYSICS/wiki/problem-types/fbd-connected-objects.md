---
type: problem-type
status: draft
---

# Problem Type — FBD: Connected Objects

## How to Recognize It

Two or more objects connected by a rope, string, rod, or in contact with each other. The system moves together (same acceleration magnitude). A tension force appears in the rope between them. The problem asks for acceleration OR tension (or a contact force between objects).

**Keywords:** "two blocks connected by a rope," "block A pushes block B," "Atwood machine," "two masses over a pulley," "find the tension."

## Given Information

- Masses of each object (m₁, m₂)
- External forces (applied force, gravity)
- Friction coefficients (if surfaces are involved)
- Whether the rope is massless (almost always yes in intro physics)

## Unknown Requested

- Acceleration of the system
- Tension in the rope
- Contact force between objects

## Diagram

Draw a separate FBD for EACH object. Include tension as a force on each object pulling toward the rope's connection point. (By Newton's Third Law, both objects experience the same tension magnitude, in opposite directions.)

## Equations

For the system as a whole (to find acceleration):
$$\sum F_{\text{external on system}} = (m_1 + m_2) \cdot a$$

For one object alone (to find tension T):
$$\sum F_{\text{on m}_1} = m_1 \cdot a$$

## Solving Pattern

1. Draw a FBD for each object separately.
2. For "system" equation: add up all external forces (ignore internal tension, it cancels), set equal to total mass × a.
3. Solve for acceleration.
4. Substitute a back into one object's FBD equation to find tension.
5. Check: tension should be between 0 and the total external force.

## Worked Example: Two Blocks on a Frictionless Surface

Block A (2 kg) pulled right by F = 10 N, connected by rope to Block B (3 kg).

**System:** ΣF = F = (m_A + m_B) × a → a = 10/5 = 2.0 m/s²

**Block B alone (to find tension T):** ΣF on B = T = m_B × a = 3 × 2.0 = 6.0 N

**Block A alone (to verify):** F − T = m_A × a → 10 − 6 = 2 × 2.0 = 4 ✓

## Atwood Machine Special Case

Masses m₁ and m₂ hang over a pulley (m₁ < m₂). Define positive as the direction m₂ falls.

$$a = \frac{(m_2 - m_1)g}{m_1 + m_2} \qquad T = \frac{2m_1 m_2 g}{m_1 + m_2}$$

Derivation: ΣF on m₁: T − m₁g = m₁a; ΣF on m₂: m₂g − T = m₂a. Add both equations → a. Substitute back → T.

## Unit Check

Tension in N. Acceleration in m/s². If you got a > g for any component of this system, something is wrong.

## Traps

- Drawing tension on only one object (it acts on both — in opposite directions).
- Forgetting to separate the equations when solving for tension (can't use the whole-system equation for T because T cancels in that one).
- Wrong sign for one mass in the Atwood setup — be consistent about which direction you define as positive.
- Confusing the "system acceleration" with "one block's acceleration" (they're the same magnitude when connected, but sometimes different if the rope goes over a pulley at a different angle).

## Drills

[[../drills/newtons-second-law-drill]] (Problems 4 and 7)
