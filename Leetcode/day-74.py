
# 1089. Duplicate Zeros
class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        
        n = len(arr)  
        i = 0         
        while i < n:
            if arr[i] == 0:                
                for j in range(n - 1, i, -1):
                    arr[j] = arr[j - 1]
                i += 1                     
            i += 1                        
        
s = Solution()
arr1 = [1,0,2,3,0,4,5,0]
s.duplicateZeros(arr1)
print(arr1)
arr2 = [1,2,3]
s.duplicateZeros(arr2)
print(arr2)