
# 412. Fizz Buzz

class Solution:
    def fizzBuzz(self, n):
        lst = []
        for i in range(1, n+1):
                
            if i%3==0 and i%5==0:
                lst.append("FizzBuzz")
            elif i%3 ==0:
                lst.append("Fizz")
                     
            elif i%5 ==0:
                lst.append("Buzz")
            else:
                lst.append(str(i))

        return lst          

s = Solution()
print(s.fizzBuzz(3))
print(s.fizzBuzz(5))
print(s.fizzBuzz(15))

