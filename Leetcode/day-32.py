
# 1523. Count Odd Numbers in an Interval Range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (1 if low % 2 != 0 or high % 2 != 0 else 0)

s = Solution()
print(s.countOdds(3,7))
print(s.countOdds(8,10))

