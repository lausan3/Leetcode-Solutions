class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        2-D Prefix Sum Solution:
        Calculate the 2-D prefix sum grid (which represents the area of the square at bottom right i j), then use it to calculate the maximum side length

        Time: O(mn)
        Space: O(mn)
        """
        m = len(mat)
        n = len(mat[0])
        psum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                psum[r][c] = psum[r - 1][c] + psum[r][c - 1] - psum[r - 1][c - 1] + mat[r - 1][c - 1]
            
        # calculate answer
        def get_rect(x1, y1, x2, y2) -> int:
            return psum[x2][y2] - psum[x1 - 1][y2] - psum[x2][y1 - 1] + psum[x1 - 1][y1 - 1]

        boundary, max_side_len = min(m, n), 0
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                for side_len in range(max_side_len + 1, boundary + 1):
                    br_row = r + side_len - 1
                    br_col = c + side_len - 1

                    if (
                        br_row <= m and
                        br_col <= n and
                        get_rect(r, c, br_row, br_col) <= threshold
                    ):
                        max_side_len += 1
                    else:
                        break
        
        return max_side_len