class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest_price = prices[0]
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            profit = max(price - lowest_price, profit)
        return profit