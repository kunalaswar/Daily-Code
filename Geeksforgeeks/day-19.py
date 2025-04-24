
# # Rotating an Array

# class Solution:
#     def leftRotate(self, arr, d):
#         # code
#         n = len(arr)
#         temp = arr[:d]
#         for i in range(n - d):
#             arr[i] = arr[i + d]
#         arr[n - d:] = temp
#         return arr
    

# s = Solution()    
# res = s.leftRotate([-1, -2, -3, 4, 5, 6, 7],2)
# print(res)
