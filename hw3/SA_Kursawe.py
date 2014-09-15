# -*- coding: utf-8 -*-

"""
Homework 2: THe Kursawe Model
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
sin=math.sin 
sqrt=math.sqrt
random.seed()

class simulatedAnnealing:

  def __init__(self):
    pass
  
  def energy(self,x,emax,emin):
    a=0.8; b=3; xsize=3
    f1=np.sum([-10*e**(-0.2*sqrt(x[z]**2+x[z+1]**2)) for z in xrange(xsize-1)])
    f2=np.sum([abs(x[z])**a+5*sin(x[z]**b)])
    ener=f1+f2
    eMron= (ener-emin)/(emax-emin)
    return eMron

  def neighbour(self,x,xmax,xmin):
    def __new(x,z):
        return xmin+(xmax-xmin)*rand(0,1) if rand(0,1)<0.33 else x[z] 
    x_new=[__new(x,z) for z in xrange(3)]
    return x_new

  def do_a_randJump(self, e, en, t, k):
      p=math.e**(-(e-en)/(t*k))<rand(0,1)
#      print p
      return p

  def baselining(self):
    emax=-1;emin=1; a=0.8; b=3; xsize=3;
    for x in xrange(int(1e3)):
      x_tmp=[randi(-5,5) for z in xrange(3)]
      ener=np.sum([-10*e**(-0.2*sqrt(x_tmp[z]**2+x_tmp[z+1]**2)) for z in xrange(xsize-1)])+\
      np.sum([abs(x_tmp[z])**a+5*sin(x_tmp[z]**b)])
      if ener>=emax:
        emax=ener
      elif ener<=emin:
        emin=ener
    return emax,emin

  f=open('log_sa_kursawe.txt','w')
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
  emax, emin = sa.baselining()
  print emax, emin
  # Initial state and energy
  sb=s=[rand(-4,4) for z in xrange(3)]
  eb=e=sa.energy(s,emax,emin)
  #print e

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

    elif sa.do_a_randJump(en,e,k,kooling): # The cooling factor needs to be reallylow for some reason!!
      s, e=sn, en; sa.say('?')

    sa.say('.')
    if k%40==0: sa.say('\n')# sa.say(format(sb,'0.2f'))

  sa.say('\n'),sa.say('Best Value Found '), sa.say(sb)

# Print Energy and best value.
  print sb
if __name__=='main':
  main()
