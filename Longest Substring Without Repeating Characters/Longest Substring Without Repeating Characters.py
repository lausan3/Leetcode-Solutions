class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) O(m) space where n = len(s) and m = len(charset)
        longest = 0
        l = 0
        last_seen = {}

        for r, char in enumerate(s):
            if char in last_seen:
                l = last_seen[char] + 1
            
            last_seen[char] = r
            longest = max(longest, r - l + 1)

        return longest