from vpython import *
#Web VPython 3.2
a = vec(1,0,0) 
b = vec(0,1,0)
c = vec(0,0,1)

d = vec(0.5,0,0)
e = vec(0,0.5,0)
f = vec(0,0,0.5)



acyl = cylinder (axis=a, color = color.yellow, radius=.05)
bcyl = cylinder (axis=b, color = color.green, radius=.05)
ccyl = cylinder (axis=c, color = color.blue, radius=.05)

acyl2 = cylinder (axis=b, color = color.red, radius=.05, pos=acyl.pos+acyl.axis)
acyl3 = cylinder (axis=c, color = color.purple, radius=.05, pos=acyl.pos+acyl.axis)

bcyl2 = cylinder (axis=c, color = color.orange, radius=.05, pos=bcyl.pos+bcyl.axis)
bcyl3 = cylinder (axis=a, color = color.cyan, radius=.05, pos=bcyl.pos+bcyl.axis)

ccyl2 = cylinder (axis=b, color = color.magenta, radius=.05, pos=ccyl.pos+ccyl.axis)
ccyl3 = cylinder (axis=a, color = color.yellow, radius=.05, pos=ccyl.pos+ccyl.axis)

cylinder (axis=c, color = color.magenta, radius=.05, pos=acyl2.pos+acyl2.axis)
cylinder (axis=a, color = color.green, radius=.05, pos=bcyl2.pos+bcyl2.axis)
cylinder (axis=b, color = color.blue, radius=.05, pos=ccyl3.pos+ccyl3.axis)

half1 = cylinder (axis = d, color = color.yellow, radius = .1)
half2 = cylinder (axis = e, color = color.yellow, radius = .1)
half3 = cylinder (axis = f, color = color.yellow, radius = .1)

cylinder (axis = b, color = color.yellow, radius = .05, pos = half1.pos+half1.axis)
cylinder (axis = b, color = color.yellow, radius = .05, pos = half3.pos+half3.axis)

half4
half5
half6