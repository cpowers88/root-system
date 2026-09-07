---
type: worked-example
timeline: reference
tags: [physics, calculus, school]
status: draft
---

# Projectile Motion from First Principles (Integration Method)

**A ball rolls horizontally off a 1.20 m table at 2.50 m/s. How far from the base
does it land?** — solved by writing the differential equations of motion and
integrating twice with boundary conditions, rather than by selecting a kinematic
formula. Followed by a from-scratch explanation of what `d²y/dt² = −g` means and
why `d` notation says "change."

> **Filed here 2026-08-19 on Chris's instruction.** This began as
> `.ROOT\needs_for_physics.md`, a loose root-level scratch file from the
> **2026-07-30 → 08-23 calculus-physics bridge sprint**
> (`../math-readiness-path.md` § Dated Evening Schedule). It was twice flagged as
> misplaced (2026-08-02 file-structure review; the Aug 12 update plan) and left in
> place both times pending Chris's call. Moved with `git mv`, so its history is
> intact. **Its own header named `calculus-links/` or `worked-examples/` as
> candidate homes; `worked-examples/` was chosen** because the artifact is a
> complete worked problem — `calculus-links/` pages are single-concept bridges on a
> fixed template, and [[../calculus-links/2d-kinematics-components]] already owns
> that concept.
>
> **⚠ Provenance: Gemini-assisted, not independently verified line by line.** The
> numerical result was checked (`t = √(2h/g) = 0.4949 s`, `R = 2.50 × 0.4949 =
> 1.24 m` ✓) and the derivation is sound, but the prose is another model's and has
> **not** been rewritten to this hub's authoring standards
> (`../authoring-standards.md` § Beginner-Readable Writing Rules). **It is Chris's
> own study material, kept in his own words** — treat it as a record of how he
> worked the idea, not as a hub-authored reference page.
>
> **Why this problem is worth keeping in this form:** it is the same physics as
> [[projectile-cliff-example]] but reached the opposite way. That page pattern-matches
> to standard projectile equations; this one *derives* them. Chris's known failure
> mode is unchecked substitution, not unknown formulas — so a page showing where the
> formulas come from is the direct counterweight.

```python
import math

# Given values
h = 1.20 # height in meters
v0x = 2.50 # initial horizontal speed in m/s
g = 9.80 # acceleration due to gravity in m/s^2 (or 9.81)

# Time to fall: y(t) = h - 0.5 * g * t^2 = 0 => t = sqrt(2h/g)
t_fall = math.sqrt(2 * h / g)

# Horizontal distance: x = v0x * t
x_distance = v0x * t_fall

print(f"Time: {t_fall} s")
print(f"Distance: {x_distance} m")


```

```text
Time: 0.49487165930539345 s
Distance: 1.2371791482634835 m


```

To solve this projectile motion problem using a rigorous calculus-based approach, we start from first principles by defining the kinematic differential equations of motion, integrating them with respect to time, and applying the appropriate boundary conditions.

---

### Step 1: Define the Coordinate System and Constants

Let us establish a Cartesian coordinate system where:

* The origin $(x = 0, y = 0)$ is located on the floor directly beneath the edge of the table where the ball rolls off.
* The positive $x$-axis points horizontally in the direction of the ball's motion.
* The positive $y$-axis points vertically upward.

Based on this coordinate system:

* Initial position at time $t = 0$: $x_0 = 0$, $y_0 = h = 1.20\text{ m}$.
* Initial velocity components:
* Horizontal velocity: $v_x(0) = \frac{dx}{dt}\Big\vert{}_{t=0} = v_{0x} = 2.50\text{ m/s}$.
* Vertical velocity: $v_y(0) = \frac{dy}{dt}\Big\vert{}_{t=0} = 0\text{ m/s}$ (since the ball rolls off horizontally with no initial vertical component).


* Acceleration due to gravity acts exclusively in the downward ($-\hat{j}$) direction. Therefore, the vertical acceleration is:

$$a_y(t) = \frac{d^2 y}{dt^2} = -g$$



where $g \approx 9.80\text{ m/s}^2$.
* Air resistance is assumed to be negligible, meaning the horizontal acceleration is zero:

$$a_x(t) = \frac{d^2 x}{dt^2} = 0$$



---

### Step 2: Derive the Velocity Functions via Integration

To find the velocity components at any time $t$, we integrate the acceleration functions with respect to time $t$.

