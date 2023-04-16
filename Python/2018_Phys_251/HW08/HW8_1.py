"""
Created on Tue Apr 17 11:43:31 2018

@author: Aaron Escobar

Homework 8 Problem 1
"""
import numpy as np
import matplotlib.pyplot as plt

#here i created an array for symbols so that each iteration of dt would get a different symbol
symbol = ['1','.','x','^']
# create a delta t array for all the dt's being used for each problem
dt = np.array([0.01,0.05,0.1,0.5])


# a) y' = t*e^(3t)-2y ---------------------------------------------------------

ti = 0.0
tf = 1.0
y0 = 0.0

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y0                  #initial condition is placed into empty y array
    y_prime = np.empty(n)    #empty y' array 
   
    # Forward Euler for loop
    for k in range(n-1):
        y_prime[k] = t[k]*np.exp(3*t[k])-2*y[k] # given function
        y[k+1] = y[k] + dt[i]*y_prime[k]        # FE
    plt.figure(1)
    plt.plot(t,y,symbol[i],markersize=10,label = r'$\Delta t ={}$'.format(dt[i]))

#PLOTTING
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ Solution\ of\ dy/dt = te^{3t} -2y$')

# b) y' = 1 + (t-y)^2 ---------------------------------------------------------    

ti = 2.0
tf = 3.0
y2 = 1.0

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y2                  #initial condition is placed into empty y array
    y_prime = np.empty(n)    #empty y' array 
    
    # Forward Euler for loop
    for k in range(n-1):
        y_prime[k] = 1 + ((t[k]-y[k])**2) # given function
        y[k+1] = y[k] + dt[i]*y_prime[k]  # FE
    plt.figure(2)
    plt.plot(t,y,symbol[i],markersize=10,label = r'$\Delta t ={}$'.format(dt[i]))

#PLOTTING
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ Solution\ of\ dy/dt = 1 + (t-y)^2$')

# c) y' = 1 + y/t -------------------------------------------------------------

ti = 1.0
tf = 2.0
y1 = 1.0

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y1                  #initial condition is placed into empty y array
    y_prime = np.empty(n)    #empty y' array 
   
    #Forward Euler for loop
    for k in range(n-1):
        y_prime[k] = 1 + (y[k]/t[k])     # given function
        y[k+1] = y[k] + dt[i]*y_prime[k] # FE
    plt.figure(3)
    plt.plot(t,y,symbol[i],markersize=10, label = r'$\Delta t ={}$'.format(dt[i]))

#PLOTTING
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ Solution\ of\ dy/dt = 1 + \frac{y}{t}$')
 
# d) y' = cos(2t) + sin(3t) ---------------------------------------------------

ti = 0.0
tf = 2 * np.pi
y0 = 0.0

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y0                  #initial condition is placed into empty y array
    y_prime = np.empty(n)    #empty y' array 
    
    #Forward Euler for loop
    for k in range(n-1):
        y_prime[k] = np.cos(2*t[k])+np.sin(3*t[k]) # given function
        y[k+1] = y[k] + dt[i]*y_prime[k]           # FE
    plt.figure(4)
    plt.plot(t,y,symbol[i],markersize=10, label = r'$\Delta t ={}$'.format(dt[i])) 

#PLOTTING
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ Solution\ of\ dy/dt = cos(2t)+sin(3t)$')     