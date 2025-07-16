
# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def  lowerbound(self,nums,target):
        n= len(nums)
        l = 0
        r = n-1
        ans = n
        
        while l<=r:
            mid = (l+r)//2

            if nums[mid] >= target:   
                ans = mid 
                r = mid - 1
            else:
                # right 
                l = mid + 1    
        return ans       

    def  upperbound(self,nums,target):
        n= len(nums)
        l = 0
        r = n-1
        ans = n
        
        while l<=r:
            mid = (l+r)//2

            if nums[mid] >target:
                ans = mid 
                r = mid - 1
            else:
                # right 
                l = mid + 1    
        return ans       

    def searchRange(self, nums,target):
        lb = self.lowerbound(nums,target)
        ub = self.upperbound(nums,target)

        if lb ==ub:
            # not persent Element 
            return [-1,-1]
        else:
            return [lb,ub-1]    

s = Solution()
print(s.searchRange([5,7,7,8,8,10], target = 8))
print(s.searchRange([5,7,7,8,8,10], target = 6))
print(s.searchRange([], target = 0))


