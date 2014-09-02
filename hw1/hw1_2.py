"""
Homework 1 

Authored by Rahul 
Last updated September, 1st 2014
"""

from __future__ import division
import sys,re,random,math,datetime,re,time
sys.dont_write_bytecode = True

rand=random.random
randi=random.randint
exp=math.exp

class simulatedAnnealing:

  def __init__(self):
    pass
  
  def energy(self,x):
    e=x**2+(x-2)**2
    e_norm=(e)/(23960)
   # print e_norm
    return e

  def neighbour(self, x, xmin, xmax):
    x_new=x+xmin+(xmax-xmin)*rand()
    return x_new

  def pAcceptance(self, e, en, t):
    p=exp(-(en-e)/t)
   # print p
    return p
 
  f=open('output.log','w')
  def say(self,x): 
    self.f.write(str(x)); 
    sys.stdout.flush()
 
# Initial temperature
 
class main:

  k=1
  kmax=2000
  
  xmax=100;
  xmin=-100;
  
  sa=simulatedAnnealing()

  # Initial state and energy
  s=randi(-1000,1000)
  e=sa.energy(s)

  # Initial best state and energy
  sb=s;
  eb=e;
 
 # sa.say(sb)
  emax=e
  
  while (k<kmax):# and e > emax): 
    sn=sa.neighbour(sb,xmax,xmin)
    en=sa.energy(sn)
    t=k/kmax
    if en<eb:
      sa.say('!')
      sb=sn
      eb=en

    if en<e:
      s=sn
      e=en
      sa.say('+')
    
    elif sa.pAcceptance(e, en, t)>rand():
      s=sn
      e=en
      sa.say('?')
  
    sa.say('.')
    k=k+1
    if k%50==0: sa.say('\n'), sa.say(sb)
 # print emax
if __name__=='main':
  main()
