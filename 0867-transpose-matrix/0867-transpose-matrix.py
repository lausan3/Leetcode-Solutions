class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW_LEN, COL_LEN = len(matrix), len(matrix[0])

        # This creates an n * m matrix out of an m * n matrix
        res = [[0] * ROW_LEN for i in range(COL_LEN)]
        
        for r in range(ROW_LEN):
            for c in range(COL_LEN):
                res[c][r] = matrix[r][c]

        return res