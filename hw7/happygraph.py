from __future__ import division
from searcher import *
from models import *
import sys, sk
from decimal import *
import numpy as np
from anzeigen import *
from time import gmtime, strftime
import sys, random, math, datetime, time,re
sys.dont_write_bytecode = True
rdivDemo=sk.rdivDemo

#for x in [Viennet3]:
for x in [Schaffer, Kursawe, 
          Fonseca, ZDT1, ZDT3, Viennet3]:
          
  early=True
  E=[]
  for i in xrange(50): sys.stdout.write('_')
  print '\n'
  print 'Model: ', x.__name__ 
  for i in xrange(50): sys.stdout.write('-')
  print '\n'
  print strftime("%a, %d %b %Y %H:%M:%S ", gmtime()), '\n'

  for y in [diffEvolve, GA,SimulatedAnnealer, MaxWalkSat]:
    eb=30*[0]
    print 'Searcher: ', y.__doc__ 
    k=x()
    reps=30
    dspl=anzeigen();
    hi, lo, kooling, indepSize, iterations = k.eigenschaften()
    print 'Settings:'
    print 'min=', lo, ', max=', hi, ', Cooling Factor=', kooling, '\n'
    if early: print 'Early Termination!'  , '\n'
    for r in xrange(reps):
      a=y(x,disp=False,early=early)
      eb[r] =  a.runSearcher()
    eb.insert(0,y.__name__)
    E.append(eb)
    #print dspl.xtile(eb[1:])
    """for r in xrange(reps):
      print dspl.xtile(eb[r:r+50], lo=lo, hi=hi)"""
    print 'Energy: ', "{:.3E}".format(Decimal(str(np.sum(eb[1:])/reps)))
  
  def _rDiv():
    rdivDemo(E)
  _rDiv()
    
  #
  
  sys.stdout.write('\n')
