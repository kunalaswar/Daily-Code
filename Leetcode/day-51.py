
# 912. Sort an Array

import heapq
class Solution:
    def sortArray(self, nums):

  
        heapq.heapify(nums)  
        result = []
        while nums:
            result.append(heapq.heappop(nums))
        return result


s = Solution()
print(s.sortArray([5,2,3,1]))
print(s.sortArray([5,1,1,2,0,0]))
