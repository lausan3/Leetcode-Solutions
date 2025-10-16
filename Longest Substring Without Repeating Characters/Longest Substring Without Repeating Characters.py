class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) O(m) space where n = len(s) and m = len(charset)

        longest = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            if s[r] in seen:
                seen.clear()
                l = r

            longest = max(longest, r - l + 1)
            seen.add(s[r])

        return longest