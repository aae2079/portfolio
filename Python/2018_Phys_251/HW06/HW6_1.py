"""
Created on Thu Mar 29 11:03:43 2018

@author: Aaron Escobar

Homework 6 Problem 1
"""
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
# Set the function equal to f
f = lambda x: x**2

# Define the Midpoint Rectangle using def and for loop
def mymidpoint(f,a,b,n):
    dx = (b-a)/float(n)
    xmid = (a+a+dx)/2.0
    
    A=0
    for i in range(n):
        ymid  = f(xmid)
        A    += ymid
        xmid += dx
    A = dx*A
    return A
#------------------------------------------------------------------------------

# Main Script
    
nmax = 100 # max value for n is 100 which for loop will run through
a=0 # lower bound
b=1 # upper boud 
n = np.linspace(1,nmax,nmax,dtype=int) # create an n array

Aexact = 1.0/3.0       # Analytical solution of Integral
delta = np.empty(nmax) # create a delta array
A = np.empty(nmax)     # create an empty area A for Area

for i in range(nmax):
    A[i]     = mymidpoint(f,a,b,n[i])
    Aapprox  = mymidpoint(f,a,b,n[i])
    delta[i] = abs((Aapprox-Aexact)/Aexact)

print(A)
    
plt.plot(n,delta,'.')
plt.grid(which = 'major')
plt.xlabel(r'$ n $')
plt.ylabel(r'$ \delta _n $')
plt.title(r'$ \delta _n\ vs.\ n$')
