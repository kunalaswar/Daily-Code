
# Largest product

class Solution:
    def findMaxProduct(self, arr, k):
        n = len(arr)
        if k > n:
            return 0  # not enough elements

        max_product = 0

        for i in range(n - k + 1):
            product = 1
            for j in range(i, i + k):
                product *= arr[j]
            max_product = max(max_product, product)

        return max_product



s = Solution()
print(s.findMaxProduct([1, 2, 3, 4], 2))   # Output: 12
print(s.findMaxProduct([1, 6, 7, 8], 3))   # Output: 336

