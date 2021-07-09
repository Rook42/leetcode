from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # idea: new array w/ words from end
        # faster method, slightly worse memory use

        # get indexes of all spaces
        spaces = [index for index, char in enumerate(s) if char == " "]

        n = []  # new holder array
        for each in spaces[::-1]:  # working from end, so reverse
            n.extend(s[each::])  # add word to new array
            del s[each::]  # kill word in old array

        if spaces:  # if there were any spaces,
            n.append(n.pop(0))  # move the one now at beginning of n to end
            n.extend(s)  # finish moving
            s.clear()
            s.extend(n)
