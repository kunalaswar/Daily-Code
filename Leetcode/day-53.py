# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices):
        profit = 0
        n = len(prices)

        for i in range(n-1):
            if prices[i+1] > prices[i]:
                profit +=  (prices[i+1] - prices[i])

        return profit
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))

print(s.maxProfit([1,2,3,4,5]))

print(s.maxProfit([7,6,4,3,1]))

