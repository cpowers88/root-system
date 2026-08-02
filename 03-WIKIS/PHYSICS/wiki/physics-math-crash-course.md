\---

type: guide
timeline: now
status: ready
reference\_priority: core
tags: \[physics, math, school, meta-learning]
---

# Physics Math Crash Course

## What This Course Is For

This is the complete math bridge for the PHYS 2211 material represented by all
18 stages of this wiki. It is a review of the math physics actually uses, not a
second algebra, trigonometry, or calculus course.

The governing order is always:

```text
physical situation -> sketch -> known quantities -> math relationship
-> solve -> units -> physical reasonableness
```

Use \[\[math-readiness-path]] to decide **when** to study each module. Use this
page to learn or refresh **how** the math works. The current entry point is
\[\[#Stage 4 Immediate Bridge — Projectile Motion]].

## How to Use It Without Creating a Math Detour

For each module:

1. Read the physical anchor and exact meaning.
2. Cover the worked example and attempt it on paper.
3. Compare your work with the solution pattern.
4. Complete the transfer check with no notes.
5. Explain aloud what the math move meant physically.

A module is ready for use when you can recognize the needed move from a physics
situation. Memorizing a formula without knowing the situation is not a pass.

## The Whole Math Structure

```text
units and notation
  -> algebra and proportional reasoning
    -> functions, graphs, and slope
      -> geometry, trig, and radians
        -> vectors and components
          -> derivatives and integrals
            -> rotation, oscillation, waves, and relativity
```

The upper levels sit on the lower ones. When a physics problem stalls, move down
only far enough to repair the missing support, then return to the physics.

## Stage-to-Math Map

|Physics stage|Math used most|Crash-course module|
|-|-|-|
|1 — Measurement|scientific notation, units, dimensions, sig figs, proportions|1–2|
|2 — 1D motion|functions, graphs, slope, derivatives, areas, integrals|3, 7–8|
|3 — Vectors|geometry, trig, inverse trig, components|4–6|
|4 — 2D motion|components, quadratics, component derivatives|5–8|
|5–6 — Forces/circular motion|equation rearrangement, systems, incline trig, radians|2, 4, 6, 9|
|7–8 — Work/energy|dot product, powers, definite integrals, graph area|6, 8|
|9 — Momentum|signed components, systems, force-time integrals|6, 8|
|10–12 — Rotation/statics|radians, cross product, torque trig, integrals, equilibrium systems|6, 8–9|
|13–14 — Gravity/fluids|inverse-square ratios, geometry, density, multi-step algebra|2, 4, 10|
|15–17 — Oscillations/waves|sine/cosine functions, phase, trig derivatives, logs, simple differential equations|7, 11|
|18 — Relativity|ratios, radicals, limits, approximations|2, 10, 12|
|Labs throughout|uncertainty, graph slope, linearization, fit interpretation|13|

\---

# Module 1 — Numbers, Notation, and Calculator Control

## Scientific Notation

Write a number as:



```



$$a \\\\times 10^n \\\\qquad 1 \\\\le |a| < 10$$



```



The coefficient carries the measured digits; the exponent carries scale.



```text
45,000 = 4.5 x 10^4
0.00072 = 7.2 x 10^-4
```

For multiplication, multiply coefficients and add exponents. For division,
divide coefficients and subtract exponents.

$$\\frac{(6.0\\times10^7)(3.0\\times10^{-2})}{2.0\\times10^3}
= 9.0\\times10^2$$

## Calculator Discipline

* Use the `EE` or `EXP` key for powers of ten: `6.0 EE 7`, not
`6.0 x 10 ^ 7` unless you understand the calculator's precedence.
* Put an entire numerator and denominator in parentheses.
* Keep extra digits during the calculation; round once at the end.
* Check angle mode before trig: `DEG` for degree inputs, `RAD` for radian inputs.
* Estimate the sign and order of magnitude before pressing Enter.

## Significant Figures

* Multiplication/division: match the input with the fewest significant figures.
* Addition/subtraction: match the input with the fewest decimal places.
* Exact counts and defined conversion factors do not limit significant figures.

Example: `2.4 m x 3.15 m = 7.56 m^2`, reported as `7.6 m^2`.

## Transfer Check

Without notes, calculate `(3.0 x 10^5)(4.0 x 10^-3)` and state the correctly
rounded result. Before calculating, predict whether the answer is closer to
`10^2`, `10^3`, or `10^8`.

\---

# Module 2 — Units, Dimensions, Algebra, and Proportions

## Units Are Part of the Number

Treat units as algebraic factors.

$$72\\frac{\\mathrm{km}}{\\mathrm{h}}
\\left(\\frac{1000,\\mathrm{m}}{1,\\mathrm{km}}\\right)
\\left(\\frac{1,\\mathrm{h}}{3600,\\mathrm{s}}\\right)
=20\\frac{\\mathrm{m}}{\\mathrm{s}}$$

The unwanted units cancel. If they do not cancel to the requested unit, the
conversion chain is incomplete or reversed.

## Dimensional Analysis

In mechanics, the base dimensions are mass `M`, length `L`, and time `T`.

```text
velocity:     L/T
acceleration: L/T^2
force:        ML/T^2
energy:       ML^2/T^2
```

An equation can add or equate terms only when their dimensions match. In

$$x=x\_0+v\_0t+\\frac12at^2$$

every term has dimension `L`. Dimensions can reject a bad equation, but they
cannot prove that a dimensionless factor such as `1/2` is correct.

## Rearranging Equations Safely

Use inverse operations on the entire equation. Do not move symbols by an
unexplained sign-changing ritual.

Example: solve centripetal acceleration `a\\\_c = v^2/r` for `v`.

$$a\_cr=v^2 \\quad\\Rightarrow\\quad v=\\sqrt{a\_cr}$$

The negative square-root branch is excluded because `v` here denotes speed,
which is a magnitude. A velocity component could be negative.

## Fractions and Reciprocals

Never cancel through addition:

$$\\frac{a+b}{a}\\ne 1+b$$

The correct simplification is:

$$\\frac{a+b}{a}=1+\\frac{b}{a}$$

When dividing by a fraction, multiply by its reciprocal.

## Powers and Radicals

$$x^m x^n=x^{m+n},\\qquad \\frac{x^m}{x^n}=x^{m-n},
\\qquad (x^m)^n=x^{mn}$$

$$x^{-n}=\\frac1{x^n},\\qquad \\sqrt{x^2}=|x|$$

The last absolute value matters: a square root returns a nonnegative magnitude.

## Proportional Reasoning

If `y = kx`, then doubling `x` doubles `y`. If `y = kx^2`, doubling `x`
quadruples `y`. If `y = k/x^2`, doubling `x` makes `y` one fourth as large.

This is the fastest prediction tool in the course:

|Relationship|Scale change when `x -> 2x`|
|-|-|
|`y proportional to x`|`y -> 2y`|
|`y proportional to x^2`|`y -> 4y`|
|`y proportional to sqrt(x)`|`y -> sqrt(2)y`|
|`y proportional to 1/x`|`y -> y/2`|
|`y proportional to 1/x^2`|`y -> y/4`|

## Transfer Check

Starting with `F = GmM/r^2`, solve for `r`. Then state what happens to `F` if
only `r` triples.

\---

# Module 3 — Functions, Coordinates, Graphs, and Slope

## Function Meaning

`x(t)` means position is an output determined by time. The parentheses do not
mean multiplication.

```text
input t -> rule x(t) -> output position
```

In physics, the same situation may produce several linked functions:

$$x(t)\\longrightarrow v(t)=\\frac{dx}{dt}
\\longrightarrow a(t)=\\frac{dv}{dt}$$

## Coordinates and Signs

Choose an origin and positive direction before writing equations. A negative
value usually means opposite the chosen positive direction, not physically
impossible.

Keep these separate:

* position: location relative to the origin;
* displacement: change in position;
* distance: total path length;
* velocity: signed rate of position change;
* speed: magnitude of velocity.

## Slope

Between two points,

$$m=\\frac{y\_2-y\_1}{x\_2-x\_1}=\\frac{\\Delta y}{\\Delta x}$$

On an `x-t` graph, slope is velocity. On a `v-t` graph, slope is acceleration.
The slope's units expose its physical meaning.

Example: if position rises from `3 m` to `15 m` between `2 s` and `6 s`,

$$v\_{avg}=\\frac{15-3}{6-2}=3\\ \\mathrm{m/s}$$

## Area Under a Graph

Slope moves down the chain; signed area moves back up:

```text
slope of x-t -> v
slope of v-t -> a
area under a-t -> change in v
area under v-t -> displacement
```

Area below the horizontal axis is negative. Total distance is not always the
same as signed area/displacement.

## Common Graph Shapes

|Function|Graph|Physics appearance|
|-|-|-|
|constant|horizontal line|constant position, velocity, or acceleration|
|linear `mx+b`|straight line|constant rate|
|quadratic `at^2+bt+c`|parabola|position under constant acceleration|
|sine/cosine|repeating wave|oscillation and waves|
|inverse-square `k/r^2`|steep decay|gravity|

## Transfer Check

Sketch a velocity-time graph that is `+4 m/s` for 3 seconds and then `-2 m/s`
for 2 seconds. Find displacement and total distance. Explain why they differ.

\---

# Module 4 — Geometry, Angles, Trigonometry, and Radians

## Geometry Physics Reuses

$$\\text{rectangle area}=lw,\\qquad \\text{triangle area}=\\frac12bh$$

$$\\text{circle area}=\\pi r^2,\\qquad \\text{circumference}=2\\pi r$$

$$\\text{cylinder volume}=\\pi r^2h,\\qquad
\\text{sphere volume}=\\frac43\\pi r^3$$

Areas appear in pressure, fluid flow, and graph integrals. Volumes appear in
density and buoyancy. The perpendicular distance to a line of action appears
in torque.

## Right-Triangle Trig

Relative to the selected angle `theta`:

$$\\sin\\theta=\\frac{\\text{opposite}}{\\text{hypotenuse}},\\quad
\\cos\\theta=\\frac{\\text{adjacent}}{\\text{hypotenuse}},\\quad
\\tan\\theta=\\frac{\\text{opposite}}{\\text{adjacent}}$$

The labels opposite and adjacent change when the selected angle changes.

## Pythagorean Theorem

For perpendicular components,

$$c^2=a^2+b^2$$

This rebuilds a vector magnitude, a total acceleration from perpendicular
parts, or the length of a diagonal.

## Inverse Trig and Quadrants

Use inverse trig to recover an angle from a ratio:

$$\\theta=\\tan^{-1}\\left(\\frac{y}{x}\\right)$$

But the raw calculator answer may identify the wrong quadrant. First sketch the
signs of `x` and `y`, then use `atan2(y,x)` when available or correct the angle
manually.

## Degrees and Radians

Radians measure arc length relative to radius:

$$\\theta=\\frac{s}{r},\\qquad 2\\pi\\ \\mathrm{rad}=360^\\circ$$

$$\\theta\_{rad}=\\theta\_{deg}\\frac{\\pi}{180}$$

Calculus formulas for angular motion and trig derivatives require radians.
Degrees are convenient for geometry; radians are the natural language of
rotation.

## Trig Identities Actually Needed

The full archive contains many identities. Physics I repeatedly needs only a
small core:

$$\\sin^2\\theta+\\cos^2\\theta=1$$

$$\\sin(2\\theta)=2\\sin\\theta\\cos\\theta$$

$$\\cos(A-B)=\\cos A\\cos B+\\sin A\\sin B$$

The last identity underlies dot products and wave phase comparisons. Sum-to-
product identities become useful in Stage 17 for interference and beats.

## Non-Right Triangles

Use the law of cosines when two sides and their included angle are known:

$$c^2=a^2+b^2-2ab\\cos C$$

Use the law of sines when a known side-angle pair is available:

$$\\frac{a}{\\sin A}=\\frac{b}{\\sin B}=\\frac{c}{\\sin C}$$

Component methods are usually more dependable for physics vectors, but these
laws are useful checks.

## Transfer Check

A cable pulls with `200 N` at `35 degrees` above horizontal. Without notes,
find its horizontal and vertical components and verify that rebuilding them
returns `200 N`.

\---

# Module 5 — Vectors and Component Thinking

## Scalar Versus Vector

A scalar has magnitude only. A vector has magnitude and direction.

```text
scalar: mass, time, temperature, energy, speed
vector: displacement, velocity, acceleration, force, momentum
```

## Unit-Vector Form

$$\\vec A=A\_x\\hat i+A\_y\\hat j+A\_z\\hat k$$

The unit vectors carry direction; the components carry signed amount and units.

## Decompose, Operate, Rebuild

For an angle measured from the positive x-axis,

$$A\_x=A\\cos\\theta,\\qquad A\_y=A\\sin\\theta$$

Add vectors by components:

$$R\_x=\\sum A\_x,\\qquad R\_y=\\sum A\_y$$

Then rebuild:

$$R=\\sqrt{R\_x^2+R\_y^2},\\qquad
\\theta=\\operatorname{atan2}(R\_y,R\_x)$$

This is the central spatial move of the course: break a slanted physical
quantity into perpendicular work lanes, solve each lane, then recombine.

## Coordinate Rotation on an Incline

For a block on a ramp, rotate the axes so one axis runs along the ramp and one
runs perpendicular to it. Gravity does not rotate; its components become

$$mg\\sin\\theta\\ \\text{along the ramp},\\qquad
mg\\cos\\theta\\ \\text{perpendicular to the ramp}$$

The component formulas depend on the diagram and selected angle, not a chant
that sine always means vertical.

## Transfer Check

Two forces act on a connection: `80 N` at `20 degrees` and `55 N` at
`140 degrees`, measured counterclockwise from +x. Find the resultant components,
magnitude, and quadrant before calculating its final angle.

\---

# Module 6 — Dot Products, Cross Products, Systems, and Quadratics

## Dot Product: How Much Lies Along

$$\\vec A\\cdot\\vec B=AB\\cos\\theta=A\_xB\_x+A\_yB\_y$$

The output is a scalar. In work,

$$W=\\vec F\\cdot\\vec d=Fd\\cos\\theta$$

Only the part of force along the displacement transfers energy through work.

## Cross Product: How Much Produces Rotation

$$|\\vec A\\times\\vec B|=AB\\sin\\theta$$

The output is a vector perpendicular to the plane of `A` and `B`. Torque is

$$\\vec\\tau=\\vec r\\times\\vec F$$

Physical anchor: point the fingers of your right hand along `r`, curl toward
`F`, and your thumb points along torque. Counterclockwise torque is commonly
chosen positive when solving a planar statics problem, but the chosen sign
convention must be stated.

Dot uses cosine because it measures parallel alignment. Cross uses sine because
it measures perpendicular leverage.

## Simultaneous Equations

Connected objects, force balance, collisions, and statics often create several
equations with several unknowns.

Example pattern:

$$T-m\_1g=m\_1a$$
$$m\_2g-T=m\_2a$$

Add the equations to eliminate `T`, solve for `a`, then substitute back for
`T`. Elimination is usually cleaner than guessing separate formulas.

## Quadratic Equations

Projectile position frequently becomes

$$at^2+bt+c=0$$

Use factoring when obvious or

$$t=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}$$

Physics decides which root is usable. A negative time may describe the
mathematical extension before launch, not the requested flight time. Two
positive roots may represent passing the same height on the way up and down.

## Transfer Check

For `y(t)=12t-4.9t^2`, solve `y=5 m`. Explain the physical meaning of both
positive roots instead of discarding one automatically.

\---

# Stage 4 Immediate Bridge — Projectile Motion

This is the current practical entry point. A projectile is two independent
one-dimensional motions sharing one clock.

## Build the Model From the Sketch

For launch speed `v\\\_0` at angle `theta\\\_0`:

$$v\_{0x}=v\_0\\cos\\theta\_0,\\qquad
v\_{0y}=v\_0\\sin\\theta\_0$$

Horizontal lane:

$$a\_x=0,\\qquad v\_x=v\_{0x},\\qquad x=x\_0+v\_{0x}t$$

Vertical lane:

$$a\_y=-g,\\qquad v\_y=v\_{0y}-gt,
\\qquad y=y\_0+v\_{0y}t-\\frac12gt^2$$

## Worked Example

A ball leaves ground level at `20.0 m/s`, `30.0 degrees` above horizontal.
Ignore air resistance and find time to peak, maximum height, total flight time,
and range.

Components:

$$v\_{0x}=20\\cos30^\\circ=17.3\\ \\mathrm{m/s}$$
$$v\_{0y}=20\\sin30^\\circ=10.0\\ \\mathrm{m/s}$$

At the peak, vertical velocity is zero:

$$0=10.0-9.80t \\Rightarrow t\_{peak}=1.02\\ \\mathrm{s}$$

Height:

$$y\_{max}=10.0(1.02)-4.90(1.02)^2=5.10\\ \\mathrm{m}$$

Because launch and landing heights match, the downward half mirrors the upward
half in time:

$$t\_{flight}=2.04\\ \\mathrm{s}$$

Horizontal range:

$$R=v\_{0x}t=17.3(2.04)=35.3\\ \\mathrm{m}$$

Checks: range has units of length; it is positive; flight time is twice time to
peak only because the start and end heights match.

## Cold Transfer Rep

Launch a fresh object at `18 m/s`, `40 degrees` from a platform `6 m` above the
landing level. Find landing time, horizontal range, and landing velocity. Do not
use symmetry because the launch and landing heights differ.

\---

# Module 7 — Derivatives: Rates, Slopes, and Change

## Physical Meaning Before Rules

The derivative is an instantaneous rate of change: the slope of a graph at one
point.

$$v=\\frac{dx}{dt},\\qquad a=\\frac{dv}{dt}
=\\frac{d^2x}{dt^2}$$

The units change by division by the independent variable. Differentiating
position in meters with respect to time in seconds produces meters per second.

## Rules Needed in Physics I

$$\\frac{d}{dt}(c)=0$$

$$\\frac{d}{dt}(t^n)=nt^{n-1}$$

$$\\frac{d}{dt}\[cf(t)]=c\\frac{df}{dt}$$

$$\\frac{d}{dt}\[f+g]=f'+g'$$

$$\\frac{d}{dt}\[f(g(t))]=f'(g(t))g'(t)$$

The last is the chain rule: change through a nested dependency.

Trig derivatives use radians:

$$\\frac{d}{dt}\\sin(\\omega t+\\phi)=
\\omega\\cos(\\omega t+\\phi)$$

$$\\frac{d}{dt}\\cos(\\omega t+\\phi)=
-\\omega\\sin(\\omega t+\\phi)$$

## Motion Example

If

$$x(t)=2+6t-3t^2$$

then

$$v(t)=6-6t,\\qquad a(t)=-6$$

At `t=1 s`, velocity is zero but acceleration is not. The object is at a turning
point.

## Vector Derivatives

Differentiate each component independently:

$$\\vec r(t)=x(t)\\hat i+y(t)\\hat j$$

$$\\vec v(t)=\\frac{dx}{dt}\\hat i+\\frac{dy}{dt}\\hat j$$

In uniform circular motion, speed can stay constant while velocity changes
because the direction of the vector changes.

## Later Physical Derivatives

```text
power:                    P = dE/dt
force in momentum form:   F = dp/dt
angular velocity:         omega = dtheta/dt
angular acceleration:     alpha = domega/dt
torque:                   tau = dL/dt
force from potential:     F\\\_x = -dU/dx
```

Each reads as “how fast the quantity on top is changing.”

## Transfer Check

Given `x(t)=4t^3-6t^2+2`, find `v(t)` and `a(t)`. Find every time when velocity
is zero and determine the sign of acceleration there.

\---

# Module 8 — Integrals: Accumulation, Area, and Continuous Sums

## Physical Meaning

An integral accumulates many small contributions. Geometrically, a definite
integral is signed area under a curve.

$$\\Delta x=\\int\_{t\_1}^{t\_2}v(t),dt$$

$$\\Delta v=\\int\_{t\_1}^{t\_2}a(t),dt$$

$$W=\\int\_{x\_1}^{x\_2}F\_x(x),dx$$

$$J=\\int\_{t\_1}^{t\_2}F(t),dt$$

The integrand's units multiply by the differential's units. For work,
`N x m = J`. For impulse, `N x s = kg m/s`.

## Antiderivatives Needed

$$\\int t^n,dt=\\frac{t^{n+1}}{n+1}+C\\qquad(n\\ne-1)$$

$$\\int\\cos(kt),dt=\\frac1k\\sin(kt)+C$$

$$\\int\\sin(kt),dt=-\\frac1k\\cos(kt)+C$$

An indefinite integral needs `+C`. A definite integral uses bounds and produces
a net change, so the constants cancel.

## Constant-Acceleration Example

Starting from `a(t)=a`,

$$v(t)=\\int a,dt=at+C$$

The initial condition `v(0)=v\\\_0` makes `C=v\\\_0`, so

$$v(t)=v\_0+at$$

Integrating again and applying `x(0)=x\\\_0` gives

$$x(t)=x\_0+v\_0t+\\frac12at^2$$

Initial conditions are the physical meaning of constants of integration.

## Variable-Force Example

If a spring force magnitude grows as `F(x)=kx`, the work required to stretch it
from `0` to `X` is

$$W=\\int\_0^Xkx,dx=\\frac12kX^2$$

The triangle under the `F-x` graph gives the same result.

## Continuous Mass Distributions

Moment of inertia is a weighted sum of tiny mass pieces:

$$I=\\int r^2,dm$$

Farther mass counts more because of the `r^2` weight. In this course, the main
skill is setting up or interpreting the integral; many standard shapes use
tabulated results.

## Transfer Check

A force increases linearly from `0 N` to `12 N` over `4 m`. Find the work by
graph area and by writing an integral. Show that both methods agree.

\---

# Module 9 — Circular and Rotational Math

## Linear–Angular Bridge

Arc length connects translation and rotation:

$$s=r\\theta$$

Differentiate with respect to time:

$$v\_t=r\\omega,\\qquad a\_t=r\\alpha$$

Radial acceleration is

$$a\_r=\\frac{v^2}{r}=\\omega^2r$$

Tangential acceleration changes speed. Radial acceleration changes direction.
They are perpendicular, so

$$a=\\sqrt{a\_t^2+a\_r^2}$$

## Translation–Rotation Analogy

|Translation|Rotation|
|-|-|
|position `x`|angle `theta`|
|velocity `v`|angular velocity `omega`|
|acceleration `a`|angular acceleration `alpha`|
|mass `m`|moment of inertia `I`|
|force `F`|torque `tau`|
|momentum `p=mv`|angular momentum `L=I omega`|
|`F=ma`|`tau=I alpha`|
|`K=1/2 mv^2`|`K\\\_rot=1/2 I omega^2`|

The analogy is a map, not permission to swap symbols without checking the
physical situation and assumptions.

## Static Equilibrium

Choose signs and a pivot, then solve

$$\\sum F\_x=0,\\qquad \\sum F\_y=0,
\\qquad \\sum\\tau=0$$

Choose a pivot that passes through unknown forces when possible; those forces
then have zero lever arm and drop from the torque equation.

## Transfer Check

A `3.0 m` horizontal beam is hinged at the wall. A `200 N` load hangs at the
far end, and a vertical support force acts `2.0 m` from the hinge. Write the
torque equation about the hinge and solve the support force. Then use vertical
force balance to find the hinge's vertical force.

\---

# Module 10 — Ratios, Scaling, Geometry, and Multi-Step Models

## Inverse-Square Laws

For `F=k/r^2`, compare two states without recalculating the constant:

$$\\frac{F\_2}{F\_1}=\\left(\\frac{r\_1}{r\_2}\\right)^2$$

This is central to gravity and orbital reasoning.

## Density, Pressure, and Flow

$$\\rho=\\frac{m}{V},\\qquad P=\\frac{F}{A}$$

$$A\_1v\_1=A\_2v\_2$$

The continuity equation says the same volume rate passes each cross-section for
steady incompressible flow. If area decreases, speed increases.

Bernoulli's equation is multi-term algebra with an energy-per-volume structure:

$$P+\\frac12\\rho v^2+\\rho gy=\\text{constant along a streamline}$$

Before solving, predict which pressure, speed, or height term should rise or
fall. Then rearrange the entire equation and keep units consistent.

## Limiting-Case Checks

Ask what the equation becomes when a quantity goes to zero, becomes very large,
or two states become equal.

Examples:

* `a\\\_c=v^2/r` goes to zero when `v -> 0`.
* gravitational force goes to zero as `r -> infinity`.
* Bernoulli reduces to hydrostatic pressure when both speeds are equal.

## Transfer Check

Water enters a pipe of area `6 cm^2` at `2 m/s` and exits through area
`2 cm^2`. Find the exit speed by a ratio before doing any unit conversion.
Explain the physical direction of the change.

\---

# Module 11 — Oscillations, Waves, Phase, and Logarithms

## Sinusoidal Motion

Simple harmonic motion can be written

$$x(t)=A\\cos(\\omega t+\\phi)$$

where:

|Symbol|Meaning|Unit|
|-|-|-|
|`A`|amplitude, maximum displacement|m|
|`omega`|angular frequency|rad/s|
|`phi`|phase constant, starting position in cycle|rad|
|`T`|period|s|
|`f`|frequency|Hz = 1/s|

$$\\omega=2\\pi f=\\frac{2\\pi}{T}$$

Differentiation shows the physics:

$$v(t)=-A\\omega\\sin(\\omega t+\\phi)$$

$$a(t)=-A\\omega^2\\cos(\\omega t+\\phi)=-\\omega^2x(t)$$

Acceleration points opposite displacement, back toward equilibrium.

## Differential-Equation Reading

$$\\frac{d^2x}{dt^2}=-\\omega^2x$$

You do not need to invent its solution from scratch here. You must be able to
read it: the second time derivative of position is proportional to position and
opposite in sign. Sine and cosine are the functions whose second derivatives
have exactly that structure.

## Waves

A traveling sinusoidal wave can be represented as

$$y(x,t)=A\\sin(kx-\\omega t+\\phi)$$

with

$$k=\\frac{2\\pi}{\\lambda},\\qquad
v=\\frac{\\omega}{k}=f\\lambda$$

`kx-omega t+phi` is the phase. Points with equal phase occupy the same place in
their oscillation cycle.

The wave equation

$$\\frac{\\partial^2y}{\\partial x^2}
=\\frac1{v^2}\\frac{\\partial^2y}{\\partial t^2}$$

uses partial derivatives because `y` depends on both position and time. The
course requires reading this structure, not solving general partial differential
equations.

## Superposition and Beats

Waves add point by point:

$$y\_{total}=y\_1+y\_2$$

Useful sum identities expose the slowly varying beat envelope. The practical
result for nearby frequencies is

$$f\_{beat}=|f\_1-f\_2|$$

## Logarithms and Decibels

Logarithms turn ratios across huge scales into manageable differences:

$$\\beta=10\\log\_{10}\\left(\\frac{I}{I\_0}\\right)$$

A factor of 10 in intensity adds `10 dB`; a factor of 100 adds `20 dB`. Do not
confuse intensity ratio with perceived loudness.

## Transfer Check

For `x(t)=0.08 cos(6t+pi/3) m`, identify amplitude, angular frequency, phase,
period, and frequency. Differentiate to find velocity and acceleration.

\---

# Module 12 — Limits, Approximations, and Relativity

## Limits as Behavior

A limit asks what an expression approaches as its input approaches a value. In
physics, this is often a sanity check rather than a formal proof.

The Lorentz factor is

$$\\gamma=\\frac1{\\sqrt{1-v^2/c^2}}$$

As `v -> 0`, `gamma -> 1`, so relativistic equations reduce to familiar
Newtonian behavior. As `v -> c`, the denominator approaches zero and `gamma`
grows without bound.

## Small-Parameter Approximations

When `|x|` is much smaller than 1 and `x` is in radians,

$$\\sin x\\approx x,\\qquad \\cos x\\approx1-\\frac{x^2}{2}$$

The pendulum's familiar small-angle period depends on `sin theta approximately theta`. The approximation fails at larger angles.

For low speeds, define `beta=v/c`. If `beta^2` is tiny, then relativity is a
small correction. Estimate before calculating.

## Transfer Check

Estimate `gamma` for `v=0.01c` and for `v=0.90c`. State which case should look
Newtonian before calculating precisely.

\---

# Module 13 — Measurement Uncertainty and Lab Math

## Measurement Form

$$x=x\_{measured}\\pm\\delta x$$

Absolute uncertainty has the same unit as the measurement. Fractional and
percent uncertainty are

$$\\frac{\\delta x}{|x|},\\qquad
100\\frac{\\delta x}{|x|}%$$

For this course's appendix rules:

* addition/subtraction: add absolute uncertainties;
* multiplication/division: add percent uncertainties;
* powers: multiply percent uncertainty by the absolute value of the power.

Use \[\[appendix/uncertainty]] for examples and the course's expected convention.

## Graphs and Experimental Models

Many labs turn a relationship into a straight line:

$$y=mx+b$$

The slope and intercept must be interpreted with units. For example, graphing
`v` against `t` makes slope acceleration. Graphing spring force against
extension makes slope spring constant.

Do not report a trendline number without stating:

1. what was placed on each axis;
2. the slope's physical meaning and unit;
3. whether the intercept should physically be zero;
4. whether uncertainty supports the conclusion.

Full statistics, hypothesis tests, probability distributions, chi-square
tables, and confidence-interval workflows from the old math folder are not
part of the current Physics WIKI. Pull one only if a real PHYS 2211 lab requires
it.

## Transfer Check

Length is `(5.0 +/- 0.1) m` and width is `(2.0 +/- 0.1) m`. Calculate area and
its percent uncertainty using the course appendix rule.

\---

# High-Value Error Checklist

Before accepting a solution, ask:

* Did I draw the situation and choose axes?
* Did I separate vectors into components before adding?
* Is the calculator in the correct angle mode?
* Did I use radians where calculus or angular equations require them?
* Did I preserve signs through the algebra?
* Did I square the entire quantity, including units?
* Did I keep both quadratic roots until physics classified them?
* Did I confuse slope with area?
* Did I confuse speed with velocity or magnitude with component?
* Did I use cosine for alignment/dot product and sine for perpendicular
leverage/cross product?
* Do every term and the final answer have compatible units?
* Does the sign, scale, direction, and limiting case make physical sense?

\---

# What From the Old Math Folder Matters

The external archive at `D:\\\\SCHOOL\\\\Chatt Tech Files\\\\math` was screened on
2026-07-18. It remains external reference material; no files were copied or
modified.

## Core Support

|Source|Best use here|
|-|-|
|`Algebra\\\_Cheat\\\_Sheet.pdf`|exponents, radicals, factoring, quadratics, functions, common algebra errors|
|`Geometric and Algebraic Formula Sheet.pdf`|areas, volumes, slope, line forms, quadratic form|
|`Unit Circle ADA Compliant.pdf`|signs by quadrant and common angles|
|`Updated Formulas and Identities Labeled.pdf`|core identities, laws of sines/cosines, polar/component formulas|
|`Common\\\_Derivatives\\\_Integrals.pdf`|derivative and antiderivative lookup|
|`Applications of Derivatives - Formula Sheet.docx`|rates, velocity, acceleration, position|
|`Applications of Integration - Formula Sheet.docx`|net change, work, springs, center of mass, hydrostatic force|
|`Calculus Formula Reference Sheet.pdf`|compact derivative/integral review|

## Lookup Only When a Stage Calls for It

* derivative, integral, limit, and trig formula variants;
* u-substitution or integration by parts if a textbook derivation actually uses
them;
* Maclaurin series for small-angle or low-speed approximation context;
* logarithm sheets for sound intensity.

## Parked Outside Current Scope

* most Calc II convergence tests, general power-series interval work, trig
substitution, partial fractions, arc length, and surfaces of revolution;
* hyperbolic functions, Laplace transforms, and general differential-equation
solution machinery;
* most of the `statistics` folder beyond the uncertainty and graphing skills
named above;
* complex-number and De Moivre material.

These topics are valid mathematics, but studying them now would enlarge the path
without improving performance on the Physics WIKI's current mechanics scope.

\---

# Compact Formula Spine

This is a retrieval sheet, not a substitute for the modules.

```text
units:       multiply by conversion factors equal to 1
slope:       Delta y / Delta x
components:  Ax=A cos(theta), Ay=A sin(theta)
magnitude:   A=sqrt(Ax^2+Ay^2)
dot:         A dot B=AB cos(theta)
cross size:  |A x B|=AB sin(theta)
quadratic:   x=(-b +/- sqrt(b^2-4ac))/(2a)
derivative:  v=dx/dt, a=dv/dt
integral:    Delta x=integral(v dt), Delta v=integral(a dt)
rotation:    s=r theta, v=r omega, at=r alpha, ar=v^2/r
oscillation: omega=2pi f=2pi/T
wave:        v=f lambda=omega/k
relativity:  gamma=1/sqrt(1-v^2/c^2)
```

# Transfer-Check Answer Key

Attempt each check before opening this section.

1. **Numbers:** `1.2 x 10^3`; the expected scale is `10^3`.
2. **Algebra/scaling:** `r=sqrt(GmM/F)`; tripling `r` reduces `F` to `F/9`.
3. **Graphs:** displacement `8 m`; distance `16 m`. The negative-velocity
interval subtracts from displacement but still adds traveled distance.
4. **Trig:** `F\\\_x=164 N`, `F\\\_y=115 N`; `sqrt(F\\\_x^2+F\\\_y^2)=200 N` after rounding.
5. **Vectors:** `R\\\_x=33.0 N`, `R\\\_y=62.7 N`, `R=70.9 N`, approximately
`62.2 degrees` in Quadrant I.
6. **Quadratic:** `t=0.532 s` and `t=1.92 s`; the object passes `5 m` once on
the way up and again on the way down.
7. **Stage 4 cold rep:** `t=2.80 s`, range `38.6 m`, and landing velocity
approximately `(13.8 i - 15.9 j) m/s`, magnitude `21.0 m/s`, directed about
`49.0 degrees` below horizontal.
8. **Derivatives:** `v=12t^2-12t`, `a=24t-12`; velocity is zero at `t=0` and
`t=1 s`, with accelerations `-12 m/s^2` and `+12 m/s^2`, respectively.
9. **Integrals:** triangle area `24 J`; `F(x)=3x`, so
`integral from 0 to 4 of 3x dx=24 J`.
10. **Rotation/statics:** support force `300 N` upward; hinge vertical force
`100 N` downward for the idealized weightless beam.
11. **Fluids:** exit speed `6 m/s`; cutting area to one third requires speed to
triple to preserve volume flow rate.
12. **Oscillation:** `A=0.08 m`, `omega=6 rad/s`, `phi=pi/3`,
`T=pi/3 s=1.05 s`, `f=0.955 Hz`, `v=-0.48 sin(6t+pi/3) m/s`, and
`a=-2.88 cos(6t+pi/3) m/s^2`.
13. **Relativity:** `gamma approximately 1.00005` at `0.01c` and `2.294` at
`0.90c`; only the first is effectively Newtonian.
14. **Uncertainty:** `A=10.0 m^2`; percent uncertainty is `2%+5%=7%`, so
`A=(10.0 +/- 0.7) m^2` under the course appendix rule.

# Mastery Standard for the Crash Course

The math bridge is working when Chris can:

* translate a physical description into a sketch, variables, and units;
* rearrange equations without losing signs or dimensions;
* read physical meaning from a graph's slope and area;
* use trig and components with correct quadrant and angle mode;
* distinguish dot-product alignment from cross-product leverage and apply the
physical right-hand rule;
* interpret derivatives as rates and integrals as accumulation;
* recognize the math structure used by rotation, fluids, oscillations, waves,
and relativity;
* reject an answer using units, sign, scale, direction, or a limiting case;
* complete the current stage's transfer rep without notes.

## Next Exact Action

Work the \[\[#Stage 4 Immediate Bridge — Projectile Motion]] cold transfer rep on
paper. Start with a sketch and separate x/y equation lanes before substituting
numbers. Record the first point where the setup stops feeling automatic; that
point selects the one module to review next.

