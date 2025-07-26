
#First Repeating Element

class Solution:
    def firstRepeated(self,arr):
        # code here 
        element_index = {}
        min_index = float("inf")
        
        for i in range(len(arr)):
                if arr[i] in element_index:
                    min_index = min(min_index,element_index[arr[i]])
                else:
                    element_index[arr[i]] = i
                    
        if min_index == float("inf"):
            return -1
        else:
            return min_index + 1 
        
s = Solution()
print(s.firstRepeated([1, 5, 3, 4, 3, 5, 6]))
print(s.firstRepeated([1, 2, 3, 4]))
