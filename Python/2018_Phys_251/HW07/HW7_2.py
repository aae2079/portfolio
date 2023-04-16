"""
Created on Thu Apr 12 12:49:25 2018

@author: Aaron Escobar

Homework 7 Problem 2
"""

#import numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(5,30,200)
y = np.empty(x.size)
dfdx = np.empty(x.size)
dx = x[1]-x[0]

#for loop for both the function and derivative
for i in range(0,x.size):
    y[i] = np.sin(x[i])/x[i]
    dfdx[i] = ((x[i]*np.cos(x[i]))-np.sin(x[i]))/(x[i]**2)

"""-----------------------Main Script----------------------------------------"""

dfdxF = np.empty(x.size) #empty array for Forward difference
dfdxB = np.empty(x.size) #empty array for backward difference
dfdxC = np.empty(x.size) #empty array for central difference

for i in range(1,x.size-1):
    dfdxF[i] = (y[i+1]-y[i])/dx       # Forward Difference approximation
    dfdxB[i] = (y[i]-y[i-1])/dx       # Backward Difference approximation
    dfdxC[i] = (y[i+1]-y[i-1])/(2*dx) # Central Difference approximation
 
# PLOTTING

plt.plot(x,y,'.',markersize='3',label='Function')
plt.plot(x,dfdx,'g.',markersize='3',label='Analytical Solution')
plt.plot(x,dfdxF,'r.',markersize='3',label='Forward Difference')
plt.plot(x,dfdxB,'y.',markersize='3',label='Backward Difference')
plt.plot(x,dfdxC,'b.',markersize='3',label='Central Difference')
plt.ylim([-0.20,0.20])
plt.grid(which='major')
plt.title(r'$Problem\ 2$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()