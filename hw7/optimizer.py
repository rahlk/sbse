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
  if modelName.__doc__=="Simulated Annealing":
    return {'Max: ': hi, 'Min: ': lo, 'Cooling Factor: ':kooling,
            'Iterations: ': iterations}
  elif modelName.__doc__=="Max Walk-SAT":
    return {'Max: ': hi, 'Min: ': lo, 'Retries: ': 100,
            'Iterations: ': 100}
  elif modelName.__doc__=='Genetic Algorithm':
    return {'Max: ': hi, 'Min: ': lo, 'Population: ': 50, 
            'Generations: ': 400, 'crossover: ': 0.6}
  elif modelName.__doc__=='Differential Evolution':
    return {'Max: ': hi, 'Min: ': lo, 'Iterations: ': 100, 
            'NP: ':100, 'f: ':0.75, 'cf: ':0.3}
  elif modelName.__doc__=='Particle Swarm Optimization':
    return {'Max: ': hi, 'Min: ': lo, 'Iterations: ': 100, 
            'Number of Particles: ':30, 'phi1: ':1.3, 'phi2: ':2.6}
  
for x in [Schaffer, Kursawe, 
           Fonseca, ZDT1, ZDT3, Viennet3]:
  early=True
  E=[]
  for i in xrange(50): sys.stdout.write('_')
  print '\n'
  print 'Model: ', x.__name__ 
  for i in xrange(50): sys.stdout.write('-')
  print '\n'
  print strftime("%a, %d %b %Y %H:%M:%S ", gmtime()), 'GMT', '\n'

  for y in [PSO, diffEvolve, GA, SimulatedAnnealer, MaxWalkSat]:
    eb=30*[0]
    print 'Searcher: ', y.__doc__ 
    k=x()
    reps=30
    dspl=anzeigen();
    hi, lo, kooling, indepSize, thresh, iterations = k.eigenschaften()
    print 'Settings:'
    toprint=what2say(k,y);
    for k in toprint:
      print k, toprint[k]
    #if early: print 'Early Termination!'  , '\n'
    for r in xrange(reps):
      a=y(x,disp=False,early=early)
      eb[r] =  a.runSearcher()
    eb.insert(0,y.__doc__)
    E.append(eb)
    #print dspl.xtile(eb[1:])
    """for r in xrange(reps):
      print dspl.xtile(eb[r:r+50], lo=lo, hi=hi)"""
    print 'Energy: ', "{:.3E}".format(Decimal(str(np.sum(eb[1:])/reps))), '\n'
  
  def _rDiv():
    rdivDemo(E)
  _rDiv()
    
  #
  
  sys.stdout.write('\n')
