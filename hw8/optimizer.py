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

def what2say(k,modelName):
  hi, lo, kooling, indepSize, thresh, iterations = k.eigenschaften()
  if modelName.__doc__=="SA ":
    return {'Max: ': hi, 'Min: ': lo, 'Cooling Factor: ':kooling,
            'Iterations: ': iterations}
  elif modelName.__doc__=="MWS":
    return {'Max: ': hi, 'Min: ': lo, 'Retries: ': 100,
            'Iterations: ': 100}
  elif modelName.__doc__=='GA ':
    return {'Max: ': hi, 'Min: ': lo, 'Population: ': 50, 
            'Generations: ': 400, 'crossover: ': 0.6}
  elif modelName.__doc__=='DE ':
    return {'Max: ': hi, 'Min: ': lo, 'Iterations: ': 100, 
            'NP: ':100, 'f: ':0.75, 'cf: ':0.3}
  elif modelName.__doc__=='PSO':
    return {'Max: ': hi, 'Min: ': lo, 'Iterations: ': 100, 
            'Number of Particles: ':30, 'phi1: ':1.3, 'phi2: ':2.6}

#===============================================================================
# Baselining
#===============================================================================
emin=10**32;
emax=-10**32;
baselining = {}

for x in [Schaffer, Kursawe, 
          Fonseca, ZDT1, ZDT3, Viennet3, DTLZ7]:
  baselining.update({x.__doc__:(0, 0)})
  for y in [PSO, GA, diffEvolve, SimulatedAnnealer, MaxWalkSat]:
    k=modelBasics(x)
    eMax, eMin = k.baselining(x)
    (emax, emin) = baselining[x.__doc__]
    emax= eMax if eMax>emax else emax
    emin= eMin if eMin<emin else emin
    baselining.update({x.__doc__:(emax, emin)})
    

for x in [Fonseca, ZDT1, ZDT3, Viennet3, DTLZ7]:
  early=True
  E=[]
  E1= [] 
  E2 = []
  for i in xrange(50): sys.stdout.write('_')
  print '\n'
  print 'Model: ', x.__doc__ 
  for i in xrange(50): sys.stdout.write('-')
  print '\n'
  print strftime("%a, %d %b %Y %H:%M:%S ", gmtime()), 'GMT', '\n'
  (e1, e2)= baselining[x.__doc__]
  print e1, e2
  for y in [PSO, diffEvolve, GA, SimulatedAnnealer, MaxWalkSat]:
    print 'Searcher: ', y.__doc__ 
    k=x()
    reps=30
    eb  = []
    ebIndv1 = []
    ebIndv2 = []
    dspl=anzeigen();
    hi, lo, kooling, indepSize, thresh, iterations = k.eigenschaften()
    #print 'Settings:'
    toprint=what2say(k,y);
    #for k in toprint:
    # print k, toprint[k]
    #if early: print 'Early Termination!'  , '\n'
    for r in xrange(reps):
      a=y(x,disp=False,early=early)
      eTmp =  a.runSearcher(e1, e2)
      eb.append(eTmp[0]); ebIndv1.append(eTmp[1][0]); ebIndv2.append(eTmp[1][1]); 
    eb.insert(0,y.__doc__)
    ebIndv1.insert(0, y.__doc__)
    ebIndv2.insert(0, y.__doc__)
    E.append(eb)
    E1.append(ebIndv1)
    E2.append(ebIndv2)
    
    #print dspl.xtile(eb[1:])
    """for r in xrange(reps):
      print dspl.xtile(eb[r:r+50], lo=lo, hi=hi)"""
    print 'Energy: ', "{:.3E}".format(Decimal(str(np.sum(eb[1:])/reps))), '\n'
  
  def _rDiv():
    rdivDemo(E)
    rdivDemo(E1)
    rdivDemo(E2)
  _rDiv()
    
  #
  
  sys.stdout.write('\n')
