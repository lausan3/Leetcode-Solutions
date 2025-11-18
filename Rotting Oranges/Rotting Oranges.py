class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS approach:

        Count # of fresh oranges and positions of rotting oranges
        init max time var

        BFS for each rotting orange, rotting them (marking as 2) and appending its row, col, and time.
        also remember to decrement # of fresh oranges
        replace max time var if needed

        return time if # of fresh oranges is 0 else -1

        Time: O(m * n)
        Space: O(m * n)
        """
        m, n = len(grid), len(grid[0])
        starting = []
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    starting.append((r, c, 0))

        q = deque(starting)
        max_time = 0

        dirs = [
            (-1,0),
            (0,1),
            (1,0),
            (0,-1)
        ]

        while q:
            r, c, time = q.popleft()

            max_time = max(max_time, time)

            for delta in dirs:
                dr, dc = r + delta[0], c + delta[1]

                if (
                    0 <= dr < m and
                    0 <= dc < n and
                    # (dr, dc) not in visited and
                    grid[dr][dc] == 1
                ):
                    grid[dr][dc] = 2
                    fresh -= 1
                    q.append( (dr, dc, time + 1) )

        return max_time if fresh == 0 else -1