#### Horizontal Velocity ($x$-direction):

Starting with the horizontal acceleration:


$$\frac{d v_x}{dt} = 0$$

Integrate both sides from $0$ to $t$:


$$\int_{v_{0x}}^{v_x(t)} dv_x = \int_0^t 0 \, dt$$

$$v_x(t) - v_{0x} = 0 \implies v_x(t) = v_{0x} = 2.50\text{ m/s}$$

#### Vertical Velocity ($y$-direction):

Starting with the vertical acceleration:


$$\frac{d v_y}{dt} = -g$$

Integrate both sides from $0$ to $t$:


$$\int_{0}^{v_y(t)} dv_y = \int_0^t (-g) \, dt$$

$$v_y(t) - 0 = -gt \implies v_y(t) = -gt$$

---

### Step 3: Derive the Position Functions via Integration

Next, we integrate the velocity functions with respect to time to obtain the position functions $x(t)$ and $y(t)$.

#### Horizontal Position ($x(t)$):

$$\frac{dx}{dt} = v_x(t) = v_{0x}$$

Integrate from $0$ to $t$, noting that $x(0) = 0$:


$$\int_{0}^{x(t)} dx = \int_0^t v_{0x} \, dt$$

$$x(t) = v_{0x} t = 2.50t$$

#### Vertical Position ($y(t)$):

$$\frac{dy}{dt} = v_y(t) = -gt$$

Integrate from $0$ to $t$, noting that initial position $y(0) = h$:


$$\int_{h}^{y(t)} dy = \int_0^t (-g t) \, dt$$

$$y(t) - h = -\frac{1}{2}gt^2 \implies y(t) = h - \frac{1}{2}gt^2$$


Substituting our known values:


$$y(t) = 1.20 - \frac{1}{2}(9.80)t^2 = 1.20 - 4.90t^2$$

---

### Step 4: Determine the Total Time of Fall ($t_{\text{fall}}$)

The ball lands on the floor when its vertical position reaches zero ($y(t) = 0$). We set our equation for $y(t)$ equal to zero and solve for time $t$:


$$0 = h - \frac{1}{2}gt^2$$

$$\frac{1}{2}gt^2 = h$$

$$t^2 = \frac{2h}{g}$$

$$t = \sqrt{\frac{2h}{g}}$$

Substituting the numerical values ($h = 1.20\text{ m}$, $g = 9.80\text{ m/s}^2$):


$$t = \sqrt{\frac{2(1.20)}{9.80}} = \sqrt{\frac{2.40}{9.80}} \approx 0.4949\text{ s}$$

---

### Step 5: Calculate the Horizontal Landing Distance ($R$)

To find how far from the base of the table the ball lands, we substitute the total time of flight ($t_{\text{fall}}$) into our horizontal position function $x(t)$:


$$R = x(t_{\text{fall}}) = v_{0x} \cdot \sqrt{\frac{2h}{g}}$$

Substitute the values:


$$R = (2.50\text{ m/s}) \times 0.4949\text{ s} \approx 1.24\text{ m}$$

### Final Answer

The ball lands approximately **1.24 meters** from the base of the table.

