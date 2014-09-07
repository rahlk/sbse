"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
# imports specific to the plots in this example

import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
import matplotlib.animation as animation

import math
exp=math.exp

def pAcceptance(e, en, t, k):
    p=exp(-(en-e)/(k*t))
#    print p
    return p
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt

# Twice as wide as it is tall.
fig = plt.figure(figsize=(5,5),dpi=100)

#---- First subplot
ax = fig.add_subplot(1, 1, 1, projection='3d')
X = np.arange(0, 1, 0.01)
Y = np.arange(0, 1, 0.01)
X, Y = np.meshgrid(X, Y)
Z = np.exp(-(X-Y)/0.9)
#Z = np.sin(R)

#---- Second subplot
ax = fig.add_subplot(111, projection='3d')
F=ax.plot_wireframe(-X, Y, Z, rstride=10, cstride=10)

plt.show()