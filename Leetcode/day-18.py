
#283. Move Zeroes
# Note that you must do this in-place without making a copy of the array.
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


# class Solution:
#     def moveZeroes(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         for val in nums:
#             if val ==0:
#                 nums.remove(val)
#                 nums.append(val)
#         return nums        

# s = Solution()
# res = s.moveZeroes([0,1,0,3,12])
# print(res)

#OR


# def moveZeroes(nums):
#     for val in nums[:]:
#         print(val)
#         if val == 0 :
#             nums.append(0)
#             nums.remove(0)
#     return nums

# nums = [int(i) for i in input("Enter a List of value :").split()]        
# res = moveZeroes(nums)
# print(res)


#* OR
def moveZeros(nums):
    number_zeros = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[number_zeros] =nums[i]
            number_zeros = number_zeros+1
    for i in range(number_zeros,len(nums)):
        nums[i] = 0
    return nums

nums =  [int(i) for i in input("Enter List Of Values : ").split()]
res = moveZeros(nums)
print(res)




