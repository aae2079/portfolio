"""
Created on Tue Apr 24 12:21:43 2018

@author: Aaron Escobar

Homework 9 Problem 2
"""

import numpy as np
import matplotlib.pyplot as plt

#here i created an array for symbols so that each iteration of dt would get a different symbol
symbol = ['1','.','x','^']
# create a delta t array for all the dt's being used for each problem
dt = np.array([0.01,0.1,1.0])

#Given information

g = 9.8 #m/s^2
ti = 0.0 #initial time
tf = 10.0 #final time
y0 = 1000.0 #initial y condition
v0 = 0.0    #initial y' condition

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    v = np.empty(n)
    y[0]=y0                  #initial condition is placed into empty y array
    v[0]=v0
    dydt = np.empty(n)       #empty y' array
    dvdt = np.empty(n)
   
    # Forward Euler for loop
    for k in range(n-1):
        dydt[k] = -g*t[k]                   # given function
        dvdt[k] = -g
        y[k+1] = y[k] + dt[i]*dydt[k]        # FE
        v[k+1] = v[k] + dt[i]*dvdt[k]
    plt.figure(1)
    plt.plot(t,y,symbol[i],markersize=3,label = r'$y(t) \Delta t ={}$'.format(dt[i]))
    plt.plot(t,v,symbol[i],markersize=3,label = r'$v(t) \Delta t ={}$'.format(dt[i]))
    
    #Euler Cromer for loop
    for j in range(n-1):
        dydt[j] = -g*t[j]                   # given function
        dvdt[j] = -g
        y[j+1] = y[j] + dt[i]*dydt[j+1]
        v[j+1] = v[j] + dt[i]*dvdt[j]
    plt.figure(2)
    plt.plot(t,y,symbol[i],markersize=3,label = r'$y(t) \Delta t ={}$'.format(dt[i]))
    plt.legend()
    plt.plot(t,v,symbol[i],markersize=3,label = r'$v(t) \Delta t ={}$'.format(dt[i]))
    plt.legend()

plt.figure(1)
plt.legend()
plt.grid(which='major')
plt.title(r'Forward Euler: $x$ and $v$ vs. t')
plt.ylim([-150,1040])

plt.figure(2)
plt.legend()
plt.grid(which='major')
plt.title(r'Euler Cromer: $x$ and $v$ vs. t')
plt.ylim([-150,1040])