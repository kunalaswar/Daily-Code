  
# 69. Sqrt(x)
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0 
        while i*i<=x:
            i = i+1
    
        else:
            return  i-1    
        
s  = Solution()        
res = s.mySqrt(4)
print(res)

