"""
Created on Thu Apr 26 20:08:26 2018

@author: Aaron Escobar

Homework 9 Problem 4
"""

import numpy as np
import matplotlib.pyplot as plt

#here i created an array for symbols so that each iteration of dt would get a different symbol
symbol = ['1','.','x']
# create a delta t array for all the dt's being used for each problem
dt = np.array([0.01,0.1,1.0])


# a) dy/dt = -gt ---------------------------------------------------------

Theta = np.pi/4
g = 9.8 #m/s^2
v0 = 10 #m/s
y0 = 0  #m
tf = (2*(v0)*np.sin(Theta))/g #time of flight projectile motion
ti = 0

#analytical solution
t1 = np.linspace(ti,tf,30)
v0_y = v0*np.cos(Theta)
y = np.empty(t1.size)
v_y = np.empty(t1.size)

for i in range(t1.size):
    y[i] = v0_y*t1[i] - 1./2. *g*t1[i]**2
    v_y[i] = v0_y - g*t1[i]

plt.figure(1)    
plt.plot(t1,y,'.',label='y vs. t')

plt.figure(2)
plt.plot(t1,v_y,'.',label='v_y vs. t')


# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1 #number of elements in array per each delta t
    t = np.linspace(ti,tf,n) #time array
    y = np.empty(n)          #empty y array
    v = np.empty(n)
    y[0]=y0                  #initial condition is placed into empty y array
    v[0] = v0
    dydt = np.empty(n)      #empty y' array 
   
    # Forward Euler for loop
    for k in range(n-1):
        dydt[k] = v0 - g*t[k]
        y[k+1] = y[k] + dt[i]*dydt[k] # FE
        v[k+1] = dydt[k]+(dt[i]*(-g))
    plt.figure(3)
    plt.plot(t,y,symbol[i],markersize=7,label = r'$\Delta t ={}$'.format(dt[i]))
   
    plt.figure(4)
    plt.plot(t,v,symbol[i],markersize=7,label = r'$\Delta t ={}$'.format(dt[i]))
   
    #Velocity Verlet for loop
    for j in range(n-1):
        dydt[j] = v0 - g*t[j]
        y[j+1] = y[j]+(dydt[j]*dt[i])+((dt[i]**2)/2)*-g
        v[j+1] = dydt[j]+(dt[i]*((2*-g)/2))
    plt.figure(5)
    plt.plot(t,y,symbol[i],markersize=7,label = r'$\Delta t ={}$'.format(dt[i]))    
    plt.figure(6)
    plt.plot(t,v,symbol[i],markersize=7,label = r'$\Delta t ={}$'.format(dt[i]))
    
""" Plotting """

#Figure(1)
plt.figure(1)
plt.grid(which='major')
plt.title(r'Analytical Solution: $y$ vs. $t$' )
plt.ylabel(r'$y(m)$')
plt.xlabel('$t(s)$')
plt.legend()


#Figure(2)
plt.figure(2)
plt.grid(which='major')
plt.title(r'Analytical Solution: $v_y$ vs. $t$' )
plt.ylabel(r'$v_y$(m/s)')
plt.xlabel('$t(s)$')
plt.legend()


#Figure(3)
plt.figure(3)
plt.grid(which='major')
plt.title(r'Euler: $y$ vs. $t$' )
plt.ylabel(r'$y(m)$')
plt.xlabel('$t(s)$')
plt.legend()



#Figure(4)
plt.figure(4)
plt.grid(which='major')
plt.title(r'Euler: $v_y$ vs. $t$' )
plt.ylabel(r'$v_y(m/s)$')
plt.xlabel('$t(s)$')
plt.legend()


#Figure(5)
plt.figure(5)
plt.grid(which='major')
plt.title(r'Velocity Verlet: $y$ vs. $t$' )
plt.ylabel(r'$y(m)$')
plt.xlabel('$t(s)$')
plt.legend()

#Figure(6)
plt.figure(6)
plt.grid(which='major')
plt.title(r'Velocity Verlet: $v_y$ vs. $t$' )
plt.ylabel(r'$v_y(m/s)$')
plt.xlabel('$t(s)$')
plt.legend()