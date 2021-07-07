from solution import Solution

class TestSolution:
  def test_one(self):
    s = Solution()
    assert 1 == s.minSetSize(arr=[1,9])