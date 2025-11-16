class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes_sorted = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        dp = [0] * n
        dp[0] = 1
        
        longest = 0

        for i in range(1, n):
            for j in range(n):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

            longest = max(longest, dp[i])

        return longest + 1