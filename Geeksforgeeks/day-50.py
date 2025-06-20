
# Check String

class Solution:
    def check (self,s):
        first = s[0]
        for i in s :
            if first != i:    
                return False
        return True
    
s = Solution()    
print(s.check("geeks"))

print(s.check("gggg"))


        