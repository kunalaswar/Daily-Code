# Product array puzzle
# Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[].
# Note: Each element is res[] lies inside the 32-bit integer range.

# Examples:
# Input: arr[] = [10, 3, 5, 6, 2]
# Output: [180, 600, 360, 300, 900]
# Explanation: For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
# For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
# For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
# For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
# For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.
# Input: arr[] = [12, 0]
# Output: [0, 12]
# Explanation: For i = 0, res[i] is 0.
# For i = 1, res[i] is 12.

# class Solution:
#     def productExceptSelf(self, arr):
#         lst = []
#         for i in range(len(arr)):
#             # print(i)
#             product = 1
#             for j in range(len(arr)):
#                 if i ==j:
#                     continue
#                 else:

#                     product *= arr[j]
#             lst.append(product)     
#         return lst              
        


# s = Solution()        
# print(s.productExceptSelf([10, 3, 5, 6, 2]))
# print(s.productExceptSelf([12, 0]))

#
# class Solution:
#     def productExceptSelf(self, arr):
#         lst = []
#         total_product = 1
#         for i in range(len(arr)):
#             total_product = total_product * arr[i]
#         # print(total_product)
#         for i in range(len(arr)):
#             answer = total_product // arr[i]
#             lst.append(answer)

#         return lst    
        
# s = Solution()        
# print(s.productExceptSelf([10, 3, 5, 6, 2]))
# print(s.productExceptSelf([12, 0])) 

#
class Solution:
    def productExceptSelf(self, arr):

        lst = []
        total_product = 1
        zero_count = 0

        # count zeros and product of non-zero numbers
        for num in arr:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num

        # if more than one zero
        if zero_count > 1:
            return [0] * len(arr)

        # build answer
        for num in arr:
            # one zero case
            if zero_count == 1:
                if num == 0:
                    lst.append(total_product)
                else:
                    lst.append(0)

            # no zero case
            else:
                lst.append(total_product // num)
        return lst

        
s = Solution()        
print(s.productExceptSelf([10, 3, 5, 6, 2]))
print(s.productExceptSelf([12, 0]))  
