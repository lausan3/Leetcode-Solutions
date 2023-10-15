class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW_LEN = len(matrix)
        COL_LEN = len(matrix[0])
        
        zeroes = []

        # take a pass to find natural zeroes
        for r in range(ROW_LEN):
            for c in range(COL_LEN):
                if matrix[r][c] == 0:
                    zeroes.append([r, c])


        # run through zeroes. set row and col to 0
        for zero in zeroes:
            r = zero[0]
            c = zero[1]

            # change row
            for col in range(COL_LEN):
                matrix[r][col] = 0

            # change col
            for row in range(ROW_LEN):
                matrix[row][c] = 0