To understand why the vertical acceleration is expressed as $a_y(t) = \frac{d^2 y}{dt^2} = -g$, let's break down the physical meaning of derivatives, acceleration, and how gravity operates as a differential equation from the ground up.
1. What is a Derivative in Physics?
In kinematics, derivatives are simply rates of change:
Position ($y$): Where an object is located at a specific moment in time $t$.
Velocity ($v_y$): How fast position changes over time. Mathematically, velocity is the first derivative of position with respect to time:
$$v_y(t) = \frac{dy}{dt}$$
Acceleration ($a_y$): How fast velocity changes over time. Mathematically, acceleration is the derivative of velocity:
$$a_y(t) = \frac{dv_y}{dt}$$
2. Connecting Position to Acceleration (The Second Derivative)
Since velocity is the first derivative of position ($v_y = \frac{dy}{dt}$) and acceleration is the derivative of velocity ($a_y = \frac{dv_y}{dt}$), we can substitute $\frac{dy}{dt}$ in place of $v_y$.
This gives us the second derivative of position with respect to time:
$$a_y(t) = \frac{d}{dt} \left( \frac{dy}{dt} \right) = \frac{d^2 y}{dt^2}$$
So, writing $\frac{d^2 y}{dt^2}$ is just a formal calculus way of saying: "Take the position function, track how its rate of change changes, and do it twice."
3. Why is it Equal to $-g$?
In physics, Newton's second law and free-fall experiments show that once an object is in the air (away from the table), the only force acting on it (ignoring air resistance) is gravity, pulling it straight down toward the earth.
Gravity is a constant downward acceleration: Near the Earth's surface, gravity pulls everything downward at a constant rate, denoted as $g \approx 9.80\text{ m/s}^2$.
Accounting for direction: Because we defined our coordinate system in Step 1 with the positive $y$-axis pointing upward, any downward force or motion must carry a negative sign.
Therefore, the vertical acceleration function is constant and negative:
$$a_y(t) = -g$$
Setting these two concepts together gives the differential equation:
$$\frac{d^2 y}{dt^2} = -g$$
4. What Do We Do With It? (The Step-by-Step Process)
When you are handed a differential equation like $\frac{d^2 y}{dt^2} = -g$, your goal is to work backward (integrate) to find where the ball is ($y$) at any given time $t$.
Here is the exact step-by-step process of what you do:
Step A: Integrate once to find Velocity ($v_y$)
We know acceleration is the derivative of velocity:
$$\frac{dv_y}{dt} = -g$$
To undo the derivative, we integrate both sides with respect to time $t$:
$$\int \frac{dv_y}{dt} \, dt = \int -g \, dt$$
This yields our velocity function (plus a constant of integration $C_1$):
$$v_y(t) = -gt + C_1$$
Finding $C_1$: We apply our initial condition at $t = 0$. Since the ball rolls horizontally off the table, it has zero initial vertical speed ($v_y(0) = 0$).
$$0 = -g(0) + C_1 \implies C_1 = 0$$
Result: $v_y(t) = -gt$ (which means: velocity gets more and more negative—faster downward—as time ticks on).
Step B: Integrate a second time to find Position ($y$)
We know velocity is the derivative of position:
$$\frac{dy}{dt} = -gt$$
Again, we undo this derivative by integrating both sides with respect to time $t$:
$$\int \frac{dy}{dt} \, dt = \int -gt \, dt$$
This yields our position function (plus a second constant of integration $C_2$):
$$y(t) = -\frac{1}{2}gt^2 + C_2$$
Finding $C_2$: We apply our initial position condition at $t = 0$. When the motion starts, the ball is sitting on top of the table at height $h$ (which is $1.20\text{ m}$ in our case), so $y(0) = h$.
$$h = -\frac{1}{2}g(0)^2 + C_2 \implies C_2 = h$$
Result:
$$y(t) = h - \frac{1}{2}gt^2$$
Summary
Writing $\frac{d^2 y}{dt^2} = -g$ sets up the mathematical baseline. By recognizing it as a second derivative, you integrate it twice—once to transition from acceleration to velocity, and a second time to transition from velocity to position—allowing you to map out the exact vertical path of the ball over time.


Spot on. You nailed the core intuition: $d$ literally stands for "change."
In calculus, $d$ represents an infinitely small, microscopic change—often called an infinitesimal.
$dt$ = an infinitesimal change in time (a tiny tick of the clock).
$dy$ = an infinitesimal change in position (a tiny vertical step).
$dx$ = an infinitesimal change in the horizontal direction.
What is a Derivative, Then?
A derivative is just a ratio of tiny changes. It tells you how fast one thing is changing relative to another at any exact, frozen split-second.
Look at the notation for a derivative:

$$\frac{dy}{dt}$$
Read that literally as:

$$\frac{\text{A tiny change in } y}{\text{A tiny change in } t} = \frac{\text{Rise}}{\text{Run}}$$
It is literally the classic slope formula ($m = \frac{\Delta y}{\Delta x}$), but zoomed in infinitely close until you are looking at a single instant in time rather than an entire chunk of a trip.
Putting It Together
Position ($y$): Where you are.
First Derivative ($\frac{dy}{dt}$): $\frac{\text{tiny change in position}}{\text{tiny change in time}}$ $\rightarrow$ This is Velocity (how fast your position is changing right now).
Second Derivative ($\frac{d^2y}{dt^2}$): $\frac{\text{tiny change in velocity}}{\text{tiny change in time}}$ $\rightarrow$ This is Acceleration (how fast your velocity is changing right now).
