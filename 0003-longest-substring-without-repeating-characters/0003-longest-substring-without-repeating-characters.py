class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        l = 0
        subset = set()

        for r in range(len(s)):
            # while character is in the subset, remove values from subset from left
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            
            subset.add(s[r])
            maxCount = max(maxCount, r - l + 1)

        return maxCount