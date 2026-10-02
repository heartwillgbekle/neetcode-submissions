class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        current = float("inf")

        for price in prices:
            profit = price - current
            maxprofit = max(maxprofit, profit)
            current = min(current, price)

        return maxprofit

        