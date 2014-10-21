"""
ANZEIGEN -> translates to display in German.
It's almost Oktober :)
"""

from __future__ import division

class anzeigen:
  def __init__(self):
        pass
  def pairs(self,lst):
    last = lst[0]
    for i in lst[1:]:
        yield last, i
        last = i  
  def xtile(self,lst, lo=0, hi=1, width=50,
               chops=[0.1 , 0.3, 0.5, 0.7, 0.9],
               marks=["-" , " ", " ", "-", " "],
               bar="|", star="*", show=" %0.3F"):
    """The function _xtile_ takes a list of (possibly)
    unsorted numbers and presents them as a horizontal
    xtile chart (in ascii format). The default is a
    contracted _quintile_ that shows the
    10,30,50,70,90 breaks in the data (but this can be
    changed- see the optional flags of the function).
    """
    def pos(p)   : return ordered[int(len(lst) * p)]
    def place(x) :
      return int(width * float((x - lo)) / (hi - lo+1e-4))
    def pretty(lst) :
      return ', '.join([show % x for x in lst]) #add show % before the 1st x
    ordered = sorted(lst)
    lo = (ordered[0]);
    hi = (ordered[-1]);
    what = [pos(p)   for p in chops]
    where = [place(n) for n in  what]
    out = [" "] * width
    for one, two in self.pairs(where):
      for i in range(one, two):
        out[i] = marks[0]
      marks = marks[1:]
    out[int(width / 2)] = bar
    out[place(pos(0.5))] = star
    return ''.join(out) + "," + pretty(what)
