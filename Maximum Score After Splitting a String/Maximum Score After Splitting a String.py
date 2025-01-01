class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        for i in range(len(s)):
            left, right = s[:i+1], s[i+1:]

            left_score = right_score = 0

            for char in left:
                if char == "0":
                    left_score += 1
            
            for char in right:
                if char == "1":
                    right_score += 1

            max_score = max(max_score, left_score + right_score)

        return max_score