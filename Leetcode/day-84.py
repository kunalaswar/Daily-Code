
 # 1. Two Sum
class Solution:
    def twoSum(self, nums: list[int], target):
        prevMap = {} 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

sol = Solution()
my_nums = [2, 7, 11, 15]
my_target = 9
result = sol.twoSum(my_nums, my_target)
print(f"The indices are: {result}")
