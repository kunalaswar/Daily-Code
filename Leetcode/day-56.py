
#  905. Sort Array By Parity

class Solution:
    def sortArrayByParity(self, nums):
           # start = 0
        lst = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                lst.append(nums[i])
                
        for i in range(len(nums)):
            if  nums[i]%2!=0:   
                lst.append(nums[i])
        return lst

s = Solution()        
print(s.sortArrayByParity([3,1,2,4]))

print(s.sortArrayByParity([0]))
