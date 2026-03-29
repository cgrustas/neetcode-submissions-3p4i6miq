class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0

        while sell < len(prices):
            # if you lose money by selling, don't sell, hold (move the buy and sell date forward).
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            
            sell += 1
    
        return maxProfit
