import pytest
import math
def minEatingSpeed(piles, h):
   left = 1
   right  = max(piles)
   while left < right:
       middle = (left + right) // 2
       hours_spend = 0
       for pile in piles:
           hours_spend += math.ceil(pile/middle)

       if hours_spend <= h:
           right = middle

       else:
           left = middle + 1
   return right




def test_minEatingSpeed_1():
    assert 4 == minEatingSpeed([3,6,7,11],8)

def test_minEatingSpeed_2():
    assert 30 == minEatingSpeed([30,11,23,4,20],5)

def test_minEatingSpeed_3():
    assert 23 == minEatingSpeed([30, 11, 23, 4, 20], 6)