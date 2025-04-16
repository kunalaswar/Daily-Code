
# Reverse array in groups

class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):
        i = 0
        while(i<len(arr)):
            end = i + k
            arr[i:end] = arr[i:end][::-1]
            i = i+k
            return arr
            
s = Solution()
res = s.reverseInGroups([1,2,3,4,5],3)
print(res)