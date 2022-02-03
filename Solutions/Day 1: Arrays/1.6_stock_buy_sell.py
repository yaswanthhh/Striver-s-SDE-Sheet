class Solution(object):
    def maxProfit(self, prices):
        lowest, profit = prices[0], 0
        for i in prices:            
            if i < lowest:
                lowest = i
                continue
            t = i - lowest
            print(i)
            if t > profit:
                profit = t
            
        return profit
