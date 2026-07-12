---
type: common-errors
tags: [next, physics]
---

# Common Errors — Stage 4: Motion in Two Dimensions

1. **Treating 2D motion as a single 1D problem.** You cannot use one kinematic equation in two dimensions. Separate into x and y, solve each independently, then combine if needed.

2. **Assuming horizontal velocity changes during flight.** In the no-air-resistance model, there is no horizontal force. vₓ = v₀ₓ = constant throughout the entire trajectory. It does not decrease as the ball "slows down" — there is nothing slowing it horizontally.

3. **Forgetting that at the peak, the ball still has horizontal velocity.** At maximum height, vᵧ = 0, but vₓ = v₀ₓ (unchanged). The ball is moving horizontally at the peak — it is not momentarily at rest.

4. **Using the range formula when heights differ.** R = v₀² sin 2θ / g only works when the launch and landing heights are exactly equal. For cliff problems or anything asymmetric, go back to y(t) = final height and solve the quadratic.

5. **Sign errors with g.** In the kinematic equations as written (vᵧ = v₀ᵧ - gt, y = v₀ᵧ t - ½gt²), g is a positive number (9.80 m/s²) and the negative sign is explicit. Do not plug in g = -9.80 or you will double-negative yourself. Keep consistent with your coordinate system (upward positive).

6. **Taking the negative root of a quadratic for time.** When solving a quadratic for t, two roots appear. The negative root corresponds to a time before launch — physically meaningless. Always take the positive root.

7. **Calling "centripetal force" a separate force on a free body diagram.** Centripetal force is not a new kind of force — it is the net inward force. It is always provided by something real: tension, gravity, friction, or normal force. Draw only the real forces on the FBD.

8. **Thinking centripetal acceleration is zero because speed is constant.** Constant speed does not mean zero acceleration. In circular motion, the direction of velocity changes every instant, so dv⃗/dt ≠ 0 even when |v⃗| is constant.

9. **Using the diameter instead of the radius.** In a_c = v²/r, r is the radius (half the diameter). If a problem gives diameter, divide by 2 before using the formula.

10. **Getting the subscript order wrong in relative velocity.** Always write the full v⃗_PA = v⃗_PB + v⃗_BA before plugging in numbers. Check that the middle subscripts cancel. Do not guess the sign.

11. **Reporting only centripetal acceleration when speed is also changing.** If a problem says an object is speeding up or slowing down while turning, there is a tangential component too. Report a_r and a_t separately, or combine as a = √(a_r²+a_t²) — never just a_c alone.

12. **Adding a_r and a_t like plain numbers instead of perpendicular components.** They are perpendicular to each other (radial vs. tangent to the path). Combine with the Pythagorean theorem, not simple addition.
