
# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n):
            
        # base case
        if n<=0:
            return False
        if n==1:
            return True
        if n%2!=0:
            return False
        # Recursive case
        return self.isPowerOfTwo(n//2)          
        
s = Solution()
print(s.isPowerOfTwo(1))

print(s.isPowerOfTwo(16))

print(s.isPowerOfTwo(3))


        