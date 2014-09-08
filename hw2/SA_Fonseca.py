"""
Homework 2: The Fonseca Model
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
  
  def energy(self,x,emax,emin):
    f1, f2=(1-e**np.sum([(x[z]-1/(np.sqrt(z+1))) for z in xrange(3)])),\
    (1-e**np.sum([(x[z]+1/(np.sqrt(z+1))) for z in xrange(0,3)]))
    ener=f1+f2
    eNorm= (ener-emin)/(emax-emin)
#   print e_norm
    return eNorm

  def neighbour(self,x,xmax,xmin):
    def __new(x,z):
        return xmin+(xmax-xmin)*rand(0,1) if rand(0,1)<0.5 else x[z] 
    x_new=[__new(x,z) for z in xrange(3)]
    return x_new

  def do_a_randJump(self, e, en, t, k):
      p=math.e**(-(e-en)/(t*k))<rand(0,1)
#      print p
      return p

  def baselining(self):
    emax=-1;emin=1;
    for x in xrange(int(1e3)):
      x_tmp=[randi(-4,4) for z in xrange(3)]
      ener=(1-e**np.sum([(x_tmp[z]-1/(np.sqrt(z+1))) for z in xrange(3)]))+\
      (1-e**np.sum([(x_tmp[z]+1/(np.sqrt(z+1))) for z in xrange(3)]))
      
      if ener>=emax:
        emax=ener
      elif ener<=emin:
        emin=ener
    return emax,emin

  f=open('log_sa_fonseca.txt','w')
  def say(self,x):
    self.f.write(str(x));
    sys.stdout.flush()

# Initial temperature

class main:

  k=1
  kmax=5000

  xmax=4;
  xmin=-4;

  sa=simulatedAnnealing()
  emax, emin = sa.baselining()
  print emax, emin
  # Initial state and energy
  sb=s=[rand(-4,4) for z in xrange(3)]
  eb=e=sa.energy(s,emax,emin)
  print e

  print 'Initial Best', sb

  for k in xrange(1,kmax):
    #print k
    sn=sa.neighbour(s,xmax,xmin)
    en=sa.energy(sn,emax,emin)
    t=k/kmax

    if en<eb:
      eb, sb=en, sn; sa.say('!')

    if en<e:
      s, e = sn, en; sa.say('+')

    elif sa.do_a_randJump(en,e,k,1e-3): # The cooling factor needs to be reallylow for some reason!!
      s, e=sn, en; sa.say('?')

    sa.say('.')
    if k%40==0: sa.say('\n')# sa.say(format(sb,'0.2f'))

  sa.say('\n'),sa.say('Best Value Found '), sa.say(sb)

# Print Energy and best value.
  print sb
if __name__=='main':
  main()
