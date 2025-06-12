
class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index]) 
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]    
    
s = Solution()    
res = s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(res)

s = Solution()    
res = s.findDisappearedNumbers([1,1])
print(res)
