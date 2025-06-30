
# Sum of distinct elements

class Solution:
    def findSum(self, arr):
        seen = {}
        total = 0
        
        for num in arr:
            if num not in seen:
                seen[num] = True
                total += num
                
        return total


s = Solution()
print(s.findSum([1, 2, 3, 4, 5]))

print(s.findSum([5,5,5,5,5]))