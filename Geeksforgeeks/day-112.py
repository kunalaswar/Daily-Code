# Find missing in second array

# Given two integer arrays a and b, the task is to find the numbers which are present in the first array a, but not present in the second array b.

# Note: Numbers to be returned should in order as they appear in array a.

# Examples :
# Input: a[] = [1, 2, 3, 4, 5, 10], b[] = [2, 3, 1, 0, 5]
# Output: [4, 10]
# Explanation: 4 and 10 are present in first array, but not in second array.
# Input: a[] = [4, 3, 5, 9, 11], b[] = [4, 9, 3, 11, 10]
# Output: [5]  
# Explanation: Second array does not contain element 5.
# Input: a[] = [9], b[] = [7, 9, 4, 9, 9, 9]
# Output: []  

#User function Template for python3


# class Solution:
#     def findMissing(self,a,b):
#         lst = []
        
#         for val in a:
#             if val not in b:

#                 lst.append(val)
#         return lst    
    

# s = Solution()
# print(s.findMissing([1, 2, 3, 4, 5, 10],[2, 3, 1, 0, 5]))
# print(s.findMissing([4, 3, 5, 9, 11],[4, 9, 3, 11, 10]))
# print(s.findMissing([9], [7, 9, 4, 9, 9, 9]))

# optimized 
class Solution:
    def findMissing(self,a,b):
        lst = []
        b_set = set(b)
        
        for val in a:
            if val not in b_set:

                lst.append(val)
        return lst    
    

s = Solution()
print(s.findMissing([1, 2, 3, 4, 5, 10],[2, 3, 1, 0, 5]))
print(s.findMissing([4, 3, 5, 9, 11],[4, 9, 3, 11, 10]))
print(s.findMissing([9], [7, 9, 4, 9, 9, 9]))

