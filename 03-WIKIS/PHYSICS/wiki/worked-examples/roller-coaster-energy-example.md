---
type: worked-example
stage: 8
---

# Worked Example: Roller Coaster Energy Conservation

## Physical Situation

A roller coaster car starts from rest at the top of a hill at height h₁ = 40.0 m. It rolls down and goes through a loop of radius R = 15.0 m. Find:
(a) The speed at the bottom of the hill (h = 0).
(b) The speed at the top of the loop.
(c) The minimum speed needed at the top of the loop to maintain contact with the track.

Assume the track is frictionless and the coaster is a point particle.

## System and Approach

System: roller coaster car + Earth.
No friction → mechanical energy is conserved.
Reference: set y = 0 at the bottom of the hill (lowest point).

## Part (a): Speed at the Bottom

State 1 (top of hill): v₁ = 0, h₁ = 40.0 m
State 2 (bottom): v₂ = ?, h₂ = 0

Energy conservation:

```
Ki + Ui = Kf + Uf
½mv₁² + mgh₁ = ½mv₂² + mgh₂
0 + mgh₁ = ½mv₂² + 0
```

Mass cancels:

```
gh₁ = ½v₂²
v₂ = √(2gh₁) = √(2 · 9.8 · 40.0) = √784 = 28.0 m/s
```

## Part (b): Speed at the Top of the Loop

The top of the loop is at height h₃ = 2R = 2(15.0) = 30.0 m above the bottom.

State 2 (bottom): v₂ = 28.0 m/s, h₂ = 0
State 3 (top of loop): v₃ = ?, h₃ = 30.0 m

```
½mv₂² + 0 = ½mv₃² + mgh₃
½v₂² = ½v₃² + gh₃
v₃² = v₂² − 2gh₃ = (28.0)² − 2(9.8)(30.0)
v₃² = 784 − 588 = 196
v₃ = 14.0 m/s
```

## Part (c): Minimum Speed at the Top of the Loop

At the top of the loop, the car is traveling in a circle. The centripetal force is provided by gravity and the normal force:

```
N + mg = mv²/R
```

The minimum speed occurs when N = 0 (car barely maintains contact):

```
mg = mv_min²/R
v_min = √(gR) = √(9.8 · 15.0) = √147 = 12.1 m/s
```

Since v₃ = 14.0 m/s > v_min = 12.1 m/s, the coaster successfully completes the loop.

## What Height Is Needed to Just Complete the Loop?

If you want the minimum starting height h_min that allows the coaster to complete the loop:

At the top of the loop, set v = v_min = √(gR).

```
Energy from h_min to top of loop:
mgh_min = ½mv_min² + mg(2R)
gh_min = ½(gR) + 2gR = gR/2 + 2gR = 5gR/2
h_min = 5R/2 = 5(15.0)/2 = 37.5 m
```

So the coaster must start at least 37.5 m above the bottom to complete a 15 m radius loop. (Starting at 40 m > 37.5 m confirms the car completes the loop.)

## Key Lessons

1. **Choose y = 0 at the lowest point** — all heights are then positive and unambiguous.
2. **Mass always cancels** in pure energy conservation problems (no friction, no external work).
3. **Two-step problems:** Use energy to find speed at the top of the loop, then use Newton's 2nd law (circular motion) to find the force condition.
4. **Frictionless assumption is critical** — real roller coasters must start higher to account for energy losses.
