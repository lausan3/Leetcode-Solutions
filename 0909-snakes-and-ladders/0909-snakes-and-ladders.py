class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # currRow = (num - 1) // n
        # currCol = (num - 1) % n
        # returns new position at board[row][col] from a number
        def getNewPos(num: int) -> int:
            row = (num - 1) // n
            col = (num - 1) % n
            
            if row % 2 == 1:
                # invert column index if row is odd
                col = n - col - 1

            row = n - row - 1

            return board[row][col]

        q = deque([1])  # start BFS at boustro label 1
        visited = { 1 : 0}  # value : # of rolls to get there
        target = n ** 2
        
        while q:
            curr = q.popleft()  # current square label
            print(f"running {curr}")

            # add all squares we can get to from a dice roll's distance away
            for i in range(curr + 1, 1 + min(curr + 6, target)):
                next = i
                nextPos = getNewPos(next)

                print(f"converting {next} to {nextPos}")

                if next > target: return -1

                # replace starting curr for this pass to the one at nextPos if it's a snake or ladder
                if nextPos != -1:
                    next = nextPos
                
                # count the amount to get to the next square by getting the previous square + 1
                if next == target: return visited[curr] + 1

                if next not in visited:
                    visited[next] = visited[curr] + 1
                    q.append(next)
                    
        return -1