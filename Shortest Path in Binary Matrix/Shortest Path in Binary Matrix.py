from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS Solution
        m, n = len(grid), len(grid[0])

        q: deque[tuple[int, int, int]] = deque()

        if grid[0][0] == 0:
            q.append((0, 0, 1))

        # down, downright, right
        directions = [(1, 0), (1, 1), (0, 1)]

        while q:
            curr_r, curr_c, path_length = q.popleft()

            for r, c in directions:
                dr, dc = curr_r + r, curr_c + c

                if dr == m - 1 and dc == n - 1:
                    return path_length + 1

                if (
                        0 <= dr < m and
                        0 <= dc < n and
                        grid[dr][dc] == 0
                ):
                    q.append((dr, dc, path_length + 1))

        return -1