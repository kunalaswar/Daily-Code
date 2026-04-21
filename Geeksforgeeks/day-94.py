 # Non-Repeating Element

# Find the first non-repeating element in a given array arr of integers and if there is not present any non-repeating element then return 0

# Note: The array consists of only positive and negative integers and not zero.

# Examples:
# Input: arr[] = [-1, 2, -1, 3, 2]
# Output: 3
# Explanation: -1 and 2 are repeating whereas 3 is the only number occuring once. Hence, the output is 3. 
# Input: arr[] = [1, 1, 1]
# Output: 0
# Explanation: There is not present any non-repeating element so answer should be 0.


def firstNonRepeating(arr): 
    dct = {}
    for val in arr:
        if val  not in dct:
            dct[val]= 1
        else:
            dct[val] +=1 
    # print(dct)       
    for key,value in dct.items():
        if value==1:
            return key
    return 0    
       
print(firstNonRepeating([-1, 2, -1, 3, 2]))    
print(firstNonRepeating([1,1,1]))    
