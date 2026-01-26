class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)

        curr_row_sum = [0] * m
        curr_col_sum = [0] * n

        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                matrix[r][c] = min(
                    rowSum[r] - curr_row_sum[r],
                    colSum[c] - curr_col_sum[c]
                )

                curr_row_sum[r] += matrix[r][c]
                curr_col_sum[c] += matrix[r][c]

        return matrix