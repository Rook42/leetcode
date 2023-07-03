import pytest
from solution import Solution


class TestSolution:
    def test_one(self):
        s = Solution()
        assert 1 == s.romanToInt("I")

    def test_two(self):
        s = Solution()
        assert 2 == s.romanToInt("II")

    def test_three(self):
        s = Solution()
        assert 4 == s.romanToInt("IV")

    def test_four(self):
        s = Solution()
        assert 3 == s.romanToInt("III")

    def test_five(self):
        s = Solution()
        assert 58 == s.romanToInt("LVIII")

    def test_six(self):
        s = Solution()
        assert 1994 == s.romanToInt("MCMXCIV")
