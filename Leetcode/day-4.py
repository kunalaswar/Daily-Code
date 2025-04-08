
# 27. Remove Element:

# class solution:
        
#     def removeElement(nums,val):
#         lst = []  
#         nums[:] = [x for x in nums if x !=val]
#         return len(nums)
# s = solution()
# print(s.removeElement( [3, 2, 2, 3],3))


# def removeElement(nums, val):
#     nums[:] = list(filter(lambda x: x != val, nums))
#     return len(nums)

# print(removeElement([3, 2, 2, 3], 3))  # Output: 2

