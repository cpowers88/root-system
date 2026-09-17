---
type: worked-example
timeline: reference
status: draft
---

# Projectile Launched from a Cliff (Angled Launch, Asymmetric)

## Problem Statement

A ball is thrown from the top of a cliff 40.0 m high at a speed of 15.0 m/s at an angle of 30.0° above the horizontal. Find: (a) the time of flight until the ball hits the ground, (b) the horizontal distance from the base of the cliff, and (c) the speed and direction of the ball just before impact.

## Problem Type

[[../problem-types/projectile-angled-launch]] — asymmetric (different launch and landing heights, so the range formula cannot be used).

## Given

- Initial speed: v₀ = 15.0 m/s
- Launch angle: θ₀ = 30.0°
- Cliff height: h = 40.0 m
- g = 9.80 m/s²

## Unknown

(a) Time of flight t
(b) Horizontal range R
(c) Landing speed and angle below horizontal

## Diagram

```
  v₀ at 30°
  /
 /
O ← launch point (origin)
|               <-- top of cliff, 40.0 m above ground
|
|
|
ground (y = -40.0 m, taking launch point as y = 0)

x-axis: rightward = positive
y-axis: upward = positive
```

## Model / Equation Choice

Standard projectile equations. Launch point is origin (x₀ = 0, y₀ = 0). The ball hits the ground at y = -40.0 m.

Do NOT use the range formula — launch and landing heights differ.

## Solution Steps

**Step 1: Decompose initial velocity.**
```
v₀ₓ = 15.0 cos 30.0° = 15.0 × 0.866 = 13.0 m/s
v₀ᵧ = 15.0 sin 30.0° = 15.0 × 0.500 = 7.50 m/s
```

**Step 2: Use y(t) = 0 to find time of flight (ball lands at y = -40.0 m).**
```
y = v₀ᵧ t - ½g t²
-40.0 = 7.50t - ½(9.80)t²
-40.0 = 7.50t - 4.90t²
4.90t² - 7.50t - 40.0 = 0
```

Apply quadratic formula (a = 4.90, b = -7.50, c = -40.0):
```
t = [7.50 ± √(7.50² + 4(4.90)(40.0))] / (2 × 4.90)
  = [7.50 ± √(56.25 + 784)] / 9.80
  = [7.50 ± √840.25] / 9.80
  = [7.50 ± 28.99] / 9.80
```

Take the positive root (negative root gives a time before launch):
```
t = (7.50 + 28.99) / 9.80 = 36.49 / 9.80 = 3.72 s
```

**(a) Time of flight = 3.72 s**

**Step 3: Find horizontal range.**
```
R = v₀ₓ × t = 13.0 × 3.72 = 48.4 m
```

**(b) Horizontal range = 48.4 m from the base of the cliff.**

**Step 4: Find landing velocity.**
```
vₓ = v₀ₓ = 13.0 m/s       (unchanged throughout)
vᵧ = v₀ᵧ - g t = 7.50 - 9.80(3.72) = 7.50 - 36.5 = -29.0 m/s    (downward)
```

Landing speed:
```
|v| = √(vₓ² + vᵧ²) = √(13.0² + 29.0²) = √(169 + 841) = √1010 = 31.8 m/s
```

Angle below horizontal:
```
θ = tan⁻¹(|vᵧ|/vₓ) = tan⁻¹(29.0/13.0) = tan⁻¹(2.23) = 65.8° below horizontal
```

**(c) Landing speed = 31.8 m/s at 65.8° below horizontal.**

## Units Check

- t: from quadratic with units (m and m/s²), result in s ✓
- R = (m/s)(s) = m ✓
- |v| = √((m/s)² + (m/s)²) = m/s ✓

## Final Answer

(a) 3.72 s  (b) 48.4 m  (c) 31.8 m/s at 65.8° below horizontal

## Explain-Back Prompt

Close the page and explain: Why couldn't we use R = v₀² sin 2θ / g here? Why did we get two roots from the quadratic, and why did we discard the negative one? What does the negative vᵧ at landing tell you about the ball's direction?

## Common Trap

Using R = v₀² sin 2θ / g — this formula is only valid when launch and landing heights are equal. When they differ, always go back to y(t) = landing height and solve the quadratic.

Also: choosing the wrong root. The negative root is physically meaningless (it corresponds to a time before launch). Always pick the positive root.

## Sources

- Serway & Jewett, 10th ed., Ch. 4.3, Example 4.3, pp. 92–94.
