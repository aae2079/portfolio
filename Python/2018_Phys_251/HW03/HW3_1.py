"""
Created on Tue Feb 20 10:46:01 2018

@author: Aaron Escobar

Homework 3 Problem 1
"""
#import matplotlib and numpy modules
import matplotlib.pyplot as plt
import numpy as np

#create an array from -pi to pi with 50 elements
theta = np.linspace(-np.pi,np.pi,50)
n = theta.size #size the array, this gives us the amount of elements within it

#1. f1(theta) = cos(2*theta)
f1 = np.empty(n) #create an 'empty' array for f1

#calculate f1 using a for loop
for i in range(n):
    f1[i] = np.cos(2*theta[i])

plt.figure(1)
plt.plot(theta,f1,'.', label = 'cos(2${\Theta}$)')
plt.grid(which='major')
plt.xlabel('${\Theta}$')
plt.ylabel('$f_1({\Theta})$')
plt.title('$f_1({\Theta}) = cos(2{\Theta})$')
plt.legend(loc=3)

#2. f2(theta) = 2cos^2(theta) - 1
f2 = np.empty(n) #create an 'empty' array for f2

#calculate f2 using a for loop
for i in range(n):
    f2[i] = 2*(np.cos(theta[i])**2) - 1
plt.figure(2)   
plt.plot(theta,f2,'.',label = '$2cos^2({\Theta})-1$')
plt.grid(which='major')
plt.xlabel('${\Theta}$')
plt.ylabel('$f_2({\Theta})$')
plt.title('$f_2({\Theta}) = 2cos^2({\Theta}) - 1$')
plt.legend()


#3. f3(theta) = sec(theta) + tan(theta)
f3 = np.empty(n) #create an 'empty' array for f2

#calculate f3 using a for loop
for i in range(n):
    f3[i] = (np.cos(theta[i]))**-1 + np.tan(theta[i])
    
plt.figure(3)
plt.plot(theta,f3,'.', label = 'sec(${\Theta}$) + tan(${\Theta}$)')
plt.ylim([-3,3])
plt.xlim([-5,5])
plt.grid(which='major')
plt.xlabel('${\Theta}$')
plt.ylabel('$f_3({\Theta})$')
plt.title('$f_3({\Theta}) = sec({\Theta}) + tan({\Theta})$')
plt.legend()