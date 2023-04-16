"""
Homework 1 Problem 3

Created on Wed Jan 31 22:23:44 2018

@author: Aaron Escobar
"""

import numpy as np 
r = 10;                #(m)radius of sphere
b = 39.37              #(in) the amount of inches in a meter
pi= np.pi

A_m  = 4*pi*r**2       #(m^2) Surface area of sphere in meters^2
A_in = 4*pi*(r*b)**2   #(in^2) Surface are of sphere in inches^2

print('The surface area of a sphere with r=10 is {0:.2f} m and {1:.2f} in'.format(A_m,A_in)) #will print answer both in m and in