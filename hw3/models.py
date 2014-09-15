"""
A models file that can be imported to run optimizers
"""
from __future__ import division
import sys
import math, random, numpy as np, scipy as sp
sys.dont_write_bytecode = True
# Define some aliases.
rand=random.uniform
randi=random.randint
exp=math.e
sin=math.sin 
sqrt=math.sqrt

class modelBasics(object):
  def __init__(i,model):
    i.model=model()
  def do_a_randJump(self, e, en, t, k):
    p=exp**(-(e-en)/(t**k))<rand(0,1)
    return p
  def neighbour(self,x,xmax,xmin):
    return [xmin+(xmax-xmin)*rand(0,1)]
  def energy(i,x,emax,emin):
    ener=i.model.score(x);
    e_norm= (ener-emin)/(emax-emin)
    return e_norm
  def baselining(i,model):
    emax=0;emin=1;
    indepSize=i.model.indepSize;
    for x in xrange(10000):
      x_tmp=[randi(-1000,1000) for z in xrange(indepSize)]
      ener=i.model.score(x_tmp);
      if ener>emax:
        emax=ener
      elif ener<emin:
        emin=ener
    return emax,emin
  f=open('log_sa_schaffer.txt','w')
  def say(i,x):
    sys.stdout.write(str(x));
    sys.stdout.flush()
      
class Schaffer(object):

  def __init__(i,hi=100,lo=-100,kooling=0.7, indepSize=1, iterations=2000):
    i.hi, i.lo, i.kooling, i.indepSize, i.iterations= hi, lo, kooling, indepSize, iterations
  def f1(i,x):
    return x*x
  def f2(i,x):
    return (x-2)**2
  def score(i,x):
    return i.f1(x[0])+i.f2(x[0])
  def getInit(i):
    return i.hi, i.lo, i.kooling, i.indepSize, i.iterations
    
class Kursawe(object):
  def __init__(i,hi=5,lo=-5,kooling=0.6, a=0.8, b=3, indepSize=3, iterations=2000):
    i.hi, i.lo, i.kooling, i.a, i.b, i.indepSize, i.iterations= hi, lo, kooling, a, b, indepSize, iterations
  def f1(i,x):
    return np.sum([-10*exp**(-0.2*sqrt(x[z]**2+x[z+1]**2)) for z in xrange(i.indepSize-1)])
  def f2(i,x):
    np.sum([abs(x[z])**i.a+5*sin(x[z]**i.b) for z in xrange(i.indepSize)])
  def score(i,x):
    return i.f1(x)+i.f2(x)
  def getInit(i):
    return i.hi, i.lo, i.kooling, i.indepSize, i.iterations
  
    
    

