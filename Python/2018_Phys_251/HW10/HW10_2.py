"""
Created on Tue May  1 17:18:05 2018

@author: Aaron Escobar

Homework 10 Problem 2: Non - Linearized Pendulum
"""

import numpy as np
from numpy import sin
import matplotlib.pyplot as plt


#here i created an array for symbols so that each iteration of dt would get a different symbol
symbol = ['1','.','x','^']
# create a delta t array for all the dt's being used for each problem
dt = np.array([0.01,0.1,0.5])
color = ['cyan','limegreen','b']
color2 = ['m','pink','orange']


g  = 9.8
L  = 9.8
ti = 0.0 #initial time
tf = 10.0 #final time
theta0 = np.pi/18 #initial y condition
omega0 = 0.0    #initial y' condition


"""----------------------------- Main Script -------------------------------"""

# for loop for dt's
for i in range(dt.size):
    n = int((tf-ti)/dt[i])+1     #number of elements in array per each delta t
    t = np.linspace(ti,tf,n)     #time array
    omega       = np.empty(n)    #empty FE omega array
    theta       = np.empty(n)    #empty FE theta array
    omega_VV    = np.empty(n)    #empty VV omega array 
    theta_VV    = np.empty(n)    #empty VV theta array
    omega[0]    = omega0         #initial conidtions
    theta[0]    = theta0         #initial conditions
    omega_VV[0] = omega0         #initial conditions
    theta_VV[0] = theta0         #initial conditions
    
   
    # Forward Euler for loop
    for k in range(n-1):
        theta[k+1] = theta[k] + (dt[i] * omega[k])
        omega[k+1] = omega[k] - (dt[i] * (-g/L)*sin(theta[k]))
    
    plt.figure(1)
    plt.plot(t,theta,symbol[i],color=color[i],markersize=5,label = r'FE - $\Theta$ vs. $t$ for $\Delta$ t ={}'.format(dt[i]))
    plt.figure(2)
    plt.plot(t,omega,symbol[i],color=color[i],markersize=5,label = r'FE - $\omega$ vs. $t$ for $\Delta$ t ={}'.format(dt[i]))
    
    # Velocity Verlet for loop
    for j in range(n-1):     
        theta_VV[j+1] = theta_VV[j] + omega_VV[j]*dt[i] + (((dt[i]**2)/2) * (-g/L)*sin(theta_VV[j]))
        omega_VV[j+1] = omega_VV[j] + (dt[i]/2)*(((-g/L) * sin(theta_VV[j])) - ((g/L) * sin(theta_VV[j+1])))
    
    plt.figure(1)
    plt.plot(t,theta_VV,symbol[i],color=color2[i],markersize=5,label = r'VV - $\Theta$ vs. $t$ for $\Delta$ t ={}'.format(dt[i]))
    plt.figure(2)
    plt.plot(t,omega_VV,symbol[i],color=color2[i],markersize=5,label = r'VV - $\omega$ vs. $t$ for $\Delta$ t ={}'.format(dt[i]))

"""---------------------------------PLOTTING--------------------------------""" 

#Plot figure 1 
plt.figure(1)
plt.grid(which='major')
plt.legend()
plt.title(r'Forward Euler and Velocity Verlet: $\Theta$ vs. $t$')

#Plot figure 2
plt.figure(2)
plt.grid(which='major')
plt.legend(loc=2)
plt.title(r'Forward Euler and Velocity Verlet: $\omega$ vs. $t$')
