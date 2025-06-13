#Stock buy and sell
'''
Given an array prices[] of length n, representing the prices of the stocks on different days.
The task is to find the maximum profit possible by buying and selling the stocks on different days when at most 
one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.
'''
class Solution:
    def maximumProfit(self, prices):
        if prices == sorted(prices, reverse = True):
            return 0
        if prices == sorted(prices):
            return prices[-1]-prices[0]
        else:
            buy_price = prices[0]
            current_profit = 0
            max_profit = 0
            for today in range(len(prices)-1):
                if prices[today] < buy_price:
                    buy_price = prices[today]
                current_profit = prices[today+1] - buy_price
                max_profit = max(max_profit,current_profit)
            return max_profit