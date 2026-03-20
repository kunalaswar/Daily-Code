 # Missing And Repeating
#  Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.

# Examples:
# Input: arr[] = [2, 2]
# Output: [2, 1]
# Explanation: Repeating number is 2 and the missing number is 1.
# Input: arr[] = [1, 3, 3] 
# Output: [3, 2]
# Explanation: Repeating number is 3 and the missing number is 2.
# Input: arr[] = [4, 3, 6, 2, 1, 1]
# Output: [1, 5]
# Explanation: Repeating number is 1 and the missing number is 5.


# def findTwoElement(arr):
#     n = len(arr)
#     freq = {}
#     for i in range(1,n+1):
#         # missing 
#         if i not in arr:
#             missing = i 
#         # repeating
#     for val in arr:
#         if val not in freq:
#             freq[val] = 1
#         else:
#             freq[val] += 1
#     for val in freq:
#         if freq[val] > 1:
#             duplicate = val        
#     return [duplicate,missing]
    
    
# print(findTwoElement([2, 2]))    
    
    

def findTwoElement(arr):
    n = len(arr)
    freq = {}

    # count frequency
    for val in arr:
        freq[val] = freq.get(val, 0) + 1

    # find missing and duplicate
    for i in range(1, n+1):
        if i not in freq:
            missing = i
        if freq.get(i, 0) > 1:
            duplicate = i

    return [duplicate, missing]  
    
print(findTwoElement([2,2]))    

    
        

