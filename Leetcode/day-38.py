
# 509. Fibonacci Number

class Solution:
    def fib(self, n):
        # base case
        if n==0:
            return 0
        if n==1:
            return 1    
        # recursive case 
        return self.fib(n-1) + self.fib(n-2)

s = Solution()
print(s.fib(2))

print(s.fib(3))

print(s.fib(4))

