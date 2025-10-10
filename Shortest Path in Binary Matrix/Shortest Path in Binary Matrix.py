from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS Solution
        m, n = len(grid), len(grid[0])

        q: deque[tuple[int, int, int]] = deque()

        if grid[0][0] == 0:
            q.append((0, 0, 1))

            [
                [0,1,1,0,1],
                [0,1,0,1,0],
                [0,1,0,1,0],
                [1,0,1,1,0],
                [1,1,1,1,0]
            ]

        # down, downleft, downright, right, upleft, upright, up, left
        directions = [(1, 0), (1, -1), (1, 1), (0, 1), (-1, -1), (-1, 1), (-1, 0), (0, -1)]
        visited: set[tuple[int, int]] = set()

        while q:
            curr_r, curr_c, path_length = q.popleft()

            if curr_r == m - 1 and curr_c == n - 1:
                return path_length

            visited.add((curr_r, curr_c))

            for r, c in directions:
                dr, dc = curr_r + r, curr_c + c

                if (
                        0 <= dr < m and
                        0 <= dc < n and
                        (dr, dc) not in visited and
                        grid[dr][dc] == 0
                ):
                    q.append((dr, dc, path_length + 1))

        return -1