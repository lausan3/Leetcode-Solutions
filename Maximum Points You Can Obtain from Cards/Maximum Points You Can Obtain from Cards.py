class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tempSum = sum(cardPoints[:k])
        maxPoints = tempSum

        n = len(cardPoints)

        for i in range(k):
            tempSum += cardPoints[n - 1 - i] - cardPoints[k - 1 - i]

            maxPoints = max(maxPoints, tempSum)

        return maxPoints