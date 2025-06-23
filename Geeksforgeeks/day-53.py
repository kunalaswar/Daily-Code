
# 
# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Special case for 0
        if n == 0:
            return 5
        
        result = 0
        place = 1
        while n > 0:
            r = n % 10
            if r == 0:
                r = 5
            result += r * place
            place *= 10    
            n = n // 10                 
        return result
                   
                


s = Solution()                
print(s.convertFive(1004))
