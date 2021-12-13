import pytest
import Solution as S

s = S.Solution()


class Test_Solution:

    def test_case1(self):
        input = "leetcode"
        assert s.maxPower(input) == 2

    def test_case2(self):
        input = "abbcccddddeeeeedcba"
        assert s.maxPower(input) == 5

    def test_case3(self):
        input = "triplepillooooow"
        assert s.maxPower(input) == 5

    def test_case4(self):
        input = "hooraaaaaaaaaaay"
        assert s.maxPower(input) == 11

    def test_case5(self):
        input = "tourist"
        assert s.maxPower(input) == 1
