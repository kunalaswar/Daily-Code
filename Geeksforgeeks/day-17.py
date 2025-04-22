
# Value equal to index value
# Given an array arr. Your task is to find the elements whose value is equal to 
# that of its index value ( Consider 1-based indexing ).

# class Solution:
#     def valueEqualToIndex(self, arr):
#         lst = []
#         for i in range(1,len(arr)):
#             if arr[i]==(i+1):
#                 lst.append(i+1)
#         return lst        
            
# arr = [15, 2, 45, 4 , 7]
# sol = Solution()
# result = sol.valueEqualToIndex(arr)
# print(result)


#OR
# def valueEqualToIndex(arr) :
#     lst = []
#     for i in range(1,len(arr)+1):
#         if arr[i - 1] == i:
#             lst.append(i)
#     return lst

# arr = [15, 2, 45, 4 , 7]       
# print(valueEqualToIndex(arr))

