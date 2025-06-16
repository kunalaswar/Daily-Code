# User function Template for python3
class Solution:
    def minAnd2ndMin(self, arr):
        n = len(arr)
        if n < 2:
            return [-1]
        
        first = second = float('inf')

        for num in arr:
            if num < first:
                second = first
                first = num
            elif first < num < second:
                second = num

        if second == float('inf'):
            return [-1]
        else:
            return [first, second]

arr = [5, 15, 14, 5, 16, 17, 5, 17, 3, 8, 17, 4, 9]
s = Solution()
print(s.minAnd2ndMin(arr)) 