class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
      out = 0
      tileSet = list(set(tiles))
      tileCount = {}
      for each in tileSet:
        tileCount.update({each: tiles.count(each)})

      #permutations w/ dups: n! / ex.AA=2!BBB=3!
      allCombinations = len(tiles)
      counter = 1 
      while counter < len(tiles):
        allCombinations += self.getPermutation(len(tiles))
        counter += 1
      dupCombinations = 1
      for each in tileCount:
        dupCombinations *= self.getPermutation(tileCount[each])
      out = (allCombinations / dupCombinations)
      return out
      
    def getPermutation(self, num):
      if num <= 1:
        out = num
      else:
        out = num * self.getPermutation(num - 1)
      return out