
# 35. Search Insert Position
# and not found then insert return the last index number 


class Solution:
    def searchInsert(self,nums,target):
        for i in range(len(nums))     :
            if nums[i] >= target:
                return i
        return len(nums)   

nums = [1,3,5,6]
s = Solution()
print(s.searchInsert(nums,7))


