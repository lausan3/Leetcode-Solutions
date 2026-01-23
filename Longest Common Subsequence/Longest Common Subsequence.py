class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Editorial Tabulation Approach:
        Our dp array is 2D from 0 -> m and 0 -> n where m = len(text1) and n = len(text2)
        Each cell represents the largest size of the subsequence possible of 
         text1[i] and text2[j]
        Iterating over the pairs of letters in text1 and text2 in reverse,
         If they match, dp[i][j] is 1 + bottom right cell.
         If they don't match, dp[i][j] is the max of the right and bottom cells.

        Time: O(mn)
        Space: O(mn)
        """
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
        """
        Editorial Brute Force Recursive Approach:
        The idea is that we need to draw lines from text1 to text2 of matching letters
        from left to right to find common subsequences.

        Time: O(2^n)
        Space: O(2^n)
        """
        """
        if len(text1) == 0 or len(text2) == 0:
            return 0
        
        letter1 = text1[0]
        first_occur = 0

        for i in range(len(text2)):
            if text2[i] == letter1:
                first_occur = i
                break

        # remove first letter from text1 and try next letters
        case1 = self.longestCommonSubsequence(text1[1:], text2)
        # letter is in text2, solve the rest of the text2
        case2 = 0
        if letter1 in text2:
            case2 = 1 + self.longestCommonSubsequence(text1[1:], text2[first_occur + 1:])

        return max(case1, case2)
        """