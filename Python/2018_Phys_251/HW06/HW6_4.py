"""
Created on Tue Apr  3 15:02:56 2018

@author: Aaron Escobar

Homework 6 Problem 4
"""
from scipy.integrate import quad

f = lambda x: ((x**3)/81)+1

def simpson(f,a,b,n):
   dx=(b-a)/n
   A = f(a) + f(b)
   for i in range(1, n, 2):
       A += 4 * f(a + i * dx)
   for i in range(2, n-1, 2):
       A += 2 * f(a + i * dx)
   A = A*dx/3
   return A 

def trapazoidal(f,a,b,n):
    dx = (b-a)/float(n)
    A = 0
    A += (f(a) + f(b))/2.0
    for i in range(1,n,1):
        A += f(a + i*dx)
    A = dx*A
    return A

a = 0
b = 4
n = 2

Atrap = trapazoidal(f,a,b,n)

Asim  = simpson(f,a,b,n)

Aexact,err = quad(f,a,b)

deltaA = abs((Atrap-Asim)/Asim)

print('A_Trapezoid = {}'.format(Atrap))
print('A_Simpson   = {}'.format(Asim))
print('A_Exact     = {}'.format(Aexact))
print('Relative difference between A_Simpson and A_Trapezoid = {}'.format(deltaA))