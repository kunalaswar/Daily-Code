
# Multiply Array


class Solution:
    def longest(self, arr, n):
        pr = 1
        for i in arr:
            pr *= i
        return pr    
    
s = Solution()    
print(s.longest([1, 2, 3, 4, 5], 5)) 
print(s.longest([
5,5,5,5,5,5,5,5,5,5],10))

                