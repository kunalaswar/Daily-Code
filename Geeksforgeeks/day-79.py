
# # At Least K Occurrences

# class Solution:
#     def firstElementKTime(self, arr,k):
#         count = {}  
#         for num in arr:
#             if num in count:
#                 count[num] += 1
#             else:
#                 count[num] = 1

#             if count[num] == k:
#                 return num  
#         return -1  


# s = Solution()        
# print(s.firstElementKTime([1, 7, 4, 3, 4, 8, 7], k = 2))

# print(s.firstElementKTime([3, 1, 3, 4, 5, 1, 3, 3, 5, 4], k = 3))
    
# print(s.firstElementKTime([10, 8, 2], k = 10))
