class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        It should be noticed that now that we can buy and sell a stock on the same day, waiting to sell a stock at the peak vs buying and selling
         constantly generates the same amount of money due to the total profit being profit - sell price.

        Knowing this, it's clear that checking consecutive days for profit and adding up the total gives us the answer.
        """
        max_profit = 0

        for day in range(1, len(prices)):
            max_profit = max(max_profit, max_profit + prices[day] - prices[day - 1])

        return max_profit