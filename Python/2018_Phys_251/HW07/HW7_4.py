"""
Created on Thu Apr 12 21:37:00 2018

@author: Aaron Escobar

Homework 7 Problem 4
"""
#import numpy and pyplot

import numpy as np
import matplotlib.pyplot as plt


"""Here I used lambda function for both the orignial 
function and derivative because it is easier in this case over a for loop because 
there is no give x range to iterate only dx"""

f    = lambda x: np.exp(-x**2) #function
dfdx = lambda x: -2*x*np.exp(-x**2) #analytical solution

#given range for delta x
dx   = np.logspace(-4,-1,12) 
x    = 1 #value that approximations and derivative aare being evaulted at

"""Here I used 'def' for approximations and delta function because it is easier 
in this case as well, no given x range to iterate in so a for loop would be 
dificult"""

#Foward Difference Approximation
def Forward(f,x,dx):
    dfdxF = (f(x+dx)-f(x))/dx
    return dfdxF
#Backward Difference Approximation
def Backward(f,x,dx):
    dfdxB = (f(x)-f(x-dx))/dx
    return dfdxB
#Central Difference Approximation
def Central(f,x,dx):
    dfdxC = (f(x+dx)-f(x-dx))/(2*dx)
    return dfdxC
#Delta Fucntion: Function(5) in notes
def Delta(approx,analytical):
    delta = abs(approx - analytical)
    return delta

"""------------------------------MAIN SCRIPT-------------------------------"""

#preallocate arrays for delta FD,BD,CD
deltaF = np.empty(dx.size)
deltaB = np.empty(dx.size)
deltaC = np.empty(dx.size)

"""for loop used here to iterate the Delta function for every difference 
approximation, evaluated at x =1"""

for i in range(dx.size):
    deltaF[i] = Delta(Forward(f,x,dx[i]),dfdx(1))
    deltaB[i] = Delta(Backward(f,x,dx[i]),dfdx(1))
    deltaC[i] = Delta(Central(f,x,dx[i]),dfdx(1))
    
#PLOTTING   
plt.loglog(dx,deltaF,'bo',label='FD error')
plt.loglog(dx,deltaB,'y*',label='BD error')
plt.loglog(dx,deltaC,'g^',label='CD error')
plt.grid(which='major')
plt.xlabel(r'$\Delta x$')
plt.ylabel(r'$\delta$')
plt.legend()
plt.title(r'$\delta \ vs.\Delta x$')