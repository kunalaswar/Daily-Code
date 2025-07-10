
# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum += nums[i]
        # print(curr_sum)
        # print("-------")
            if curr_sum > max_sum :
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum  = 0

        return max_sum  


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


print(s.maxSubArray([1]))

print(s.maxSubArray([5,4,-1,7,8]))