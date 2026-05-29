 # Minimum Number in a sorted rotated array
# Given an array of distinct elements which was initially sorted. This array may be rotated at some unknown point. The task is to find the minimum element in the given sorted and rotated array. 

# Example 1:
# Input:
# N = 10
# arr[] = {2,3,4,5,6,7,8,9,10,1}
# Output: 1
# Explanation: The array is rotated 
# once anti-clockwise. So minimum 
# element is at last index (n-1) 
# which is 1.
# Example 2:
# Input:
# N = 5
# arr[] = {3,4,5,1,2}
# Output: 1
# Explanation: The array is rotated 
# and the minimum element present is
# at index (n-2) which is 1.
# Your Task:
# The task is to complete the function minNumber() which takes the array arr[] and its starting and ending indices (low and high) as inputs and returns the minimum element in the given sorted and rotated array.


def minNumber(arr,low,high):
    low = 0
    high = len(arr)-1 
    while low < high:

            mid = (low + high) // 2

            if arr[mid] > arr[high]:

                low = mid + 1

            else:

                high = mid

    return arr[low]
print(minNumber( (2,3,4,5,6,7,8,9,10,1),0,9))        
print(minNumber( (3,4,5,1,2),0,4))
