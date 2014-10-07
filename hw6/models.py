"""
A models file that can be imported to run optimizers
"""
from __future__ import division
import sys, types
import math, random, numpy as np, scipy as sp
sys.dont_write_bytecode = False
# Define some aliases.
rand=random.uniform
randi=random.randint
exp=math.e
sin=math.sin 
sqrt=math.sqrt
pi=math.pi

class modelBasics(object):
  def __init__(i,model):
    i.model=model()
    i.name=model.__name__
  def do_a_randJump(i, e, en, t, k):
    p=exp**(-(e-en)/(t**k))<rand(0,1)
    return p
  def simpleneighbour(self,x,xmax,xmin):
      return xmin+(xmax-xmin)*rand(0,1)
  def neighbour(i,x,xmax,xmin):
    def __new(x,z):
        return xmin+(xmax-xmin)*rand(0,1) if rand(0,1)<1/(i.model.indepSize) \
          else x[z] 
    x_new=[__new(x,z) for z in xrange(i.model.indepSize)]
    return x_new
  def energy(i,x,emax,emin):
    ener=i.model.score(x);
    e_norm= abs((ener-emin)/(emax-emin))
    return e_norm
  def baselining(i,model):
    emax=0;emin=0;
    indepSize=i.model.indepSize;
    for _ in xrange(int(1e3)):
      x_tmp=[rand(i.model.baselo,i.model.basehi) for _ in xrange(indepSize)]
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

  def __init__(i,hi=100,lo=-100, basehi=1000, baselo=-1000, kooling=0.7, 
               indepSize=1, thresh=1e-2, iterations=2000):
    i.hi, i.lo, i.basehi, i.baselo, i.kooling, i.indepSize, i.thresh, i.iterations= \
    hi, lo, basehi, baselo, kooling, indepSize, thresh, iterations
    random.seed()
  def f1(i,x):
    return x*x
  def f2(i,x):
    return (x-2)**2
  def score(i,x):
    from compiler.ast import flatten
    flatten = lambda x: x if not isinstance(x, list) else x[0]
    return i.f1(flatten(x))+i.f2(flatten(x))
  def eigenschaften(i):
    return i.hi, i.lo, i.kooling, i.indepSize, i.thresh, i.iterations
    
class Kursawe(object):
  def __init__(i,hi=5,lo=-5,kooling=0.6, a=0.8, b=3, indepSize=3, basehi=1000, 
               baselo=-1000, thresh=1e-2, iterations=2000):
    i.hi, i.lo, i.basehi, i.baselo, i.kooling = hi, lo, basehi, baselo, kooling
    i.a, i.b, i.indepSize, i.thresh, i.iterations= a, b, indepSize, thresh, iterations
    random.seed()
  def f1(i,x):
    return np.sum([-10*exp**(-0.2*sqrt(x[z]**2+x[z+1]**2)) \
                   for z in xrange(i.indepSize-1)])
  def f2(i,x):
    return np.sum([abs(x[z])**i.a+5*sin(x[z]**i.b) \
                   for z in xrange(i.indepSize)])
  def score(i,x):
    return i.f1(x)+i.f2(x)
  def eigenschaften(i):
    return i.hi, i.lo, i.kooling, i.indepSize, i.thresh, i.iterations
    
class Fonseca(object):
  def __init__(i,hi=4,lo=-4, basehi=5, baselo=-5, kooling=1.99, indepSize=3, 
               thresh=1e-2, iterations=2000):
    i.hi, i.lo, i.basehi, i.baselo, i.kooling, i.indepSize, i.thresh, i.iterations= \
    hi, lo, basehi, baselo, kooling, indepSize, thresh, iterations
    random.seed()
  def f1(i,x):
    return (1-exp**np.sum([(x[z]-1/((i.indepSize)**0.5)) \
                           for z in xrange(i.indepSize)]))
  def f2(i,x):
    return (1-exp**np.sum([(x[z]+1/((i.indepSize)**0.5)) \
                           for z in xrange(i.indepSize)]))
  def score(i,x):
    return i.f1(x)-i.f2(x)
  def eigenschaften(i):
    return i.hi, i.lo, i.kooling, i.indepSize, i.thresh, i.iterations
    
class ZDT1(object):
  def __init__(i,hi=1,lo=0, basehi=1, baselo=0, kooling=7e-3, indepSize=30, 
               thresh=1e-2, iterations=2000):
    i.hi, i.lo, i.basehi, i.baselo= hi, lo, basehi, baselo 
    i.kooling, i.indepSize, i.thresh, i.iterations= kooling, indepSize, thresh, iterations
    random.seed()
  def f1(i,x):
    return x[0]
  def g(i,x):
    return (1+9*(np.sum(x[1:]))/(i.indepSize-1))
  def f2(i,x):
    return i.g(x)*(1-sqrt(x[0]/i.g(x)))
  def score(i,x):
    return (i.f1(x)-i.f2(x))
  def eigenschaften(i): # German for features
    return i.hi, i.lo, i.kooling, i.indepSize, i.thresh, i.iterations
  
class ZDT3(object):
  def __init__(i,hi=1,lo=0, basehi=1, baselo=0, kooling=7e-3, indepSize=30, 
               thresh=1e-2, iterations=2000):
    i.hi, i.lo, i.basehi, i.baselo = hi, lo, basehi, baselo 
    i.kooling, i.indepSize, i.thresh, i.iterations = kooling, indepSize, iterations
    random.seed()
  def f1(i,x):
    return x[0]
  def g(i,x):
    return (1+9*(np.sum(x[1:]))/(i.indepSize-1))
  def f2(i,x):
    return i.g(x)*(1-(x[0]/i.g(x))**0.5-(x[0]/i.g(x))*sin(10*math.pi*x[0]))
  def score(i,x):
    return (i.f1(x)-i.f2(x))
  def eigenschaften(i): # German for features
    return i.hi, i.lo, i.kooling, i.indepSize, i.thresh, i.iterations


class Viennet3(object):
  def __init__(i,hi=1,lo=0, basehi=1, baselo=0, kooling=7e-3, indepSize=2, 
               thresh=1e-2, iterations=2000):
    i.hi, i.lo, i.basehi, i.baselo =  hi, lo, basehi, baselo
    i.kooling, i.indepSize, i.thresh, i.iterations= kooling, indepSize, thresh,
    iterations 
    random.seed()
  def f1(i,x):
    return 0.5*x[0]**2+x[1]**2+sin(x[0]**2+x[1]**2)
  def f2(i,x):
    return (3*x[0]-2*x[1]+4)**2/8+(x[0]-x[1]+1)**2/27+15
  def f3(i,x):
    return 1/(x[0]**2+x[1]**2+1)-1.1*exp**(-x[0]**2-x[1]**2)
  def score(i,x):
    return (i.f1(x)-i.f2(x)-i.f3(x))
  def eigenschaften(i): # German for features
    return i.hi, i.lo, i.kooling, i.indepSize, i.thresh, i.iterations

