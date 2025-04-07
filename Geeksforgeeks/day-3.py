class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum = 0
        for val in range(n+1):
            sum = sum+val
        return sum   

s =Solution()        
print(s.seriesSum(5))


