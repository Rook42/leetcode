import pytest
from Solution import Solution


class TestSolution:

    s = Solution()

    def test_case_1(self):
        input = [1, 2, 3, 1]
        expected = 4
        assert self.s.rob(input) == expected

    def test_case_2(self):
        input = [2, 7, 9, 3, 1]
        expected = 12
        assert self.s.rob(input) == expected
