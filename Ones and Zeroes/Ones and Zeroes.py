class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_z_o(s: str) -> List[int]:
            c = [0] * 2

            for char in s:
                c[ord(char) - ord('0')] += 1

            return c

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            count = count_z_o(s)

            for i in range(m, count[0] - 1, -1):
                for j in range(n, count[1] - 1, -1):
                    dp[i][j] = max(1 + dp[i - count[0]][j - count[1]], dp[i][j])

        return dp[m][n]