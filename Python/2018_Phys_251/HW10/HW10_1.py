"""
Created on Tue May  1 17:18:05 2018

@author: Aaron Escobar

Homework 10 Problem 1: Harmonic Motion
"""

import numpy as np
from numpy import sin,cos
import matplotlib.pyplot as plt


#here i created an array for symbols so that each iteration of dt would get a different symbol
symbol = ['1','.','x','^']
color  = ['cyan','limegreen']
color2 = ['b','pink']

# create a delta t array for all the dt's being used for each problem
dt = np.array([0.5,1.0])


ks = 1             #spring constant
m  = 100.0         #mass
ti = 0.0           #initial time
tf = 100.0         #final time
x0 = 0.0           #initial conditions
v0 = 1.0           #initial conditions
w = np.sqrt(ks/m)  #solve omega

"""--------------------------- Analytical solution -------------------------"""
A = 0 # calculated A
B = 1/np.sqrt(1/50) # calculated B

def analytical(A,B,t):
    x = A*cos(w*t) +    B*sin(w*t)
    v = -A*w*sin(w*t) + B*w*cos(w*t)
    return x,v

ta = np.linspace(ti,tf,100)
xa,va = analytical(A,B,ta)

#plotting Analytical solutions

plt.figure(1)
plt.plot(ta,xa,'r')
plt.figure(2)
plt.plot(ta,va,'r')


"""------------------------------ Main Script ------------------------------"""
# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1    #number of elements in array per each delta t
    t = np.linspace(ti,tf,n)    #time array
    x_FE = np.empty(n)          #empty y array
    v_FE = np.empty(n)
    x_VV = np.empty(n)          #empty y array
    v_VV = np.empty(n)
    
    x_FE[0] = x0                # Set initial conditions
    v_FE[0] = v0                # Set initial conditions
    x_VV[0] = x0                # Set initial conditions
    v_VV[0] = v0                # Set initial conditions
   
    # Forward Euler for loop
    for k in range(n-1):
        x_FE[k+1] = x_FE[k] + dt[i] * v_FE[k]
        v_FE[k+1] = v_FE[k] + dt[i] * ((-2*ks)/m) * x_FE[k]
         
    plt.figure(1)
    plt.plot(t,x_FE,symbol[i],color=color[i],markersize=5,label = r'$Forward\ Euler\ \Delta t ={}$'.format(dt[i]))
    plt.figure(2)
    plt.plot(t,v_FE,symbol[i],color=color[i],markersize=3,label = r'$Forward\ Euler\ \Delta t ={}$'.format(dt[i]))
    
    # Velocity Verlet for loop
    for j in range(n-1):
        x_VV[j+1] = x_VV[j] + v_VV[j]*dt[i] + ((dt[i]**2)/2) * (-2*ks/m) *x_VV[j]
        v_VV[j+1] = v_VV[j] + (dt[i] * ((-2*ks/m)*x_VV[j])-((2*ks/m)*x_VV[j+1]))/2
    
    plt.figure(1)
    plt.plot(t,x_VV,symbol[i],color=color2[i],markersize=5,label = r'$Velocity\ Verlet \Delta t ={}$'.format(dt[i]))
    plt.figure(2)
    plt.plot(t,v_VV,symbol[i],color=color2[i],markersize=5,label = r'$Velocity\ Verlet \Delta t ={}$'.format(dt[i]))
    
""" PLOTTING """

#Plot Figure 1
plt.figure(1)
plt.grid(which='major')
plt.title(r'Harmonic Motion: $x$ vs. $t$')
plt.legend()

#Plot Figure 2
plt.figure(2)
plt.grid(which='major')
plt.title(r'Harmonic Motion: $v$ vs. $t$')
plt.legend()