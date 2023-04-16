"""
Created on Thu Apr  5 11:18:43 2018

@author: Aaron Escobar

Homework 7 Problem 1
"""
#import numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
x = np.linspace(0,2*pi,100)
y = np.empty(x.size)
dfdx = np.empty(x.size)
dx = x[1]-x[0] #delta x; change in x

#for loop for both the function and derivative
for i in range(0,x.size):
    y[i] = np.cos(x[i]) + np.sin(x[i])
    dfdx[i] = np.cos(x[i])-np.sin(x[i])

#preallocate arrays for FD,BD,CD
dfdxF = np.empty(x.size)
dfdxB = np.empty(x.size)   
dfdxC = np.empty(x.size)

#For loop for FD, BD, CD approximations
for i in range(1,x.size-1):
    dfdxF[i] = (y[i+1]-y[i])/dx
    dfdxB[i] = (y[i]-y[i-1])/dx
    dfdxC[i] = (y[i+1]-y[i-1])/(2*dx)

#PLOTTING
plt.plot(x,y,'1',label='Given Function',markersize=5)
plt.plot(x,dfdx,'^',label='Analytical solution',markersize=5)
plt.plot(x,dfdxF,'*',label = 'Forward difference',markersize=3)
plt.plot(x,dfdxB,'+',label = 'Backward difference',markersize=3)
plt.plot(x,dfdxC,'x',label = 'Central difference',markersize=3)
plt.grid(which='major')
plt.legend(loc=9)
plt.ylim(-1.5,1.5)
plt.title(r'$Problem\ 1$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

