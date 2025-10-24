class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Optimal bottom-up dynamic programming solution - Given by Cedric at GSWEP

        The approach is to gradually build out a matrix containing the size of the largest
         possible square side length created for each cell incrementally using dynamic
         programming.

        For each cell, if it's a cell we want to keep track of, check the top, left, and
         top left cells for 1s. If we can construct this square, store the size of the
         max square that can be created by adding the minimum of these three stored values
         + 1 to include itself.

        # Time: O(m * n)
        # Space: O(m * n)
        """
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        max_length = 0

        # O(m * n) time
        for r in range(m):
            for c in range(n):
                cell = matrix[r][c]

                if cell == "1":
                    if (
                        r > 0 and c > 0 and
                        matrix[r-1][c] == "1" and # top
                        matrix[r][c-1] == "1" and # left
                        matrix[r-1][c-1] == "1"   # top left
                    ):
                        memo[r][c] = min(memo[r-1][c], memo[r][c-1], memo[r-1][c-1]) + 1
                    else:
                        memo[r][c] = 1

                    max_length = max(max_length, memo[r][c])
        
        return max_length * max_length