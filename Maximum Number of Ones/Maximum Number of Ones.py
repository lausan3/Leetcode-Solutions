class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        """
        Greedy mathematical approach (from editorial):

        Time: O(l^2 * log l^2) where l = side length
        Space: O(l^2)
        """

        count = []

        for r in range(sideLength):
            for c in range(sideLength):
                possible_ones = (1 + (width - c - 1) // sideLength) * (1 + (height - r - 1) // sideLength)

                count.append(possible_ones)

        count.sort(reverse=True)

        return sum(count[:maxOnes])
