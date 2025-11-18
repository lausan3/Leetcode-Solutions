class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        """
        Brute force BFS approach:

        Perform BFS from each gate's row, col, and distance from gate (Starting at 0).

            rooms[r][c] is min(rooms[r][c], distance)
            For each direction that it can go in,
                append to queue its row, col, and curr distance + 1

        Time: O(m*n)
        Space: O(m*n)
        """
        m = len(rooms)
        n = len(rooms[0])
        gates = []
        
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    gates.append( (r, c, 0) )

        queue = deque(gates)

        dirs = [
            (-1, 0),  # up
            (1, 0),  # down
            (0, -1),  # left
            (0, 1)  # right
        ]

        while queue:
            r, c, dist = queue.popleft()

            rooms[r][c] = min(rooms[r][c], dist)

            for direction in dirs:
                dr, dc = r + direction[0], c + direction[1]

                if (
                    0 <= dr < m and
                    0 <= dc < n and
                    rooms[dr][dc] != 0 and rooms[dr][dc] != -1 and
                    rooms[dr][dc] > dist + 1
                ):
                    queue.append( (dr, dc, dist + 1) )

        return rooms