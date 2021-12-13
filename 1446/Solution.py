class Solution:
    def maxPower(self, s: str) -> int:
        oldchar: str = ''
        strcharnum: int = 0
        maxstrcharnum: int = 0
        for char in s:
            if char == oldchar:
                strcharnum += 1
            else:
                oldchar = char
                strcharnum = 1
            if strcharnum > maxstrcharnum:
                maxstrcharnum = strcharnum

        return maxstrcharnum
