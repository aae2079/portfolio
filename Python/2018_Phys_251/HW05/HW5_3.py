"""
Created on Tue Mar 27 12:41:14 2018

@author: Aaron Escobar

Homework 5 Problem 3
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # to plot a 3D object you must import this module!!
from matplotlib import cm 

dname = '/Users/aaron_escbr/Downloads' #directory name
fname = 'data_2D_grid_T.txt' # file name

dfname = '{0:s}/{1:s}'.format(dname,fname)

data_2D = np.genfromtxt(dfname,skip_header=13)

x = data_2D[:,0] # x data
y = data_2D[:,1] # y data
z = data_2D[:,2] # z data

cols = np.unique(x).shape[0] # returns unique elements of an array

X = x.reshape(-1,cols) # reshape x,y and z arrays to be able to graph
Y = y.reshape(-1,cols)
Z = z.reshape(-1,cols)

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X,Y,Z,cmap=cm.terrain, antialiased=False)
plt.savefig('hw5_3_fig1.png')
plt.title(r'$Bilinear\ Interpoltation$')
plt.show()

X1 = np.arange(-10,10,0.5) #new x array
Y1 = np.arange(-10,10,0.5) # new y array
n = X1.size


x2 = np.empty(n)
y2 = np.empty(n)
Z_in = np.empty(n+1)

#main bilinear interp for loop
for i in range(0,n-1):
    for j in range(0,n-1):
        a         = Z[i,j] * (x[i+1]-x2[i]) * (y[j+1]-y2[j])
        b         = Z[i,j+1] * (x[i+1]-x2[i]) * (y2[j]-y[j])
        c         = Z[i+1,j] * (x2[i]-x[i]) * (y[j+1]-y2[j])
        d         = Z[i+1,j+1] * (x2[i]-x[0]) * (y2[j]-y[j])
        for k in range(0,n-1):
            Z_in[k] = (a + b + c + d)/((x[i+1]-x[i])*(y[i+1]-y[i]))
          
Znew = Z_in.reshape(-1,cols)


# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1,Y1,Znew,cmap=cm.terrain, antialiased=False)
plt.savefig('hw5_3_fig2.png')
plt.title(r'$Bilinear\ Interpoltation$')
plt.show()
