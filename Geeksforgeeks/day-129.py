#  Roof Top
# You are given and array arr[] representing the heights of n consecutive buildings. You can move from the roof of a building to the roof of the next adjacent building. You need to find the maximum number of consecutive steps you can put forward such that every step is to a higher building than the previous one. 

# Examples:
# Input: arr[] = [1, 2, 2, 3, 2] 
# Output: 1 
# Explanation: Only pairs like 1 -> 2 or 2 -> 3 increase in height, and each such run has just 1 step. So the maximum consecutive upward steps is 1.
# Input: arr[] = [10, 20, 30, 40, 25, 50]
# Output: 3
# Explanation: 10 -> 20 -> 30 -> 40 are strictly increasing heights, so the maximum consecutive upward steps is 3.
# Input: arr[] = [4, 3, 2, 1]
# Output: 0
# Explanation: There are no contiguous increasing heights

def maxStep(arr):

    count = 0
    maximum = 0

    for i in range(1, len(arr)):

        if arr[i] > arr[i-1]:

            count += 1

            maximum = max(maximum, count)

        else:

            count = 0

    return maximum
print(maxStep([1, 2, 2, 3, 2] ))
print(maxStep([10, 20, 30, 40, 25, 50]))
print(maxStep([4, 3, 2, 1]))
