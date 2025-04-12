    

#  67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert binary string to interger
        num1 = int(a,2)
        num2 = int(b,2)

        total = num1 + num2
        return bin(total)[2:]
    
s = Solution()    
res = s.addBinary("11","1")
print(res, type(res))