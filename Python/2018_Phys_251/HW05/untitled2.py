#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:33:59 2018

@author: aaron_escbr
"""
import numpy as np

n = int(input('n = '))

k = np.empty([n,n],dtype=int)

    
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            k[i,j] = 2
        elif i == j+1:
            k[i,j] = -1
        elif i == j-1:
            k[i,j] = -1
        else:
            k[i,j] = 0
            
print(k)
print()

a = np.empty([n,n],dtype=int)

k2 = np.zeros([n,n]) 
for i in range(0,n):
    for j in range(0,n):
        for h in range(0,n):
            k2[i][j] += k[i][h] * k[h][j]

for i in range(0,n):
    for j in range(0,n):
        a[i][j] = k2[i][j] - k[i][j]
        
print(a)