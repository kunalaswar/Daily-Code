
# Ceil The Floor

#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x,arr):
        floor = -1
        ceil = -1
        for i in arr:
            if i <= x:
                floor = max(floor,i)
            if i >= x:
                if ceil == -1:
                    ceil = i
                else:
                    ceil = min(ceil,i)        
        return [floor,ceil]            
    
s = Solution()    
print(s.getFloorAndCeil(x = 7 , arr = [5, 6, 8, 9, 6, 5, 5, 6]))
print(s.getFloorAndCeil(x = 10 , arr= [5, 6, 8, 8, 6, 5, 5, 6]))


