class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Intuition:
        For each letter in the string, grow from it to see if there's palindromes.

        1. Keep count = 0
        2. For each letter in the string, try to grow pointers outward. 
        3. Count ++ if palindrome
        4. Also account for even substrings

        Time: O(n^2)
        Space: O(1)
        """
        palindrome_count = 0
        n = len(s)

        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                palindrome_count += 1
                l -= 1
                r += 1
            l, r = i, i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                palindrome_count += 1
                l -= 1
                r += 1
            
        return palindrome_count