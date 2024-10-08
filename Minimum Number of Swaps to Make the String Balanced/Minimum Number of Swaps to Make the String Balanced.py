class Solution:
    def minSwaps(self, s: str) -> int:
        opening = closing = swaps = 0

        for l in range(len(s)):
            if s[l] == '[':
                opening += 1
            else:
                closing += 1
            
            if closing > opening:
                for r in range(len(s) - 1, -1, -1):
                    if s[r] == '[':
                        s = s[:l] + s[r] + s[l+1:r] + s[l] + s[r:]
                        opening += 1
                        closing -= 1
                        swaps += 1
                        break

        return swaps