class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Preword:
        I had tried a Bottom-Up solution before reading the editorial. I was doing something similar to the solution where I was keeping the
        maximum amount of cherries to be picked up by each robot, but couldn't figure out how to combine the states. The solution is move the robots
        at the same time, which I had ruled out from thinking of the brute force dfs solution.

        Bottom-Up DP Solution:
        The idea is to keep track of the number of cherries to be picked up by both robots SIMULTANEOUSLY by tracking the dp array in three dimensions, 
        the current row, the column of the first robot, and the column of the second robot.
        
        1. We maintain an array dp[m][n][n].
        2. We move up from the last row for this approach.
        3. Every time the robots move up, they check their possible three paths below them for the max.
        4. Then we return dp[0][0][n-1] (their starting states)
        """
        m = len(grid)
        n = len(grid[0])
        
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]

        for r in reversed(range(m)):
            for c1 in range(n):
                for c2 in range(n):
                    new_cherries = 0

                    # add curr pos
                    new_cherries += grid[r][c1]
                    if c1 != c2:
                        new_cherries += grid[r][c2]
                    
                    # add prev pos
                    if r != m - 1:
                        prev_max = 0
                        for i in range(c1 - 1, c1 + 2):
                            for j in range(c2 - 1, c2 + 2):
                                if 0 <= i < n and 0 <= j < n:
                                    prev_max = max(prev_max, dp[r + 1][i][j])

                        new_cherries += prev_max

                    dp[r][c1][c2] = new_cherries
        
        return dp[0][0][n - 1]