# Highest and Lowest Frequencies
# Given an array, the task is to find the difference between the highest occurrence and lowest occurrence of any numbers in an array. If only one type of element is present in the array return 0

# Examples:
# Input: arr[] = [1, 2, 2]
# Output: 1
# Explanation:  Lowest occurring element (1) occurs once. Highest occurring element (2) occurs 2 times
# Input: arr[] = [7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]
# Output: 2
# Explanation : Lowest occurring element (2) occurs once. Highest occurring element (7) occurs 3 times


def findDiff(arr):
    freq = {}

    # Count frequencies
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_freq = max(freq.values())
    min_freq = min(freq.values())

    return max_freq - min_freq

print(findDiff([1, 2, 2]))
print(findDiff([7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]))
        
    
    
    
    