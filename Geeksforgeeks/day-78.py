
# Find Kth Rotation

class Solution:
    def findKRotation(self, arr):
        # code here
        left  = 0
        right  = len(arr)-1

        while left <= right:
            if arr[left]<=arr[right]:
                return left
            
            mid = (left+right)//2
            next_ = (mid+1)%len(arr)
            prev  = (mid-1 + len(arr)) %len(arr)

            if arr[mid] <= arr[prev] and arr[mid] <= arr[next_]:
                return mid
            
            if arr[mid]>=arr[left]:
                left = mid + 1
            else:
                right = mid - 1 

        return 0

s = Solution()
print(s.findKRotation([5, 1, 2, 3, 4]))

print(s.findKRotation([1, 2, 3, 4, 5]))


# Using Linear Search 

# class Solution:
#     def findKRotation(self, arr):
#         # code here
        
#         min_index = 0
#         min_value = arr[0]

#         for i in range(1, len(arr)):
#             if arr[i] < min_value:
#                 min_value = arr[i]
#                 min_index = i

#         return min_index
