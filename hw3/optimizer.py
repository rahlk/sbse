from __future__ import division
from searcher import *
from models import *
import sys
from decimal import *
import numpy as np
from anzeigen import *
from time import gmtime, strftime
import sys, random, math, datetime, time,re
sys.dont_write_bytecode = True


for x in [Schaffer, Kursawe, 
          Fonseca, ZDT1, Viennet3]:
  early=True
  eb=30*[0]
  for y in [SimulatedAnnealer]:#[SimulatedAnnealer, MaxWalkSat]:
    print 'Model: ', x.__name__ 
    print 'Searcher: ', y.__name__ 
    print strftime("%a, %d %b %Y %H:%M:%S ", gmtime()), '\n'
    k=x()
    reps=1
    dspl=anzeigen();
    hi, lo, kooling, indepSize, iterations = k.eigenschaften()
    print 'Einstellungen:'
    print 'min=', lo, ', max=', hi, ', Cooling Factor=', kooling, '\n'
    if early: print 'Early Termination!'  , '\n'
    for r in xrange(reps):
      a=y(x,disp=True,early=early)
      eb[r] =  a.runSearcher()
    
    #print dspl.xtile(eb[1:])
    """for r in xrange(reps):
      print dspl.xtile(eb[r:r+50], lo=lo, hi=hi)"""
    print 'Energy: ', "{:.3E}".format(Decimal(str(np.sum(eb)/reps)))
    
  #
  
  sys.stdout.write('\n')
