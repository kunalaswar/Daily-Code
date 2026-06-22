# Remove Duplicates from an array
# Given an array arr[] consisting of positive integers, return the array by removing all duplicate numbers.

# Example:
# Input: arr[] = [2, 2, 3, 3, 7, 5] 
# Output: [2, 3, 7, 5]
# Explanation: After removing the duplicates 2 and 3 we get 2 3 7 5.
# Input: arr[] = [1, 2, 3, 4, 5] 
# Output: [1, 2, 3, 4, 5]
# Explanation: There doesn't exists any duplicate element.

# def remDuplicate(arr):
#     lst = []
#     for val in arr:
#         if val not in lst:
#             lst.append(val)
#     return lst        

# print(remDuplicate([2, 2, 3, 3, 7, 5] ))
# print(remDuplicate( [1, 2, 3, 4, 5] ))

# 
def remDuplicate(arr):
    seen = set()
    ans = []

    for num in arr:

        if num not in seen:

            seen.add(num)
            ans.append(num)

    return ans

print(remDuplicate([2, 2, 3, 3, 7, 5] ))
print(remDuplicate( [1, 2, 3, 4, 5] ))


    