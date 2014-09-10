"""
Homework 2
Last updated  Sunday, Sep  7 17:51:42 2014
@author: Rahul Krishna
"""

from __future__ import division
import sys,re,random,math,datetime,re,time
import numpy as np
import scipy as sp
sys.dont_write_bytecode = False

# Define some aliases.
rand=random.uniform
randi=random.randint
e=math.e
random.seed()

class simulatedAnnealing:

  def __init__(self):
    pass

  def energy(self,x):
    emax, emin = self.baselining()
    f1, f2=(1-e**np.sum([(x[z]-1/(np.sqrt(z+1))) for z in xrange(3)])),\
    (1-e**np.sum([(x[z]+1/(np.sqrt(z+1))) for z in xrange(0,3)]))
    ener=f1+f2
    e_norm= (ener-emin)/(emax-emin)
#   print e_norm
    return e_norm

  def neighbour(self,x,xmax,xmin):
    def __new(x,z):
      if rand(0,1)>0.33:
        return xmin+(xmax-xmin)*rand(0,1)
      else:
        return x[z]
    x_new=[__new(x,z) for z in xrange(3)]
    return x_new

  def randJump(self, e, en, t, k):
      p=math.e**(-(e-en)/(t*k))<rand(0,1)
#      print p
      return p

  def baselining(self):
    emax=0;emin=1;
    for x in xrange(1,10000):
      x_tmp=[rand(-4,4) for z in xrange(3)]
      ener=(1-e**np.sum([(x_tmp[z]-1/(np.sqrt(z+1))) for z in xrange(0,3)]))+\
      (1-e**np.sum([(x_tmp[z]+1/(np.sqrt(z+1))) for z in xrange(0,3)]))
#      print e
      if ener>emax:
        emax=ener
      elif e<emin:
        emin=ener
    return emax,emin

  f=open('log.txt','w')
  def say(self,x):
    self.f.write(str(x));
    sys.stdout.flush()

# Initial temperature

class main:

  k=1
  kmax=2000

  xmax=4;
  xmin=-4;

  sa=simulatedAnnealing()

  # Initial state and energy
  sb=s=[rand(-4,4) for z in xrange(3)]
  eb=e=sa.energy(s)
  print e

  print 'Initial Best', sb

  for k in xrange(1,kmax):
    #print k
    sn=sa.neighbour(s,xmax,xmin)
    en=sa.energy(sn)
    t=k/kmax

    if en<eb:
      eb, sb=en, sn; sys.stdout.write('!')

    if en<e:
      s, e = sn, en; sys.stdout.write('+')

    elif sa.randJump(en,e,k,0.0001):
      s, e=sn, en; sys.stdout.write('?')

    sys.stdout.write('.')
    if k%40==0: sys.stdout.write('\n')# sa.say(format(sb,'0.2f'))

  sys.stdout.write('\n'),sys.stdout.write('Best Value Found '), #sa.say(format(sb,'0.2f'))

# Print Energy and best value.
  print e
  print sb
if __name__=='main':
  main()
