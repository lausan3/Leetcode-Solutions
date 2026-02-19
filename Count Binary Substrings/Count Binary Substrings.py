class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Brute Force Approach:

        Time: O(n)
        Space: O(1)
        """
        groups = [1]

        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        substring_count = 0

        for i in range(1, len(groups)):
            substring_count += min(groups[i - 1], groups[i])

        return substring_count
