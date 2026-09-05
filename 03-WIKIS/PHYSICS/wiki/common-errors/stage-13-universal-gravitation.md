---
type: common-errors
tags: [physics]
timeline: later
---

# Common Errors — Stage 13: Universal Gravitation (Ch 13)

1. **Using g = 9.8 m/s² everywhere.** This value holds only near Earth's surface. At altitude h above the surface, g = GM_E/(R_E + h)². For satellites, Moon, or other planets, you must calculate g from the general formula g = GM/r².

2. **Confusing the distance r with altitude h.** Newton's law uses r = distance from center to center. If a satellite is 200 km above Earth's surface and Earth's radius is 6371 km, then r = 6571 km — not 200 km. Always add the planet's radius.

3. **Treating F = mg as a special case of F = GMm/r² — then forgetting they're the same thing.** Near Earth's surface: F = mg = GMm/R² → g = GM/R². These are identical. The confusion: forgetting that the "g" in mgh (Stage 7 PE) loses accuracy at high altitude, while U = −GMm/r is always correct.

4. **Getting the sign of gravitational PE wrong.** U = −GMm/r is NEGATIVE for all finite distances (the system is bound). U → 0 as r → ∞. This means adding energy to an orbit raises it (less negative U), which is counterintuitive: a satellite in a higher orbit has MORE total energy, but slower speed.

5. **Applying Kepler's 3rd law to orbits around different central bodies.** T² = (4π²/GM)r³ — the constant (4π²/GM) changes depending on which mass M is at the center. The Sun's version and Earth's version are different. Keep M clear.

6. **Computing escape speed as v_escape = v_circular × √2 without knowing why.** At circular orbit: KE = GMm/(2r), total energy = −GMm/(2r). To escape: total energy = 0. So you need to double the KE → speed increases by √2. This is worth understanding, not just memorizing.

7. **Assuming orbital speed increases with radius.** Counterintuitively, higher orbits have LOWER orbital speed (v_c = √(GM/r) decreases as r increases). The Moon moves slower than the International Space Station.
