from vpython import *
#Web VPython 3.2
scene.width = 1250
scene.height = 550

# System objects
''' Set radius (in meters) and mass (in kg) of each '''
earth = sphere(color=color.cyan, radius=6.371e6, mass=5.972e24)
moon = sphere(color=color.white, radius=1.737e6, mass=7.342e22)
ship = sphere(radius=1e6, mass=15000, color=color.yellow, make_trail=True, interval=10)

# Initial positions
''' Set earth, moon, and ship positions '''
# The Earth and moon are ~384,400,000 meters apart. Half of this is 192,200,000 meters.
earth.pos = vec(-1.922e8, 0, 0)
moon.pos = vec(1.922e8, 0, 0)
# The ship starts 10 Earth radii to the left of the Earth's center.
ship.pos = vec(earth.pos.x - 10 * earth.radius, 0, 0)

# Initial velocity of the ship
ship.vel = vec(0, 2500, 0)

# Gravitational force function
G = 6.67e-11
def force(ship, other):
    global crashed # access the crashed variable outside this function
    ''' Compute the r vector and the distance (magnitude of this vector) '''
    r_vec = other.pos - ship.pos
    distance = mag(r_vec)
    
    if distance < other.radius:
        crashed = True
    
    # Calculate the gravitational force using Newton's law of universal gravitation
    force_magnitude = (G * ship.mass * other.mass) / distance**2
    force_direction = norm(r_vec)
    force = force_magnitude * force_direction
    
    return force

# Simulation loop goes here
dt = 60
crashed = False
while not crashed:
    rate(1000)
    ''' Fill in the steps to update the ship's position by one timestep. '''
    # Calculate the net force on the ship from the Earth and the Moon
    force_on_ship_from_earth = force(ship, earth)
    force_on_ship_from_moon = force(ship, moon)
    
    ship.force = force_on_ship_from_earth + force_on_ship_from_moon
    
    # Update velocity using the force (a = F/m)
    ship.vel = ship.vel + (ship.force / ship.mass) * dt
    
    # Update position using the velocity
    ship.pos = ship.pos + ship.vel * dt