#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:31:41 2018

@author: aaron_escbr
"""
"""
Created on Wed Feb 14 14:28:41 2018

@author: Aaron Escobar

Problem 2: for loops and arrays 
"""
#Import numpy
import numpy as np          

n = 100                       # number of elements being used                            

#preallocate array
a=np.empty(100,dtype='int')   # create an empty array of data type int

#Main script for loop 
for i in range(0,100):
    a[i]= i+1                 # since python starts at zero we add one so we start at 1 
print(a)
for j in range(40,60):
    if(j%2!=0):               # this command will print only the odd numbers from the given range
        print(j)