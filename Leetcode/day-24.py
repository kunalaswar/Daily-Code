# 169. Majority Element
class Solution:
    def majorityElement(self, nums):

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        max_count = 0
        majority = None

        for num in count:
            if count[num] > max_count:
                max_count = count[num]
                majority = num

        return majority
           
sol = Solution()

nums = [2, 2, 1, 1, 2, 2]

result = sol.majorityElement(nums)

print(result)            