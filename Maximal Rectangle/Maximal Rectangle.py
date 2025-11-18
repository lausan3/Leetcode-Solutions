class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Monotonically Increasing stack solution (from editorial):

        This solution is similar to LC #84, find largest rectangle in histogram.

        Essentially, we want to keep a monotonically increasing stack that represents

        Time: O(m * n)
        Space: O(n)
        """
        m, n = len(matrix), len(matrix[0])

        max_area = 0
        dp = [0] * n

        # Direct copy from LC #84
        def find_area() -> int:
            stack = [-1]

            maxarea = 0
            for i in range(len(dp)):

                while stack[-1] != -1 and dp[stack[-1]] >= dp[i]:
                    maxarea = max(
                        maxarea, dp[stack.pop()] * (i - stack[-1] - 1)
                    )
                stack.append(i)

            while stack[-1] != -1:
                maxarea = max(
                    maxarea, dp[stack.pop()] * (len(dp) - stack[-1] - 1)
                )

            return maxarea

        for r in range(m):
            for c in range(n):
                dp[c] = dp[c] + 1 if matrix[r][c] == "1" else 0

            max_area = max(max_area, find_area())
        
        return max_area

        """
        Bottom Up Dynamic Programming Solution (from Editorial):

        The approach essentially calculates the number of concurrent 1s from left to right, while also
         simultaneously checking the values above widths above it to find areas.

        Time: O(m * n^2)
        Space: O(m * n)
        """
        # maxarea = 0

        # dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == "0":
        #             continue

        #         # compute the maximum width and update dp with it
        #         width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

        #         # compute the maximum area rectangle with a lower right corner at [i, j]
        #         for k in range(i, -1, -1):
        #             width = min(width, dp[k][j])
        #             maxarea = max(maxarea, width * (i - k + 1))

        # return maxarea