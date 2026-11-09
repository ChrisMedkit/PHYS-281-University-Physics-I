from vpython import *
#GlowScript 2.9 VPython

''' Glowscript documentation:
    https://www.glowscript.org/docs/VPythonDocs/index.html '''

# beam of seesaw
beam = box(pos=vec(0,0,0), size=vec(1, 0.03, 0.005), color=vec(1,0.75,0.5), mass=0.200, omega=0)
''' Compute the moment of inertia of the beam pivoted about the center of mass.  
https://en.wikipedia.org/wiki/List_of_moments_of_inertia '''


# pivot point and axle
pivot = vec(0,0.015,0)
length = 0.1
axle = cylinder(pos=pivot-vec(0,0,length/2), axis=vec(0,0,length), radius=0.005, color=vec(1,0,0))
''' Apply the parallel axis theorem to modify the moment of inertia to be about this pivot point. '''


# weights
density = 3000
weight1 = sphere(pos=vec(0.4, 0, 0), radius=0.02)
weight2 = sphere(pos=vec(-0.2, 0, 0), radius=0.025)
''' Assign a mass to each weight based on volume and density. '''

''' The weights will be rigidly bonded to the beam, we we can treat 
the beam plus weights as one rigid object with one moment of inertia.
Compute the additional moment of inertia from each weight. ''' 


''' The total moment of inertia of the system should be stored in one variable. '''


t = 0
dt = 0.01
gravity = vec(0, -9.8, 0)

angle_graph = gcurve(color=color.red)

while True:
    # Limits frame rate.
    rate(1/dt)
    
    ''' Plot the angle as a function of time, using beam.axis.  
    (Look up axis in the documentation for a box object.) '''
        
    
    ''' Set torque to zero. '''
    torque = vec(0,0,0)
    
    ''' Add the torque from gravity acting on the beam and on the weights. '''
    
    ''' Update beam.omega (angular velocity). The beam.omega is the z component
    only, so use torque.z in your update formula, not the full vector torque.'''
    
    # This adds viscous friction to the axle so the motion settles to equilibrium.  
    beam.omega *= 1 - 0.02
    
    ''' Use the rotate function to rotate each object around the z axis 
    by the proper amount about the pivot point. (Look it up.) 
    https://www.glowscript.org/docs/VPythonDocs/rotation.html '''
    
    # Updates time.
    t += dt
    