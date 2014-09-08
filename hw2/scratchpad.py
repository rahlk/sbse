## -*- coding: utf-8 -*-
#"""
#Created on Sun Sep 07 18:09:19 2014
#
#This Scarathpad is used to run code fragments before importing them
#
#@author: Rahul
#"""
import numpy as np
from math import e
from math import sqrt
from math import sin
import random
#
randi=random.randint
rand=random.uniform
#a, b=0.8, 1
#xsize=3
#x=[randi(-5,5) for z in xrange(3)]
#f1=np.sum([-10*e**(-0.2*sqrt(x[z]**2+x[z+1]**2)) for z in xrange(xsize-1)])
#f2=np.sum([abs(x[z])**a+5*sin(x[z])**b])
#ener=f1+f2
#print ener
xmax, xmin=4, -4
def neighbour(x,xmax,xmin):
    return xmin+(xmax-xmin)*rand(0,1)
randIndx=randi(0,2)
x=xn=[rand(-4,4) for z in xrange(3)]
xn[randIndx]=neighbour(xn[randIndx],xmax,xmin)
Step=np.linspace(xmin,xmax,10)
for i in xrange(np.size(Step)):
    xNew=xn; xNew[randIndx]=Step[i]
    if score(xNew,emax,emin)<xBest:
        xBest=score(xNew,emax,emin)
        print i, xBest
        xn=xNew
print x
print xn
