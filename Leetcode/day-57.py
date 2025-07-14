# 75. Sort Colors

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        i = 0

        while i<=right:
            if nums[i]==1:
                i +=1
            elif nums[i]==0:
                nums[i],nums[left] = nums[left],nums[i]
                i+=1
                left+=1
            else:
                nums[i],nums[right] = nums[right],nums[i]
            # i+=1
                right-=1
        return nums
s = Solution()                
print(s.sortColors([2,0,2,1,1,0]))
print(s.sortColors([2,0,1]))


# OR 