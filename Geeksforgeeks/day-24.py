
# Multiply left and right array sum

class Solution:
    def multiply(self, arr):
        # Code here
        start = 0
        end = len(arr)
        while(start<=end):
            n= len(arr)
            mid = n//2
            left = arr[:mid]
            right  = arr[mid:]
            sum_left = sum(left)
            sum_right = sum(right)
            return sum_left * sum_right
        

sol = Solution()
print(sol.multiply([1, 2, 3, 4]))      
print(sol.multiply([1, 2, 3, 4, 5]))
