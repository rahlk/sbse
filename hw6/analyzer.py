from __future__ import division
from a12 import a12

class analyser:
  def __init__(self,less=True):
    self.old=[];
    self.new=[];
    self.less=less;
  def addtolog(self, old, new):
    O = self.old
    O.append(old)
    N = self.new
    N.append(new)
    return O, N
  def bettered(self, new, old):
    roundoff=lambda n: round(n,2)
    def quartiles(lst):
      def p(x) : return int(100*roundoff(lst[x]))
      n  = int(len(lst)*0.25)
      return p(n) , p(2*n) , p(3*n)
    def betterifless():
      p1, median1, p3= quartiles(new)
      IQR1=p3-p1
      p1, median2, p3= quartiles(old)
      IQR2=p3-p1
      return median1<median2, IQR1<IQR2
    def betterifmore():
      p1, median1, p3= quartiles(new)
      IQR1=p3-p1
      p1, median2, p3= quartiles(old)
      IQR2=p3-p1
      return median1>median2, IQR1>IQR2
    def same(): return a12(new, old)<=0.56
    if self.less:
      betterMedian, betterIQR = betterifless()
      return betterMedian, betterIQR, same()
    else:
      betterMedian, betterIQR = betterifmore()
      return betterMedian, betterIQR, same()
  def isItGettinBetter(self, lst):
    self.old, self.new = self.addtolog(lst[0:49], lst[50:])
    out = False
    for old, new in zip(self.old, self.new):
      betterMedian, betterIQR, same = self.bettered(new, old)
      if ((same and not betterIQR) or (not same and not betterMedian)): out=False
      elif(not same and betterMedian): out=out or False
    return out