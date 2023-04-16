#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:29:27 2018

@author: aaron_escbr
"""

import numpy as np

n=int(input('Enter n: '))         # rows
m=int(input('Enter m: '))      # columns

# create an empty matrix nxm of float elements
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.empty.html
a=np.empty([n,m],dtype='float')

# fill the matrix with 1/(i+j)
for i in range(0,n):
    for j in range(0,m):
        ip=i+1
        jp=j+1
        a[i,j]=1.0/(ip+jp)           # assign value to element (i,j) of A
        
print(a)