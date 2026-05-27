# Third Largest
# Given an array, arr[] of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.

# Examples:
# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The third largest element in the array [2, 4, 1, 3, 5] is 3.
# Input: arr[] = [10, 2]
# Output: -1
# Explanation: There are less than three elements in the array, so the third largest element cannot be determined.
# Input: arr[] = [5, 5, 5]
# Output: 5
# Explanation: In the array [5, 5, 5], the third largest element can be considered 5, as there are no other distinct elements.

#  Use >= when duplicates should also count 
# def thirdLargest(arr):
#     firstmax = -1
#     secmax = -1
#     thirdmax = -1
#     for i in arr:
#         if i > firstmax:
#             thirdmax = secmax
#             secmax = firstmax
#             firstmax = i
#     # return firstmax
#         elif secmax < i < firstmax:
#             thirdmax = secmax
#             secmax = i
#         elif thirdmax < i < secmax:  
#             thirdmax = i
            
#     return thirdmax


# print(thirdLargest([2, 4, 1, 3, 5]))
# print(thirdLargest([10, 2]))


#
def thirdLargest(arr):
    firstmax = -1
    secmax = -1
    thirdmax = -1
    
    for i in arr:    
        # new first maximum
        if i >= firstmax:    
            thirdmax = secmax    
            secmax = firstmax    
            firstmax = i    
        # new second maximum
        elif i >= secmax:    
            thirdmax = secmax    
            secmax = i    
        # new third maximum
        elif i >= thirdmax:    
            thirdmax = i
    
    return thirdmax

print(thirdLargest([2, 4, 1, 3, 5]))
print(thirdLargest([10, 2]))
print(thirdLargest([5, 5, 5]))