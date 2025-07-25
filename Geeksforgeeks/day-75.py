
#  Check Equal Arrays

class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        
           
        
        freqA = {}
        freqB = {}

        for x in a:
            freqA[x] = freqA.get(x, 0) + 1

        for x in b:
            freqB[x] = freqB.get(x, 0) + 1

        return freqA == freqB

s = Solution()
print(s.checkEqual(a = [1, 2, 5, 4, 0], b = [2, 4, 5, 0, 1]))
print(s.checkEqual(a = [1, 2, 5], b = [2, 4, 15]))
