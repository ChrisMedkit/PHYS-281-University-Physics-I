from vpython import *
#Web VPython 3.2

#creating vectors
a = vec(1, 2, 0)
b = vec (-1, 1, 0)
s = 3

#vector addition and scalar multiplication
print ("a", a)
print ("s*a", s*a)
print ("b", b)
print ("a+b", a+b)

#printing the magnitude of vectors
print ("|a|=", mag(a))
print ("|a|=", sqrt(a.x**2 + a.y**2 + a.z**2))
print ("|a|=", a.mag)

#making normal vectors
print ("a^=", hat(a))
print ("a^=", a.hat)

#making arrows
#arrow(axis=a, color=color.red)
#arrow(axis=b, color=color.green)


#more advanced arrows
a_arrow = arrow(axis=a, color=color.red, pos=vec(-1,0,0))
#making an arrow for b from the end of a
b_arrow = arrow(axis=b, color=color.green, pos=a_arrow.pos)
arrow(axis=b, color = color.green, pos=a_arrow.pos+a_arrow.axis)

#making a yellow arrow for a+b, starting at the tail of a
ab_arrow = arrow (axis=a+b, color=color.yellow, pos = a_arrow.pos)

#making a blue arrow for a-b starting from the tip of b
#ba_arrow = arrow (axis=a-b, color = color.blue, pos = b_arrow.pos+b_arrow.axis)



#cylinder
cylinder (axis=a-b, color = color.blue, pos = b_arrow.pos+b_arrow.axis, radius=.05)

#box
box(size=vec(5,0.1,2))

platform = box(size=vec(5,0.1,2))
#platform.rotate(axis=vec(0,0,1), angle = radians(15), origin=a_arrow.pos)