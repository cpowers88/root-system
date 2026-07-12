---
type: problem-type
status: draft
---

# Vertical Circular Motion Problems

## How to Recognize This Problem Type

- Object moves in a vertical circle: ball on a string, roller coaster loop, object going over a hill.
- The problem asks about forces or speed at a specific point on the circle — usually at the top or bottom.
- Key phrase: "minimum speed," "just barely maintains contact," "string just goes slack."

## Given Information Usually Includes

- Mass m and radius r
- Speed at one point (often need energy conservation to find speed at another — that's Stage 8)
- Sometimes asked: minimum speed at the top, maximum speed at the bottom, tension at a given point

## Unknown Usually Asked For

Tension T (or normal force n) at top or bottom. Minimum speed at top. Normal force at top of hill (when does contact break?).

## Diagram

Draw the FBD at EACH POSITION SEPARATELY. The inward direction rotates.

**At the TOP (string or loop):**
```
Center of circle is BELOW the object (below the top of the loop).
Wait — no. Center is in the middle of the loop.
At the TOP: center is below. Both T and mg point downward = INWARD.

     TOP:  [object]
            ↓ T   (string pulls object toward center = downward)
            ↓ mg  (gravity, also downward = also inward)
            
ΣF_inward = T + mg = mv²/r
T = mv²/r - mg
```

**At the BOTTOM:**
```
     BOTTOM: Center is above the object.
             ↑ T  (string/track pushes toward center = upward)
             ↓ mg (gravity, away from center = downward)
             
ΣF_inward = T - mg = mv²/r
T = mv²/r + mg
```

**At the TOP OF A HILL (object on road, not a loop):**
```
Center of hill's curvature is below the road surface.
Gravity mg pulls DOWN toward center = INWARD.
Normal force n pushes UP away from center = OUTWARD.

mg - n = mv²/r
n = m(g - v²/r)
When n = 0: v = √(gr) → object leaves the road
```

## Equations Used

**Top of loop (string/track):**
```
T + mg = mv²/r   →   T = mv²/r - mg
```

**Bottom of loop:**
```
T - mg = mv²/r   →   T = mv²/r + mg
```

**Minimum speed at top (T = 0, string just barely taut):**
```
mg = mv²_min/r   →   v_min = √(gr)
```

**Top of hill (normal force goes to zero):**
```
mg - n = mv²/r   →   v = √(gr) when n = 0
```

## Solving Pattern

1. Identify the position: top, bottom, or somewhere else.
2. Identify the direction of "inward" at that position.
3. Draw FBD, marking each force as inward (+) or outward (−).
4. Write: (sum of inward forces) − (sum of outward forces) = mv²/r.
5. Solve for the unknown.

## Unit Checks

[mv²/r] = kg·(m²/s²)/m = kg·m/s² = N ✓
[√(gr)] = √(m/s²·m) = √(m²/s²) = m/s ✓

## Traps

- **Incorrectly assigning gravity direction at the top.** At the top of the loop, gravity points INWARD (toward center). This trips up students who automatically write T − mg = mv²/r everywhere. At the top it's T + mg = mv²/r.
- **Assuming T is the same everywhere on the loop.** It's not. Tension is smallest at the top (gravity helps) and largest at the bottom (gravity opposes).
- **Mixing up "top of loop" and "top of hill."** In a loop, you're inside and the track pushes outward; minimum speed keeps you on the track. On a hill, you're outside and the road pushes upward; exceed the speed and you leave the road.

## Drills

[[../drills/circular-motion-forces-drill]]
