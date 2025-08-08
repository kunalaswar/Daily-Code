
# 888. Fair Candy Swap

class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        diff = (sumA - sumB) // 2

        setB = set(bobSizes)          
        for a in aliceSizes:          
            b = a - diff              
            if b in setB:
                return [a, b]

s = Solution()
print(s.fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))
print(s.fairCandySwap(aliceSizes = [1,2], bobSizes = [2,3]))
print(s.fairCandySwap(aliceSizes = [2], bobSizes = [1,3]))