class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """
        Bottom Up DP solution:

        Similar to maximal square except we run through each row and column twice to compute the plus lengths

        The calculation portion is calculating the number of concurrent 1s in all four directions (two nested for loops)

        Time: O(n^2)
        Space: O(n^2)
        """
        banned = set([ (r, c) for r, c in mines ])  # for O(1) search

        dp = [[0] * n for _ in range(n)]

        largest_k = 0

        for r in range(n):
            count = 0
            # left to right
            for c in range(n):
                count = 0 if (r,c) in banned else count + 1
                dp[r][c] = count
            
            count = 0
            # right to left
            for c in range(n - 1, -1, -1):
                count = 0 if (r,c) in banned else count + 1
                if count < dp[r][c]: dp[r][c] = count
        
        for c in range(n):
            count = 0
            # up to down
            for r in range(n):
                count = 0 if (r,c) in banned else count + 1
                if count < dp[r][c]: dp[r][c] = count
            
            count = 0
            # down to up
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > largest_k: largest_k = dp[r][c]

        return largest_k