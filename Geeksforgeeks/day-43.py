
# Count of smaller elements

class Solution:
    def countOfElements(self, x, arr):
        # Code Here
        count = 0
        for val in arr:
            if val <=x:
                count = count + 1
        return count        
        
s = Solution()        
res = s.countOfElements(x = 9, arr = [10, 1, 2, 8, 4, 5] )
print(res)

s = Solution()        
res = s.countOfElements( x = 2, arr = [1, 2, 2, 5, 7, 2, 9] )
print(res)

