"""
Created on Thu Apr 12 13:10:25 2018

@author: aaron_escbr

Homework 7 Problem 3
"""
#import numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,200)
y = np.empty(x.size)
dfdx = np.empty(x.size)
d2dx = np.empty(x.size)
dx = x[1]-x[0]

#for loop used for function and analytical solutions for df/dx and d2/dx2
for i in range(0,x.size):
    y[i] = np.exp(-x[i]**2)
    dfdx[i] = -2*x[i]*np.exp(-x[i]**2)
    d2dx[i] = 4*(x[i]**2)*np.exp(-x[i]**2)

#preallocate arrays for approximations
dfdxF = np.empty(x.size)
dfdxB = np.empty(x.size)
dfdxC = np.empty(x.size)
d2dxC = np.empty(x.size)

#For Loop for FD,BD,CD,CD2 approximations
for i in range(1,x.size-1):
    dfdxF[i] = (y[i+1]-y[i])/dx
    dfdxB[i] = (y[i]-y[i-1])/dx
    dfdxC[i] = (y[i+1]-y[i-1])/(2*dx)
    d2dxC[i] = (y[i+1]-(2*y[i])+y[i-1])/(dx**2)

#PLOTTING    
plt.plot(x,y,'^',markersize=3,label='Given Function') #graph original function
plt.plot(x,dfdx,'.',markersize=3,label='1st Derivative Analytical') #graph deriavtive function
plt.plot(x,dfdxF,'1',markersize=3,label='Forward Difference') #graph forward approximation
plt.plot(x,dfdxB,'*',markersize=3,label='Backward Difference') # graph backward approximation
plt.plot(x,dfdxC,'+',markersize=3,label='Central Difference') # graph central approximation
plt.plot(x,d2dxC,'x',markersize=3,label='2nd Derivatve CD') #graph 2nd order central approximation
plt.plot(x,d2dx,'o',markersize=3,label ='2nd Derivative Analytical')  #grph analytical solution 2nd derivative
plt.ylim([-2.0,1.5])
plt.legend()
plt.grid(which='major')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'$Problem\ 3$')