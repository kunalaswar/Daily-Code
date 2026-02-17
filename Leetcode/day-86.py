# 27. Remove Element
class Solution:
    def removeElement(self, nums , val):
        k = 0   # count of elements not equal to val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
    
s = Solution()    
print(s.removeElement(nums = [3,2,2,3],val=3))
