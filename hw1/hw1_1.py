"""
Simulated Annealing

Homework 1 

Authored by Rahul 
Last updated 08/28/2014
"""

from __future__ import division
import sys,re,random,math,datetime,re,time
sys.dont_write_bytecode = True

f=open('output.log','w')
rand=random.random
randi=random.randint
exp=math.exp

class simulatedAnnealing:
  def say(x): 
    f.write(str(x)); sys.stdout.flush()

  def energy(x):
    return x**2+(x-2)**2

  def neighbour(x):
    return x-100+200*rand()

  def pAcceptance(e, en, t):
    p=exp((e-en)/t)
    return p
 
  # Initial state and energy
  s=randi(-1000,1000)
  e=energy(s)

  # Initial best state and energy
  sb=s;
  eb=e;

  k=1 # Initial temperature
  kmax=2000
  emax=40
  say(sb)

  while (k<kmax): 
    sn=neighbour(sb)
    en=energy(sn)
    t=k/kmax
  #  print t
    if en<eb:
      say('!')
      sb=sn
      eb=en

    if en<e:
      s=sn
      e=en
      say('+')
  
    elif pAcceptance(e, en, t)>rand():
      s=sn
      e=en
      say('?')
  
    say('.')
    k=k+1
    if k%50==0: say('\n'), say(sb)
if __name__=='main':
  simulatedAnnealing()
