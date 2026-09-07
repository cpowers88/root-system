---
type: common-errors
tags: [physics]
timeline: later
---

# Common Errors — Stage 15: Oscillatory Motion (Ch 15)

1. **Confusing period T, frequency f, and angular frequency ω.** T = 1/f = 2π/ω. These are three different ways to describe the same repetition rate. Using ω where f is needed (or vice versa) in the wave or energy equations is the most common algebra error in this chapter.

2. **Thinking amplitude affects the period.** For an ideal spring-mass system and for a simple pendulum (small angle), the period T is INDEPENDENT of amplitude. Bigger swings take the same time as smaller swings. This is one of the most surprising and testable facts of SHM.

3. **Getting the phase constant φ wrong.** x(t) = A cos(ωt + φ). At t = 0: x₀ = A cos φ and v₀ = −Aω sin φ. You need BOTH initial conditions to pin down φ. A common mistake: using only x₀ and ignoring v₀, leading to ambiguity (two values of φ satisfy x₀ alone — you need v₀ to pick the correct one).

4. **Confusing the restoring force with friction or drag.** The restoring force F = −kx always points toward equilibrium (opposite to displacement). Drag opposes velocity (opposite to the direction of motion). They are different forces, act in different directions, and have very different effects.

5. **Using KE = ½mv_max² everywhere instead of ½mv² + ½kx².** Total energy E = ½kA² is constant. At a general position x: KE = E − PE = ½kA² − ½kx². Using v_max everywhere implies the object is at equilibrium — true only at x = 0.

6. **Applying the simple pendulum formula beyond small angles.** T = 2π√(L/g) is valid only for θ_max ≲ 15°. For larger amplitudes, the period is longer and the formula overestimates the frequency.

7. **Mixing up what "physical pendulum" means.** A simple pendulum is a point mass on a massless string. A physical pendulum is any rigid body pivoting about a point not at its center of mass — the formula changes: T = 2π√(I/mgd), where I is moment of inertia about the pivot and d is distance from pivot to center of mass.

8. **Confusing forced oscillation frequency with natural frequency.** When a system is driven at an external frequency ω_d, it oscillates at ω_d, not at its natural frequency ω₀ = √(k/m). Resonance occurs when ω_d ≈ ω₀ — that is when the amplitude is largest. It is wrong to say "the system always oscillates at ω₀ no matter what drives it."
