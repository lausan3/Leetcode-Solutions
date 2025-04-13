class Solution:
    def countGoodNumbers(self, n: int) -> int:
        result = 1

        for i in range(n):
            if i % 2 == 0:
                result *= 5
            else:
                result <<= 2

        return result % 1_000_000_007