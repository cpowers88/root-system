---
type: common-errors
tags: [later, physics]
---

# Common Errors — Stage 10: Rotation of a Rigid Object (Ch 10)

1. **Confusing angular and tangential quantities.** ω is in rad/s (angular), v_t = rω is in m/s (tangential/linear). Students often substitute ω directly for v in kinematic energy equations — they are NOT interchangeable unless you are tracking radians vs. meters.

2. **Forgetting that moment of inertia depends on the rotation axis.** I = MR² for a ring about its central axis, but I = ½MR² for a solid disk, and I = 2MR²/5 for a sphere. Using the wrong formula — or using the formula for one axis when the problem requires another — gives a completely wrong answer.

3. **Applying the parallel-axis theorem in the wrong direction.** The theorem is I = I_cm + Md²; you can only ADD Md² to go from the center-of-mass axis to a parallel offset axis. You cannot subtract Md² from a non-center-of-mass axis and call the result I_cm.

4. **Using τ = rF (instead of τ = rF sin φ) without checking the angle.** The moment arm is r_⊥ = r sin φ, where φ is the angle between the position vector r and the force F. If the force is perpendicular to r, sin 90° = 1 and the formula reduces to τ = rF — but this is not always the case.

5. **Not accounting for both translational and rotational KE in rolling problems.** A rolling object has K = ½mv² + ½Iω². Forgetting the rotational term gives a speed that is too high (all energy goes to translation). Forgetting the translational term gives a speed that is too low.

6. **Assuming v_cm = Rω without verifying the no-slip condition.** This relationship holds only for rolling without slipping. If the problem involves sliding, you need the friction force and separate translational and rotational equations.

7. **Confusing clockwise vs. counterclockwise sign conventions for torque.** Pick one direction as positive and stick to it throughout the problem. Mixing conventions causes wrong sums for τ_net.

8. **Forgetting that torque depends on where the force is applied.** The same force applied at different points creates different torques. Force at the axis creates zero torque (r = 0). Force farther from the axis creates larger torque (larger r). This is why door hinges are placed at one edge, not the center.
