# Move all negative elements to end
# Given an unsorted array arr[ ] having both negative and positive integers. Place all negative elements at the end of the array without changing the order of positive elements and negative elements.

# Note: Don't return any array, just in-place on the array.

# Examples:
# Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
# Output : [1, 3, 2, 11, 6, -1, -7, -5]
# Explanation: By doing operations we separated the integers without changing the order.
# Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
# Output : [7, 9, 10, 11, -5, -3, -4, -1]


# def segregateElements(arr):
#     pos = []
#     neg = []
#     for i in arr:
#         if i > 0:
#             pos.append(i)
#         else:
#             neg.append(i)

#     # print(pos+neg)
#     return pos+neg

# s = segregateElements([1, -1, 3, 2, -7, -5, 11, 6])
# print(s)

#
def segregateElements(arr):
    pos = []
    neg = []

    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    # modify same array (important)
    arr[:] = pos + neg

segregateElements([1, -1, 3, 2, -7, -5, 11, 6])    



# arr = [-5, 7, -3, -4, 9, 10, -1, 11]
arr = [1, -1, 3, 2, -7, -5, 11, 6]
pos = 0 
for i in range(len(arr)):
    if arr[i]>=0 :
        temp = arr[i]

        j = i 
        while(j>pos):
            arr[j] = arr[j-1]
            j -= 1

        arr[pos] = temp 
        pos += 1 

print(arr)    




