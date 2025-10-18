class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # possible bfs solution
        m, n = len(board), len(board[0])
        q = deque()

        # populate starting nodes in q
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    next_index = 1
                    q.append( ( r, c, next_index, set([ (r,c) ]) ) )

        # coordinates and amount of letters left to search
        # up, down, left, right
        dirs = [
            (-1,0), (1,0), (0,-1), (0,1)
        ]

        while q:
            r, c, next_index, visited = q.popleft()

            if next_index >= len(word):
                return True

            next_letter = word[next_index]

            for row, col in dirs:
                dr, dc = r + row, c + col

                if (
                    0 <= dr < m and
                    0 <= dc < n and
                    board[dr][dc] == next_letter and
                    (dr, dc) not in visited
                ):
                    visited.add((dr,dc))
                    q.append((dr, dc, next_index + 1, visited))

        return False