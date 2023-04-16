"""
Created on Wed Feb 14 14:29:49 2018

@author: Aaron Escobar

Problem 5: Basic Plots
"""
#Import matplotlib and numpy
import matplotlib.pyplot as plt 
import numpy as np

#1. y = x^2 x = 0 to 10 incraments of 0.5
def f(x):
    return x**2

x = np.arange(0.0,10.0,0.5)

plt.figure(1)
plt.plot(x,f(x))
plt.title('$x^{2}$')
plt.xlabel ('x')
plt.ylabel ('y')
plt.grid(which='major')
plt.show()     
 
#2. y = sin(x) x = 0 to 4pi incraments of pi/4   
def g(x_2):
    return np.sin(x_2)

x_2 = np.arange(0.0,4*np.pi,(np.pi/4))


plt.figure(2)
plt.plot(x_2,g(x_2))
plt.title('$sin(x) from [0,{\pi}] incraments of {\pi}/4$')
plt.xlabel ('x')
plt.ylabel ('y')
plt.grid(which='major')
plt.show()     

#3. y = sin(x) x = 0 to 4pi incraments of pi
def h(x_3):
    return np.sin(x_3)

x_3 = np.arange(0.0,4*np.pi,np.pi)

plt.figure(3)
plt.plot(x_3,h(x_3))
plt.title('$ sin(x) from [0,{\pi}]  incraments  of  {\pi} $')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(which='major')
plt.show()

#4. r = e^a*theta theta = -8pi to 8pi a = 0.1
a = 0.1
def r(theta):
    return np.exp(a*theta)

theta = np.arange(-8*np.pi,8*np.pi)

plt.figure(4)
plt.plot(theta,r(theta))
plt.title('$e^{a\Theta}$')
plt.xlabel('r')
plt.ylabel('${\Theta}$')
plt.grid(which='major')
plt.show()

