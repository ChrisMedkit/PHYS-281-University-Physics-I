from vpython import *
#GlowScript 2.9 VPython
ball = sphere(pos=vec(0,2,0), radius=.2, mass=0.5, vel=vec(0,0,0), color=color.green, opacity=0.7, make_trail=True)
# The amplitude is the  ^ initial y position of the ball
center = sphere(radius=0.1)

dt = 0.01
t = 0
k=40

plot = True # (2a) When this is true, graphs are plotted
if plot: 
    gpos = gcurve(color=color.blue) # Creates a curve on the graph
    gvel = gcurve(color=color.green)
    gacc = gcurve(color=color.red)
    # (2b) Create new curves for velocity and acceleration

prev_time = None
crossed = False
while True:
    rate(1/dt)
    
    # (1a) Update force
    F_y = -k * ball.pos.y
    ball.force = vec(0, F_y, 0)
    
    a = ball.force / ball.mass

    # Graphing the current data
    if plot:
        gpos.plot(t, ball.pos.y) # Adds a position data point to the graph
        gvel.plot(t, ball.vel.y)
        gacc.plot(t, a.y)
        # (2b) Add data points to the curves for velocity and acceleration
    
    # (1b) Update velocity and position
    ball.vel = ball.vel + a * dt
    ball.pos = ball.pos + ball.vel * dt
    
    
    t += dt # update the time
    
    
    old_y = ball.pos.y
    
    # (3) Check if crosses the origin going downwards.
    if ball.pos.y < 0 and old_y >= 0:
        
        fraction = ball.pos.y / (ball.pos.y - old_y)
        t_crossing = t - dt * fraction
        
    # If so, save the time of crossing as time.
        print(f"\nDownward crossing detected at t = {t_crossing:7.4f}")
        
        if prev_time is not None:
            # a. Print the time of crossing
            # a. Print the time elapsed (the Period T)
            period = t_crossing - prev_time
            print(f"Time: {t_crossing:7.4f} s | Period (T): {period:7.4f} s")
        else:
        # This is the first crossing (T/4)
            print(f"Time of first crossing (T/4): {t_crossing:7.4f} s")
            
        # Save the current crossing time for the next calculation
            prev_time = t_crossing
        
print("\nSimulation finished.")

        
        
        