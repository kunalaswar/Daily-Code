
# 594. Longest Harmonious Subsequence
class Solution:
    def findLHS(self, nums):
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
                
        max_length = 0
        for key in dict1:
            if key+1 in dict1:
                max_length = max(max_length, dict1[key] + dict1[key + 1])
        
        return max_length
    
s = Solution()    
print(s.findLHS([1,3,2,2,5,2,3,7]))

print(s.findLHS([1,2,3,4]))
print(s.findLHS([1,1,1,1]))
        
