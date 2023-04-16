"""
Created on Thu Apr 26 13:53:29 2018

@author: Aaron Escobar

Homework 9 Problem 3
"""
import numpy as np
import matplotlib.pyplot as plt
symbol = ['1','.','*']

m = 1.0 #kg
ks = 1.0 #N/m
w = np.sqrt(ks/m)
dt = np.array([0.01,0.1,1.0]) #dt array

x0 = 10.0 #initial conditon for x
v0 = 2.0  #initial condition for x' or v

ti = 0
tf = 4*np.pi #chose 4pi because it's 2 periods 

n = dt.size

for i in range(n):
    n = int((tf-ti)/dt[i])+1
    t = np.linspace(ti,tf,n)
    x = np.empty(n)
    x_prime=np.empty(n)
    v = np.empty(n)
    x[0] = x0
    v[0] = v0
    E = np.empty(n)
    T = np.empty(n)
    V = np.empty(n)
    
    #Forward Euler
    for k in range(n-1):
        v[k]   = (-w*x0*np.sin(w*t[k]))+(v0*np.cos(w*t[k]))
        x[k+1] = x[k]+(dt[i]*v[k])
        v[k+1] = v[k]+(dt[i]*(-ks/m)*x[k])
        T[k] = (1/2)*m*((v[k])**2)
        V[k] = (1/2)*ks*((x[k])**2)
        E[k] = T[k]+V[k]
    plt.figure(1)
    plt.plot(t,x,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    plt.figure(2)
    plt.plot(t,v,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    plt.figure(3)
    plt.plot(t,E,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    
    #Euler Cromer
    for j in range(n-1):
        v[j]   = (-w*x0*np.sin(w*t[j]))+(v0*np.cos(w*t[j]))
        x[j+1] = x[j]+(dt[i]*v[j+1])
        v[j+1] = v[j]+(dt[i]*(-ks/m)*x[j])
        T[j] = (1/2)*m*((v[j])**2)
        V[j] = (1/2)*ks*((x[j])**2)
        E[j] = T[j]+V[j]
    plt.figure(4)
    plt.plot(t,x,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    plt.figure(5)
    plt.plot(t,v,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    plt.figure(6)
    plt.plot(t,E,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    
    #Verlet
    for z in range(n-1):
        v[z]   = (-w*x0*np.sin(w*t[z]))+(v0*np.cos(w*t[z]))
        x[z+1] = (2*x[z])-(x[z-1])+((dt[i]**2)*(-ks/m)*(x[z]))
        v[z]   = (x[z+1]-x[z-1])/(2*dt[i])
        T[z] = (1/2)*m*((v[z])**2)
        V[z] = (1/2)*ks*((x[z])**2)
        E[z] = T[z]+V[z]
    plt.figure(7)
    plt.plot(t,x,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))   
    plt.figure(8)
    plt.plot(t,v,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    plt.figure(9)
    plt.plot(t,E,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    
    #Velocity Verlet
    for a in range(n-1):
        v[a]   = (-w*x0*np.sin(w*t[a]))+(v0*np.cos(w*t[a]))
        x[a+1] = (x[a])+(v[a]*dt[i])+(((dt[i]**2)/2)*(-ks/m)*x[a])
        v[a+1] = v[a]+(dt[i]*((((-ks/m)*x[a])+((-ks/m)*x[a+1]))/2))
        T[a] = (1/2)*m*((v[a])**2)
        V[a] = (1/2)*ks*((x[a])**2)
        E[a] = T[a]+V[a]     
    plt.figure(10)
    plt.plot(t,x,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    plt.figure(11)
    plt.plot(t,v,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
    plt.figure(12)
    plt.plot(t,E,symbol[i],markersize='5',label = r'$\Delta t ={}$'.format(dt[i]))
   
""" Plotting """

#Figure(1)
plt.figure(1)
plt.grid(which='major')
plt.title(r'Forward Euler: $x$ vs. $t$' )
plt.ylabel(r'$x(m)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([-12,12])

#Figure(2)
plt.figure(2)
plt.grid(which='major')
plt.title(r'Forward Euler: $\frac{dx}{dt}$ vs. $t$' )
plt.ylabel(r'$\frac{dx}{dt}(m/s)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([-12,12])

#Figure(3)
plt.figure(3)
plt.grid(which='major')
plt.title(r'$E$ vs. $t$' )
plt.ylabel(r'$E(J)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([46,57])
plt.xlim([0,4])


#Figure(4)
plt.figure(4)
plt.grid(which='major')
plt.title(r'Euler Cromer: $x$ vs. $t$')
plt.ylabel(r'$x(m)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([-12,12])

#Figure(5)
plt.figure(5)
plt.grid(which='major')
plt.title(r'Euler Cromer: $\frac{dx}{dt}$ vs. $t$' )
plt.ylabel(r'$\frac{dx}{dt}(m/s)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([-12,12])

#Figure(6)
plt.figure(6)
plt.grid(which='major')
plt.title(r'$E$ vs. $t$' )
plt.ylabel(r'$E(J)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([46,57])
plt.xlim([0,4])

#Figure(7)
plt.figure(7)
plt.grid(which='major')
plt.title(r'Verlet: $x$ vs. $t$' )
plt.ylabel(r'$x(m)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([-12,12])

#Figure(8)
plt.figure(8)
plt.grid(which='major')
plt.title(r'Verlet: $\frac{dx}{dt}$ vs. $t$' )
plt.ylabel(r'$\frac{dx}{dt}(m/s)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([-12,12])

#Figure(9)
plt.figure(9)
plt.grid(which='major')
plt.title(r'$E$ vs. $t$' )
plt.ylabel(r'$E(J)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([46,57])
plt.xlim([0,4])

#Figure(10)
plt.figure(10)
plt.grid(which='major')
plt.title(r'Velocity Verlet: $x$ vs. $t$' )
plt.ylabel(r'$x(m)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([-12,12])

#Figure(11)
plt.figure(11)
plt.grid(which='major')
plt.title(r'Velocity Verlet: $\frac{dx}{dt}$ vs. $t$' )
plt.ylabel(r'$\frac{dx}{dt}(m/s)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([-12,12])


#Figure(12)
plt.figure(12)
plt.grid(which='major')
plt.title(r'$E$ vs. $t$' )
plt.ylabel(r'$E(J)$')
plt.xlabel('$t(s)$')
plt.legend()
plt.ylim([46,57])
plt.xlim([0,4])
