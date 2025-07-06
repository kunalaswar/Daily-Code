
# Peak element

class Solution:   
    def peakElement(self,arr):
        # Code here
        left = 0
        right = len(arr)-1
        while(left < right):
            mid = left +(right-left)//2
            if arr[mid]>arr[mid+1]:
                right = mid

            else:

                left = mid +1 

        return right   # Or left   
                

s = Solution()                
print(s.peakElement( [1, 2, 4, 5, 7, 8, 3]))
print(s.peakElement([10, 20, 15, 2, 23, 90, 80]))
print(s.peakElement([1, 2, 3]))
