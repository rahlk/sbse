from __future__ import division
from searcher import *
from models import *
import sys
from decimal import *
import numpy as np
from anzeigen import *
from time import gmtime, strftime
import sk
import sys, random, math, datetime, time,re
from base import xtile
sys.dont_write_bytecode = True
rseed=random.seed
rdivdemo=sk.rdivDemo
#===============================================================================
# Baselining
#===============================================================================
emin=10**32;
emax=-10**32;
baselining = {}

for x in [Schaffer, Kursawe, 
          Fonseca, ZDT1, ZDT3, Viennet3]:
  baselining.update({x.__doc__:(0, 0)})
  rseed(1)
  for y in [SimulatedAnnealer, MaxWalkSat]:
    k=modelBasics(x)
    eMax, eMin = k.baselining(x)
    (emax, emin) = baselining[x.__doc__]
    emax= eMax if eMax>emax else emax
    emin= eMin if eMin<emin else emin
    baselining.update({x.__doc__:(emax, emin)})
    

for x in [ZDT1]:
  rseed(1)
  early=True
  eb=30*[0]
  eb1=30*[0]
  eb2=30*[0]
  (e1, e2)= baselining[x.__doc__]
  for y in [SimulatedAnnealer, MaxWalkSat]:
    print 'Model: ', x.__doc__ 
    print 'Searcher: ', y.__doc__ 
    print strftime("%a, %d %b %Y %H:%M:%S ", gmtime()), '\n'
    k=x()
    reps=30
    dspl=anzeigen();
    E=[]
    E1=[]
    E2=[]
    hi, lo, kooling, indepSize, iterations = k.eigenschaften()
    print 'Settings:'
    print 'min=', lo, ', max=', hi, ', Cooling Factor=', kooling, '\n'
    if early: print 'Early Termination!'  , '\n'
    for r in xrange(reps):
      a=y(x,e1, e2, disp=False,early=early)
      eTmp =  a.runSearcher()
      E.append([eTmp[0]])
      #E1.append(eb1[r])
      #E2.append(eb2[r])
    #print dspl.xtile(eb[1:])
    """for r in xrange(4):
      print dspl.xtile(eb[r:r+50], lo=lo, hi=hi)"""
    E.insert(0, y.__doc__)
    print E
    #E1.insert(0, 'Objective 1')
    #E2.insert(0, 'Objective 2')
    print 'Best Energy: ', "{:.3F}".format(Decimal(str(np.sum(eb)/reps))), '\n'

def _rDiv():
    rdivdemo(E)
_rDiv()    
for _ in xrange(50): sys.stdout.write('_')
print '\n'
    
     
  #
  
sys.stdout.write('\n')
