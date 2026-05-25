# Second Largest

# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:
# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

# def getSecondLargest(arr):
#     firstmax = 0
#     secmax = 0
#     for i in arr:
#         if i > firstmax:
#             firstmax = i
#         elif secmax < i < firstmax:
#             secmax = i
#     return  secmax   

# print(getSecondLargest([12, 35, 35, 10, 34, 1]))
# print(getSecondLargest([10, 5, 10]))
# print(getSecondLargest([10, 10, 10]))  

#

def getSecondLargest( arr):

    firstmax = -1
    secmax = -1
    for i in arr:
        if i > firstmax:
            secmax = firstmax
            firstmax = i
        elif secmax < i < firstmax:
            secmax = i
    return secmax
       
print(getSecondLargest([12, 35, 35, 10, 34, 1]))
print(getSecondLargest([10, 5, 10]))
print(getSecondLargest([10, 10, 10]))   
      