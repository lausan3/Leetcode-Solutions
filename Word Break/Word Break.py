class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Bottom-Up Iterative DP solution:

        init memo = [False] * n

        for every index i that matches a word's length in wordDict or we have
         calculated a previous part of s that matched a word,
            if the word we construct from s matches a word in wordDict, 
                mark that index as true

        the solution is memo[n - 1]

        Time: O(n * m * s) where s = len(s) (n in code) and m = len(wordDict)
        Space: O(n)
        """
        n = len(s)
        memo = [False] * n

        for i in range(n):
            for word in wordDict:
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or memo[i - len(word)]:
                    if s[i - len(word) + 1 : i + 1] == word:
                        memo[i] = True
                        break

        return memo[n - 1]
