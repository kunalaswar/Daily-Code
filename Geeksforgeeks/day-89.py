# Index of an Extra Element
# You have given two sorted arrays arr1[] & arr2[] of distinct elements. The first array has one element extra added in between. Return the index of the extra element.

# Note: 0-based indexing is followed.
# Examples
# Input: a[] = [2,4,6,8,9,10,12], b[] = [2,4,6,8,10,12]
# Output: 4
# Explanation: In the first array, 9 is extra added and it's index is 4.
# Input: a[] = [3,5,7,8,11,13], b[] = [3,5,7,11,13]
# Output: 3
# Explanation: In the first array, 8 is extra and it's index is 3.
# Input: a[] = [3,5], b[] = [3]
# Output: 1
# Explanation: In the first array, 5 is extra and it's index is 1.


def findExtra(a,b):
    for i in range(len(a)):
        # print(a[i])
        if a[i] not in b:
            return i

print(findExtra([2,4,6,8,9,10,12],[2,4,6,8,10,12]))    
print(findExtra([3,5,7,8,11,13],[3,5,7,11,13]))    



        
