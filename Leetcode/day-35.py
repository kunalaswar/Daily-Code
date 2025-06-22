
# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum = 0
        mul = 1
        while(temp>0)   :
            r = temp%10
            sum  = sum+r
            mul = mul*r
            temp = temp//10
        return mul-sum 
s = Solution()    
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))
