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
from anzeigen import *
from dynamikliste import *
# from sk import Num
import analyzer

# Define some aliases.
rand = random.uniform
randi = random.randint
exp = math.exp

class SimulatedAnnealer(object):
  def __init__(self, modelName, disp=False, early=False):
    self.modelName = modelName
    self.disp = disp
    self.early = early
  def runSearcher(self):
    modelbasics = modelBasics(self.modelName);
    modelFunction = self.modelName()
    anz = anzeigen();
    hi, lo, kooling, indepSize, iterations = modelFunction.eigenschaften()
    emax, emin = modelbasics.baselining(self.modelName)
    sb = s = [randi(lo, hi) for z in xrange(indepSize)];
    eb = e = modelbasics.energy(s, emax, emin)
    enRec = dynamikliste()  # Creates a growing list.
    enRec[0] = 0;  # Since iterations start from 1, lets initialize enRec[0] to 0
    analyser = analyzer.analyser()
    epochs = 5 if self.early else iterations;
    k = 1;
    while epochs and k < iterations:
      sn = modelbasics.neighbour(s, hi, lo)
      en = modelbasics.energy(sn, emax, emin)
      t = k / iterations
      if en < eb:
        eb, sb, enRec[k] = en, sn, en;
        if self.disp: 
          modelbasics.say('!')

      if en < e:
        s, e, enRec[k] = sn, en, en; 
        if self.disp: 
          modelbasics.say('+')

      if modelbasics.do_a_randJump(en, e, t, kooling):  # The cooling factor needs to be reallylow for some reason!!
        s, e, enRec[k] = sn, en, en; 
        if self.disp: 
          modelbasics.say('?')
      else:
        enRec[k] = en  
      if self.disp:
        modelbasics.say('.')
      if k % 50 == 0 and k > 50:
        # print enRec[:-10]
        proceed = analyser.isItGettinBetter(enRec[k - 100:])
        if proceed:
          epochs += 1;
        else:
          epochs -= 1;
        # print enRec[k-40:] #
      k = k + 1
      if k % 40 == 0:
        if self.disp: 
          modelbasics.say('\n')  # sa.say(format(sb,'0.2f'))    
        
    if self.disp: 
      modelbasics.say('\n'),  # modelbasics.say('Best Value Found '), modelbasics.say(sb)

  # Print Energy and best value.
    for i in xrange(k):
      if self.disp:
        if i % 50 == 0:
          print anz.xtile(enRec[i - 50:]) 
    if self.disp: 
      modelbasics.say('\n')
    return eb
    
class MaxWalkSat(object):
  def __init__(self, modelName, disp=False, early=True, maxTries=100, maxChanges=100):
    self.modelName = modelName
    self.disp = disp
    self.maxTries = maxTries
    self.maxChanges = maxChanges
  def runSearcher(self):
    modelbasics = modelBasics(self.modelName);
    modelFunction = self.modelName()
    hi, lo, kooling, indepSize, iterations = modelFunction.eigenschaften()
    emax, emin = modelbasics.baselining(self.modelName)
    for i in xrange(self.maxTries):
        # Lets create a random assignment, I'll use list comprehesions here.
        x = xn = xb = [rand(lo, hi) for z in xrange(indepSize)]
        # Create a threshold for energy, let's say thresh=0.1% of emax (which is 1) for starters
        thresh = 1e-7
        for j in xrange(self.maxChanges):
            # Let's check if energy has gone below the threshold.
            # If so, look no further.
            if modelbasics.energy(xn, emax, emin) < thresh:
                if self.disp:
                  modelbasics.say('.')
                break
            else:
                randIndx = randi(0, indepSize - 1)  # Choose a random part of solution x
                if rand(0, 1) > 1 / (indepSize + 1):  # Probablity p=0.33
                    y = xn[randIndx]
                    xn[randIndx] = modelbasics.simpleneighbour(y, hi, lo)
                    if self.disp:
                      modelbasics.say('+')
                    # print 'Random change on', randIndx
                else:
                    # xTmp is a temporary variable
                    xBest = emax;
                    # Step from xmin to xmax, take 10 steps
                    Step = np.linspace(lo, hi, 100)
                    if self.disp:
                      modelbasics.say('!')
                    for i in xrange(np.size(Step)):
                        xNew = xn; xNew[randIndx] = Step[i];
                        if modelbasics.energy(xNew, emax, emin) < xBest:
                            xBest = modelbasics.energy(xNew, emax, emin)
                            xn = xNew
            
            if modelbasics.energy(xn, emax, emin) < modelbasics.energy(xb, emax, emin):
              xb = xn
              print modelbasics.energy(xn, emax, emin)
    return modelbasics.energy(xb, emax, emin)
    
if __name__ == 'main':
  SimulatedAnnealer(Schaffer)
  
