#largest Element in Array
from typing import List

class Solution:
    def largest(self, arr):   
        max_val = arr[0]
        for val in arr:
            if val > max_val:
                max_val = val
        return max_val  
    

s = Solution()
print(s.largest([1, 8, 7, 56, 90]))

    