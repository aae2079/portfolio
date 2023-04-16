"""
Created on Tue Apr 24 12:14:03 2018

@author: Aaron Escobar

Homework 9 Problem 1
"""
import numpy as np
import matplotlib.pyplot as plt

#here i created an array for symbols so that each iteration of dt would get a different symbol
symbol = ['1','.','x','^']
# create a delta t array for all the dt's being used for each problem
dt = np.array([0.01,0.1,1.0])

#given information
g = 9.8 #m/s^2
ti = 0.0 #initial time
tf = 10.0 #final time
y0 = 1000.0 #initial y condition

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y0                  #initial condition is placed into empty y array
    dydt = np.empty(n)    #empty y' array 
   
    # Forward Euler for loop
    for k in range(n-1):
        dydt[k] = -g*t[k] # given function
        y[k+1] = y[k] + dt[i]*dydt[k]        # FE
    plt.figure(1)
    plt.plot(t,y,symbol[i],markersize=7,label = r'$\Delta t ={}$'.format(dt[i]))

#PLOTTING
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ Solution\ of\ dy/dt = -gt $')