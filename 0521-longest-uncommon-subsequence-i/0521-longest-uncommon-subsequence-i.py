class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        a_length = len(a)
        b_length = len(b)
        return max(a_length,b_length)