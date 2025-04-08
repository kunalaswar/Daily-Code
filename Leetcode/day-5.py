
# # 26. Remove Duplicates from Sorted Array
# from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        
#         if not nums: return 0
#         i = 0
#         for j in range(1, len(nums)):
#             if nums[j] != nums[i]:
#                 i += 1
            
#                 nums[i] = nums[j]
#         return i + 1

# s=Solution()    
# result = s.removeDuplicates( [1,1,2])
# print(result)




# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         unique = []
#         for val in nums:
#             if val not in unique:
#                 unique.append(val)
        
#         # Copy back to nums to follow the in-place requirement
#         for i in range(len(unique)):
#             nums[i] = unique[i]
        
#         return len(unique)

# s=Solution()    
# result = s.removeDuplicates( [1,1,2])
# print(result)

