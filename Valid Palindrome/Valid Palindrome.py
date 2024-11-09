class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        s = ''.join(filter(str.isalnum, s.lower()))

        while l < r:
            if sl[l] != sl[r]:
                return False

            l += 1
            r -= 1

        return True