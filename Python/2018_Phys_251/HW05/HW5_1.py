"""
Created on Fri Mar 23 23:32:58 2018

@author: Aaron Escobar

Homework 5 Problem 1
"""
# import needed modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dname = '/Users/aaron_escbr/Downloads' #directory name 
fname = 'velocity_run018.txt'          #file name

dfname = '{0:s}/{1:s}'.format(dname,fname)

velocity_run = np.genfromtxt(dfname,skip_header=1)

t       = velocity_run[:,0] # time data
v       = velocity_run[:,1] # velocity data
v_error = velocity_run[:,2] # velocity uncertainty

# plot given data
plt.figure(1)
plt.plot(t,v,'.',label='Data Points')
plt.errorbar(t,v,v_error,label='Error Bars')
plt.grid(which='major')
plt.legend(loc = 2)
plt.title(r'$Velocity\ vs.\ Time$')
plt.xlabel(r'$Time(s)$')
plt.ylabel(r'$Velocity(m/s)$')
plt.savefig('hw5_1_fig1.png')


# Linear interpolotaion for velocity vs time
n   = t.size
ti = np.empty(n-1)
vi = np.empty(n-1)

for i in range(0,n-1):
    ti[i] = (t[i]+t[i+1])/2
    vi[i] = v[0] + (t[i]-t[0])*((v[1]-v[0])/(t[1]-t[0]))

plt.figure(2)
plt.plot(ti,vi,'.',label = 'Data Points')
plt.grid(which='major')
plt.legend()
plt.title(r'$Linear\ Interpolation\ Graph$')
plt.xlabel(r'$Time(s)$')
plt.ylabel(r'$Velocity(m/s)$')
plt.savefig('hw5_1_fig2.png')

    
#Scipy Curve Fit
def linear(x,m,b):
    y = m*x + b
    return y

popt,pcov = curve_fit(linear,t,v,sigma=v_error)

m=popt[0]
b=popt[1]

print('m is {:0}'.format(m))
print('b is {:1}'.format(b))

plt.figure(3)
plt.plot(t,v,'.',label='Data Points')
plt.plot(t,linear(t,*popt),label='curve fit')
plt.grid(which='major')
plt.title(r'$Velocity\ vs.\ Time\ - Curve\ Fit$')
plt.xlabel(r'$Time(s)$')
plt.ylabel(r'$Velocity(m/s)$')
plt.legend()
plt.savefig('hw5_1_fig3.png')
    
