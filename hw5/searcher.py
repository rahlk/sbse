# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 03:04:43 2014

@author: rkrsn
"""
from __future__ import division
import sys
import math, random, numpy as np, scipy as sp
from math import ceil
sys.dont_write_bytecode = False
from models import *
from anzeigen import *
from dynamikliste import *
# from sk import Num
import analyzer
import types

# Define some aliases.
rand = random.uniform
randi = random.randint
exp = math.exp

class SimulatedAnnealer(object):
  " SA"
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
    enRec[0] = 0;  
    # Since iterations start from 1, lets initialize enRec[0] to 0
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

      if modelbasics.do_a_randJump(en, e, t, kooling):  
        # The cooling factor needs to be really low for some reason!!
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
      modelbasics.say('\n'),  
  # Print Energy and best value.
    for i in xrange(k):
      if self.disp:
        if i % 50 == 0:
          print anz.xtile(enRec[i - 50:]) 
    if self.disp: 
      modelbasics.say('\n')
    return eb
    
class MaxWalkSat(object):
  "MSW"
  def __init__(self, modelName, disp=False, early=True, maxTries=100, 
               maxChanges=100):
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
        # Create a threshold for energy, 
        # let's say thresh=0.1% of emax (which is 1) for starters
        thresh = 1e-2
        for j in xrange(self.maxChanges):
            # Let's check if energy has gone below the threshold.
            # If so, look no further.
            if modelbasics.energy(xn, emax, emin) < thresh:
                break
            else:
              # Choose a random part of solution x
                randIndx = randi(0, indepSize - 1)  
                if rand(0, 1) > 1 / (indepSize + 1):  # Probablity p=0.33
                    y = xn[randIndx]
                    xn[randIndx] = modelbasics.simpleneighbour(y, hi, lo)
                    # print 'Random change on', randIndx
                else:
                    # xTmp is a temporary variable
                    xBest = emax;
                    # Step from xmin to xmax, take 10 steps
                    Step = np.linspace(lo, hi, 10)
                    for i in xrange(np.size(Step)):
                        xNew = xn; xNew[randIndx] = Step[i];
                        if modelbasics.energy(xNew, emax, emin) < xBest:
                            xBest = modelbasics.energy(xNew, emax, emin)
                            xn = xNew
            
            if modelbasics.energy(xn, emax, emin) < modelbasics.energy(xb, 
                                                                       emax, 
                                                                       emin):
              xb = xn
              print modelbasics.energy(xn, emax, emin)
    return modelbasics.energy(xb, emax, emin)
  
class GA(object):
  " GA"
  def __init__(self, modelName, disp=False, early=True, popcap=50, 
               generations=400, crossover=0.6):
    self.modelName = modelName
    self.disp = disp
    self.popcap = popcap
    self.generations = generations
    self.crossover= crossover
  def runSearcher(self):
    modelbasics = modelBasics(self.modelName);
    modelFunction = self.modelName()
    hi, lo, kooling, indepSize, iterations = modelFunction.eigenschaften()
    emax, emin = modelbasics.baselining(self.modelName)
    #---------------------------------------------------------------------------
    def init_pop(indepSize, lo, hi, N=self.popcap):
      return [[rand(lo,hi) for _ in xrange(indepSize)] for _ in xrange(N)]
    
    #---------------------------------------------------------------------------
    def evalPop(Pop, emax, emin):
      score=[];
      for individual in Pop:
        score.append(modelbasics.energy(individual,emax,emin))
      indices=[i[0] for i in sorted(enumerate(score), key=lambda x:x[1], 
                                    reverse=False)]
      scores=[i[1] for i in sorted(enumerate(score), key=lambda x:x[1], 
                                   reverse=False)]
      return [Pop[z] for z in indices], scores
    
    #---------------------------------------------------------------------------
    def evolve(Pop, emax, emin, hi, lo, indepSize, retain=0.2, randSelect=0.05, 
               crossover=self.crossover, mutate=1/(indepSize*(hi-lo))):
      parents, score=evalPop(Pop, emax, emin)
      parents=parents[:int(len(score)*retain)]
      # Increase diversity by selecting bad parents
      for indv in parents[int(len(score)*retain):]:
        if rand(0,1)<randSelect:
          parents.append(indv)
      
      # Crossover parents to create children
      childern=[]
      numChildren=len(Pop)-len(parents)
      
      while len(childern)<numChildren:
        he=randi(0,len(parents)-1);
        she=randi(0,len(parents)-1);
        #print parents
        if he!=she:
          he=parents[he]; she=parents[she]
          if indepSize==1:
            flatten = lambda x: x if not isinstance(x, list) else x[0]
            #print he, she
            child=0.5*(flatten(he)+flatten(she)) \
            if mutate<rand(0,1) else rand(lo,hi)
          else:
            #print he, she
            child=he[:int(0.5*indepSize)]+she[int(0.5*indepSize):]
            if mutate>rand(0,1): child[randi(0,indepSize-1)]=rand(lo,hi)
          childern.append(child)
      
      parents.extend(childern)
      
      return parents
    
    #---------------------------------------------------------------------------
    Pop=init_pop(indepSize, lo, hi, self.popcap)
    pn, en= evalPop(Pop, emax, emin)
    eb=en[0]
    pBest=pn[0]
    for i in xrange(self.generations):
      Pop=evolve(Pop, emax, emin, hi, lo, indepSize) # Spit out the magic 
                                                     # variables please
      pn, en= evalPop(Pop, emax, emin)
      if en[0]<eb:
        eb=en[0]; pBest=pn[0]
    #print pBest 
    return eb         
    
if __name__ == 'main':
  SimulatedAnnealer(Schaffer)
  
