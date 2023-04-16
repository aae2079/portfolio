#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:58:28 2018

@author: Aaron Escobar

Homework 4 Problem 2 Nonlinear Regression
"""
#import modules needed to solve problem
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dname=r'/Users/aaron_escbr/class_data_01'                  # directory where the file is located
fname='sinusoidal_data.csv'                                # name of the file 
dfname ='{0:s}/{1:s}'.format(dname,fname)                  # concatenate directory and file name

sindata=np.genfromtxt(dfname,delimiter=',',skip_header=1)  # sindata is a ndarray
                                                           # skip one header -> skip_header=1
                                                           # csv             -> delimiter=','
        
t = sindata[:,0]        # set first column equal to t
V = sindata[:,1]        #     second       equal to V                    

#plot voltage with respect to time 
plt.figure(1)
plt.plot(t,V,'g.',label='voltage data points',MarkerSize='3')
plt.grid(which='major')
plt.xlabel(r'$time\,\,(s)$')
plt.ylabel(r'$Voltage\,$')
plt.xlim([0,0.025])
plt.title(r'$Voltage\, vs.\, Time\,$')
plt.legend()
plt.savefig('Hw4_2figs1.png')


#create a model for curve fit which is given 
def Voltage(t,A,a,w):
    V_fun = A*np.exp(-a*t)*np.sin(w*t)
    return V_fun
    
popt,pcov = curve_fit(Voltage,t,V,p0=(0.5,125,5E3)) #p0 is an initial guess that in this case is given

A=popt[0] #calculate a value for A, alpha, and omega
a=popt[1]
w=popt[2]

print('A={}'.format(A)) # prints a value for A, alpha, and omega onto console
print('a={}'.format(a))
print('w={:E}'.format(w))

# plot data  
plt.figure(2)
plt.plot(t,V,'g.',MarkerSize='3')
plt.grid(which='major')                 # add grid
plt.title(r'$Voltage\, vs.\, Time\,$')
plt.xlabel(r'$time\,\,(s)$')   # label in x: time
plt.ylabel(r'$Voltage\,(volts)$')    # label in y: velocity
plt.plot(t,Voltage(t,*popt),'y')
plt.xlim([0,.025])
plt.legend()                   # show legend                                  
plt.show()                     # show plot


