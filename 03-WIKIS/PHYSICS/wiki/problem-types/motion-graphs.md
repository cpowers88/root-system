---
type: problem-type
status: draft
---

# Motion Graph Problems

## How to Recognize This Problem Type

The problem gives you a graph (x-t, v-t, or a-t) and asks you to extract quantities from it, or asks you to sketch one graph from another. Key phrases: "from the graph, find...," "sketch the velocity-time graph for the motion shown," "what is the acceleration between t = 2 s and t = 5 s?"

## Given Information Usually Present

A graph with labeled axes and one or more clearly defined time segments. Sometimes a verbal description of motion to convert into a graph.

## Unknown Usually Requested

- Velocity from an x-t graph (find the slope)
- Acceleration from a v-t graph (find the slope)
- Displacement from a v-t graph (find the area under the curve)
- A matching v-t graph given x-t, or vice versa

## Diagram to Draw

The problem provides the graph — your job is to annotate it. Draw tangent lines at specific points to find instantaneous slopes. Draw rectangles or triangles to find areas.

## Three Graphs and Their Relationships

| Graph | y-axis | x-axis | Slope means | Area means |
|---|---|---|---|---|
| x-t | position (m) | time (s) | velocity (m/s) | n/a |
| v-t | velocity (m/s) | time (s) | acceleration (m/s²) | displacement (m) |
| a-t | acceleration (m/s²) | time (s) | jerk (rarely used) | change in velocity (m/s) |

## How to Read Each Graph

### From an x-t graph:
- Steep slope → high speed (large |v|)
- Zero slope (horizontal line) → object is at rest
- Negative slope → moving in −x direction
- Curved (concave up) → speeding up; (concave down) → slowing down; (linear) → constant velocity

**To find v at a point:** draw the tangent line at that point; slope = Δx/Δt = v

### From a v-t graph:
- The value of v at any time reads directly off the y-axis
- Positive v → moving in +x; negative v → moving in −x
- Slope of line = acceleration: a = Δv/Δt
- Area between curve and t-axis = displacement (positive area above t-axis = +x displacement; negative area below = −x displacement)

**To find displacement from t₁ to t₂:** calculate the area under the v-t curve (rectangle, triangle, or trapezoid as appropriate)

### From an a-t graph:
- Constant (horizontal) line → constant acceleration → kinematic equations apply
- Area under the curve = change in velocity: Δv = ∫a dt

## Step-by-Step Solving Pattern

**Reading a slope:**
1. Pick two well-separated points on the line segment.
2. Read off their coordinates: (t₁, y₁) and (t₂, y₂).
3. Slope = (y₂ − y₁) / (t₂ − t₁). Include units.

**Finding area under v-t curve:**
1. Identify the shape: rectangle (v = const), triangle (v changes linearly from 0), or trapezoid.
2. Area of rectangle = base × height = Δt × v
3. Area of triangle = ½ × base × height = ½ × Δt × Δv
4. Add areas; count areas below the t-axis as negative.

## Unit Checks

- Slope of x-t: [m/s] ✓
- Slope of v-t: [m/s / s] = [m/s²] ✓
- Area under v-t: [m/s × s] = [m] ✓

## Common Traps

- Reading velocity from an x-t graph as the y-value instead of the slope. The y-value is position, not velocity.
- Treating a curved x-t section as having the same velocity throughout. Velocity is changing — must use tangent at each point.
- Forgetting that area below the t-axis on a v-t graph is negative displacement (object moving backward).
- Confusing "steep" with "high position." Steep slope on x-t = high speed, not a high location.

## Practice Drills

- [[../drills/motion-graphs-drill]]

## Sources

- Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed., Ch. 2.3–2.5, pp. 28–38.
