#answer\
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 10000
        profit = 0

        for i in prices:
            min_price = min(i, min_price)
            profit = max(profit, i - min_price)
        return profit


# better
def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit