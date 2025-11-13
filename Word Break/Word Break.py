class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Brute force Two Pointer solution:

        init 2 pointers at 0

        move right pointer until we find a word in wordDict
        adjust pointer as necessary

        answer is if r - l pointer is 0 (no excess letters)
        """
        l = r = 0

        while r < len(s):
            if s[l:r + 1] in wordDict:
                l = r + 1

            r += 1

        return r - l == 0