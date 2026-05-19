# Form Divisible by 3 from Array
# You are given an array arr[] of integers. You can form new integers by concatenating any two integers from the array (treating them as strings). For example, given 19 and 4, you can form 194 and 419.

# Determine whether it is possible to construct a single integer using all the digits of the given numbers (in any order) such that the resulting number is divisible by 3.

# Examples:
# Input: arr[] = [40, 50, 90]
# Output: true
# Explanation: One such number is 405090.
# Input: arr[] = [1, 4]
# Output: false
# Explanation: The numbers we can form are 14 and 41. But neither of them are divisible by 3.

class Solution:

    def isPossible(self, arr):

        total = 0

        for i in arr:

            a = str(i)

            for digit in a:

                total += int(digit)

        return total % 3 == 0


s = Solution()        
print(s.isPossible([40, 50, 90]))
print(s.isPossible([1, 4]))