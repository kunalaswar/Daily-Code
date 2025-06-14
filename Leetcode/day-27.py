
# 575. Distribute Candies

class Solution:
    def distributeCandies(self, candyType):
        # lst = []
        # for i in candyType:
        #     if i not in lst:
        #         lst.append(i)

        lst = set(candyType)
        
        if len(lst)>len(candyType)//2:
            return len(candyType)//2
        else:
            return len(lst)
        
s = Solution()        
print(s.distributeCandies([1,1,2,2,3,3]))
print(s.distributeCandies([1,1,2,3]))
print(s.distributeCandies( [6,6,6,6]))
