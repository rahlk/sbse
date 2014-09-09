# -*- coding: utf-8 -*-
"""
MaxWalkSat
Created on Mon Sep 08 02:15:42 2014

@author: Rahul

The Algorithm:

FOR i = 1 to max-tries DO
  solution = random assignment
  FOR j =1 to max-changes DO
    IF  score(solution) > threshold
        THEN  RETURN solution
    FI
    c = random part of solution
    IF    p < random()
    THEN  change a random setting in c
    ELSE  change setting in c that maximizes score(solution)
    FI
RETURN failure, best solution found

"""

## Standard imports

from __future__ import division
import sys,re,random,math,datetime,re,time
import numpy as np
import scipy as sp
sys.dont_write_bytecode = False

## Define some aliases.
rand=random.uniform
randi=random.randint
e=math.e
sin=math.sin
sqrt=math.sqrt
random.seed()

maxTries=100
maxChanges=100

## Create a class that defines all definitions in MaxWalkSat
class mWalkSat:

    def __init__(self):
        pass

## All we really need is a scoring function, which in our case would be the
## energy.


    def score(self,x,emax,emin):
        f1, f2=(1-e**np.sum([(x[z]-1/(np.sqrt(z+1))) for z in xrange(3)])),\
        (1-e**np.sum([(x[z]+1/(np.sqrt(z+1))) for z in xrange(0,3)]))
        ener=f1-f2
        eNorm= (ener-emin)/(emax-emin)
       #print e_norm
        return eNorm

    def baselining(self):
        emax=-1;emin=1;
        for x in xrange(int(1e3)):
          x_tmp=[randi(-4,4) for z in xrange(3)]
          ener=(1-e**np.sum([(x_tmp[z]-1/(np.sqrt(z+1))) for z in xrange(3)]))-\
          (1-e**np.sum([(x_tmp[z]+1/(np.sqrt(z+1))) for z in xrange(3)]))
          if ener>=emax:
            emax=ener
          elif ener<=emin:
            emin=ener
        return emax, emin

    def neighbour(self,x,xmax,xmin):
        return xmin+(xmax-xmin)*rand(0,1)

    f=open('log_mwalksat.txt','w')
    def say(self,x):
        self.f.write(str(x));
        sys.stdout.flush()

class main:
    # Create an instance of the maxWalkSAT class
    mwSAT=mWalkSat()
    score=mwSAT.score # Create an alias for the score function (Not required)
    neighbour=mwSAT.neighbour
    say=mwSAT.say
    # Do a baselining study on the score function
    emax, emin= mwSAT.baselining()
    # First define the limits of the independent the variables
    xmax, xmin=4, -4
    for i in xrange(maxTries):
        # Lets create a random assignment, I'll use list comprehesions here.
        x=xn=xb=[rand(-4,4) for z in xrange(3)]
        # Create a threshold for energy, let's say thresh=0.1% of emax (which is 1) for starters
        thresh=1e-7
        for j in xrange(maxChanges):
            # Let's check if energy has gone below the threshold.
            # If so, look no further.
            if score(xn,emax,emin)<thresh:
                say('.')
                break
            else:
                randIndx=randi(0,2) # Choose a random part of solution x
                if rand(0,1)<0.25: # Probablity p=0.33
                    y=xn[randIndx]
                    xn[randIndx]=neighbour(y,xmax,xmin)
                    say('+')
                    #print 'Random change on', randIndx
                else:
                    # xTmp is a temporary variable
                    xTmp= xn; xTmp[randIndx]=rand(-4,4)
                    xBest=score(xTmp,emax,emin);
                    # Step from xmin to xmax, take 10 steps
                    Step=np.linspace(xmin,xmax,10)
                    say('!')
                    for i in xrange(np.size(Step)):
                        xNew=xn; xNew[randIndx]=Step[i];
                        if score(xNew,emax,emin)<xBest:
                            xBest=score(xNew,emax,emin)
                            xn=xNew

            if j%40==0: say('\n')
        say('\n')
        for z in xrange(50): say('_')
        say('\n')
        if score(xn,emax,emin)<score(xb,emax,emin):
            xb=xn
    say('Best solution found: '), say(xb)



