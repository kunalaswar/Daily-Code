
# 

class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return []

        result = [arr[0]]  # First element is always unique in a sorted array

        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                result.append(arr[i])

        return result

s = Solution()
print(s.removeDuplicates([2, 2, 2, 2, 2]))
print(s.removeDuplicates([1, 2, 4]))