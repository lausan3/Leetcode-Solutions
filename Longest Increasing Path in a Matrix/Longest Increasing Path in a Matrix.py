class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Top Down DP Solution:
        
        For each cell, return longest increasing path in the matrix
        from this cell

        If you don't add memo table, you get TLE
        
        Time: O(mn)
        Space: O(mn)
        """
        m = len(matrix)
        n = len(matrix[0])
        dirs = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(r, c) -> int:
            if dp[r][c] != 0:
                return dp[r][c]

            for dx, dy in dirs:
                new_r, new_c = r + dx, c + dy
                if (0 <= new_r < m and
                    0 <= new_c < n and
                    matrix[new_r][new_c] > matrix[r][c]
                   ):
                    dp[r][c] = max(dp[r][c], dfs(new_r, new_c))
            
            dp[r][c] += 1
            return dp[r][c]
        
        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
                
        return res
        