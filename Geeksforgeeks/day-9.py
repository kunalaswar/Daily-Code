
#Sum of Array

class Solution:
    def arraySum(self, arr):
        total = 0
        for num in arr:
            total += num  
        return total
    

obj = Solution()
result = obj.arraySum([1, 2, 3, 4])
print(result)  # Output: 10
