class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # neetcode io
        # time: O(n * m) where n is the amount and m is the length of the coins
        # time: O(n) where n is amount
        # we're going to use memoization

        dp = [amount + 1] * (amount + 1) # cache of size (amount + 1)^2. going to contain the amount of coins used
                                         # to get that amount
        dp[0] = 0

        # compute every value in dp in reverse (bottom up)
        for a in range(1, amount + 1):
            for c in coins: # compute this a amount
                if a - c >= 0: # if the amount - coin amount 
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # return the cached amount if it's in range (not the amount + 1 # of 1 coins)
        return dp[amount] if dp[amount] != amount + 1 else -1