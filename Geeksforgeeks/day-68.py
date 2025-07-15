
#
class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        # return freq        
       
        for key, value in freq.items():
            if value % 2 != 0:
                return key
            
                

s = Solution()                
print(s.getOddOccurrence([1, 2, 3, 2, 3, 1, 3]))
print(s.getOddOccurrence([5, 7, 2, 7, 5, 2, 5]))