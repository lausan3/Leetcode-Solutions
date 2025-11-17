class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Dynamic Programming Bottom-up solution:

        For each entry in the matrix, check if 1
            if 1, check the top, left, and top left items in matrix are 1. If so, dp[r][c] = min(dp left, dp top, dp top left) + 1.

        Time: O(m * n)
        Space: O(m * n)
        """
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]

        max_sides = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "0":
                    continue

                if r <= 0 or c <= 0:
                    dp[r][c] = 1
                    max_sides = max(max_sides, 1)

                left = int(matrix[r][c - 1])
                top = int(matrix[r - 1][c])
                top_left = int(matrix[r - 1][c - 1])
                
                dp[r][c] = min(dp[r][c - 1], dp[r - 1][c], dp[r - 1][c - 1]) + 1

                max_sides = max(max_sides, dp[r][c])

        return max_sides ** 2