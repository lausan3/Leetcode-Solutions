class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # initial least cost for every step + the two steps at the top is 0
        dp = [0 for _ in range(len(cost) + 2)]

        # starting from the top step, find the minimum cost to go up to it by adding the 
        # cost for the current step + the minimum of the two steps above it
        for i in range(len(cost) - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])