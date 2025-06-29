
#  674. Longest Continuous Increasing Subsequence


class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        max_count = 1
        count = 1
        for i in range(len(nums)-1):
            if nums[i]< nums[i+1]:
                count = count + 1
                max_count = max(max_count,count) 
           

            else:
                count = 1

        return max_count

s = Solution()    
print(s.findLengthOfLCIS([1,3,5,4,7]))

print(s.findLengthOfLCIS([2,2,2,2,2]))
