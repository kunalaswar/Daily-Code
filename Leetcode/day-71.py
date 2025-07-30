
# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed,n):
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_l = (i==0) or (flowerbed[i-1]==0)
                empty_r = (i==len(flowerbed) - 1) or (flowerbed[i + 1]==0)

                if empty_l and empty_r:
                    flowerbed[i] = 1
                    count +=1
                    if count >=n:
                        return True
                    
        return count>=n

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], n = 1))
print(s.canPlaceFlowers([1,0,0,0,1], n = 2))

        
