# src: https://youtu.be/lLixGoGuClc and my own c++ sudoku solver
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        ## backtracking problem
        # we'll use sets to keep track of the nums in the rows, cols, and subsquares
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subsqs = [set() for _ in range(9)]

        # obtain rows and cols with numbers in them
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)

                    box_id = i // 3 * 3 + j // 3 # which subsq empty cell located in
                    subsqs[box_id].add(num)

        def backtrack(i, j):
            nonlocal solved
            if i >= 9:
                solved = True
                return

            new_i = i + (j + 1) // 9
            new_j = (j + 1) % 9

            if board[i][j] != ".": # ignore cells with values in them
                backtrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    box_id = i // 3 * 3 + j // 3

                    if num not in rows[i] and num not in cols[j] and num not in subsqs[box_id]:
                        rows[i].add(num)
                        cols[j].add(num)
                        subsqs[box_id].add(num)
                        board[i][j] = str(num)
                        
                        backtrack(new_i, new_j)

                        # backtrack
                        if not solved:
                            rows[i].remove(num)
                            cols[j].remove(num)
                            subsqs[box_id].remove(num)
                            board[i][j] = "."

        solved = False

        backtrack(0, 0)