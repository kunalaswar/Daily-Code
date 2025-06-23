
# 
# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        result = 0
        place = 1
        while(n>0):
            r = n % 10
            if r == 0:
                r = 5
            result += r * place
            place *= 10    
            n = n//10                 
        return result     
                


s = Solution()                
print(s.convertFive(1004))
