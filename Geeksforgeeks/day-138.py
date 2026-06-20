# Find the closest pair from two arrays
# Given two sorted arrays arr1[] and arr2[] of size n and m and a number x, find the pair whose sum is closest to x and the pair has an element from each array. In the case of multiple closest pairs return any one of them.
# Note : In the driver code, the absolute difference between the sum of the closest pair and x is printed.
# Examples:
# Input : arr1[] = [1, 4, 5, 7], arr2[] = [10, 20, 30, 40], x = 32
# Output : [1, 30]
# Explanation:The closest pair whose sum is closest to 32 is [1, 30] = 31.
# Input : arr1[] = [1, 4, 5, 7], arr2[] = [10, 20, 30, 40], x = 50 
# Output : [7, 40] 
# Explanation: The closest pair whose sum is closest to 50 is [7, 40] = 47.


# def findClosestPair(arr1, arr2, x):
#     min_diff = float('inf')
#     ans = []

#     for i in arr1:
#         for j in arr2:

#             diff = abs(x - (i + j))
#             if diff < min_diff:
#                 min_diff = diff
#                 ans = [i, j]

#     return ans        

# print(findClosestPair([1, 4, 5, 7],[10, 20, 30, 40], x = 32))    
        
#
def findClosestPair(arr1, arr2, x):
    i = 0
    j = len(arr2) - 1
    min_diff = float('inf')
    ans = [0, 0]
    while i < len(arr1) and j >= 0:
        curr_sum = arr1[i] + arr2[j]
        diff = abs(x - curr_sum)

        if diff < min_diff:

            min_diff = diff
            ans = [arr1[i], arr2[j]]

        if curr_sum > x:
            j -= 1
        else:
            i += 1
    return ans

print(findClosestPair([1, 4, 5, 7],[10, 20, 30, 40], x = 32))    
        
        