from __future__ import division
from searcher import *
from models import *
import sys
import numpy as np
from anzeigen import *
from time import gmtime, strftime
import sys, random, math, datetime, time,re
sys.dont_write_bytecode = True


for x in [Schaffer]:
  eb=20*[None]
  for y in [MaxWalkSat]:
    print 'Model: ', x.__name__ 
    print 'Searcher: ', y.__name__ 
    print strftime("%a, %d %b %Y %H:%M:%S ", gmtime()), '\n'
    k=x()
    dspl=anzeigen();
    hi, lo, kooling, indepSize, iterations = k.eigenschaften()
    print 'Searcher settings:'
    print 'min=', lo, ', max=', hi, ', Cooling Factor=', kooling, '\n'
    for r in xrange(20):
      a=y(x,disp=False)
      eb[r] =  a.runSearcher()
    #print xtile(eb)
    print 'Energy: ', np.sum(eb)/20
    print dspl.xtile(eb, lo=lo, hi=hi)
  #for x in xrange(50): sys.stdout.write('-')
  
  sys.stdout.write('\n')