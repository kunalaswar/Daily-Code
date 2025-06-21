
# 2520. Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while(temp > 0):
            r = temp %10
            if num %r==0: 
                count = count +1
            temp = temp//10    

            
        return count

s = Solution()    
print(s.countDigits(7))
print(s.countDigits(121))
# print(s.countDigits(1248))

