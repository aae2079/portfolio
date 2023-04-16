#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:28:33 2020

@author: Aaron Escobar
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import fsolve

#import data from local excel file
df = pd.read_excel('/Users/aaron_escbr/Desktop/data_experiment.xlsx',)

#365 NM
#convert the data from string to float
x = df['Voltage - 365'].astype(float)
y = df['Photocurrent - 365'].astype(float)
yerr = df['Error of I - 365'].astype(float)

#removes NaN from data set
x = x[~np.isnan(x)] 
y = y[~np.isnan(y)] 
err = yerr[~np.isnan(yerr)] 

#Plot the data with its errorbars
plt.errorbar(x,y,yerr=err,color='m',markersize=0.3,fmt='.',linewidth=1)
#plt.plot(x,y,'.',markersize =3, color = 'm') #without error bars
# plt.yscale('log')
plt.xlabel('Voltage [V]')
plt.ylabel('Photocurrent I [pA]')
plt.title('Plot of photcurrent induced by wavelength of 365 nm')
plt.grid()
plt.xlim(-1.7,0)
#---------- curve_fit process-------------------------


def func(x, a, b, c, d ,e ,g):
    return a + b*x + c*x**2 + d*x**3 + e*x**4 +g*x**5 #function a+bx+cx^2+dx^3+ex^4+gx^5

popt, pcov = curve_fit(func,x,y)
print(popt) #print out parameter matrix

#x array for curve fit plotting
x_fit = np.arange(-1.6,0,0.001)

#plot the curve fit
plt.plot(x_fit,func(x_fit,*popt), 'k--', label= 'line of best fit')

#set paramters a,b,c,d,e,g equal to the popt matrix 
a = popt[0]
b = popt[1] 
c = popt[2] 
d = popt[3] 
e = popt[4] 
g = popt[5]



#------------ graphing 1st and 2nd derivative of curve fit---------------
#find the maximum curvatuve using of 3rd derivative = 0
def func(x):
    return 60*g*x**2 + 24*e*x+6*d
x = fsolve(func,0) 
y_prime = b+ 2*c*x+ 3*d*x**2 + 4*e*x**3 + 5*g*x**4 #1st derivative
y_2prime = 2*c + 6*d*x + 12*e*x**2 + 20*g*x**3
dx = -y_prime/y_2prime
Vstop1 = x + dx #stopping voltage 
y = a + b*Vstop1 + c*Vstop1**2 + d*Vstop1**3 + e*Vstop1**4 +g*Vstop1**5
plt.plot(Vstop1,y,'ro',label = 'Vstop')
plt.legend()
Vstop1_err = 0.25

print(Vstop1)
plt.figure(1)
plt.show()
plt.legend()


#405 NM-----------------------------------------------------------------
#convert the data from string to float
x = df['Voltage - 405'].astype(float)
y = df['Photocurrent - 405'].astype(float)
yerr = df['Error of I - 405'].astype(float)

#removes NaN from data set
x = x[~np.isnan(x)] 
y = y[~np.isnan(y)] 
err = yerr[~np.isnan(yerr)] 

#Plot the data with its errorbars
plt.errorbar(x,y,yerr=err,color='royalblue',markersize='0.01',fmt='.',linewidth=1)
#plt.plot(x,y,'.',markersize =3,color='royalblue') #without error bars
#plt.yscale('log')
plt.xlabel('Voltage [V]')
plt.ylabel('Photocurrent I [pA]')
plt.title('Plot of photcurrent induced by wavelength of 405 nm')
plt.grid()
plt.xlim(-1,0.25)

#---------- curve_fit process-------------------------
def func(x, a, b, c, d ,e ,g):
    return a + b*x + c*x**2 + d*x**3 + e*x**4 +g*x**5 #function a+bx+cx^2+dx^3+ex^4+gx^5

popt, pcov = curve_fit(func,x,y)
print(popt) #print out parameter matrix

#x array for curve fit plotting
x_fit = np.arange(-1.6,0,0.001)

#plot the curve fit
plt.plot(x_fit,func(x_fit,*popt), 'k--', label= 'line of best fit')

#set paramters a,b,c,d,e,g equal to the popt matrix 
a = popt[0]
b = popt[1] 
c = popt[2] 
d = popt[3] 
e = popt[4] 
g = popt[5]

