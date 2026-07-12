---
type: problem-type
status: draft
---

# Non-Uniform Circular Motion (Tangential + Radial Acceleration)

## How to Recognize This Problem Type

An object moves along a curved or circular path AND the problem says its speed is changing — "speeding up," "slowing down," "accelerating around the curve," or gives a rate of change of speed directly. If speed is explicitly constant, use [[circular-motion]] instead.

## Given Information Usually Present

Radius of curvature r, instantaneous speed v, and either dv/dt directly or enough information to find it (e.g., a tangential force and mass).

## Unknown Usually Requested

Total acceleration magnitude and direction, or one of the two components (radial or tangential) individually.

## Diagram to Draw

Point on the curved path with two perpendicular arrows: a_r pointing toward the center of curvature, a_t pointing along the direction of motion (same direction as v if speeding up, opposite if slowing down). See [[../concepts/tangential-and-radial-acceleration]].

## Equations Commonly Used

[[../equations/tangential-and-radial-acceleration]]

## Step-by-Step Solving Pattern

1. Sketch the path and the object's position; draw v tangent to the path.
2. Compute a_r = v²/r using the instantaneous speed at that point.
3. Compute a_t = dv/dt (often given directly, or found from a tangential force via F_t = ma_t).
4. Combine: a = √(a_r² + a_t²). Draw a_r and a_t as two legs of a right triangle if a direction is needed.
5. Check: if the problem says "constant speed," a_t must be zero — if you calculated otherwise, re-check the setup.

## Unit Checks

Both a_r and a_t are m/s². Combining with the Pythagorean theorem preserves m/s².

## Common Traps

- Forgetting the tangential component and reporting only a_r when the object is speeding up or slowing down.
- Adding a_r + a_t directly instead of combining perpendicular components with √(a_r²+a_t²).
- Using a stale or average speed for a_r = v²/r instead of the instantaneous speed at the point in question.

## Practice Drills

[[../drills/tangential-radial-acceleration-drill]]

## Sources

Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Section 4.5.
