---
type: problem-type
status: draft
---

# Problem Type — Vector Decomposition

## How to Recognize It

The problem gives you a vector as magnitude + angle and asks for components, OR gives you components and asks for magnitude + direction. Any time you need to translate between magnitude-and-angle form and component form.

## Typical Given Information

- Magnitude (speed, force, displacement length) and an angle (measured from +x, or from vertical, or from some reference direction)
- OR: two components (x and y values) — and you need the full vector description

## Unknown Requested

- Components: Ax and Ay (often needed before vector addition or Newton's 2nd law)
- OR: magnitude |A⃗| and direction θ (often needed as the final answer)

## Diagram

Always draw a right triangle:
```
        |
        |   /  A
     Ay |  /
        | /
        |/ θ
   -----+------
           Ax
```
Label A (hypotenuse), Ax (horizontal leg), Ay (vertical leg), θ (angle at origin).

## Equations

```
Ax = A cos θ      (x-component, when θ is from +x)
Ay = A sin θ      (y-component, when θ is from +x)
A  = √(Ax² + Ay²) (magnitude from components)
θ  = tan⁻¹(Ay/Ax) (direction from components — always check quadrant!)
```

## Solving Pattern

**Magnitude + angle → components:**
1. Draw the vector and label θ from +x.
2. Compute Ax = A cos θ (may be negative if in Q2 or Q3).
3. Compute Ay = A sin θ (may be negative if in Q3 or Q4).
4. Check signs: Q1 (+,+), Q2 (−,+), Q3 (−,−), Q4 (+,−).

**Components → magnitude + direction:**
1. Compute A = √(Ax² + Ay²).
2. Compute θ_calc = tan⁻¹(Ay/Ax) from a calculator.
3. Adjust for quadrant: if Ax < 0, add 180° to θ_calc.
4. State direction clearly (e.g., "61° above +x axis" or "29° south of west").

## Unit Check

Components have the same unit as the magnitude. Magnitude reconstructed from components should match the original (within rounding).

## Common Traps

- Swapping sin and cos (sketch prevents this).
- Not adjusting for quadrant after using tan⁻¹.
- Using the angle from the wrong reference (if the problem gives angle from +y, sin and cos swap).

## Drill

[[../drills/vector-components-drill]]
