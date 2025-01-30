class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_fish = 0

        def dfs(r,c):
            if (r >= m or r < 0 or c >= n or c < 0 or grid[r][c] <= 0):
                return 0
            
            fish = grid[r][c]
            grid[r][c] = -1

            return fish + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r,c))

        return max_fish