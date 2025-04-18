
# Alternates in an Array
# You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).


class Solution:
    def getAlternates(self, arr):
        # Code Here
       lst = [arr[i] for i in range(0,len(arr),2)]
       return lst

s = Solution()    
print(s.getAlternates([1,2,3,4]))

