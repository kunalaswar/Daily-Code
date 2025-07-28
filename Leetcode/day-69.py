
# 598. Range Addition II

class Solution:
    def maxCount(self, m: int, n: int, ops):
    
        if not ops:
            return m * n
    
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
    
        return min_a * min_b

s = Solution()
print(s.maxCount(m = 3, n = 3, ops = [[2,2],[3,3]]))

print(s.maxCount(m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))

print(s.maxCount( m = 3, n = 3, ops = []))