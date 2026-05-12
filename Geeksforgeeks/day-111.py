# Total count
# Given an array arr[] of positive integers and an integer k, split each element into the minimum number of parts such that every part is less than or equal to k, and find the total number of parts formed from all elements of the array.

# Examples:
# Input: k = 3, arr[] = [5, 8, 10, 13]
# Output: 14
# Explanation: Each number is expressed as a sum of numbers less than or equal to k as 5 (3 + 2), 8 (3 + 3 + 2), 10 (3 + 3 + 3 + 1), and 13 (3 + 3 + 3 + 3 + 1). Therefore, the total count of parts is (2 + 3 + 4 + 5) = 14.
# Input: k = 4, arr[] = [10, 2, 3, 4, 7]
# Output: 8
# Explanation: Each number is expressed as a sum of numbers less than or equal to k as 10 (4 + 4 + 2), 2 (2), 3 (3), 4 (4), and 7 (4 + 3). Therefore, the total count of parts is (3 + 1 + 1 + 1 + 2) = 8.


def totalCount(k, arr):
    total = 0
    for num in arr:
        part = (num + k-1)//k 
        print("------")
        print(part)
        print("------")
        total = total + part 

    return total    


print(totalCount(k = 3, arr = [5, 8, 10, 13]))

    