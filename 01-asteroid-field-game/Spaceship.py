from vpython import *
#Web VPython 3.2
while True:
    # Sets width and height in pixels of the canvas
    scene.width = 500
    scene.height = 500
    
    # Sets the zoom so that its a distance of 40 from the middle to the edge
    scene.range = 40
    # Prevents automatic rescaling if an object goes off screen
    scene.autoscale = False
    
    # Prevents the users from changing the view in any way
    scene.userspin = False
    scene.userzoom = False
    scene.userpan = False
    
    ''' (1a) Define the ship with radius, color, initial velocity '''
    ship = sphere(radius=1.5, color=color.cyan, vel=vec(20,10,0))
    
    
    ''' (2c) Reset the ship's initial velocity to zero '''
    ship.vel= vector(0,0,0)
    ''' (4a) Create list of 20 treasures with random initial positions '''
    
    treasures = []
    for i in range(20):
        treasures.append(sphere(vel=vec(random()*20-10, random()*20-10,0),radius = 0.75, color=color.green,pos=vec(random()*80 - 40, random()*80 - 40, 0)))
        
    ''' (8a) Add random initial velocities above to treasures and asteroids '''
    
    ''' (6a) Create list of 20 asteroids with random initial positions '''
    
    asteroids = []
    for i in range(20):
        asteroids.append(sphere(vel=vec(random()*20-10, random()*20-10,0),radius = 0.75, color=color.white,pos=vec(random()*80 - 40, random()*80 - 40, 0)))
    
    dt = 1/100
    playing = True
    while playing:  # playing will be set to False when the game ends with win or loss
        # Sets the frame rate
        rate(1/dt)
    
        ''' (2a) Use keyboard input to set the acceleration '''
        key = keysdown()  # returns a list of keys currently down
        acceleration = vector(0,0,0)
        if "up" in key:
            acceleration += vec(0,50,0)
        if "down" in key:
            acceleration += vec(0,-50,0)
        if "left" in key:
            acceleration += vec(-50,0,0)
        if "right" in key:
            acceleration += vec(50,0,0)
    
        ''' (2b) Change ship velocity based on the current acceleration '''
        ship.vel += acceleration * dt
        
        ''' (9) Add panning. '''
        ''' (8b) Modify movement and PBCs to include all ship, treasures, and asteroids '''
        ''' (1b) Implement movement using the current velocity as average velocity '''
        ship.pos += ship.vel * dt
        ''' (3) Implement periodic boundary conditions'''
        ship.pos.x -= round(ship.pos.x/(2*scene.range)) * 2*scene.range
        ship.pos.y -= round(ship.pos.y/(2*scene.range)) * 2*scene.range
        ''' (4b) If the ship touches a treasure, it is collected '''
        for t in reversed(treasures):
            distance = mag(ship.pos - t.pos)
            sum_of_radii = ship.radius + t.radius
    
        if distance < sum_of_radii:
            treasures.remove(t)
            t.visible = False
    
        ''' (5a) If all treasures are collected, the player wins '''
        if len(treasures) == 0:
            playing = False
            print("winner winner winner " + "it took " + dt + " time to win")
            
        ''' (5b) Keep track of and print the time taken to win '''
        ''' (6b) If the ship touches an asteroid, the player loses '''
        for a in asteroids:
            distance = mag(ship.pos - a.pos)
            sum_of_radii = ship.radius + a.radius
        
        if distance < sum_of_radii:
            playing = False
            print("You lose")
            break
    ''' (7a) Enclose the whole code in a while True: and uncomment these 2 lines '''
    sleep(1)  # wait 1 second before allowing restart
    scene.waitfor("keyup")  # wait for a keyup to start again
    
    ''' (7b) Clear out all objects by setting .visible to False for each object '''
    for obj in [ship] + treasures + asteroids:
        obj.visible = False
