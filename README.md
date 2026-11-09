# Physics 1: Computational Physics with VPython

Coursework for Physics 1. The course has two parts:

- **Simulation assignments**: Web VPython (GlowScript) programs that simulate physical systems, from vectors through oscillations, energy, rotation, gravity and projectile motion, ending in a final simulation project.
- **Labs**: hands-on lab write-ups on projectile motion, circular motion, springs, torque and Young's modulus.

Each simulation folder holds the program and the assignment handout (`.docx`) it was written for. Folder numbers follow the numbers on the assignment handouts.

## Repository Structure

### Simulation assignments

| Folder | Topic | Physics concepts |
|---|---|---|
| [`00a-vectors-intro`](./00a-vectors-intro) | Vector basics | Vector addition, scalar multiplication, magnitude, unit vectors |
| [`00b-vectors-cube`](./00b-vectors-cube) | Building a wireframe in 3D | Position and axis vectors, tip-to-tail placement |
| [`01-asteroid-field-game`](./01-asteroid-field-game) | Asteroid Field Game | Kinematics, acceleration from key input, periodic boundaries |
| [`03-moon-shot`](./03-moon-shot) | Moon Shot Simulation | Newtonian gravity, numerical integration, orbits |
| [`04-harmonic-oscillator`](./04-harmonic-oscillator) | Harmonic Oscillator Simulation | Hooke's law, Euler-Cromer method, period |
| [`05-energy-graph`](./05-energy-graph) | Energy Graph Activity | Potential, kinetic and total energy, force from a potential |
| [`06-damped-driven-oscillator`](./06-damped-driven-oscillator) | Damped and Driven Harmonic Oscillator | Damping, driving force, resonance |
| [`07-seesaw`](./07-seesaw) | Seesaw Simulation | Torque, moment of inertia, parallel axis theorem |
| [`10-final-simulation-project`](./10-final-simulation-project) | **Final project:** Penalty Kickz game | Forces, drag, wind, collisions |

### Labs

| Folder | Topic |
|---|---|
| [`labs/projectile-motion`](./labs/projectile-motion) | Projectile Motion lab and written report |
| [`labs/circular-motion`](./labs/circular-motion) | Circular Motion Lab |
| [`labs/spring-oscillation`](./labs/spring-oscillation) | Spring Oscillation Lab |
| [`labs/torque-exploration`](./labs/torque-exploration) | Torque Exploration Lab |
| [`labs/youngs-modulus`](./labs/youngs-modulus) | Young's Modulus Lab |

## Simulation Assignments

### 00a - Vectors Intro (`Test.py`)
**Purpose:** Practice the VPython vector toolkit.
**Description:** Creates 3D vectors and prints their sum, scalar multiple, magnitude (three equivalent ways) and unit vector. It then draws arrows to show tip-to-tail vector addition, with a yellow arrow for `a + b`, plus a cylinder and a box. Some lines are commented out, such as the `a - b` arrow and the platform rotation.

### 00b - Vectors Cube (`Assignment1.py`)
**Purpose:** Place objects in 3D space using position and axis vectors.
**Description:** Chains colored cylinders end to end, each starting at the tip of another, to trace the 12 edges of a unit cube along the x, y and z axes. Thicker yellow half-length cylinders are then added from the origin.
**Status:** Unfinished. The last three lines (`half4`, `half5`, `half6`) are bare names with no definition, so they raise an error at runtime.

### 01 - Asteroid Field Game (`Spaceship.py`, `1_Asteroid_Field_Game.docx`)
**Purpose:** Combine kinematics, lists and collision checks into a small game. The handout is a 20-point, step-by-step assignment.
**Description:** The player flies a ship with the arrow keys. Key presses change acceleration, and acceleration changes velocity and position. Periodic boundary conditions wrap the ship around the screen edges. The goal is to collect 20 green treasures while avoiding 20 white asteroids, and the program can restart after a win or loss.
**Status:** Work in progress. The collision checks sit outside their `for` loops, so only the last treasure and asteroid are tested. The win message adds a number to a string, which raises a `TypeError`. Treasures and asteroids are given velocities but are never moved, and the panning step (9) is not implemented.

### 03 - Moon Shot Simulation (`Moonshot.py`, `3_Moon_Shot_Simulation.docx`)
**Purpose:** Simulate a spacecraft under the gravity of two bodies and explore the orbits it produces.
**Description:** Places the Earth and Moon at realistic masses, radii and separation, fixed in space, and launches a ship from 10 Earth radii to the left of the Earth with a sideways velocity. Each step sums Newton's gravitational force from both bodies, then updates velocity and position with a 60-second time step. The loop ends when the ship comes within the radius of either body. The handout then has you vary the launch speed to study the original orbit, larger orbits where the Moon matters, a figure-8 orbit that needs 5 to 6 significant figures of speed, and a new orbit of your own.

### 04 - Harmonic Oscillator Simulation (`Oscillation.py`, `4_Harmonic_Oscillator_Simulation.docx`)
**Purpose:** Simulate simple harmonic motion, graph it, and measure its period.
**Description:** A ball on a spring (`F = -ky`, `k = 20` in the handout) is stepped forward with the Euler-Cromer method. Position, velocity and acceleration are graphed together. The code also tries to measure the period by timing successive downward crossings of the origin, using linear interpolation for the exact crossing time. The handout compares the measured period with the calculated one and asks about accuracy and precision.
**Status:** The crossing detection never fires because `old_y` is saved after the position update, so the test `y < 0 and old_y >= 0` can never be true. Move `old_y = ball.pos.y` to before the update to fix it. The final "Simulation finished" line is also unreachable.

