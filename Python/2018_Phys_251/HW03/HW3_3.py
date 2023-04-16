"""
Created on Tue Feb 20 17:44:52 2018

@author: Aaron Escobar

Homework 3 Problem 3
"""
#Import matplotlib and numpy modules
import matplotlib.pyplot as plt
import numpy as np

# given information
g    = 9.8              # (m/s^2) acceleration due to gravity
v0_x = 40*np.cos(45)    # (m/s) initial x-velocity component
v0_y = 40*np.sin(45)    # (m/s) initial y-velocity component

# create time array with 100 values between 0 and 7
t    = np.linspace(0,7,100)
n    = t.size           # size the array 

#1. plot x vs t and y vs t ----------------------------------------------------

#calculate x-component using a for loop

x    = np.empty(n)      # create/preallocate an 'empty' y array for the for loop
for i in range(n):        
    x[i] = v0_x * t[i]

#calculate y-component using a for loop    

y    = np.empty(n)      # create/preallocate an 'empty' y array for the for loop
for i in range(n):         
    y[i] = v0_y*t[i] - 1./2. *g*t[i]**2
    
#plotting
plt.figure(1)
plt.plot(t,x,label = 'x vs. t')
plt.plot(t,y,label='y vs. t')
plt.grid(which = 'major')
plt.xlabel('Time(sec)')
plt.ylabel('Position(m)')
plt.title('Distance vs. Time')
plt.legend()


#2. Plot Vx vs. t and Vy vs. t ------------------------------------------------
       
#calculate velocity x-component using a for loop

v_x  = np.empty(n)      # create/prealocate an 'empty' x-velocity array for the for loop
for j in range (n):
    v_x[j] = v0_x

#calculate velocity y-component using a for loop

v_y  = np.empty(n)      # create/prealocate an 'empty' y-velocity array for the for loop        
for j in range(n):
    v_y[j] = v0_y - g*t[j]

#plotting    
plt.figure(2)
plt.plot(t,v_x, label ='v_x vs. t')
plt.plot(t,v_y, label = 'v_y vs. t')
plt.grid(which = 'major')
plt.xlabel('Time(sec)')
plt.ylabel('Velocity(m/s)')
plt.title('Velocity vs. Time')
plt.legend()

#3. Plot trajectory of ball ---------------------------------------------------

#plotting
plt.figure(3)
plt.plot(x,y, label = 'trajectory; x vs. y')
plt.grid(which='major')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.title('Trajectory of Ball')
plt.legend(loc=3)

