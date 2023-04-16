#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 00:38:54 2018

@author: Aaron Escobar

Homework 4 Problem 3 Free Fall - bouncing ball

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dname=r'/Users/aaron_escbr/class_data_01' # directory where file is located
fname = 'free_fall_run18_csv.csv'         # file name with extension
dfname ='{0:s}/{1:s}'.format(dname,fname)                  # concatenate directory and file name

ff_data=np.genfromtxt(dfname,delimiter=',',skip_header=1) #ff_data is an ndarray

t = ff_data[:,0] # set first column equal to time
p = ff_data[:,1] # set second column equal to position

#plot the data
plt.figure(1)
plt.plot(t,p,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Position\ vs.\ Time$')
plt.legend()



#parabola 1-------------------------------------------------------------------
P1 = ff_data[47:79]
t1= P1[:,0]
p1=P1[:,1]

#plot the respective data set
plt.figure(2)
plt.plot(t1,p1,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Parabola\ 1, Position\ vs.\ Time$')
plt.legend()

#create a model for curve fit
def parabola(x,a,b,c):
    y = a*(x**2)+b*x + c
    return y

popt,pcov = curve_fit(parabola,t1,p1)

a=popt[0] #calculate a value for a,b, and c
b=popt[1]
c=popt[2]

#plot curve fit
plt.plot(t1,parabola(t1,*popt),label='curve fit')
plt.legend()

g1 = 2*a #calcute accleration due to gravity
print('g1={}'.format(g1))


#parabola 2-------------------------------------------------------------------

P2=ff_data[79:104]
t2=P2[:,0]
p2=P2[:,1]

#plot the respective data set
plt.figure(3)
plt.plot(t2,p2,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Parabola\ 2, Position\ vs.\ Time$')
plt.legend()

#create a model for curve fit
def parabola(x,a,b,c):
    y = a*(x**2)+b*x + c
    return y
popt,pcov = curve_fit(parabola,t2,p2)

a=popt[0] #calculate a value for a,b, and c
b=popt[1]
c=popt[2]

#plot curve fit
plt.plot(t2,parabola(t2,*popt),label='curve fit')
plt.legend()

g2 = 2*a #calcute accleration due to gravity
print('g2={}'.format(g2))

#parabola 3-------------------------------------------------------------------

P3=ff_data[105:127]
t3=P3[:,0]
p3=P3[:,1]

#plot the respective data set
plt.figure(4)
plt.plot(t3,p3,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Parabola\ 3, Position\ vs.\ Time$')
plt.legend()

#create a model for curve fit
def parabola(x,a,b,c):
    y = a*(x**2)+b*x + c
    return y
popt,pcov = curve_fit(parabola,t3,p3)

a=popt[0] #calculate a value for a,b, and c
b=popt[1]
c=popt[2]

#plot curve fit
plt.plot(t3,parabola(t3,*popt),label='curve fit')
plt.legend()

g3 = 2*a #calcute accleration due to gravity
print('g3={}'.format(g3))

#parabola 4-------------------------------------------------------------------

P4=ff_data[127:146]
t4=P4[:,0]
p4=P4[:,1]

#plot the respective data set
plt.figure(5)
plt.plot(t4,p4,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Parabola\ 4, Position\ vs.\ Time$')
plt.legend()

#create a model for curve fit
def parabola(x,a,b,c):
    y = a*(x**2)+b*x + c
    return y
popt,pcov = curve_fit(parabola,t4,p4)

a=popt[0] #calculate a value for a,b, and c
b=popt[1]
c=popt[2]

#plot curve fit
plt.plot(t4,parabola(t4,*popt),label='curve fit')
plt.legend()

g4 = 2*a #calcute accleration due to gravity
print('g4={}'.format(g4))

#parabola 5-------------------------------------------------------------------

P5=ff_data[147:162]
t5=P5[:,0]
p5=P5[:,1]

#plot the respective data set
plt.figure(6)
plt.plot(t5,p5,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Parabola\ 5, Position\ vs.\ Time$')
plt.legend()

#create a model for curve fit
def parabola(x,a,b,c):
    y = a*(x**2)+b*x + c
    return y
popt,pcov = curve_fit(parabola,t5,p5)

a=popt[0] #calculate a value for a,b, and c
b=popt[1]
c=popt[2]

#plot curve fit
plt.plot(t5,parabola(t5,*popt),label='curve fit')
plt.legend()

g5 = 2*a #calcute accleration due to gravity
print('g5={}'.format(g5))

#parabola 6-------------------------------------------------------------------

P6=ff_data[162:177]
t6=P6[:,0]
p6=P6[:,1]

#plot the respective data set
plt.figure(7)
plt.plot(t6,p6,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Parabola\ 6, Position\ vs.\ Time$')
plt.legend()

#create a model for curve fit
def parabola(x,a,b,c):
    y = a*(x**2)+b*x + c
    return y
popt,pcov = curve_fit(parabola,t6,p6)

a=popt[0] #calculate a value for a,b, and c
b=popt[1]
c=popt[2]

#plot curve fit
plt.plot(t6,parabola(t6,*popt),label='curve fit')
plt.legend()

g6 = 2*a #calcute accleration due to gravity
print('g6={}'.format(g6))

#parabola 7-------------------------------------------------------------------

P7=ff_data[177:189]
t7=P7[:,0]
p7=P7[:,1]

#plot the respective data set
plt.figure(8)
plt.plot(t7,p7,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Parabola\ 7, Position\ vs.\ Time$')
plt.legend()

#create a model for curve fit
def parabola(x,a,b,c):
    y = a*(x**2)+b*x + c
    return y
popt,pcov = curve_fit(parabola,t7,p7)

a=popt[0] #calculate a value for a,b, and c
b=popt[1]
c=popt[2]

#plot curve fit
plt.plot(t7,parabola(t7,*popt),label='curve fit')
plt.legend()

g7 = 2*a #calcute accleration due to gravity
print('g7={}'.format(g7))

#parabola 8-------------------------------------------------------------------

P8=ff_data[189:200]
t8=P8[:,0]
p8=P8[:,1]

plt.figure(9)
plt.plot(t8,p8,'.',label='position data')
plt.grid(which='major')
plt.xlabel(r'$time(s)$')
plt.ylabel(r'$position(m)$')
plt.title(r'$Parabola\ 8, Position\ vs.\ Time$')

#create a model for curve fit set
def parabola(x,a,b,c):
    y = a*(x**2)+b*x + c
    return y
popt,pcov = curve_fit(parabola,t8,p8)

a=popt[0] #calculate a value for a,b, and c
b=popt[1]
c=popt[2]

#plot curve fit
plt.plot(t8,parabola(t8,*popt),label='curve fit')
plt.legend()

g8 = 2*a #calcute accleration due to gravity
print('g8={}'.format(g8))

#Part2. Find aveage g and standard deviation of g -----------------------------

#Create a gravity array
g = np.array([g1,g2,g3,g4,g5,g6,g7,g8])

n=g.size #sizing the array so we can get a number of elements

S = 0
S1= 0

#create an array for the sum of all gravity constants
for i in range(0,n):
    S += g[i]
   
g_bar = S/n #this gives us the average of the gravitational acceleration
print('g_bar={}'.format(g_bar)) #print gravity

for i in range(0,n):
    S1 += (g[i]-g_bar)**2
    
sigma_g=np.sqrt(S1/(n-1)) # calculate the standard deviation using formula given

print('sigma_g={}'.format(sigma_g))