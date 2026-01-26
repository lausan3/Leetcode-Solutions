class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        My Initial Intuition:
        1. Define the locations of each letter on the keyboard
        2. Recurse with two decisions:
           2a. Type the next letter from the each finger
           2b. If we still have a finger to use, start it at this letter
        3. Return the minimum distance.
        """
        n = len(word)
        # dp[from][to][i] = cost
        dp = [
            [
                [
                    -1 for _ in range(n)
                ]
                for _ in range(27)
            ] for _ in range(27)
        ]

        def cost(from_ltr: int, to_ltr: int) -> int:
            if from_ltr == 26:  # currently hovering
                return 0
            else:
                return abs(from_ltr // 6 - to_ltr // 6) + abs(from_ltr % 6 - to_ltr % 6)

        def dfs(i: int, left: int = 26, right: int = 26):
            if i == n:
                return 0

            if dp[left][right][i] == -1:
                to = ord(word[i]) - ord('A')

                dp[left][right][i] = min(
                    cost(left, to) + dfs(i + 1, to, right),
                    cost(right, to) + dfs(i + 1, left, to)
                )

            return dp[left][right][i]
            
        return dfs(0)