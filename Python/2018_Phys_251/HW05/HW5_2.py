"""
Created on Tue Mar 27 11:12:44 2018

@author: Aaron Escobar

Homework 1 Problem 2
"""
#import modules needed
import numpy as np
import matplotlib.pyplot as plt

dname = '/Users/aaron_escbr/Downloads'
fname = 'fc_thist_00520.txt'

dfname = '{0:s}/{1:s}'.format(dname,fname)

fc_thist_00520 = np.genfromtxt(dfname,skip_header=2)

t = fc_thist_00520[:,0] #time data
s1 = fc_thist_00520[:,7] #s1 data


#Plotting Data
plt.figure(1)
plt.plot(t,s1,'.')
plt.grid(which='major')
plt.xlabel(r'$Time(s)$')
plt.ylabel(r'$Concetration\ of\ H_2 S(ppm)$')
plt.title(r'$Concetration\ vs.\ Time$')
plt.savefig('hw5_2_fig1.png')


#calculating linear interpolation from 1 to 400 with step of 1
t1   = np.arange(1,401,1) # new time array
s1_1 = np.empty(400)      # new s1 array

#main for loop
for i in range(0,400):
    s1_1[i]=s1[0] + (t[i]-t[0])*((s1[1]-s1[0])/t[1]-t[0])

#plotting new set of data
plt.figure(2)
plt.plot(t1,s1_1,'.',label='linear interpolation')
plt.grid(which='major')
plt.legend()
plt.title(r'$Velocity\ vs.\ Time$')
plt.xlabel(r'$Time(s)$')
plt.ylabel(r'$Concetration\ of\ H_2 S(ppm)$')
plt.title(r'$Concetration\ vs.\ Time\ Linear\ Interp\ 1$')
plt.savefig('hw5_2_fig2.png')

#calculation linear interpolation from 1 t0 401 in steps of 10
t2 = np.arange(1,401,10) # new time array
s1_2 = np.empty(40)      # new s1 array
 
#main for loop for interp               
for i in range(0,40):
    s1_2[i]=s1[0] + (t[i]-t[0])*((s1[1]-s1[0])/t[1]-t[0])

#plotting of new data   
plt.figure(3)
plt.plot(t2,s1_2,'.',label='linear interpolation')
plt.grid(which='major')
plt.legend()
plt.title(r'$Velocity\ vs.\ Time$')
plt.xlabel(r'$Time(s)$')
plt.ylabel(r'$Concetration\ of\ H_2 S(ppm)$')
plt.title(r'$Concetration\ vs.\ Time\ Linear\ Interp\ 2$')
plt.savefig('hw5_2_fig3.png')
