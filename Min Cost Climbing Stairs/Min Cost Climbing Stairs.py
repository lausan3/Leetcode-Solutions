class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Space-Optimized Bottom-Up Approach:

        Build up from the bottom two results (costs of steps 0 and 1) to get to
         step n and n - 1.
        
        we only need two variables instead of a whole array.

        Time: O(n)
        Space: O(1)
        """
        n = len(cost)

        first, second = cost[0], cost[1]

        for i in range(2, n):
            third = min(first, second) + cost[i]

            first = second
            second = third

        return min(second, first)
        """
        Bottom-Up Approach:

        Build up from the bottom two results (costs of steps 0 and 1) to get to
         step n and n - 1.

        Time: O(n)
        Space: O(n)
        """
        # n = len(cost)

        # dp = [0] * (n + 1)
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # for i in range(2, n):
        #     dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        # return min(dp[n-1], dp[n-2])

        """
        Editorial Top-Down Approach:

        Recursively build out a memo table from the top -> bottom.
        We are going down to base case once and propagating the values up from the bottom,
         then returning the result.

        Time: O(n)
        Space: O(n)
        """
        # n = len(cost)
        # memo = {}

        # def minimum_cost(i):
        #     if i <= 1:
        #         return 0
        #     if i in memo:
        #         return memo[i]

        #     down_one = minimum_cost(i - 1) + cost[i - 1]
        #     down_two = minimum_cost(i - 2) + cost[i - 2]

        #     memo[i] = min(down_one, down_two)
        #     return memo[i]

        # return minimum_cost(n)
