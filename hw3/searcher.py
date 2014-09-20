# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 03:04:43 2014

@author: rkrsn
"""
from __future__ import division
import sys
import math, random, numpy as np, scipy as sp
sys.dont_write_bytecode = False
from models import *

# Define some aliases.
rand=random.uniform
randi=random.randint
exp=math.exp

class SimulatedAnnealer(object):
  def __init__(self,modelName, disp=False):
    self.modelName=modelName
    self.disp=disp
  def runSearcher(self):
    modelbasics=modelBasics(self.modelName);
    modelFunction=self.modelName()
    hi, lo, kooling, indepSize, iterations=  modelFunction.getInit()
    emax, emin = modelbasics.baselining(self.modelName)
    sb=s=[randi(lo,hi) for z in xrange(indepSize)];
    eb=e= modelbasics.energy(s,emax,emin)
    for k in xrange(1,iterations):
      sn=modelbasics.neighbour(s,hi,lo)
      en=modelbasics.energy(sn,emax,emin)
      t=k/iterations
      if en<eb:
        eb, sb=en, sn; 
        if self.disp: 
          modelbasics.say('!')

      if en<e:
        s, e = sn, en; 
        if self.disp: 
          modelbasics.say('+')

      elif modelbasics.do_a_randJump(en,e,t,kooling): # The cooling factor needs to be reallylow for some reason!!
        s, e=sn, en; 
        if self.disp: 
          modelbasics.say('?')
      if self.disp:
        modelbasics.say('.')
      if k%40==0: 
        if self.disp: 
          modelbasics.say('\n')# sa.say(format(sb,'0.2f'))

    if self.disp: 
      modelbasics.say('\n'),#modelbasics.say('Best Value Found '), modelbasics.say(sb)

  # Print Energy and best value.
    if self.disp: 
      modelbasics.say('\n')
    return eb

class MaxWalkSat(object):
  def __init__(self, modelName, disp=False, maxTries=100, maxChanges=100):
    self.modelName=modelName
    self.disp=disp
    self.maxTries=maxTries
    self.maxChanges=maxChanges
  def runSearcher(self):
    modelbasics=modelBasics(self.modelName);
    modelFunction=self.modelName()
    hi, lo, kooling, indepSize, iterations=  modelFunction.getInit()
    emax, emin = modelbasics.baselining(self.modelName)
    for i in xrange(self.maxTries):
        # Lets create a random assignment, I'll use list comprehesions here.
        x=xn=xb=[rand(lo,hi) for z in xrange(indepSize)]
        # Create a threshold for energy, let's say thresh=0.1% of emax (which is 1) for starters
        thresh=1e-7
        for j in xrange(self.maxChanges):
            # Let's check if energy has gone below the threshold.
            # If so, look no further.
            if modelbasics.energy(xn,emax,emin)<thresh:
                if self.disp:
                  modelbasics.say('.')
                break
            else:
                randIndx=randi(0,indepSize-1) # Choose a random part of solution x
                if rand(0,1)>1/(indepSize+1): # Probablity p=0.33
                    y=xn[randIndx]
                    xn[randIndx]=modelbasics.simpleneighbour(y,hi,lo)
                    if self.disp:
                      modelbasics.say('+')
                    #print 'Random change on', randIndx
                else:
                    # xTmp is a temporary variable
                    xBest=emax;
                    # Step from xmin to xmax, take 10 steps
                    Step=np.linspace(lo,hi,100)
                    if self.disp:
                      modelbasics.say('!')
                    for i in xrange(np.size(Step)):
                        xNew=xn; xNew[randIndx]=Step[i];
                        if modelbasics.energy(xNew,emax,emin)<xBest:
                            xBest=modelbasics.energy(xNew,emax,emin)
                            xn=xNew
        
        if modelbasics.energy(xn,emax,emin)<modelbasics.energy(xb,emax,emin):
          xb=xn
    return modelbasics.energy(xb,hi,lo)
    
if __name__=='main':
  sa(Schaffer)
  
