class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set() # set containing the layers of the bfs

        # dfs
        def dfs(r, c):
            # out of bounds
            if (r < 0 or r == rows or c < 0 or c == cols
            # water or visited
                or grid[r][c] == 0 or (r, c) in visit):
                return 0

            # if not, visit the cell
            visit.add((r,c))
            # get max island area
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea