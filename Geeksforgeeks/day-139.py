# Modify the Array
# Given an array arr, return the modified array in such a way that if the current and next numbers are not zero and are equal then double the current and replace the next number with 0. After the modification, rearrange the array such that all 0's are shifted to the end.

# Note:  The sequence of the non-zeros should in the same order in output.

# Examples:
# Input: arr[] = [2, 2, 0, 4, 0, 8] 
# Output: [4, 4, 8, 0, 0, 0] 
# Explanation: At index 0 and 1 both the elements are the same. So, we change the element at index 0 to 4 and the element at index 1 is 0 then shift all the zeros to the end of the array. So, the array become [4, 4, 8, 0, 0, 0]. After this there is no further change as the remaining array elements are either 0 or not same.
# Input: arr[] = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8] 
# Output: [4, 2, 12, 8, 0, 0, 0, 0, 0, 0]
# Explanation: Since the elements at indexes 1 to 2 are same, we change array to [4, 2, 6, 6, 8, 0, 0, 0, 0, 0]. Now we have two 6s same, so array becomes [4, 2, 12, 8, 0, 0, 0, 0, 0, 0]


def modifyAndRearrangeArr (arr): 
    for i in range(len(arr)-1):
        if arr[i] != 0 and arr[i] == arr[i+1]:
            arr[i] = arr[i] * 2
            arr[i+1] = 0

    ans = []
    for num in arr:
        if num != 0:
            ans.append(num)
        
    while len(ans) < len(arr):
        ans.append(0)

    return ans


print(modifyAndRearrangeArr([2, 2, 0, 4, 0, 8]))
print(modifyAndRearrangeArr([0, 2, 2, 2, 0, 6, 6, 0, 0, 8] ))
