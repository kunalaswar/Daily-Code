

from collections import Counter
class Solution:
    def intersect(self, nums1,nums2):
        count = Counter(nums1)
        lst = []

        for num in nums2:
            if count[num] > 0:
                lst.append(num)
                count[num] -= 1
        
        return lst         

s = Solution()     
res = s.intersect( [1,2,2,1], [2,2])
print(res)