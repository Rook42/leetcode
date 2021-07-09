from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #just do it the stupid way
        arr = []
        for each in matrix:
            arr += each
        arr.sort()
        return arr[k - 1]



