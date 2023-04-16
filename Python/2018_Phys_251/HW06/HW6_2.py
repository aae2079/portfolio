"""
Created on Thu Mar 29 12:46:20 2018

@author: Aaron Escobar

Homework 6 Problem 2
"""
from scipy.integrate import quad
import numpy as np


def trapazoidal(f,a,b,n):
    dx = (b-a)/float(n)
    A = 0
    A += (f(a) + f(b))/2.0
    for i in range(1,n,1):
        A += f(a + i*dx)
    A = dx*A
    return A


"-------------------------------Main Script -----------------------------------"

# 1) x^4 ---------------------------------------------------------------------

f1 = lambda x: x**4 

a = 0
b = 4
n = np.array([1,10,100,1000]) #create an n array holding 1,10,100 and 1000
Atrap = np.empty(n.size)      #empty array for Area

#for loop for calculating Area for n = 1,10,10 and 1000
for i in range(n.size):
    Atrap[i] = trapazoidal(f1,a,b,n[i])

print('Trapezoidal Method of Integration for #1 using n=1,10,100,1000')
print('A_trap = {}'.format(Atrap))

#Calculate exact value of integral
Aint,err=quad(f1,a,b)

print('Integral of x^4 = {}'.format(Aint))
print('')

# 2) 2/(x-4) ---------------------------------------------------------------------
f2 = lambda x: 2/(x-4)

a = 0
b = 3 
n = np.array([1,10,100,1000]) #create an n array holding 1,10,100 and 1000
Atrap2 = np.empty(n.size)     #empty array for Area

#for loop for calculating Area for n = 1,10,10 and 1000
for i in range(n.size):
    Atrap2[i] = trapazoidal(f2,a,b,n[i])

print('Trapezoidal Method of Integration for #2 using n=1,10,100,1000')
print('A_trap = {}'.format(Atrap2))

#Calculate exact value of integral
Aint,err = quad(f2,a,b)

print('Integral of 2/(x-4) = {}'.format(Aint))
print('')

# 3) x^2*lnx ---------------------------------------------------------------------
f3 = lambda x: x**2 * np.log(x)

a = 1
b = 4 
n = np.array([1,10,100,1000]) #create an n array holding 1,10,100 and 1000
Atrap3 = np.empty(n.size)     #empty array for Area

#for loop for calculating Area for n = 1,10,10 and 1000
for i in range(n.size):
    Atrap3[i] = trapazoidal(f3,a,b,n[i])
print('Trapezoidal Method of Integration for #3 using n=1,10,100,1000')
print('A_trap = {}'.format(Atrap3))

#Calculate exact value of integral
Aint,err = quad(f3,a,b)

print('Integral of x^2*lnx = {}'.format(Aint))
print('')

# 4) e^2x*sin2x ---------------------------------------------------------------------

f4 = lambda x: np.exp(2*x) * np.sin(2*x)

a = 0   
b = 2*np.pi 
n = np.array([1,10,100,1000]) #create an n array holding 1,10,100 and 1000
Atrap4 = np.empty(n.size)     #empty array for Area

#for loop for calculating Area for n = 1,10,10 and 1000
for i in range(n.size):
    Atrap4[i] = trapazoidal(f4,a,b,n[i])

print('Trapezoidal Method of Integration for #4aa using n=1,10,100,1000')
print('A_trap = {}'.format(Atrap4))

#Calculate exact value of integral
Aint,err = quad(f4,a,b)

print('Integral of e^2x * sin(2x) = {}'.format(Aint))
print('')