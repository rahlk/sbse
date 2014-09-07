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
    f1, f2=(1-e**np.sum([(x[z]-1/(np.sqrt(z+1))) for z in xrange(0,3)])), \
    (1-e**np.sum([(x[z]+1/(np.sqrt(z+1))) for z in xrange(0,3)]))
    ener=f1+f2
    e_norm= (ener-emin)/(emax-emin)
#   print e_norm
    return e_norm

  def neighbour(xmax,xmin):
    x=[xmin+(xmax-xmin)*rand(0,1) for z in xrange(3)]
    return x

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
<<<<<<< HEAD
  sb=s=randi(-1000,1000)
  eb=e=sa.energy(s)
=======
  s=randi(-100,100)
  e=sa.energy(s)
>>>>>>> 491fdd592d5769557842e0777604f79905108754
  print e
  # Initial best state and energy

  sa.say(sb)

  for k in xrange(1,kmax):
    sn=sa.neighbour(s,xmax,xmin)
    en=sa.energy(sn)
    t=k/kmax

    if en<eb:
      eb, sb=en, sn; sa.say('!')

    if en<e:
      s, e = sn, en; sa.say('+')

    elif sa.randJump(en,e,k,0.0001):
      s, e=sn, en; sa.say('?')

    sa.say('.')
    if k%40==0: sa.say('\n'), sa.say(format(sb,'0.2f'))

  sa.say('\n'),sa.say('Best Value Found '), sa.say(format(sb,'0.2f'))

# Print Energy and best value.
  print e
  print sb
if __name__=='main':
  main()
