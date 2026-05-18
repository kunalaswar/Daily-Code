# Three way partitioning
# Given an array and a range a, b. The task is to partition the array around the range such that the array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to return the modified array.

# Note: The generated output is true if you modify the given array successfully. Otherwise false.

# Geeky Challenge: Solve this problem in O(n) time complexity.

# Examples:
# Input: arr[] = [1, 2, 3, 3, 4], a = 1, b = 2
# Output: true
# Explanation: One possible arrangement is: {1, 2, 3, 3, 4}. If you return a valid arrangement, output will be true.
# Input: arr[] = [1, 4, 3, 6, 2, 1], a = 1, b = 3
# Output: true
# Explanation: One possible arrangement is: {1, 3, 2, 1, 4, 6}. If you return a valid arrangement, output will be true.

#User function template for Python
class Solution:

    def threeWayPartition(self, arr, a, b):

        left = []
        middle = []
        right = []

        for num in arr:

            if num < a:
                left.append(num)

            elif num <= b:
                middle.append(num)

            else:
                right.append(num)

        arr[:] = left + middle + right

        return arr


s = Solution()

print(s.threeWayPartition([1,2,3,3,4],1,2))
print(s.threeWayPartition([1, 4, 3, 6, 2, 1], a = 1, b = 3))