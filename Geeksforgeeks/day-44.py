#   Count pair sum

def countPairs(arr1, arr2, x):
    s = set(arr2)  # put all elements of arr2 in a set for fast lookup
    count = 0

    for a in arr1:
        if (x - a) in s:
            count += 1

    return count
        
print(countPairs([1, 3, 5, 7], [2, 3, 5, 8], 10))  # Output: 2
print(countPairs([1, 2, 3, 4], [5, 6, 7, 8], 5))   # Output: 0