#------------ graphing 1st and 2nd derivative of curve fit---------------
#find the maximum curvatuve using of 3rd derivative = 0
def func(x):
    return 60*g*x**2 + 24*e*x+6*d
x = fsolve(func,0) 
y_prime = b+ 2*c*x+ 3*d*x**2 + 4*e*x**3 + 5*g*x**4 #1st derivative
y_2prime = 2*c + 6*d*x + 12*e*x**2 + 20*g*x**3
dx = -y_prime/y_2prime
Vstop2 = x + dx #stopping voltage 
y = a + b*Vstop2 + c*Vstop2**2 + d*Vstop2**3 + e*Vstop2**4 +g*Vstop2**5
plt.plot(Vstop2,y,'ro', label = 'Vstop')
plt.legend()
Vstop2_err = 0.15

print(Vstop2)

plt.figure(2)
plt.show()
plt.legend()


#-------------------436 NM START OF A NEW DATA SET ---------------------------
#convert the data from string to float
x = df['Voltage - 436'].astype(float)
y = df['Photocurrent - 436'].astype(float)
yerr = df['Error of I - 436'].astype(float)

#removes NaN from data set
x = x[~np.isnan(x)] 
y = y[~np.isnan(y)] 
err = yerr[~np.isnan(yerr)] 


#Plot the data with its errorbars
plt.errorbar(x,y,yerr=err,color='limegreen',markersize='0.01',fmt='.',linewidth=1)
#plt.plot(x,y,'.',markersize ='3', color = 'limegreen') #without error bars
#plt.yscale('log')
plt.xlabel('Voltage [V]')    
plt.ylabel('Photocurrent I [pA]')
plt.title('Plot of photcurrent induced by wavelength of 436 nm')
plt.grid()
plt.xlim(-1,0.25)

#---------- curve_fit process-------------------------
x_dat = x[200:1630]
y_dat = y[200:1630]

def func(x, a, b, c, d ,e ,g):
    return a + b*x + c*x**2 + d*x**3 + e*x**4 +g*x**5 #function a+bx+cx^2+dx^3+ex^4+gx^5

popt, pcov = curve_fit(func,x_dat,y_dat)
print(popt) #print out parameter matrix

#x array for curve fit plotting
x_fit = np.arange(-1.6,0.2,0.001)

#plot the curve fit
plt.plot(x_fit,func(x_fit,*popt), 'k--', label= 'line of best fit')

#set paramters a,b,c,d,e,g equal to the popt matrix 
a = popt[0]
b = popt[1] 
c = popt[2] 
d = popt[3] 
e = popt[4] 
g = popt[5]


#------------ graphing 1st and 2nd derivative of curve fit---------------
#find the maximum curvatuve using of 3rd derivative = 0
def func(x):
    return 60*g*x**2 + 24*e*x+6*d
x = fsolve(func,0) 
y_prime = b+ 2*c*x+ 3*d*x**2 + 4*e*x**3 + 5*g*x**4 #1st derivative
y_2prime = 2*c + 6*d*x + 12*e*x**2 + 20*g*x**3
dx = -y_prime/y_2prime
Vstop3 = x + dx #stopping voltage 
y = a + b*Vstop3 + c*Vstop3**2 + d*Vstop3**3 + e*Vstop3**4 +g*Vstop3**5
plt.plot(Vstop3,y,'ro',label = 'Vstop')
plt.legend()
Vstop3_err = 0.2

print(Vstop3)

plt.figure(3)
plt.show()
plt.legend()



#-------------------546 NM START OF A NEW DATA SET ---------------------------
#convert the data from string to float
x = df['Voltage - 546'].astype(float)
y = df['Photocurrent - 546'].astype(float)
yerr = df['Error of I - 546'].astype(float)

#removes NaN from data set
x = x[~np.isnan(x)] 
y = y[~np.isnan(y)] 
err = yerr[~np.isnan(yerr)] 

#Plot the data with its errorbars
plt.errorbar(x,y,yerr=err,color='orange',markersize=2,fmt='.',linewidth=3)
#plt.plot(x,y,'.',markersize =3, color = 'orange') #without error bars
#plt.yscale('log')
plt.xlabel('Voltage [V]')
plt.ylabel('Photocurrent I [pA]')
plt.title('Plot of photcurrent induced by wavelength of 546 nm')
plt.grid()
plt.xlim(-0.5,0.5)

