"""
Homework 1 

Authored by Rahul 
Last updated September, 1st 2014
"""

from __future__ import division
import sys,re,random,math,datetime,re,time
sys.dont_write_bytecode = True

rand=random.uniform
randi=random.randint
exp=math.exp
random.seed()

class simulatedAnnealing:

  def __init__(self):
    pass
  
  def energy(self,x,emax,emin):
    f1=x**2
    f2=(x-2)**2
    e=f1+f2
    e_norm=(e-emin)/(14379-emin)
    #print e_norm
    return e_norm

  def neighbour(self, x, xmin, xmax):
    x_new=xmin+(xmax-xmin)*rand(0,1)
    return x_new

  def pAcceptance(self, e, en, t, k):
    p=exp(-(en-e)/(k*t))
    print p
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
  emax=1;
  emin=0;
  
  sa=simulatedAnnealing()

  # Initial state and energy
  s=randi(-1000,1000)
  e=sa.energy(s,emax,emin)
  print e
  # Initial best state and energy
  sb=s;
  eb=e;
 
  sa.say(sb)
  
  while (k<kmax): 
    sn=sa.neighbour(s,xmax,xmin)
    en=sa.energy(sn,emax,emin)
    t=k/kmax
    
    if en<eb:
      sa.say('!')
      sb=sn
      eb=en

    if en<e:
      s=sn
      e=en
      sa.say('+')
    
    elif sa.pAcceptance(e, en, t, 0.01)>rand(0,1):
      s=sn
      e=en
      sa.say('?')
  
    sa.say('.')
    k=k+1
    if k%40==0: sa.say('\n'), sa.say(format(sb,'0.2f'))
  sa.say('\n'),sa.say('Best Value Found '),sa.say(format(sb,'0.2f'))
  print emax
  print emin
  print e
  print sb
if __name__=='main':
  main()
