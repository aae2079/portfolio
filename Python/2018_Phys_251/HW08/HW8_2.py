"""
Created on Thu Apr 19 22:12:30 2018

@author: Aaron Escobar

Homework 8 Problem 2
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#here i created an array for symbols so that each iteration of dt would get a different symbol
symbol = ['1','.','x','^']
# create a delta t array for all the dt's being used for each problem
dt = np.array([0.01,0.05,0.1,0.5])


# a) y' = e^(t-y) ---------------------------------------------------------

ti = 0.0 #initial time
tf = 1.0 #final time
y0 = 1.0 #initail condition


# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y0                  #initial condition is placed into empty y array
    y_prime = np.empty(n)    #empty y' array 
    
    # Forward Euler for loop
    for k in range(n-1):
        y_prime[k] = np.exp(t[k]-y[k])          # given function
        y[k+1] = y[k] + dt[i]*y_prime[k]        # FE
    plt.figure(1)
    plt.plot(t,y,symbol[i],markersize=10,label = r'$\Delta t ={}$'.format(dt[i]))


#ODEint
"""Create a new time array using 50 points, this way the line is smoother 
and we are able to see ODE with better precision."""

t1 = np.linspace(ti,tf,50) 
yprime = lambda y,t: np.exp(t-y)
ODE    = odeint(yprime,y0,t1)

#PLOTTING
plt.plot(t1,ODE,'k',label = 'ODEINT',markersize='5')
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ and\ ODEINT\ Solution\ of\ dy/dt = e^{t-y}$')

# b) y' = t^2(sin(2t)-2ty) ---------------------------------------------------------    

ti = 1.0 #initial time
tf = 2.0 #final time
y1 = 2.0 #initial condition

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y1                  #initial condition is placed into empty y array
    y_prime = np.empty(n)    #empty y' array 
    
    # Forward Euler for loop
    for k in range(n-1):
        y_prime[k] = (t[k]**2)*(np.sin(2*t[k])-(2*t[k]*y[k])) # given function
        y[k+1] = y[k] + dt[i]*y_prime[k]                    # FE
    plt.figure(2)
    plt.plot(t,y,symbol[i],markersize=10,label = r'$\Delta t ={}$'.format(dt[i]))

#ODEint
"""Create a new time array using 50 points, this way the line is smoother 
and we are able to see ODE with better precision."""
t1 = np.linspace(ti,tf,50) 
yprime = lambda y,t: (t**2)*(np.sin(2*t)-(2*t*y))
ODE    = odeint(yprime,y1,t1)

#PLOTTING
plt.plot(t1,ODE,'k',label = 'ODEINT',markersize='5')
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ and\ ODEINT\ Solution\ of\ dy/dt = t^2(sin(2t)-2ty)$')
# c) y' = -y+ty^1/2 -------------------------------------------------------------

ti = 2.0 #initial time 
tf = 3.0 #final time
y2 = 2.0 #initial conditon

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y2                  #initial condition is placed into empty y array
    y_prime = np.empty(n)    #empty y' array 
    
    #Forward Euler for loop
    for k in range(n-1):
        y_prime[k] = -y[k]+ t[k]*y[k]**(1/2) # given function
        y[k+1] = y[k] + dt[i]*y_prime[k]     # FE
    plt.figure(3)
    plt.plot(t,y,symbol[i],markersize=10, label = r'$\Delta t ={}$'.format(dt[i]))

#ODEint
"""Create a new time array using 50 points, this way the line is smoother 
and we are able to see ODE with better precision."""
t1 = np.linspace(ti,tf,50) 
yprime = lambda y,t: -y + t*y**(1/2)
ODE    = odeint(yprime,y2,t1)

#PLOTTING
plt.plot(t1,ODE,'k',label = 'ODEINT',markersize='5')
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ and\ ODEINT\ Solution\ of\ dy/dt = -y+ty^{1/2}$')
 
# d) y' = cos(2t) + sin(3t) ---------------------------------------------------

ti = 2.0 #initial time
tf = 4.0 #final time
y2 = 4.0 #initial condition

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    y[0]=y2                  #initial condition is placed into empty y array
    y_prime = np.empty(n)    #empty y' array 
    
    #Forward Euler for loop
    for k in range(n-1):
        y_prime[k] = (t[k]*y[k]+y[k])/(t[k]*y[k]+t[k]) # given function
        y[k+1] = y[k] + dt[i]*y_prime[k]               # FE
    plt.figure(4)
    plt.plot(t,y,symbol[i],markersize=10, label = r'$\Delta t ={}$'.format(dt[i])) 

#ODEint
"""Create a new time array using 50 points, this way the line is smoother 
and we are able to see ODE with better precision."""
t1 = np.linspace(ti,tf,50) 
yprime = lambda y,t: (t*y+y)/(t*y+t)
ODE    = odeint(yprime,y2,t1)

#PLOTTING
plt.plot(t1,ODE,'k',label = 'ODEINT',markersize='5')
plt.legend()
plt.grid(which='major')
plt.title(r'$Forward\ Euler\ and\ ODEINT\ Solution\ of\ dy/dt = \frac{ty+y}{ty+t}$')
