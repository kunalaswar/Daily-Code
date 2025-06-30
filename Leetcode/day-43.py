
#  121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices):
            
        minprice = float('inf')
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
        # print(minprice)        
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice

        return maxprofit

s = Solution()
print(s.maxProfit( [7,1,5,3,6,4]))


print(s.maxProfit([7,6,4,3,1]))


        