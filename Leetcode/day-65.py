
#  561. Array Partition
class Solution:
   def arrayPairSum(self,nums):
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += min(nums[i], nums[i+1])
        return total
    

s = Solution()    
print(s.arrayPairSum([1,4,3,2]))

print(s.arrayPairSum([6,2,6,5,1,2]))