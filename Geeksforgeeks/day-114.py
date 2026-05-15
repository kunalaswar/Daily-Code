# Smallest subarray with sum greater than x
class Solution:

    def smallestSubWithSum(self, x, arr):

        n = len(arr)

        ans = float('inf')

        for i in range(n):

            total = 0

            for j in range(i, n):

                total += arr[j]

                if total > x:

                    ans = min(ans, j - i + 1)
                    break

        if ans == float('inf'):
            return 0

        return ans
s = Solution()    

print(s.smallestSubWithSum(51,[1, 4, 45, 6, 0, 19]))

print(s.smallestSubWithSum(100,[1, 10, 5, 2, 7]))
