# Array End Insert

# Given an array arr that is not completely filled and a value val, you have to insert the value at the end of the array.

# Examples :
# Input: arr[] = [1, 2, 3, 4, 5], val = 90
# Output: [1, 2, 3, 4, 5, 90]
# Explanation: After inserting 90 at the end, we have array elements as 1 2 3 4 5 90.
# Input: arr[] = [1, 2, 3], val = 50
# Output: [1, 2, 3, 50]
# Explanation: After inserting 50 at the end, we have array elements as 1 2 3 50.

def insertAtEnd(arr, val):
    arr[len(arr):] = [val]
    return arr

print(insertAtEnd([1, 2, 3, 4, 5], val = 90))   

# 
def insertAtEnd(arr, val):
    arr.append(val)
    return arr

print(insertAtEnd([1, 2, 3, 4, 5], val = 90))    