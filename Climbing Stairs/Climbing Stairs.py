class Solution:
    def climbStairs(self, n: int) -> int:
        """
        At each step, you can move 1 or 2 steps.
        At a base level, this is similar to calculating a fibonacci number counting up
            instead of down.
        Therefore, memoize previously calculated solutions OR at most optimal,
         just use variables.
        """
        if n == 1:
            return 1

        """
        Space-optimized version of:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        """
        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second
