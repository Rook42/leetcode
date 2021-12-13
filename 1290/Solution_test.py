import pytest
from Solution import Solution as S, ListNode as l


class TestSolution:

    s = S()

    def test_solutionCase1(self):
        input = l.ListNode(self, [1, 0, 1])
        output = 5
        assert output == self.s.getDecimalValue(input)

    def test_solutionCase2(self):
        input = l.ListNode(self, [0])
        output = 0
        assert output == self.s.getDecimalValue(input)

    def test_solutionCase3(self):
        input = l.ListNode(self, [1])
        output = 1
        assert output == self.s.getDecimalValue(input)

    def test_solutionCase4(self):
        input = l.ListNode(
            self, [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        output = 18880
        assert output == self.s.getDecimalValue(input)

    def test_solutionCase5(self):
        input = l.ListNode(self, [0, 0])
        output = 0
        assert output == self.s.getDecimalValue(input)
