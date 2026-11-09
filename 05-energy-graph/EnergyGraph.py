from vpython import *
#Web VPython 3.2
# Parameters
xi = -1     # initial position 
vi = 1      # initial velocity
t_end = 20  # length of simulation
m = 1       # mass
dt = 0.01   # timestep

# Potential energy function
def U_func(x):
    '''Change the potential energy function here, as directed'''
    U = x**2
    return U
 
# Force function (numerical derivative)  
def F_func(U, x):
    dx = 0.0001
    return -( U(x+dx) - U(x-dx) ) / (2*dx)

# Plot curve of U(x)
Ucurve = gcurve(color=vec(1,0.5,0))
xmin = -1.5
xmax = 1.5
x1 = xmin
dx = 0.01
while x1 < xmax+dx:
    Ucurve.plot(x1, U_func(x1))
    x1 = x1 + dx

# Initialize curves to plot K, U, and E=K+U as the particle moves
Kplot = gcurve(color=color.green, dot=True)
Uplot = gcurve(color=vec(1,0.5,0), dot=True)
Eplot = gcurve(color=color.blue, dot=True)

print("Legend:")
print("U = orange")
print("K = green")
print("E = blue")

# Set position, velocity, and time  to initial conditions 
x = xi
v = vi
t = 0

# Simulation loop
while t <= t_end:
    rate(2/dt) # Show the simulation at a moderate speed (2x real time)
    
    # Plot current potential energy
    U = U_func(x)
    Uplot.plot(x, U)
    
    '''(2a) Plot current kinetic energy'''
    K = 0.5 * m * v**2  # --- NEW: Calculate Kinetic Energy
    Kplot.plot(x, K)    # --- NEW: Plot Kinetic Energy
    
    '''(2b) Plot current total energy'''
    E = K + U           # --- NEW: Calculate Total Energy
    Eplot.plot(x, E)    # --- NEW: Plot Total Energy
    
    # Update motion to new timestep
    F = F_func(U_func, x) # current force on particle
    
    '''(1a) update velocity at constant acceleration'''
    v = v + (F / m) * dt  # --- NEW: Update velocity
    
    '''(1b) update position, assuming constant velocity'''
    x = x + v * dt        # --- NEW: Update position
    
    '''(1c) update time'''
    t = t + dt            # --- NEW: Update time
    
print("End of simulation time reached.")