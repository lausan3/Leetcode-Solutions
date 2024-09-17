class Solution:
    def tribonacci(self, n: int) -> int:
        memo = { 0: 0, 1: 1, 2: 1 }

        if n not in memo:
            memo[n] = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)

        return memo[n]