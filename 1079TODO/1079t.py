from solution import Solution

class TestSolution:
  def test_one(self):
    s = Solution()
    assert 8 == s.numTilePossibilities("AAB")

  def test_two(self):
    s = Solution()
    assert 188 == s.numTilePossibilities("AAABBC")

  def test_three(self):
    s = Solution()
    assert 1 == s.numTilePossibilities("V")

  def test_four(self):
    s = Solution()
    assert 4 == s.numTilePossibilities("AB")

  def test_five(self):
    s = Solution()
    assert 18 == s.numTilePossibilities("AABB")

  def test_permutation(self):
    s = Solution()
    assert 120 == s.getPermutation(5)