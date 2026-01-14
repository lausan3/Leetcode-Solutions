class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Bottom Up DP Solution:
        
        1. Keep an m x n dp array of the minimum path sums to get to any given cell
        2. Return the minimum path sum kept by this array

        Time: O(m * n)
        Space: O(m * n)
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                right = c + 1 < n
                down = r + 1 < m
                
                if right and down:
                    dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
                elif right and not down:
                    dp[r][c] = grid[r][c] + dp[r][c + 1]
                elif not right and down:
                    dp[r][c] = grid[r][c] + dp[r + 1][c]
                else:
                    dp[r][c] = grid[r][c]

        return dp[0][0]