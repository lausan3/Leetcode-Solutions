class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def dfs(x: int) -> int:
            if x <= 1:
                return 0

            if x % 2 == 0:
                return dfs(x // 2) + 1
            else:
                return min(dfs(x + 1), dfs(x - 1)) + 1

        return dfs(n)