### 05 - Energy Graph Activity (`EnergyGraph.py`, `5_Energy_Graph_Activity.docx`)
**Purpose:** Understand how energy graphs relate to motion.
**Description:** Plots a potential energy curve `U(x)` (default `x²`, easy to swap for another function), then moves a particle through it. Force is computed as `-dU/dx` with a numerical central difference. Kinetic, potential and total energy are graphed against position as the particle moves, and the total should stay nearly flat. The lines marked (1a) to (2b) are the steps filled in for the assignment.

### 06 - Damped and Driven Harmonic Oscillator (`Damped_and_Driven.py`, `6_Damped_and_Driven_Harmonic_Oscillator_Simulation.docx`)
**Purpose:** Explore the energy of an oscillator with damping and an external driving force, and find resonance.
**Description:** The ball feels a spring force `-kx`, a damping force `-bv`, and a sinusoidal driving force `D cos(ω_d t)`. Each force is shown as a colored arrow attached to the ball, and position is plotted against time. Plots for velocity, acceleration and the three energies are included but commented out. Parameters are `k = 20`, `b = 0.5`, `D = 20`, `ω_d = 7`. The handout has you sweep the drive frequency from 1 to 12 at several damping values and graph amplitude against frequency; the undriven oscillator's natural frequency is about 6.32, which is where resonance appears.

### 07 - Seesaw Simulation (`SeesawSim.py`, `7_Seesaw_Simulation.docx`)
**Purpose:** Model rotational dynamics of a pivoted beam with weights.
**Description:** Sets up a beam, an axle at the pivot, and two spherical weights. The comment blocks outline the remaining steps: compute the beam's moment of inertia and shift it to the pivot with the parallel axis theorem, assign weight masses from density, sum the torques, update angular velocity, and rotate each object about the pivot. The handout then has you find the balance point of a weight and of the pivot, both from the simulation and by calculation.
**Status:** Starter template. The physics steps are still empty, so nothing moves yet, and the handout's answer sections are blank.

### 10 - Final Simulation Project: Penalty Kickz (`FreeKick.py`, `10_Final_Simulation_Project.docx`)
**Purpose:** Build a game, demo or simulation that uses forces, torques or momentum-conserving collisions correctly. The handout is graded on physics (100), finesse (30), "new" techniques (10), a class presentation (20) and a written report (40).
**Description:** A two-player penalty shootout. Holding space charges the power while the aiming arrow sweeps side to side. In flight, the ball is acted on by gravity, linear air drag and an adjustable wind force, and it bounces with energy loss. A goalie moves side to side at an adjustable speed, and hitting it triggers a one-dimensional elastic collision. A scoreboard tracks goals, and the first player to 5 goals with a 2-goal lead wins. Sliders control wind and goalie speed, and `R` resets the camera.
**Where it meets the rubric:** Forces (gravity, drag, wind) and a collision that follows momentum conservation cover the physics. A `Goalie` class, sliders and keyboard input cover the "new" programming features.

## Labs

### Projectile Motion (`labs/projectile-motion`)
**Purpose:** Practice projectile motion problem-solving with a spring launcher.
**Description:** Part I finds the launch speed from a horizontal shot by measuring the fall height and horizontal range. Part II uses that speed to predict the landing position for a launch at an angle. Part III is a target shot at a bullseye. `Projectile_Motion.docx` is the lab handout, and `Physics_Projectile_Motion_Report.docx` is the written report.

### Circular Motion Lab (`labs/circular-motion`)
**Purpose:** Examine uniform circular motion through the force needed to keep an object on a circular path.
**Description:** A rubber stopper on a string is swung in a circle to hold up a hanging mass. Mass, string length and period are measured for different radii, and the equations are combined to solve for `g` without assuming its value.

### Spring Oscillation Lab (`labs/spring-oscillation`)
**Purpose:** Understand and measure the oscillation of masses hanging from springs.
**Description:** Three experiments: measuring the period as a function of mass and spring stiffness with a photogate, finding an unknown mass using a known spring, and fitting position versus time from a motion detector.

### Torque Exploration Lab (`labs/torque-exploration`)
**Purpose:** Explore torque and balance through five stations.
**Description:** Stations cover balancing objects and center of mass, a seesaw, a torque board with spring scales, balance tricks, and measuring your own center of mass. Each has its own data or conclusions.

### Young's Modulus Lab (`labs/youngs-modulus`)
**Purpose:** Learn how to measure Young's modulus of a material.
**Description:** Measures nylon fishing line by plotting stretched length against force with a linear fit, and steel wire using a laser setup. Results are compared with accepted values.

## Running the Simulations

The programs are written for [Web VPython](https://www.glowscript.org/), which runs in the browser with no install.

1. Go to glowscript.org, sign in, and create a new program.
2. Paste in the contents of a file.
3. Make sure the first line reads `Web VPython 3.2` (or `GlowScript 3.2 VPython`). The files here have `from vpython import *` on line 1 for editor support, so delete that line when you paste into Web VPython.
4. Click **Run this program**.

Some features, such as `attach_arrow`, are specific to Web VPython and may not work with desktop VPython.

## Tools

- Python (Web VPython / GlowScript 3.2)
- Numerical integration (Euler and Euler-Cromer updates) for all simulations
- Microsoft Word and Excel for write-ups and graphs
