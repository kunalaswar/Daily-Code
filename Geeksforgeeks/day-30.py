#  First 1 in a Sorted Binary Array

class Solution:
    def firstIndex(self, arr):
                for i in range(len(arr)):
                 if arr[i] == 1:
                  return i
                
                return -1

sol = Solution()
print(sol.firstIndex([0, 0, 0, 0, 0, 0, 1, 1, 1, 1]))
print(sol.firstIndex([0, 0, 0, 0])) 

