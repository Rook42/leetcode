class Solution:
    def romanToInt(self, s: str) -> int:
        out = 0
        for i in range(len(s)):
            val = self.map[s[i]]
            if len(s) > i + 1:
                if self.map[s[i + 1]] > val:
                    out -= val
                else:
                    out += val
            else:
                out += val

        return out

    def __init__(self):
        self.map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
