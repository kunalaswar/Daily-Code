
class Solution:
    def find_unique(self, k, arr):
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        for num in count:
            if count[num] % k != 0:
                return num

sol = Solution()
print(sol.find_unique(3, [6, 2, 5, 2, 2, 6, 6]))  # Output: 5
print(sol.find_unique(4, [2, 2, 2, 10, 2]))      # Output: 10