#---------- curve_fit process-------------------------
x_dat = x[700:1400]
y_dat = y[700:1400]

def func(x, a, b, c, d ,e ,g):
    return a + b*x + c*x**2 + d*x**3 + e*x**4 +g*x**5 #function a+bx+cx^2+dx^3+ex^4+gx^5

popt, pcov = curve_fit(func,x_dat,y_dat)
print(popt) #print out parameter matrix

#x array for curve fit plotting
x_fit = np.arange(-1.6,0.4,0.001)

#plot the curve fit
plt.plot(x_fit,func(x_fit,*popt), 'k--', label= 'line of best fit')

#set paramters a,b,c,d,e,g equal to the popt matrix 
a = popt[0]
b = popt[1] 
c = popt[2] 
d = popt[3] 
e = popt[4] 
g = popt[5]


#------------ graphing 1st and 2nd derivative of curve fit---------------
#find the maximum curvatuve using of 3rd derivative = 0
def func(x):
    return 60*g*x**2 + 24*e*x+6*d
x = fsolve(func,0) 
y_prime = b+ 2*c*x+ 3*d*x**2 + 4*e*x**3 + 5*g*x**4 #1st derivative
y_2prime = 2*c + 6*d*x + 12*e*x**2 + 20*g*x**3
dx = -y_prime/y_2prime
Vstop4 = x + dx #stopping voltage 
y = a + b*Vstop4 + c*Vstop4**2 + d*Vstop4**3 + e*Vstop4**4 +g*Vstop4**5
plt.plot(Vstop4,y,'ro',label = 'Vstop')
plt.legend()
Vstop4_err = 0.1

print(Vstop4)

plt.figure(4)
plt.show()

#-------------------567 NM START OF A NEW DATA SET ---------------------------
#convert the data from string to float
x = df['Voltage - 567'].astype(float)
y = df['Photocurrent - 567'].astype(float)
yerr = df['Error of I - 567'].astype(float)

#removes NaN from data set
x = x[~np.isnan(x)] 
y = y[~np.isnan(y)] 
err = yerr[~np.isnan(yerr)] 


#Plot the data with its errorbars
plt.errorbar(x,y,yerr=err,color='red',markersize='1',fmt='.',linewidth=1)
#plt.plot(x,y,'.',markersize =3, color = 'red') #without error bars
#plt.yscale('log')
plt.xlabel('Voltage [V]')
plt.ylabel('Photocurrent I [pA]')
plt.title('Plot of photcurrent induced by wavelength of 567 nm')
plt.grid()
plt.xlim(-0.6,0.4)

#---------- curve_fit process-------------------------
x_dat = x[410:1393]
y_dat = y[410:1393]

def func(x, a, b, c, d ,e ,g):
    return a + b*x + c*x**2 + d*x**3 + e*x**4 +g*x**5 #function a+bx+cx^2+dx^3+ex^4+gx^5

popt, pcov = curve_fit(func,x_dat,y_dat)
print(popt) #print out parameter matrix

#x array for curve fit plotting
x_fit = np.arange(-1.6,0.4,0.001)

#plot the curve fit
plt.plot(x_fit,func(x_fit,*popt), 'k--', label= 'line of best fit')

#set paramters a,b,c,d,e,g equal to the popt matrix 
a = popt[0]
b = popt[1] 
c = popt[2] 
d = popt[3] 
e = popt[4] 
g = popt[5]


#------------ graphing 1st and 2nd derivative of curve fit---------------
#find the maximum curvatuve using of 3rd derivative = 0
def func(x):
    return 60*g*x**2 + 24*e*x+6*d
x = fsolve(func,0) 
y_prime = b+ 2*c*x+ 3*d*x**2 + 4*e*x**3 + 5*g*x**4 #1st derivative
y_2prime = 2*c + 6*d*x + 12*e*x**2 + 20*g*x**3
dx = -y_prime/y_2prime
Vstop5 = x + dx #stopping voltage 
y = a + b*Vstop5 + c*Vstop5**2 + d*Vstop5**3 + e*Vstop5**4 +g*Vstop5**5
plt.plot(Vstop5,y,'ko',label = 'Vstop')
plt.legend()
Vstop5_err = 0.2

