class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_price = prices[0]
        profit = 0

        for price in prices:
            if price < current_price:
                current_price = price
            
            change = price - current_price
            if change > profit:
                profit = change

        return profit

        