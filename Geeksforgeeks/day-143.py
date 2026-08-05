# Any Duplicate Within K Distance
# Difficulty: EasyAccuracy: 48.69%Submissions: 54K+Points: 2
# Given an unsorted array arr[] and an integer k, check if there is any duplicate within k distance. 

# Examples:

# Input: arr[] = [1, 5, 4, 5, 1], k = 3
# Output: true
# Explanation: 5 is at distance 2 which is less than or equal to k.
# Input: arr[] = [10, 2, 3, 4, 10, 5], k = 3
# Output: false
# Explanation: Only one duplicate 10 at distance 4 which is more than 3.
# Input: arr[] = [6, 8, 4, 1, 8, 5, 7], k = 3
# Output: true
# Explanation: 8 is repeated at distance 3.


class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        last_index = {}
        for i in range(len(arr)):
            if arr[i] in last_index:
                if i - last_index[arr[i]] <= k:   
                    return True
            last_index[arr[i]] = i
        return False

s = Solution()
print(s.checkDuplicatesWithinK([1, 5, 4, 5, 1], k = 3))
print(s.checkDuplicatesWithinK([10, 2, 3, 4, 10, 5], k = 3))
print(s.checkDuplicatesWithinK([6, 8, 4, 1, 8, 5, 7], k = 3))

      
