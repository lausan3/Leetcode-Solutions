class Solution:
    def minSwaps(self, s: str) -> int:
        opening = swaps = 0

        for c in s:
            if c == ']':
                if opening == 0:
                    swaps += 1
                    opening += 1
                else:
                    opening -= 1
            else:
                opening += 1

        return swaps