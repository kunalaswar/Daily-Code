
# 217. Contains Duplicate

# class Solution:
#     def containsDuplicate(self,nums):
#         set1= set()
#         for num in nums:
#             if num in set1:
#                 return True
#             set1.add(num)
#         return False
    
# nums = [int(val) for val in input("Enter value here with space = ").split()]
# s = Solution()  
# res = s.containsDuplicate(nums)  
# print("If any value appears at least twice in the array : ",res)

# OR

# def containDuplicate(nums):
#     d1 = {i:nums.count() for i in nums }
#     if d1 >1:
#         return True
#     else:
#         return False

# res = containDuplicate([1,2,3,4])    
# print(res)

