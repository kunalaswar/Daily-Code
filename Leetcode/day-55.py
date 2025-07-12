
# 80. Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:
            return n
        start = 1
        for i in range(2 ,n):
            # unique Element 
            if nums[i] !=nums[start-1]:
                start = start + 1
                nums[start] = nums[i]

        return start + 1     
    
s  = Solution()    
print(s.removeDuplicates([1,1,1,2,2,3]))
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))