print(Vstop5)

plt.figure(5)
plt.show()



#plot together
x1 = df['Voltage - 365'].astype(float)
y1 = df['Photocurrent - 365'].astype(float)
plt.plot(x1,y1,color='m',markersize=2,label = '365 nm')

x2 = df['Voltage - 405'].astype(float)
y2 = df['Photocurrent - 405'].astype(float)
plt.plot(x2,y2,color='royalblue',markersize=2,label = '405 nm')


x3 = df['Voltage - 436'].astype(float)
y3 = df['Photocurrent - 436'].astype(float)
plt.plot(x3,y3,color='limegreen',markersize=2,label = '436 nm')



x4 = df['Voltage - 546'].astype(float)
y4 = df['Photocurrent - 546'].astype(float)
plt.plot(x4,y4,color='orange',markersize=2,label = '546 nm')

x5 = df['Voltage - 567'].astype(float)
y5 = df['Photocurrent - 567'].astype(float)
plt.plot(x5,y5,color='red',markersize=2,label = '567 nm')


plt.title('Voltage vs Photocurrent Data')
plt.xlabel('Voltage [V]')
plt.ylabel('Photocurrent I [pA]')
plt.legend()
plt.grid()
plt.show()
plt.figure(6)

#frequency vs stopiing voltage

c = 3e17 #nm/s
e = 1.602e-19
wl = np.array([365,405,436,546,567]) #units of nm
h = 6.626e-34 # 
# unc_V = np.array([0.5,0.2,0.173,0.0704,0.041])
freq = c/wl
Vstop2d = np.array(np.abs([Vstop1,Vstop2,Vstop3,Vstop4,Vstop5]))
Vstop = Vstop2d.reshape(5,)
KEmax = e*Vstop
Vstop_err = np.array([Vstop1_err,Vstop2_err,Vstop3_err,Vstop4_err,Vstop5_err])

fig = plt.figure(7)
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('center')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

plt.errorbar(1/wl,Vstop,Vstop_err,fmt='.',label = 'Stopping Voltage')
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.grid()
plt.xlabel('1/$\lambda$ (nm)',labelpad = 0)
plt.ylabel('Stopping Voltage: $V_{stop}$ (V)',labelpad =0)
plt.title('Stopping Voltage vs. Frequency graph')


def func(x, a, b):
    return a + b*x  

popt, pcov = curve_fit(func,1/wl,Vstop)
print(b)
print(a)
a = popt[0]
b = popt[1]
h_obs = b*e/c #plancks

h_obs = b/c
h_exp = h/e
print(h_obs)
print(h_exp)
x_fit = np.arange(0.0017,0.0029,0.0001)
X2 = ((h_obs - h_exp)**2)/ h_exp
print(X2)

#plot the curve fit
eq = 'y =' + str(round(popt[1],2)) + "x " + str(round(popt[0],4))
plt.plot(x_fit,func(x_fit,*popt), 'k-', label= "Linear Best Fit")
plt.plot(label=eq)
plt.legend(loc=(0.1,0.6))
plt.show()

W = a
print(W)

plt.figure(8)
# fig = plt.figure(7)
# #ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

Vstop_iSES = np.array([1.4,1.1,0.9,0.4,0.3])
ViSES_err = np.array([0.1,0.1,0.1,0.1,0.1])

plt.errorbar(1/wl,Vstop_iSES,ViSES_err,fmt='.',label = 'Stopping Voltage')

def func(x, a, b):
    return a + b*x  
popt, pcov = curve_fit(func,1/wl,Vstop_iSES)
a = popt[0]
b = popt[1]


x_fit = np.arange(0.0017,0.0029,0.0001)

plt.plot(x_fit,func(x_fit,*popt), 'k-', label= "Linear Best Fit")
plt.title('Expected - Stopping Voltage vs Frequency Graph')
plt.xlabel('1/$\lambda$ (nm)',labelpad = 0)
plt.ylabel('Stopping Voltage: $V_{stop}$ (V)',labelpad =0)
plt.grid()
plt.legend(loc=(0.1,0.6))
plt.show()

W_exp = a
print(W_exp)

2.5,2.5,1,1.5,.5




