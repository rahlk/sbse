from searcher import *
from models import *
import sys

for x in [Schaffer, Kursawe, Fonseca, ZDT1]:
  eb=0
  for r in xrange(1):
    print x.__name__, '\n'
    a=sa(x,disp=True)
    k=x()
    hi, lo, kooling, indepSize, iterations = k.getInit()
    print 'min=', lo, ', max=', hi, ', Cooling Factor=', kooling
    eb +=  a.runSearcher()
  
  print eb/20  
  for x in xrange(50): sys.stdout.write('-')
  sys.stdout.write('\n')
  
  
