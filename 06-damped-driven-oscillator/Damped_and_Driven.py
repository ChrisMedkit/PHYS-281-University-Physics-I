from vpython import *
#Web VPython 3.2
# Initial position set to 0 as requested
ball = sphere(pos=vec(0,0,0), radius=.2, mass=0.5, vel=vec(0,0,0), color=color.green, opacity=0.7, make_trail=True)
center = sphere(radius=0.1)

dt = 0.0001
t = 0
k = 20
b = .5  # Damping constant
D = 20
omega_d = 7
plot = True # (2a) When this is true, graphs are plotted
if plot:
    gpos = gcurve(color=color.black, label="Position") # Position curve is back on
    # (2b) Create new curves for velocity and acceleration
    #gvel = gcurve(color=color.green) # Creates a curve on the graph
    #gacc = gcurve(color=color.red) # Creates a curve on the graph

    # Create new curves for energy (commented out)
    #gke = gcurve(color=color.blue, label="Kinetic Energy")
    #gpe = gcurve(color=color.red, label="Potential Energy")
    #gte = gcurve(color=color.black, label="Total Energy")

''' Uncomment these lines when it's time to show the arrows. ''' 
# Initialize force vectors so arrows can attach
ball.spring_force = vec(0,0,0)
ball.damping_force = vec(0,0,0)
ball.driving_force = vec(0,0,0)
# Attach the arrows
attach_arrow(ball, "spring_force", color=vec(0.5,0.5,0.5), scale=0.1, shaftwidth=0.1)
attach_arrow(ball, "damping_force", color=vec(0.75,0.5,0), scale=0.1, shaftwidth=0.1)
attach_arrow(ball, "driving_force", color=vec(1,1,0), scale=0.1, shaftwidth=0.1)

while True:
    # Update forces individually for the arrows
    ball.spring_force = -k*ball.pos
    ball.damping_force = -b*ball.vel
    ball.driving_force = D * cos(omega_d * t) * vec(0,1,0) # Driving force added
    
    # Calculate total force
    ball.force =  ball.spring_force + ball.damping_force + ball.driving_force
    
    # Plot curves
    if plot:
        gpos.plot(t, ball.pos.y) # Plotting position
        #gvel.plot(t, ball.vel.y)
        #gacc.plot(t, ball.force.y/ball.mass)
        
        # Calculate energies (commented out)
        #ke = 0.5 * ball.mass * mag(ball.vel)**2
        #pe = 0.5 * k * mag(ball.pos)**2
        #te = ke + pe
        
        # Plot energies (commented out)
        #gke.plot(t, ke)
        #gpe.plot(t, pe)
        #gte.plot(t, te)

    # Set frame rate
    rate(1/dt)
    t += dt # updates the time
    
    # Update velocity and position
    ball.vel += ball.force/ball.mass*dt
    ball.pos += ball.vel*dt