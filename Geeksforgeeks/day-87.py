# Two sum -Pairs with 0 Sum
# Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.
# Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

# Examples:
# Input: arr = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, 1]]
# Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
# arr[2] + arr[4] = 1 + (-1) = 0.
# The distinct pair are [-1,1].
# Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# Output: [[-6, 6],[-1, 1]]
# Explanation: The distinct pairs are [-1, 1] and [-6, 6].

# def getPairs(arr):
#     result = set()
#     for i in range(len(arr)):        
#         for j in range(len(arr)):
#             if i != j and arr[i] + arr[j]==0:
#                 if arr[i]<arr[j]:
#                     pair = (arr[i],arr[j])
#                 else:
#                     pair = (arr[j],arr[i])    
#                 result.add(pair)  
#     res = [list(p) for p in result]
#     res.sort()
#     return res
                 
# print(getPairs([-1, 0, 1, 2, -1, -4]) )
    
class Solution:
    def getPairs(self, arr):
        seen = set()
        result = set()

        for num in arr:
            if -num in seen:
                if num < -num:
                    pair = (num, -num)
                else:
                    pair = (-num, num)
                result.add(pair)

            seen.add(num)        
        res = [list(p) for p in result]
        res.sort()
        return res            

s = Solution()             
print(s.getPairs([-1, 0, 1, 2, -1, -4]) )
print(s.getPairs([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))

    
