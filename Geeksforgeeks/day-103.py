# Segregate 0s and 1s
# Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

# Examples :
# Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 0, 0, 1, 1, 1, 1, 1].
# Input: arr[] = [1, 1]
# Output: [1, 1]
# Explanation: There are no 0s in the given array, so the modified array is [1, 1]

def segregate0and1( arr):
    arr.sort()
    print(arr)
segregate0and1([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])    
segregate0and1([1, 1]) 
    
#
def segregate0and1( arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)            
segregate0and1([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])    
segregate0and1([1, 1]) 
    
    

def segregate0and1(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]    
    print(arr)

segregate0and1([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])    
segregate0and1([1, 1]) 
               