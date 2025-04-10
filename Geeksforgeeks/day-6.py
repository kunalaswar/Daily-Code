# Sorted Array Search
# Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.


# class Solution:
    
#     def searchInSorted(self,arr, k):
#         lst = [val for val in arr ]
        
#         arr.sort()
#         if k in arr:
#             return True
#         return False   


# arr1 = [1, 2, 3, 4, 6]
# s = Solution()        
# res = s.searchInSorted(arr1,k=6)
# print(res)

#  

# def is_present_binary_search(arr, k):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == k:
#             return True
#         elif arr[mid] < k:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return False


# arr1 = [1, 2, 3, 4, 6]      
# s = is_present_binary_search(arr1,k = 6)
# print(s)
