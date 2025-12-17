class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Editorial One-Pass double DP solution:

        Essentially, the solution works by iteratively calculating the profit from the left and right side of the prices array,
         then taking the maximum of left[i] + right[i + 1].

        The calculation for each side is as follows:
         side_profits[side] = max(previous profit, profit from selling from max or min value seen from side)

        From the left side, we track the minimum value to BUY at.
        From the right side, we track the maximum value to SELL at.
        """
        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        right_profits = [0] * (length + 1)

        # construct the bidirectional DP array
        for l in range(1, length):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])

        return max_profit