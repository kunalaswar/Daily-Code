#  Sum All Array Elements

# You are given an array that contains integers. You need to return the sum of all array elements.

# Examples:
# Input: arr[] = [54, 43, 2, 1, 5]
# Output: 105
# Explanation: Just sum it 54+43+2+1+5=105.
# Input: arr[] = [324, 5, 2, 2]
# Output: 333
# Explanation: Just sum it 324+5+2+2=333.


def Sum_of_all_element(arr):
    s = 0
    for i in arr:
        s = s+i 
    return s     


print(Sum_of_all_element([54, 43, 2, 1, 5]))    
print(Sum_of_all_element([324, 5, 2, 2]))    