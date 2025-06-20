
# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums):
       lst = []
       for i in nums:
        count = 0
        for j in nums:

            if j<i:
                count = count+1
        lst.append(count)
       return lst 
s = Solution()  
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))

    