class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Brute Force Approach: O(n) Time, O(1) Space.
        # Gives TLE.
        # result = 1

        # for i in range(n):
        #     if i % 2 == 0:
        #         result *= 5
        #     else:
        #         result <<= 2

        # return result % 1_000_000_007

        # Optimized Approach using Fast Exponentiation: O(log n) Time, O(1) Space.
        mod = 1_000_000_007

        def quickmultiply(x: int, y: int) -> int:
            result, multiplier = 1, x

            while y > 0:
                if y % 2 == 1:
                    result = result * multiplier % mod
                
                multiplier = multiplier * multiplier % mod
                y //= 2

            return result

        even = (n + 1) // 2
        odd = n // 2

        return quickmultiply(5, even) * quickmultiply(4, odd) % mod