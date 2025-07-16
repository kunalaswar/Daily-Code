
# Type of array

class Solution:
    def maxNtype(self , arr):
        #code here.
        n = len(arr)
        asc = 0
        desc = 0

        for i in range(n-1):
            if arr[i]< arr[i+1]:
                asc+=1
            else:
                desc+=1

        if asc == n - 1:
            return 1  # Ascending
        elif desc == n - 1:
            return 2  # Descending
        elif arr[0] > arr[-1]:
            return 4  # Ascending rotated
        else:
            return 3  # Descending rotated
    
s = Solution()
print(s.maxNtype([1, 2, 3, 4, 5]))      # Output: 1 (Ascending)
print(s.maxNtype([5, 4, 3, 2, 1]))      # Output: 2 (Descending)
print(s.maxNtype([3, 4, 5, 1, 2]))      # Output: 4 (Ascending Rotated)
print(s.maxNtype([2, 1, 5, 4, 3]))      # Output: 3 (Descending Rotated)
