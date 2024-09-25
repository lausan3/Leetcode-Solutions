class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def recurse(r, c):
            if r >= m or c >= n:
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            return recurse(r+1,c) + recurse(r,c+1)

        return recurse(0,0)