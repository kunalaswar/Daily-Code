# Max Value Permutation
# Given an array arr[] of integers, rearrange its elements in any order to maximize the value of:

# Σ(arr[i] × i), where 0 ≤ i < n
# Return the maximum possible value .

# Examples:
# Input: arr[] = [5, 3, 2, 4, 1]
# Output: 40
# Explanation: If we arrange the array as [1, 2, 3, 4, 5] then we can see that the minimum index will multiply with minimum number and maximum index will multiply with maximum number. So, 1*0 + 2*1 + 3*2 + 4*3 + 5*4 = 0+2+6+12+20 = 40 mod(109+7) = 40
# Input: arr[] = [1, 2, 3]
# Output: 8 
# Explanation: If we arrange the array as [1, 2, 3], then the minimum index will multiply with the minimum number and the maximum index will multiply with the maximum number: 1*0 + 2*1 + 3*2 = 0 + 2 + 6 = 8 mod(109+7) = 8.
# Input: arr[] = [7, 7, 7, 7]
# Output: 42
# Explanation: Each element is 7. The sum becomes: 7 ∗ 0 + 7 ∗ 1 + 7 ∗ 2 + 7 ∗ 3 = 0 + 7 + 14 + 21 = 42 

# class Solution:
#     def maxValue(self, arr): 
#         arr.sort()
#         add = 0

        
#         for i in range(len(arr)):
#             # print(i)
#             add += arr[i]* i
#         return add   

# s = Solution()        
# print(s.maxValue([5, 3, 2, 4, 1]))
# print(s.maxValue([1, 2, 3]))
# print(s.maxValue([7, 7, 7, 7]))
        
# 
class Solution:
    def maxValue(self, arr):
        n = len(arr)
        # bubble sort
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        # calculate answer
        total = 0
        for i in range(n):
            total += arr[i] * i
        return total      

s = Solution()        
print(s.maxValue([5, 3, 2, 4, 1]))
print(s.maxValue([1, 2, 3]))
print(s.maxValue([7, 7, 7, 7]))