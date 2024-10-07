class Solution:
    def minLength(self, s: str) -> int:
        i = 0
        
        # Time: O(n), Space: O(1)
        while i + 1 < len(s):
            substr = s[i:i+2]

            if substr == "AB" or substr == "CD":
                s = s[:i] + s[i+2:]
                i -= 1
            else:
                i += 1
        
        return len(s)