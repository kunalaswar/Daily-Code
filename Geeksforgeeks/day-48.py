
# Smaller and Larger

class Solution:
    def getMoreAndLess(self, arr, target):
        count_less = 0
        count_greater = 0

        for i in range(len(arr)):
            if arr[i] <= target:
                count_less += 1
            if arr[i] >= target:
                count_greater += 1

        return count_less , count_greater

s = Solution()
print(s.getMoreAndLess([1, 2, 8, 10, 11, 12, 19],  target = 0))
print(s.getMoreAndLess( [1, 5, 8, 12, 12, 12, 19], target = 12))

