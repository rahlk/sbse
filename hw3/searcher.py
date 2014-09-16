# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 03:04:43 2014

@author: rkrsn
"""
from __future__ import division
import sys
import math, random, numpy as np, scipy as sp
from scipy.odr import models
sys.dont_write_bytecode = False
from models import *

# Define some aliases.
rand=random.uniform
randi=random.randint
exp=math.exp

class sa(object):
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
if __name__=='main':
  sa(Schaffer)
  