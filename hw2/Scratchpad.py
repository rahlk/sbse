"""
Homework 2
Created on Wednesday, Sep  3 17:51:42 2014

@author: Rahul
"""

from __future__ import division
import sys,re,random,math,datetime,re,time
import numpy as np
sys.dont_write_bytecode = False

rand=random.uniform
randi=random.randint
e=math.e

xmax = 4
xmin = -4

# Generate fonseca using list comprehesions, these are bloody good!
x=[randi(-4,4),randi(-4,4),randi(-4,4)]
def neighbour(xmax,xmin):
  x=[xmin+(xmax-xmin)*rand(0,1) for z in xrange(3)]
  return x
def energy(x):
  f1, f2=(1-e**np.sum([(x[z]-1/(np.sqrt(z+1))) for z in xrange(0,3)])), \
  (1-e**np.sum([(x[z]+1/(np.sqrt(z+1))) for z in xrange(0,3)]))
  return f1+f2
print x, '\n', energy(x)