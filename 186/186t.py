from solution import Solution


class TestSolution:
    def test_one(self):
        s = Solution()
        input = [
            "t",
            "h",
            "e",
            " ",
            "s",
            "k",
            "y",
            " ",
            "i",
            "s",
            " ",
            "b",
            "l",
            "u",
            "e",
        ]
        out = [
            "b",
            "l",
            "u",
            "e",
            " ",
            "i",
            "s",
            " ",
            "s",
            "k",
            "y",
            " ",
            "t",
            "h",
            "e",
        ]
        s.reverseWords(input)
        assert input == out

    def test_two(self):
        s = Solution()
        input = ["a"]
        out = ["a"]
        s.reverseWords(input)
        assert input == out
