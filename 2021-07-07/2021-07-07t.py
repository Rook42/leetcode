import pytest

from solution import Solution

from typing import List
class TestSolution:
  s = Solution()
  matrix3: List[List[int]] = [[1,5,9],[10,11,13],[12,13,15]]
  matrix4: List[List[int]] = [[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,6]]
  def test_one(self):
    assert -5 == self.s.kthSmallest(matrix=[[-5]], k=1)

  def test_two(self):
    assert 6 == self.s.kthSmallest(matrix= self.matrix4, k=16)

  def test_three(self):
    assert 13 == self.s.kthSmallest(matrix= self.matrix3, k=8)

  def test_four(self):
    assert 1 == self.s.kthSmallest(matrix=[[1,2],[1,3]], k=1)

  def test_five(self):
    assert 5 == self.s.kthSmallest(matrix=[[1,3,5],[6,7,12],[11,14,14]], k=3)