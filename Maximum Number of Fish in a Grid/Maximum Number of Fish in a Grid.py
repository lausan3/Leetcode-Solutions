class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_fish = 0

        def dfs(r,c,curr):
            # if m < r < 0 or n < c < 0:
            #     return curr

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for ro, co in directions:
                dr, dc = r + ro, c + co

                if 0 <= dr < m and 0 <= dc < n and grid[r][c] > 0:
                    return dfs(dr, dc, curr + grid[dr][dc])

            return curr

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r,c,grid[r][c]))

        return max_fish