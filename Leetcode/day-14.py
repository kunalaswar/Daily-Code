# 268. Missing Number

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for val in range(len(nums)+1):
            if val in nums:
                pass
            else:
                return val    
                
s = Solution()                
res = s.missingNumber([3,0,1])
print(res)
