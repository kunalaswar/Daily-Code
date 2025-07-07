
# 162. Find Peak Element

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left # OR right 

s = Solution()
print(s.findPeakElement([1,2,3,1]))

print(s.findPeakElement([1,2,1,3,5,6,4]))