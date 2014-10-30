"""
rDiv Demo
"""

import sk
import random

rand=random.uniform
randi=random.randint

rdivDemo=sk.rdivDemo

Range1=[rand(0,4) for _ in xrange(5)]; Range1.insert(0,'Range1')
Range2=[rand(3,13) for _ in xrange(5)]; Range2.insert(0,'Range2')
Range3=[rand(7,17) for _ in xrange(5)]; Range3.insert(0,'Range3')
Range4=[rand(10,27) for _ in xrange(5)]; Range4.insert(0,'Range4')
Range5=[rand(12,30) for _ in xrange(5)]; Range5.insert(0,'Range5')
Range6=[rand(30,50) for _ in xrange(5)]; Range6.insert(0,'Range6')


def _rdiv():
  rdivDemo([
            Range1,
            Range2,
            Range3,
            Range4,
            Range5,
            Range6,
            ])
_rdiv()