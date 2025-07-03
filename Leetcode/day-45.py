
#1480. Running Sum of 1d Array
 
class Solution:
    def runningSum(self, nums):
        n = len(nums)
        lst  = []
        lst.append(nums[0])

        for i in range(1,len(nums)):
            x = lst[i-1]+nums[i]
            lst.append(x)

        return lst    
    

s = Solution()    
print(s.runningSum([1,2,3,4]))

print(s.runningSum([1,1,1,1,1]))

print(s.runningSum([3,1,2,10,1]))

