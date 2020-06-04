import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

#Velocity in the X direction
xv = 4.5

#Velocity in the Y direction
yv = 90

#Velocity in the Z direction
zv = 12

#Acceleration in the X direction
xa = 4

#Acceleration in the Y direction
ya = 1.22

#Acceleration in the Z direction
za = 3

#Magnitude of Velocity (Speed)
magv = math.sqrt((xv**2)+(yv**2)+(zv**2))

#Magnitude of Acceleration
maga = math.sqrt((xa**2)+(ya**2)+(za**2))

#Time to elapse for particle
t = 0

#scalar multi
s = 0

#displacement ()
disx = 0

#distance (Distance from one point to another)

#Cartesian Plane (Numerical values in the x,y,z direction)
#Grid = ["X" : 0, "Y": 0, "Z": 0]

#Grid_X_Max = int(input("What is your maximum in the X direction?"))
#Grid_X_Min = int(input("What is your minimum in the X direction?"))
#Grid_Y_Max = int(input("What is your maximum in the Y direction?"))
#Grid_Y_Min = int(input("What is your minimum in the Y direction?"))
#Grid_Z_Max = int(input("What is your maximum in the Z direction?"))
#Grid_Z_Min = int(input("What is your maximum in the Z direction?"))

#Grid_X = [Grid_X_Max,Grid_X_Min]
#Grid_Y = [Grid_Y_Max,Grid_Y_Min]
#Grid_Z = [Grid_Z_Max,Grid_Z_Min]


#distance (using velocity and time)
disx2 = magv*t

#Position
xpos = float(input("What is your initial position in the x axis?"))
ypos = float(input("What is your initial position in the y axis?"))
zpos = float(input("What is your initial position in the z axis?"))

#Acceleration (using velocity and time)

#Var for function switch
start = False

#Input variable
try:
    xv = float(input("What is your velocity in the X direction?"))
except ValueError:
    print("You need to input a number value!")
    xv = float(input("What is your velocity in the X direction?"))

try:
    yv = float(input("What is your velocity in the Y direction?"))
except ValueError:
    print("You need to input a number value!")
    yv = float(input("What is your velocity in the Y direction?"))

try:
    zv = float(input("What is your velocity in the Z direction?"))
except ValueError:
    print("You need to input a number value!")
    zv = float(input("What is your velocity in the Z direction?"))

try:
    xa = float(input("What is your acceleration in the X direction?"))
except ValueError:
    print("You need to input a number value!")
    xa = float(input("What is your acceleration in the X direction?"))

try:
    ya = float(input("What is your acceleration in the Y direction?"))
except ValueError:
    print("You need to input a number value!")
    ya = float(input("What is your acceleration in the Y direction?"))

try:
    za = float(input("What is your acceleration in the Z direction?"))
except ValueError:
    print("You need to input a number value!")
    za = float(input("What is your acceleration in the Z direction?"))

try:
    s = float(input("Does this kinematic have a scalar multiplier?"))
except ValueError:
    print("You need to input a number value!")
    s = float(input("Does this kinematic have a scalar multiplier?"))

try:
    t = float(input("How many minutes does the object moves?"))
except ValueError:
    print("You need to input a number value!")
    t = float(input("How many seconds does the object moves?"))

print("The speed of the object is " + str(magv * s) + "m/s")
print("The acceleration of the object is " + str(maga * s) + "m/s")

#Active Function
while (start == True):
    pass

#Data for a three-dimensional line
pos = 0
speed = (magv * s)
acceleration = (maga * s)
ax.plot3D(0 + pos, 0 + speed, 0 + acceleration, 'blue')