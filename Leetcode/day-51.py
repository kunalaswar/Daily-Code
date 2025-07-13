
# 912. Sort an Array

import heapq
class Solution:
    def sortArray(self, nums):

  
        heapq.heapify(nums)  
        result = []
        while nums:
            result.append(heapq.heappop(nums))
        return result


s = Solution()
print(s.sortArray([5,2,3,1]))
print(s.sortArray([5,1,1,2,0,0]))

# OR

#^ 912. Sort an Array
# class Solution:
#     def merge(self,arr,l,mid,r):
#         a = []
#         b = []
#         for i in range(l,mid+1):
#             a.append(arr[i])

#         for i in range(mid+1,r+1):
#             b.append(arr[i])

#         i,j,k = 0,0,l
#         while k<=r:
#             if j== len(b):
#                 arr[k] = a[i]
#                 i+=1
#                 k+=1
#             elif i==len(a):
#                 j+=1
#                 k+=1
#             elif a[i]<b[j]:
#                 arr[k] = a[i]
#                 i+=1
#                 k+=1
#             else:
#                 arr[k] = b[j]
#                 j+=1
#                 k+=1

#     def mergeSort(self,nums,l,r):
#         # Base Case
#         if l>=r:
#             return 
#         # recursive Case
#         mid = (l+r)//2
#         # l to mid
#         self.mergeSort(nums,l,mid)
#         # mid to r
#         self.mergeSort(nums,mid+1,r)

#         self.merge(nums,l,mid,r)
        
#     def sortArray(self,nums):
#         self.mergeSort(nums,0,len(nums)-1)

#         return nums
        






