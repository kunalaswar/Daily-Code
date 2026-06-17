# Left Smaller Right Greater
# Given an unsorted array arr[], find the first element such that every element to its left is less than or equal to it, and every element to its right is greater than or equal to it.

# Note: If no such element exists, return -1.
# Examples : 
# Input: arr = [4, 2, 5, 7]
# Output: 5
# Explanation: All elements to the left of 5 are less than or equal to 5, and all elements to the right are greater than or equal to 5.
# Input: arr = [11, 9, 12]
# Output: -1
# Explanation: No element in the array satisfies the required condition.

# def findElement(arr):
#     n = len(arr)
#     for i in range(1,n-1):
#         left_ok = True
#         right_ok = True
#         # check left side 
#         for j in range(i):
#             if arr[j] > arr[i]:
#                 left_ok = False 
#                 break 

#         # check right side 
#         for j in range(i+1,n):
#             if arr[j] < arr[i]:
#                 right_ok  = False 
#                 break 

#         if right_ok and left_ok:
#             return arr[i]    

#     return -1 

# print(findElement([4, 2, 5, 7]))
# print(findElement([11, 9, 12]))

#
def findElement(arr):

    n = len(arr)

    leftMax = [0] * n
    rightMin = [0] * n

    leftMax[0] = arr[0]

    for i in range(1, n):

        leftMax[i] = max(leftMax[i-1], arr[i])

        rightMin[n-1] = arr[n-1]

    for i in range(n-2, -1, -1):

        rightMin[i] = min(rightMin[i+1], arr[i])

    for i in range(1, n-1):

        if arr[i] >= leftMax[i-1] and arr[i] <= rightMin[i+1]:

            return arr[i]

    return -1
        
print(findElement([4, 2, 5, 7]))
print(findElement([11, 9, 12]))      