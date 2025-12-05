class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for current_change in range(1, amount + 1):
            for coin in coins:
                if current_change - coin >= 0:
                    dp[current_change] = min(dp[current_change - coin] + 1, dp[current_change])

        return dp[amount] if dp[amount] != float('inf') else -1