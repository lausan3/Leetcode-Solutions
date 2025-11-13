class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Intuitive O(n^2) center solution:

        For every index i in s,
         find the longest length of palindromic strings that we can expand using i as its center
        
        Time: O(n^2)
        Space: O(1)
        """
        n = len(s)

        def expand(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            return j - i - 1

        largest_bounds = [0, 0]

        for i in range(n):
            odd_length = expand(i, i)

            if odd_length > largest_bounds[1] - largest_bounds[0] + 1:
                dist = odd_length // 2
                largest_bounds = [i - dist, i + dist]

            even_length = expand(i, i + 1)

            if even_length > largest_bounds[1] - largest_bounds[0] + 1:
                dist = even_length // 2 - 1
                largest_bounds = [i - dist, i + 1 + dist]

        print(largest_bounds)

        left, right = largest_bounds
        return s[left : right + 1]
