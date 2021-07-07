from typing import List
class Solution:
  def minSetSize(self, arr: List[int]) -> int:
    out = 0
    target = len(arr)/2
    dict = {}
    for each in arr:
      if not each in dict.keys():
        dict[each] = 1
      else:
        dict[each] += 1
    count: List[int] = list(dict.values())
    count.sort(reverse=True)
    sum = 0
    while sum < target:
      sum += count[out]
      out += 1
    return out


