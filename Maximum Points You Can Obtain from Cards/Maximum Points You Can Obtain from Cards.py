class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftScore = sum(cardPoints[:k])
        rightScore = sum(cardPoints[:k:-1])

        return max(leftScore, rightScore)