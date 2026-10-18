class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        maxProfit = float('-inf')
        minPrice = prices[0]

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
        
        return maxProfit