from searcher import *
from models import *

for x in [Schaffer, Kursawe]:
  a=sa(x)
  print a.runSearcher()
  